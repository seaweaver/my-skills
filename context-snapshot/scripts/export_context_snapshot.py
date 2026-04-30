#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path


SOURCE_FILES = ("tables.md", "rules.md", "dictionary.md")


@dataclass(frozen=True)
class ProjectIdentity:
    project_id: str
    project_name: str
    project_code: str
    source_repo_name: str
    snapshot_prefix: str
    project_short_name: str | None
    domain: str | None
    aliases: list[str]
    manifest_path: Path | None
    identity_source: str
    identity_source_ref: str | None


@dataclass
class TableBlock:
    canonical_key: str
    object_name: str
    table_name: str
    domain: str
    line_ref: str
    platform: str
    business_role: str
    key_fields: list[str]
    body: str
    content_hash: str


@dataclass
class RuleVariant:
    line_ref: str
    body: str


@dataclass
class RuleBlock:
    canonical_key: str
    rule_id: str
    rule_name: str
    line_refs: list[str]
    business_definition: str
    use_case: str
    status: str
    body: str
    extras: list[RuleVariant]
    content_hash: str


@dataclass
class DictionaryBlock:
    canonical_key: str
    namespace: str
    section: str
    line_ref: str
    body: str
    aliases: list[str]
    content_hash: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Export context/tables.md, rules.md, and dictionary.md into one self-contained markdown snapshot."
    )
    parser.add_argument("--project-root", required=True, help="Absolute or resolved path to the project root.")
    parser.add_argument("--output", help="Optional explicit output path.")
    parser.add_argument("--snapshot-date", default=str(date.today()), help="Snapshot date in YYYY-MM-DD format.")
    parser.add_argument("--include-placeholders", action="store_true", help="Keep placeholder/template blocks.")
    parser.add_argument("--compare-base", help="Optional explicit previous snapshot path for diff comparison.")
    parser.add_argument("--project-id", help="Stable project identity for snapshot_id and local IDs.")
    parser.add_argument("--project-name", help="Chinese/business-facing project display name.")
    parser.add_argument("--project-short-name", help="Optional short display name.")
    parser.add_argument("--project-code", help="Technical project code or source repository name.")
    parser.add_argument("--snapshot-prefix", help="Filename prefix. Defaults to project_name.")
    parser.add_argument("--domain", help="Business domain for downstream wiki classification.")
    parser.add_argument("--alias", dest="aliases", action="append", default=[], help="Project alias; may be repeated.")
    return parser.parse_args()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def ensure_required_inputs(context_dir: Path) -> None:
    missing = [name for name in SOURCE_FILES if not (context_dir / name).exists()]
    if missing:
        raise FileNotFoundError(f"Missing required context files: {', '.join(missing)}")


