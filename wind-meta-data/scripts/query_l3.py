#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
VERSION_FILE = ROOT / "VERSION.json"

DOMAIN_FILES = {
    "fund": DATA_DIR / "wind_fund_L3_full.json",
    "stock": DATA_DIR / "wind_stock_L3_full.json",
}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_version() -> dict[str, Any]:
    return load_json(VERSION_FILE)


def normalize(text: str) -> str:
    return text.casefold().strip()


def get_business_keys(fields: list[dict[str, Any]]) -> list[str]:
    keys: list[str] = []
    for field in fields:
        if field.get("is_biz_key"):
            name_en = field.get("name_en", "")
            name_cn = field.get("name_cn", "")
            if name_cn and name_en:
                keys.append(f"{name_en} ({name_cn})")
            elif name_en:
                keys.append(name_en)
            elif name_cn:
                keys.append(name_cn)
    return keys


def score_table(query: str, table_name_cn: str, table_info: dict[str, Any]) -> tuple[int, str]:
    q = normalize(query)
    name_cn = normalize(table_name_cn)
    name_en = normalize(str(table_info.get("name_en", "")))

    if q == name_cn:
        return 0, "中文表名精确匹配"
    if q == name_en:
        return 1, "英文表名精确匹配"
    if q in name_cn:
        return 2, "中文表名包含匹配"
    if q in name_en:
        return 3, "英文表名包含匹配"
    return 99, ""


def match_tables(data: dict[str, Any], table_query: str) -> list[tuple[str, dict[str, Any], int, str]]:
    matches: list[tuple[str, dict[str, Any], int, str]] = []
    for table_name_cn, table_info in data.items():
        score, rule = score_table(table_query, table_name_cn, table_info)
        if score < 99:
            matches.append((table_name_cn, table_info, score, rule))
    matches.sort(key=lambda item: (item[2], normalize(item[0])))
    return matches


def filter_fields(fields: list[dict[str, Any]], keyword: str | None) -> list[dict[str, Any]]:
    if not keyword:
        return fields
    q = normalize(keyword)
    result: list[dict[str, Any]] = []
    for field in fields:
        values = [
            str(field.get("name_cn", "")),
            str(field.get("name_en", "")),
            str(field.get("desc", "")),
            str(field.get("related_field", "")),
            str(field.get("type", "")),
        ]
        if any(q in normalize(value) for value in values):
            result.append(field)
    return result


def render_table(
    domain: str,
    table_name_cn: str,
    table_info: dict[str, Any],
    version: dict[str, Any],
    field_keyword: str | None,
    limit: int,
    matched_by: str,
) -> str:
    name_en = table_info.get("name_en", "")
    desc = table_info.get("desc", "")
    freq = table_info.get("freq", "")
    update_time = table_info.get("update_time", "")
    fields = table_info.get("fields", []) or []
    biz_keys = get_business_keys(fields)
    matched_fields = filter_fields(fields, field_keyword)[:limit]

    lines = [
        f"命中表：{table_name_cn}",
        f"英文表名：{name_en or '(无)'}",
        f"匹配方式：{matched_by}",
        f"说明：{desc or '(无)'}",
        f"更新频率：{freq or '(无)'}",
        f"更新时间：{update_time or '(无)'}",
        f"业务主键：{', '.join(biz_keys) if biz_keys else '(未标注)'}",
        f"知识库域：{domain}",
        (
            "版本："
            f"wind-meta-data skill v{version['skill_version']} / "
            f"kb v{version['kb_version']}"
        ),
    ]

    if field_keyword:
        lines.append(f"字段筛选关键字：{field_keyword}")

    if matched_fields:
        lines.append("字段列表：")
        for field in matched_fields:
            name_cn = field.get("name_cn", "")
            name_en_field = field.get("name_en", "")
            field_type = field.get("type", "")
            related = field.get("related_field", "")
            field_desc = field.get("desc", "")
            parts = [f"- {name_en_field or '(无英文名)'}"]
            if name_cn:
                parts.append(f"({name_cn})")
            if field_type:
                parts.append(f"[{field_type}]")
            if related:
                parts.append(f"关联字段: {related}")
            if field_desc:
                parts.append(f"- {field_desc}")
            lines.append(" ".join(parts))
    else:
        if field_keyword:
            lines.append("字段列表：未找到匹配字段")
        else:
            lines.append("字段列表：未请求字段筛选，可加 --contains 进一步精查")

    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Query packaged Wind L3 metadata by table.")
    parser.add_argument("--domain", required=True, choices=sorted(DOMAIN_FILES.keys()))
    parser.add_argument("--table", required=True, help="Chinese or English table name")
    parser.add_argument("--contains", help="Optional field keyword filter")
    parser.add_argument("--limit", type=int, default=50, help="Max returned fields or tables")
    args = parser.parse_args()

    version = load_version()
    data = load_json(DOMAIN_FILES[args.domain])
    matches = match_tables(data, args.table)

    if not matches:
        print(f"未在 {args.domain} L3 知识库中定位到表：{args.table}")
        print(
            "版本："
            f"wind-meta-data skill v{version['skill_version']} / "
            f"kb v{version['kb_version']}"
        )
        return 1

    if len(matches) > 1:
        print(f"命中 {len(matches)} 张候选表，请优先缩小范围。以下展示前 {min(args.limit, len(matches))} 条：")
        for table_name_cn, table_info, _, matched_by in matches[: args.limit]:
            print(f"- {table_name_cn} ({table_info.get('name_en', '')}) [{matched_by}]")
        print(
            "版本："
            f"wind-meta-data skill v{version['skill_version']} / "
            f"kb v{version['kb_version']}"
        )
        return 0

    table_name_cn, table_info, _, matched_by = matches[0]
    print(render_table(args.domain, table_name_cn, table_info, version, args.contains, args.limit, matched_by))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