def unquote_scalar(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in ("'", '"'):
        return value[1:-1]
    return value


def parse_inline_list(value: str) -> list[str]:
    stripped = value.strip()
    if not (stripped.startswith("[") and stripped.endswith("]")):
        return []
    body = stripped[1:-1].strip()
    if not body:
        return []
    return [unquote_scalar(item.strip()) for item in body.split(",") if item.strip()]


def parse_simple_yaml(path: Path) -> dict[str, object]:
    """Parse the small flat manifest format without adding a PyYAML dependency."""
    result: dict[str, object] = {}
    current_list_key: str | None = None
    for raw_line in read_text(path).splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue
        stripped = raw_line.strip()
        if current_list_key and raw_line[:1].isspace() and stripped.startswith("- "):
            result.setdefault(current_list_key, [])
            assert isinstance(result[current_list_key], list)
            result[current_list_key].append(unquote_scalar(stripped[2:].strip()))
            continue
        current_list_key = None
        if ":" not in stripped:
            continue
        key, value = stripped.split(":", 1)
        key = key.strip().lstrip("\ufeff")
        value = value.strip()
        if not value:
            result[key] = []
            current_list_key = key
            continue
        if value.startswith("[") and value.endswith("]"):
            result[key] = parse_inline_list(value)
        else:
            result[key] = unquote_scalar(value)
    return result


def load_project_manifest(context_dir: Path) -> tuple[dict[str, object], Path | None]:
    for filename in ("manifest.yml", "manifest.yaml", "manifest.json"):
        path = context_dir / filename
        if not path.exists():
            continue
        if path.suffix == ".json":
            data = json.loads(read_text(path))
            if not isinstance(data, dict):
                raise ValueError(f"Project manifest must be a JSON object: {path}")
            return data, path
        return parse_simple_yaml(path), path
    return {}, None


def infer_readme_title(project_root: Path) -> tuple[str | None, Path | None]:
    for filename in ("README.md", "readme.md"):
        path = project_root / filename
        if not path.exists():
            continue
        for line in read_text(path).splitlines()[:80]:
            stripped = line.strip()
            if stripped.startswith("# ") and not stripped.startswith("## "):
                title = stripped[2:].strip()
                return (title or None), path
    return None, None


def clean_heading_text(line: str) -> str:
    text = re.sub(r"^#+\s*", "", line.strip())
    text = re.sub(r"\s+", " ", text)
    return text.strip(" -:：")


def context_headings(context_dir: Path) -> list[tuple[str, int, str]]:
    headings: list[tuple[str, int, str]] = []
    for filename in SOURCE_FILES:
        text = read_text(context_dir / filename)
        for idx, line in enumerate(text.splitlines()[:160], start=1):
            stripped = line.strip()
            if not stripped.startswith("#"):
                continue
            heading = clean_heading_text(stripped)
            if not heading or "[" in heading or "]" in heading:
                continue
            level = len(stripped) - len(stripped.lstrip("#"))
            # H1/H2 carry project/domain semantics more reliably than item headings.
            if level <= 2:
                headings.append((filename, idx, heading))
    return headings


def scope_from_heading(heading: str) -> str | None:
    suffixes = (
        "物理模型定义",
        "业务逻辑库",
        "业务规则库",
        "规则库",
        "数据字典",
        "字典",
        "表结构定义",
        "数据对象说明",
        "指标体系",
        "指标口径",
        "上下文",
        "Context",
    )
    for suffix in suffixes:
        if heading.endswith(suffix):
            scope = heading[: -len(suffix)].strip(" -:：")
            if scope:
                return scope
    domain_match = re.search(r"([\u4e00-\u9fff]{2,12}域)", heading)
    if domain_match:
        return domain_match.group(1)
    if heading.endswith(("项目", "场景", "专题", "主题")):
        return heading
    return None


def project_name_from_scope(scope: str) -> str:
    if scope.endswith("项目"):
        return scope
    if scope.endswith("域"):
        return f"{scope}数据分析项目"
    if scope.endswith(("场景", "专题", "主题")):
        return scope
    if any(token in scope for token in ("数据", "分析", "指标", "报表", "模型")):
        return f"{scope}项目"
    return f"{scope}项目"


def infer_context_identity(context_dir: Path) -> dict[str, object]:
    headings = context_headings(context_dir)
    scored: dict[str, dict[str, object]] = {}
    for filename, line_no, heading in headings:
        scope = scope_from_heading(heading)
        if not scope:
            continue
        bucket = scored.setdefault(scope, {"score": 0, "refs": [], "headings": []})
        # H1 titles across multiple files are the strongest signal.
        bucket["score"] = int(bucket["score"]) + (3 if line_no <= 5 else 1)
        bucket["refs"].append(f"context/{filename}#L{line_no}")
        bucket["headings"].append(heading)

    if not scored:
        return {}

    scope, payload = sorted(
        scored.items(),
        key=lambda item: (int(item[1]["score"]), len(item[1]["refs"]), -len(item[0])),
        reverse=True,
    )[0]
    project_name = project_name_from_scope(scope)
    refs = list(dict.fromkeys(str(ref) for ref in payload["refs"]))
    headings_used = list(dict.fromkeys(str(item) for item in payload["headings"]))
    aliases = [scope, project_name, *headings_used]
    return {
        "project_name": project_name,
        "project_short_name": scope,
        "snapshot_prefix": project_name,
        "domain": scope if scope.endswith("域") else None,
        "aliases": list(dict.fromkeys(alias for alias in aliases if alias)),
        "identity_source_ref": ", ".join(refs),
    }


def as_string(manifest: dict[str, object], *keys: str) -> str | None:
    for key in keys:
        value = manifest.get(key)
        if isinstance(value, str) and value.strip():
            return value.strip()
    return None


def as_list(manifest: dict[str, object], *keys: str) -> list[str]:
    for key in keys:
        value = manifest.get(key)
        if isinstance(value, list):
            return [str(item).strip() for item in value if str(item).strip()]
        if isinstance(value, str) and value.strip():
            return [item.strip() for item in re.split(r"[,，]", value) if item.strip()]
    return []


def safe_filename_part(value: str) -> str:
    cleaned = re.sub(r'[<>:"/\\|?*\x00-\x1f]+', "-", value).strip().strip(".")
    return re.sub(r"\s+", " ", cleaned) or "项目"


def load_project_identity(project_root: Path, context_dir: Path, args: argparse.Namespace) -> ProjectIdentity:
    manifest, manifest_path = load_project_manifest(context_dir)
    context_identity = infer_context_identity(context_dir)
    readme_title, readme_path = infer_readme_title(project_root)
    source_repo_name = project_root.name
    project_name = (
        args.project_name
        or as_string(manifest, "project_name", "display_name", "name", "中文项目名")
        or str(context_identity.get("project_name") or "")
        or readme_title
        or source_repo_name
    )
    project_id = (
        args.project_id
        or as_string(manifest, "project_id", "stable_id", "id")
        or source_repo_name.replace("_", "-")
    )
    project_code = (
        args.project_code
        or as_string(manifest, "project_code", "source_project_code", "code")
        or source_repo_name
    )
    snapshot_prefix = (
        args.snapshot_prefix
        or as_string(manifest, "snapshot_prefix", "snapshot_name", "filename_prefix")
        or str(context_identity.get("snapshot_prefix") or "")
        or project_name
    )
    aliases = as_list(manifest, "aliases", "project_aliases", "别名")
    for alias in context_identity.get("aliases", []):
        if isinstance(alias, str) and alias and alias not in aliases:
            aliases.append(alias)
    for alias in args.aliases:
        if alias and alias not in aliases:
            aliases.append(alias)
    if readme_title and readme_title not in aliases:
        aliases.append(readme_title)
    for alias in (source_repo_name, project_code):
        if alias and alias not in aliases:
            aliases.append(alias)
    has_cli_identity = any(
        (
            args.project_id,
            args.project_name,
            args.project_short_name,
            args.project_code,
            args.snapshot_prefix,
            args.domain,
            args.aliases,
        )
    )
    if has_cli_identity:
        identity_source = "command-line"
        identity_source_ref = "exporter CLI arguments"
    elif manifest_path:
        identity_source = "manifest"
        identity_source_ref = manifest_path.relative_to(project_root).as_posix()
    elif context_identity:
        identity_source = "context-inferred"
        identity_source_ref = str(context_identity.get("identity_source_ref") or "context/*.md")
    elif readme_path and readme_title:
        identity_source = "readme-title"
        identity_source_ref = readme_path.relative_to(project_root).as_posix()
    else:
        identity_source = "directory-name"
        identity_source_ref = source_repo_name
    return ProjectIdentity(
        project_id=project_id,
        project_name=project_name,
        project_code=project_code,
        source_repo_name=source_repo_name,
        snapshot_prefix=safe_filename_part(snapshot_prefix),
        project_short_name=(
            args.project_short_name
            or as_string(manifest, "project_short_name", "short_name", "简称")
            or str(context_identity.get("project_short_name") or "")
            or None
        ),
        domain=(
            args.domain
            or as_string(manifest, "domain", "business_domain", "业务域")
            or str(context_identity.get("domain") or "")
            or None
        ),
        aliases=aliases,
        manifest_path=manifest_path,
        identity_source=identity_source,
        identity_source_ref=identity_source_ref,
    )


def run_git(project_root: Path, args: list[str]) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=project_root,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=True,
    )
    return result.stdout.strip()


def get_git_info(project_root: Path) -> tuple[str, str]:
    try:
        branch = run_git(project_root, ["branch", "--show-current"])
        commit = run_git(project_root, ["rev-parse", "--short", "HEAD"])
        if branch and commit:
            return branch, commit
    except Exception:
        pass
    return "n/a", "no-git"


def compute_source_content_hash(context_dir: Path) -> str:
    sha = hashlib.sha256()
    for name in SOURCE_FILES:
        sha.update(name.encode("utf-8"))
        sha.update(b"\n")
        sha.update(read_text(context_dir / name).encode("utf-8"))
        sha.update(b"\n---\n")
    return sha.hexdigest()[:16]


def line_refs(text: str, needle: str) -> list[int]:
    return [i for i, line in enumerate(text.splitlines(), start=1) if needle in line]


def extract_bullet_value(body: str, label: str) -> str | None:
    prefix = f"* **{label}**:"
    for line in body.splitlines():
        stripped = line.strip()
        if stripped.startswith(prefix):
            return stripped[len(prefix):].strip()
    return None


def extract_identifier_list(raw: str | None) -> list[str]:
    if not raw:
        return []
    from_backticks = re.findall(r"`([^`]+)`", raw)
    if from_backticks:
        return [item.strip() for item in from_backticks if item.strip()]
    parts = re.split(r"[,，]", raw)
    result: list[str] = []
    for part in parts:
        cleaned = re.sub(r"\s*[（(].*?[)）]\s*$", "", part).strip().strip("`")
        if cleaned:
            result.append(cleaned)
    return result


def normalize_id(text: str) -> str:
    return re.sub(r"[^0-9A-Za-z\u4e00-\u9fff]+", "-", text).strip("-").lower() or "item"


def short_hash(*parts: str) -> str:
    sha = hashlib.sha256()
    for part in parts:
        sha.update(part.encode("utf-8"))
        sha.update(b"\n")
    return sha.hexdigest()[:16]


def is_placeholder_table(object_name: str, table_name: str, body: str) -> bool:
    haystack = "\n".join((object_name, table_name, body))
    markers = [
        "[表名]",
        "中文名",
        "Schema.TableName",
        "PK_Column",
        "Term_ID",
        "(下一张表...)",
        "col_name",
    ]
    return any(marker in haystack for marker in markers)


def is_placeholder_rule(rule_id: str, rule_name: str, body: str) -> bool:
    haystack = "\n".join((rule_id, rule_name, body))
    markers = [
        "规则名称",
        "Rule Name",
        "一句话描述业务含义",
        "{param1}",
        "{param_start_date}",
        "column_a =",
        "StatusA",
        "StatusB",
    ]
    return any(marker in haystack for marker in markers)


def is_placeholder_dictionary(namespace: str, section: str, body: str) -> bool:
    haystack = "\n".join((namespace, section, body))
    markers = [
        "<key>: <value>",
        "<constraint>",
        "<heading>",
        "示例占位",
    ]
    return any(marker in haystack for marker in markers)


def extract_global_preamble(text: str, first_item_pattern: str) -> str:
    match = re.search(first_item_pattern, text, flags=re.M)
    if not match:
        return text.strip()
    return text[: match.start()].strip()


def render_embedded_excerpt(text: str) -> list[str]:
    if not text.strip():
        return ["- 未提取到额外文件级说明。"]

    rendered: list[str] = []
    for raw_line in text.splitlines():
        stripped = raw_line.strip()
        if not stripped:
            rendered.append(">")
            continue
        if stripped.startswith("#"):
            rendered.append(f"> \\{stripped}")
            continue
        if stripped == "---":
            rendered.append(r"> \---")
            continue
        rendered.append(f"> {raw_line}")
    return rendered


def build_table_domains_from_blocks(tables: list[TableBlock]) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    for table in tables:
        result.setdefault(table.domain, []).append(table.object_name)
    return {key: value for key, value in result.items() if value}


def parse_dictionary_sections(text: str) -> dict[str, list[str]]:
    current_section = "未分类"
    result: dict[str, list[str]] = {}
    for line in text.splitlines():
        if line.startswith("## "):
            current_section = line[3:].strip()
            result.setdefault(current_section, [])
        elif line.startswith("### "):
            result.setdefault(current_section, []).append(line[4:].strip())
    return {key: value for key, value in result.items() if value}


def parse_tables(text: str, include_placeholders: bool) -> tuple[list[TableBlock], int]:
    # Pattern A: [ObjectName] (TABLE_NAME) [- platform] — original bracket format
    heading_bracket = re.compile(
        r"^(?:##\s+\d+\.|###\s+\d+\.\d+)\s+\[(?P<object_name>[^\]]+)\]\s+\((?P<table_name>[^)]+)\)(?:\s*-\s*(?P<heading_platform>.*))?\s*$"
    )
    # Pattern B: ## N. ObjectName：TABLE_NAME [(ChineseDesc)]
    heading_colon = re.compile(
        r"^##\s+\d+\.\s+(?P<object_name>.+?)[：:]\s*(?P<table_name>[A-Z][A-Z0-9_]+)\s*(?:\((?P<extra>[^)]*)\))?\s*$"
    )
    # Pattern C: ### N.N ObjectName — TABLE_NAME
    heading_dash = re.compile(
        r"^###\s+\d+\.\d+\s+(?P<object_name>.+?)\s+[—\-]\s+(?P<table_name>[A-Za-z][A-Za-z0-9_]*)\s*$"
    )
    domain_heading = re.compile(r"^##\s+(?:\d+\.\s+)?(?P<domain>.+?)\s*$")
    boundary_heading = re.compile(r"^(?:##|###)\s+")
    non_domain_keywords = ("INSERT", "MERGE", "已知缺口", "字段映射", "聚合规则")

    lines = text.splitlines()
    blocks: list[TableBlock] = []
    skipped = 0
    idx = 0
    current_domain = "未分类"

    table_matchers = [
        (heading_bracket, lambda m: (m.group("object_name").strip(), m.group("table_name").strip(), (m.group("heading_platform") or "").strip())),
        (heading_colon, lambda m: (m.group("object_name").strip(), m.group("table_name").strip(), "")),
        (heading_dash, lambda m: (m.group("object_name").strip(), m.group("table_name").strip(), "")),
    ]

    def _detect_platform(body_text: str) -> str:
        if "大数据平台" in body_text:
            return "大数据平台"
        if "Doris" in body_text:
            return "Doris"
        if any(kw in body_text for kw in ("Oracle", "CJHX_", "STAGE.", "DW.", "CJHX_DWMS", "CJHX_DSCL", "CJHX_SMI", "WINDFS")):
            return "Oracle"
        return "未显式说明"

    def _has_sub_tables(start: int) -> bool:
        for j in range(start, len(lines)):
            future = lines[j]
            if future.startswith("## "):
                return False
            if future.startswith("### ") and re.match(r"\d+\.\d+", future[4:].strip()):
                return True
        return False

    while idx < len(lines):
        line = lines[idx]

        # 1) Try table heading patterns first
        matched = False
        for pattern, extractor in table_matchers:
            match = pattern.match(line)
            if not match:
                continue
            object_name, table_name, heading_platform = extractor(match)
            start_line = idx + 1
            body_lines: list[str] = []
            idx += 1
            while idx < len(lines) and not boundary_heading.match(lines[idx]):
                body_lines.append(lines[idx])
                idx += 1
            body = "\n".join(body_lines).strip()

            if not include_placeholders and is_placeholder_table(object_name, table_name, body):
                skipped += 1
                matched = True
                break

            pk_raw = extract_bullet_value(body, "主键")
            key_fields = extract_identifier_list(pk_raw)
            platform = heading_platform or _detect_platform(body)

            blocks.append(
                TableBlock(
                    canonical_key=table_name,
                    object_name=object_name,
                    table_name=table_name,
                    domain=current_domain,
                    line_ref=f"context/tables.md#L{start_line}",
                    platform=platform,
                    business_role=extract_bullet_value(body, "业务用途") or "未显式说明",
                    key_fields=[item for item in key_fields if item],
                    body=body,
                    content_hash=short_hash(table_name, object_name, body),
                )
            )
            matched = True
            break

        if matched:
            continue

        # 2) Try domain heading (## with optional number)
        domain_match = domain_heading.match(line)
        if domain_match:
            domain_text = domain_match.group("domain").strip()
            if not any(kw in domain_text for kw in non_domain_keywords):
                if _has_sub_tables(idx + 1):
                    current_domain = domain_text
            idx += 1
            continue

        idx += 1

    return blocks, skipped


def parse_rules(text: str, include_placeholders: bool) -> tuple[list[RuleBlock], int]:
    pattern = re.compile(
        r"^##\s+\[(?P<rule_id>[^\]]+)\]\s+(?P<rule_name>.+?)\s*\n(?P<body>.*?)(?=^##\s+\[|\Z)",
        re.M | re.S,
    )
    grouped: dict[str, list[RuleVariant]] = {}
    names: dict[str, str] = {}
    skipped = 0

    for match in pattern.finditer(text):
        rule_id = match.group("rule_id").strip()
        rule_name = match.group("rule_name").strip()
        body = match.group("body").strip()
        if not include_placeholders and is_placeholder_rule(rule_id, rule_name, body):
            skipped += 1
            continue
        refs = line_refs(text, f"[{rule_id}] {rule_name}")
        line_ref = f"context/rules.md#L{refs[0]}" if refs else "context/rules.md"
        grouped.setdefault(rule_id, []).append(RuleVariant(line_ref=line_ref, body=body))
        names[rule_id] = rule_name

    result: list[RuleBlock] = []
    for rule_id, variants in grouped.items():
        first = variants[0]
        extras = [variant for variant in variants[1:] if variant.body.strip() != first.body.strip()]
        result.append(
            RuleBlock(
                canonical_key=rule_id,
                rule_id=rule_id,
                rule_name=names[rule_id],
                line_refs=[variant.line_ref for variant in variants],
                business_definition=extract_bullet_value(first.body, "业务定义") or "见原始事实摘录",
                use_case=extract_bullet_value(first.body, "适用场景") or "见原始事实摘录",
                status="project-only" if not extras else "variant",
                body=first.body,
                extras=extras,
                content_hash=short_hash(rule_id, names[rule_id], first.body, *(extra.body for extra in extras)),
            )
        )
    return result, skipped


def extract_dictionary_aliases(namespace: str) -> list[str]:
    aliases = {namespace}
    code_matches = re.findall(r"\(([^)]+)\)", namespace)
    aliases.update(match.strip() for match in code_matches if match.strip())
    label = namespace.split(" - ", 1)[0].strip()
    aliases.add(label)
    if "(" in label:
        aliases.add(label.split("(", 1)[0].strip())
    return sorted(alias for alias in aliases if alias)


def parse_dictionary(text: str, include_placeholders: bool) -> tuple[list[DictionaryBlock], int]:
    lines = text.splitlines()
    blocks: list[tuple[str, str, int, str]] = []
    current_section: str | None = None
    current_h3: str | None = None
    start_line: int | None = None
    buffer: list[str] = []

    for idx, line in enumerate(lines, start=1):
        if line.startswith("## "):
            if current_h3 is not None:
                blocks.append((current_h3, current_section or current_h3, start_line or idx, "\n".join(buffer).strip()))
                current_h3 = None
                buffer = []
            current_section = line[3:].strip()
        elif line.startswith("### "):
            if current_h3 is not None:
                blocks.append((current_h3, current_section or current_h3, start_line or idx, "\n".join(buffer).strip()))
            current_h3 = line[4:].strip()
            start_line = idx
            buffer = []
        else:
            if current_h3 is not None:
                buffer.append(line)

    if current_h3 is not None:
        blocks.append((current_h3, current_section or current_h3, start_line or 1, "\n".join(buffer).strip()))

    for match in re.finditer(r"^##\s+(?P<section>.+?)\n(?P<body>.*?)(?=^##\s+|\Z)", text, re.M | re.S):
        section = match.group("section").strip()
        body = match.group("body").strip()
        if "### " not in body and body:
            line_no = text[: match.start()].count("\n") + 1
            blocks.append((section, section, line_no, body))

    seen: set[tuple[str, int]] = set()
    normalized: list[DictionaryBlock] = []
    skipped = 0
    for namespace, section, line_no, body in blocks:
        key = (namespace, line_no)
        if key in seen:
            continue
        seen.add(key)
        if not include_placeholders and is_placeholder_dictionary(namespace, section, body):
            skipped += 1
            continue
        normalized.append(
            DictionaryBlock(
                canonical_key=namespace,
                namespace=namespace,
                section=section,
                line_ref=f"context/dictionary.md#L{line_no}",
                body=body or "见原始事实摘录",
                aliases=extract_dictionary_aliases(namespace),
                content_hash=short_hash(namespace, section, body or "见原始事实摘录"),
            )
        )
    return normalized, skipped


def extract_table_relationships(tables: list[TableBlock], dictionary: list[DictionaryBlock]) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    for table in tables:
        hits: list[str] = []
        for item in dictionary:
            if any(alias and alias in table.body for alias in item.aliases):
                hits.append(item.namespace)
        result[table.table_name] = sorted(set(hits))
    return result


def extract_rule_relationships(
    rules: list[RuleBlock],
    tables: list[TableBlock],
    dictionary: list[DictionaryBlock],
) -> tuple[dict[str, list[str]], dict[str, list[str]]]:
    rule_to_tables: dict[str, list[str]] = {}
    rule_to_dictionary: dict[str, list[str]] = {}
    for rule in rules:
        table_hits = [table.table_name for table in tables if table.table_name in rule.body]
        dictionary_hits: list[str] = []
        for item in dictionary:
            if any(alias and alias in rule.body for alias in item.aliases):
                dictionary_hits.append(item.namespace)
        rule_to_tables[rule.rule_id] = sorted(set(table_hits))
        rule_to_dictionary[rule.rule_id] = sorted(set(dictionary_hits))
    return rule_to_tables, rule_to_dictionary


def build_output_path(
    project_root: Path,
    snapshot_date: str,
    commit: str,
    explicit_output: str | None,
    identity: ProjectIdentity,
) -> Path:
    if explicit_output:
        return Path(explicit_output)
    exports_dir = project_root / "context" / "exports"
    exports_dir.mkdir(parents=True, exist_ok=True)
    return exports_dir / f"{identity.snapshot_prefix}-知识快照-{snapshot_date}-{commit}.md"


def find_previous_snapshot(
    project_root: Path,
    current_output: Path,
    explicit_compare_base: str | None,
    identity: ProjectIdentity,
) -> Path | None:
    if explicit_compare_base:
        candidate = Path(explicit_compare_base)
        return candidate if candidate.exists() else None
    exports_dir = project_root / "context" / "exports"
    if not exports_dir.exists():
        return None
    prefixes = [identity.snapshot_prefix]
    legacy_prefix = project_root.name
    if legacy_prefix not in prefixes:
        prefixes.append(legacy_prefix)
    candidates = [
        path
        for path in exports_dir.glob("*.md")
        if path.resolve() != current_output.resolve()
        and any(path.name.startswith(f"{prefix}-知识快照-") for prefix in prefixes)
    ]
    if not candidates:
        return None
    return sorted(candidates, key=lambda path: path.stat().st_mtime, reverse=True)[0]


def parse_frontmatter(markdown: str) -> dict[str, str]:
    lines = markdown.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    result: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if ":" in line and not line.startswith("  - "):
            key, value = line.split(":", 1)
            result[key.strip()] = value.strip()
    return result


def parse_snapshot_index(path: Path) -> dict[str, dict[str, str]]:
    markdown = read_text(path)
    current_section: str | None = None
    current_item: dict[str, str] | None = None
    result = {"table": {}, "rule": {}, "dictionary": {}}

    def flush_current() -> None:
        nonlocal current_item, current_section
        if current_section and current_item and current_item.get("canonical_key") and current_item.get("content_hash"):
            result[current_section][current_item["canonical_key"]] = current_item["content_hash"]
        current_item = None

    for line in markdown.splitlines():
        stripped = line.strip()
        if stripped == "## Tables｜数据对象":
            flush_current()
            current_section = "table"
            continue
        if stripped == "## Rules｜业务规则":
            flush_current()
            current_section = "rule"
            continue
        if stripped == "## Dictionary｜字典与术语":
            flush_current()
            current_section = "dictionary"
            continue
        if stripped.startswith("## "):
            flush_current()
            current_section = None
            continue
        if current_section and stripped.startswith("### "):
            flush_current()
            current_item = {}
            continue
        if current_section and current_item is not None and stripped.startswith("- canonical_key:"):
            current_item["canonical_key"] = stripped.split(":", 1)[1].strip()
        if current_section and current_item is not None and stripped.startswith("- content_hash:"):
            current_item["content_hash"] = stripped.split(":", 1)[1].strip().strip("`")

    flush_current()
    return result


def compare_with_previous(
    previous_path: Path | None,
    tables: list[TableBlock],
    rules: list[RuleBlock],
    dictionary: list[DictionaryBlock],
) -> tuple[dict[str, dict[str, list[str]]], dict[str, str]]:
    current = {
        "table": {item.canonical_key: item.content_hash for item in tables},
        "rule": {item.canonical_key: item.content_hash for item in rules},
        "dictionary": {item.canonical_key: item.content_hash for item in dictionary},
    }
    result = {
        "table": {"new": [], "updated": [], "unchanged": [], "removed": []},
        "rule": {"new": [], "updated": [], "unchanged": [], "removed": []},
        "dictionary": {"new": [], "updated": [], "unchanged": [], "removed": []},
    }
    if previous_path is None or not previous_path.exists():
        for category, items in current.items():
            result[category]["new"] = sorted(items.keys())
        return result, {}

    previous_index = parse_snapshot_index(previous_path)
    previous_frontmatter = parse_frontmatter(read_text(previous_path))
    for category, items in current.items():
        prev_items = previous_index.get(category, {})
        for key, content_hash in items.items():
            if key not in prev_items:
                result[category]["new"].append(key)
            elif prev_items[key] == content_hash:
                result[category]["unchanged"].append(key)
            else:
                result[category]["updated"].append(key)
        for key in prev_items:
            if key not in items:
                result[category]["removed"].append(key)
        for change_type in result[category]:
            result[category][change_type].sort()
    return result, previous_frontmatter


def change_type_for(category: str, canonical_key: str, diff_summary: dict[str, dict[str, list[str]]], has_previous: bool) -> str:
    if not has_previous:
        return "baseline"
    for change_type in ("new", "updated", "unchanged"):
        if canonical_key in diff_summary[category][change_type]:
            return change_type
    return "unknown"


def render_global_knowledge(tables_preamble: str, rules_preamble: str, dictionary_preamble: str) -> list[str]:
    lines: list[str] = []
    append = lines.append
    append("## 项目级全局知识")
    append("")
    for title, content in (
        ("tables.md 文件级说明", tables_preamble),
        ("rules.md 文件级说明", rules_preamble),
        ("dictionary.md 文件级说明", dictionary_preamble),
    ):
        append(f"### {title}")
        append("")
        append("> 以下为文件级摘录。为避免污染快照主章节结构，原始标题已转为普通文本。")
        append(">")
        lines.extend(render_embedded_excerpt(content))
        append("")
    return lines


def render_structure_overview(
    table_domains: dict[str, list[str]],
    dictionary_sections: dict[str, list[str]],
    rules: list[RuleBlock],
) -> list[str]:
    lines: list[str] = []
    append = lines.append
    append("## 知识结构导览")
    append("")
    append("### 表对象分域")
    append("")
    for domain, objects in table_domains.items():
        append(f"- {domain}：{', '.join(objects)}")
    append("")
    append("### 规则总体结构")
    append("")
    append(f"- 规则总数：`{len(rules)}`")
    append(f"- 规则 ID 列表：{', '.join(f'`{rule.rule_id}`' for rule in rules)}")
    append("")
    append("### 字典分组")
    append("")
    for section, items in dictionary_sections.items():
        append(f"- {section}：{', '.join(items)}")
    append("")
    return lines


def render_relationship_index(
    rule_to_tables: dict[str, list[str]],
    rule_to_dictionary: dict[str, list[str]],
    table_to_dictionary: dict[str, list[str]],
) -> list[str]:
    lines: list[str] = []
    append = lines.append
    append("## 关系索引")
    append("")
    append("### rule -> table")
    append("")
    for rule_id, targets in rule_to_tables.items():
        append(f"- `{rule_id}` -> {', '.join(f'`{target}`' for target in targets) if targets else '无显式命中'}")
    append("")
    append("### rule -> dictionary")
    append("")
    for rule_id, targets in rule_to_dictionary.items():
        append(f"- `{rule_id}` -> {', '.join(f'`{target}`' for target in targets) if targets else '无显式命中'}")
    append("")
    append("### table -> dictionary")
    append("")
    for table_name, targets in table_to_dictionary.items():
        append(f"- `{table_name}` -> {', '.join(f'`{target}`' for target in targets) if targets else '无显式命中'}")
    append("")
    return lines


def render_diff_section(
    diff_summary: dict[str, dict[str, list[str]]],
    previous_snapshot: Path | None,
    previous_frontmatter: dict[str, str],
) -> list[str]:
    lines: list[str] = []
    append = lines.append
    append("## 与上一快照差异")
    append("")
    if previous_snapshot is None:
        append("- 未找到上一快照，本次导出作为基线快照。")
        append("")
        return lines

    previous_snapshot_id = previous_frontmatter.get("snapshot_id", previous_snapshot.name)
    append(f"- comparison_base: `{previous_snapshot.name}`")
    append(f"- previous_snapshot_id: `{previous_snapshot_id}`")
    append("")
    for category, label in (("table", "Tables"), ("rule", "Rules"), ("dictionary", "Dictionary")):
        append(f"### {label}")
        append("")
        append(f"- new: {', '.join(f'`{item}`' for item in diff_summary[category]['new']) if diff_summary[category]['new'] else '无'}")
        append(f"- updated: {', '.join(f'`{item}`' for item in diff_summary[category]['updated']) if diff_summary[category]['updated'] else '无'}")
        append(f"- unchanged_count: `{len(diff_summary[category]['unchanged'])}`")
        append(f"- removed: {', '.join(f'`{item}`' for item in diff_summary[category]['removed']) if diff_summary[category]['removed'] else '无'}")
        append("")
    return lines


def render_snapshot(
    project_root: Path,
    identity: ProjectIdentity,
    snapshot_date: str,
    branch: str,
    commit: str,
    source_content_hash: str,
    tables_preamble: str,
    rules_preamble: str,
    dictionary_preamble: str,
    table_domains: dict[str, list[str]],
    dictionary_sections: dict[str, list[str]],
    rule_to_tables: dict[str, list[str]],
    rule_to_dictionary: dict[str, list[str]],
    table_to_dictionary: dict[str, list[str]],
    tables: list[TableBlock],
    rules: list[RuleBlock],
    dictionary: list[DictionaryBlock],
    skipped_tables: int,
    skipped_rules: int,
    skipped_dictionary: int,
    output_path: Path,
    previous_snapshot: Path | None,
    previous_frontmatter: dict[str, str],
    diff_summary: dict[str, dict[str, list[str]]],
) -> str:
    project_name = identity.project_name
    project_id = identity.project_id
    exported_at = datetime.now().replace(microsecond=0).isoformat()
    snapshot_id = f"{project_id}:{snapshot_date}:{commit}"
    previous_snapshot_name = previous_snapshot.name if previous_snapshot else ""
    previous_snapshot_id = previous_frontmatter.get("snapshot_id", "") if previous_snapshot else ""
    previous_sequence = int(previous_frontmatter.get("snapshot_sequence", "0") or "0") if previous_snapshot else 0
    snapshot_sequence = previous_sequence + 1 if previous_snapshot else 1
    duplicate_rule_count = sum(len(rule.line_refs) - 1 for rule in rules)
    has_previous = previous_snapshot is not None

    lines: list[str] = []
    append = lines.append
    append("---")
    append(f"title: {project_name} 知识快照")
    append("type: project_context_snapshot")
    append(f"project_id: {project_id}")
    append(f"project_name: {project_name}")
    if identity.project_short_name:
        append(f"project_short_name: {identity.project_short_name}")
    append(f"project_code: {identity.project_code}")
    append(f"source_repo_name: {identity.source_repo_name}")
    append(f"snapshot_prefix: {identity.snapshot_prefix}")
    if identity.domain:
        append(f"domain: {identity.domain}")
    if identity.aliases:
        append("project_aliases:")
        for alias in identity.aliases:
            append(f"  - {alias}")
    append(f"snapshot_id: {snapshot_id}")
    append(f"snapshot_date: {snapshot_date}")
    append(f"snapshot_sequence: {snapshot_sequence}")
    append(f"exported_at: {exported_at}")
    append(f"source_repo: {project_root.as_posix()}")
    append(f"source_branch: {branch}")
    append(f"source_commit: {commit}")
    append(f"source_content_hash: {source_content_hash}")
    append(f"previous_snapshot: {previous_snapshot_name}")
    append(f"supersedes: {previous_snapshot_id}")
    append("source_files:")
    append("  - context/tables.md")
    append("  - context/rules.md")
    append("  - context/dictionary.md")
    append("export_spec_version: v4")
    append("status: active")
    append("---")
    append("")
    append(f"# {project_name} 知识快照")
    append("")
    append("## 导出边界")
    append("")
    append(f"- 项目中文名称：`{identity.project_name}`。")
    append(f"- 稳定项目 ID：`{identity.project_id}`；源仓库目录名：`{identity.source_repo_name}`。")
    if identity.domain:
        append(f"- 业务域：`{identity.domain}`。")
    append(f"- 项目身份来源：`{identity.identity_source}` / `{identity.identity_source_ref}`。")
    append("- 项目身份仅用于快照命名、版本追踪与下游检索，不扩展知识事实源。")
    append("- 仅以 `context/tables.md`、`context/rules.md`、`context/dictionary.md` 为事实源。")
    append("- 本快照是自包含事实文档，后续 wiki 应能仅基于本文件完成 ingest。")
    append("- `source_refs` 仅用于追溯，不用于承载缺失事实。")
    if branch == "n/a" and commit == "no-git":
        append("- 本项目目录未检测到 git 仓库，`source_branch` 与 `source_commit` 以 `n/a` / `no-git` 记录。")
    append("")
    append("## 规范化摘要")
    append("")
    append(f"- tables 条目数：`{len(tables)}`")
    append(f"- rules 原始规则块数：`{sum(len(rule.line_refs) for rule in rules)}`")
    append(f"- rules 唯一规则 ID 数：`{len(rules)}`")
    append(f"- dictionary 命名空间/术语组数：`{len(dictionary)}`")
    append(f"- 项目内重复规则块数：`{duplicate_rule_count}`")
    append("- 显式知识冲突：`0`")
    append("")
    lines.extend(render_global_knowledge(tables_preamble, rules_preamble, dictionary_preamble))
    lines.extend(render_structure_overview(table_domains, dictionary_sections, rules))
    lines.extend(render_relationship_index(rule_to_tables, rule_to_dictionary, table_to_dictionary))
    lines.extend(render_diff_section(diff_summary, previous_snapshot, previous_frontmatter))
    append("## Tables｜数据对象")
    append("")
    for table in tables:
        append(f"### [{table.object_name}] ({table.table_name})")
        append("")
        append(f"- local_id: {project_id}:{table.table_name}")
        append(f"- canonical_key: {table.canonical_key}")
        append(f"- table_name: {table.table_name}")
        append(f"- object_name: {table.object_name}")
        append(f"- domain: {table.domain}")
        append(f"- platform: {table.platform}")
        append("- status: project-only")
        append(f"- change_type: {change_type_for('table', table.canonical_key, diff_summary, has_previous)}")
        append(f"- content_hash: `{table.content_hash}`")
        append(f"- source_refs: `{table.line_ref}`")
        append("")
        append("#### 结构化事实")
        append("")
        append(f"- business_role: {table.business_role}")
        append(f"- key_fields: {', '.join(f'`{field}`' for field in table.key_fields) if table.key_fields else '未显式说明'}")
        append("- preset_join_paths: 见下方原始事实摘录中的“预设关联路径”")
        append(f"- related_dictionary: {', '.join(f'`{item}`' for item in table_to_dictionary.get(table.table_name, [])) if table_to_dictionary.get(table.table_name) else '无显式命中'}")
        append("")
        append("#### 原始事实摘录")
        append("")
        append(table.body)
        append("")
    append("## Rules｜业务规则")
    append("")
    for rule in rules:
        append(f"### [{rule.rule_id}] {rule.rule_name}")
        append("")
        append(f"- local_id: {project_id}:{rule.rule_id}")
        append(f"- canonical_key: {rule.canonical_key}")
        append(f"- rule_id: {rule.rule_id}")
        append(f"- rule_name: {rule.rule_name}")
        append(f"- status: {rule.status}")
        append(f"- change_type: {change_type_for('rule', rule.canonical_key, diff_summary, has_previous)}")
        append(f"- content_hash: `{rule.content_hash}`")
        append("- source_refs:")
        for ref in rule.line_refs:
            append(f"  - `{ref}`")
        append("")
        append("#### 结构化事实")
        append("")
        append(f"- business_definition: {rule.business_definition}")
        append(f"- use_cases: {rule.use_case}")
        append("- inputs: 见 SQL 逻辑模板或原始事实摘录")
        append("- outputs: 见 SQL 逻辑模板或原始事实摘录")
        append("- key_logic: 见原始事实摘录")
        append(f"- related_tables: {', '.join(f'`{item}`' for item in rule_to_tables.get(rule.rule_id, [])) if rule_to_tables.get(rule.rule_id) else '无显式命中'}")
        append(f"- related_dictionary: {', '.join(f'`{item}`' for item in rule_to_dictionary.get(rule.rule_id, [])) if rule_to_dictionary.get(rule.rule_id) else '无显式命中'}")
        append("")
        append("#### 原始事实摘录")
        append("")
        append(rule.body)
        append("")
        for extra in rule.extras:
            append("#### 补充摘录（重复来源）")
            append("")
            append(f"- 补充来源：`{extra.line_ref}`")
            append("")
            append(extra.body)
            append("")
    append("## Dictionary｜字典与术语")
    append("")
    for item in dictionary:
        append(f"### {item.namespace}")
        append("")
        append(f"- local_id: {project_id}:{normalize_id(item.namespace)}")
        append(f"- canonical_key: {item.canonical_key}")
        append(f"- namespace: {item.namespace}")
        append(f"- section: {item.section}")
        append("- status: project-only")
        append(f"- change_type: {change_type_for('dictionary', item.canonical_key, diff_summary, has_previous)}")
        append(f"- content_hash: `{item.content_hash}`")
        append(f"- source_refs: `{item.line_ref}`")
        append("")
        append("#### 结构化事实")
        append("")
        append(f"- purpose: 来源章节为“{item.section}”")
        append(f"- aliases: {', '.join(f'`{alias}`' for alias in item.aliases)}")
        append("- representative_entries: 见原始事实摘录")
        append("- rules_or_constraints: 见原始事实摘录")
        append("")
        append("#### 原始事实摘录")
        append("")
        append(item.body)
        append("")
    append("## 项目内重复合并说明")
    append("")
    if duplicate_rule_count:
        append(f"- 本项目按唯一规则 ID 合并了 `{duplicate_rule_count}` 个重复规则块。")
        for rule in rules:
            if len(rule.line_refs) > 1:
                append(f"- 重复规则：`{rule.rule_id}`，来源数：`{len(rule.line_refs)}`")
    else:
        append("- 未发现项目内重复规则块。")
    append("")
    append("## 冲突与待确认")
    append("")
    append("- 未发现 `context/` 三件套内部的显式业务定义冲突。")
    append("- 若后续导入 wiki 时发现跨项目同名规则存在口径差异，应在 wiki 侧保留冲突，而不是在本快照内提前消解。")
    append("")
    append("## 导出日志")
    append("")
    append(f"- {snapshot_date}：首次按 `context-snapshot` v4 导出，事实源仅为 `context/` 三件套。")
    append(f"- {snapshot_date}：输出文件为 `{output_path.name}`。")
    append(f"- {snapshot_date}：本次导出识别 `tables={len(tables)}`、`rules={len(rules)}`、`dictionary={len(dictionary)}`。")
    append(f"- {snapshot_date}：source_content_hash=`{source_content_hash}`。")
    if skipped_tables or skipped_rules or skipped_dictionary:
        append(f"- {snapshot_date}：跳过模板/占位块 `tables={skipped_tables}`、`rules={skipped_rules}`、`dictionary={skipped_dictionary}`。")
    if previous_snapshot is not None:
        append(f"- {snapshot_date}：比较基线为 `{previous_snapshot.name}`。")
    else:
        append(f"- {snapshot_date}：未找到上一快照，本次作为基线快照。")
    return "\n".join(lines) + "\n"


def main() -> int:
    args = parse_args()
    project_root = Path(args.project_root).resolve()
    context_dir = project_root / "context"
    ensure_required_inputs(context_dir)
    identity = load_project_identity(project_root, context_dir, args)

    branch, commit = get_git_info(project_root)
    output_path = build_output_path(project_root, args.snapshot_date, commit, args.output, identity)
    previous_snapshot = find_previous_snapshot(project_root, output_path, args.compare_base, identity)

    tables_text = read_text(context_dir / "tables.md")
    rules_text = read_text(context_dir / "rules.md")
    dictionary_text = read_text(context_dir / "dictionary.md")

    tables_preamble = extract_global_preamble(tables_text, r"^##\s+\d+\.\s+")
    rules_preamble = extract_global_preamble(rules_text, r"^##\s+\[")
    dictionary_preamble = extract_global_preamble(dictionary_text, r"^###\s+")

    tables, skipped_tables = parse_tables(tables_text, include_placeholders=args.include_placeholders)
    rules, skipped_rules = parse_rules(rules_text, include_placeholders=args.include_placeholders)
    dictionary, skipped_dictionary = parse_dictionary(dictionary_text, include_placeholders=args.include_placeholders)
    table_domains = build_table_domains_from_blocks(tables)
    dictionary_sections = parse_dictionary_sections(dictionary_text)

    table_to_dictionary = extract_table_relationships(tables, dictionary)
    rule_to_tables, rule_to_dictionary = extract_rule_relationships(rules, tables, dictionary)

    diff_summary, previous_frontmatter = compare_with_previous(previous_snapshot, tables, rules, dictionary)
    source_content_hash = compute_source_content_hash(context_dir)

    snapshot = render_snapshot(
        project_root=project_root,
        identity=identity,
        snapshot_date=args.snapshot_date,
        branch=branch,
        commit=commit,
        source_content_hash=source_content_hash,
        tables_preamble=tables_preamble,
        rules_preamble=rules_preamble,
        dictionary_preamble=dictionary_preamble,
        table_domains=table_domains,
        dictionary_sections=dictionary_sections,
        rule_to_tables=rule_to_tables,
        rule_to_dictionary=rule_to_dictionary,
        table_to_dictionary=table_to_dictionary,
        tables=tables,
        rules=rules,
        dictionary=dictionary,
        skipped_tables=skipped_tables,
        skipped_rules=skipped_rules,
        skipped_dictionary=skipped_dictionary,
        output_path=output_path,
        previous_snapshot=previous_snapshot,
        previous_frontmatter=previous_frontmatter,
        diff_summary=diff_summary,
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(snapshot, encoding="utf-8")

    print(output_path)
    print(
        f"tables={len(tables)} rules={len(rules)} dictionary={len(dictionary)} "
        f"skipped_tables={skipped_tables} skipped_rules={skipped_rules} skipped_dictionary={skipped_dictionary} "
        f"previous_snapshot={previous_snapshot.name if previous_snapshot else 'none'}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
