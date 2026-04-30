---
name: context-snapshot
description: Export a data project's context/tables.md, context/rules.md, and context/dictionary.md into one self-contained markdown snapshot. Use when a repository keeps standardized context files and needs a single fact-complete artifact for wiki ingestion, project handoff, cross-project comparison, or knowledge consolidation.
---

# Context Snapshot

Export one project's `context/` knowledge into one self-contained markdown snapshot.

The snapshot is an export artifact for downstream systems such as a wiki. It must
remain understandable even when the downstream system cannot access the original
project repository.

## When to Use

Use this skill when:
- A repository has a stable `context/` folder with `tables.md`, `rules.md`, and `dictionary.md`
- The user wants a single markdown export instead of multiple source files
- The export will later be ingested into a wiki, handed to another agent, or compared with snapshots from other projects
- Multiple data projects share the same context template and need comparable outputs

Do not use this skill when:
- The user only wants to edit the original `context/` files in place
- The repository does not use the standard three-file context structure
- The output should be a database row, spreadsheet, or CMS entry instead of markdown

## Fact Boundary

By default, the only fact sources are:
- `context/tables.md`
- `context/rules.md`
- `context/dictionary.md`

Do not introduce `README.md`, `CLAUDE.md`, reports, slides, or other files into
the exported fact set unless the user explicitly widens the scope.

Non-context files may help an operator understand the project, but they are not
part of the snapshot's canonical fact source by default.

## Role Boundary with the Wiki

This skill is the upstream producer of a wiki-ready knowledge snapshot.

Its job is to turn project-local context files into one reusable knowledge
artifact without making the downstream wiki depend on project-specific folder
layouts or ad hoc operator judgment.

This skill is responsible for:

1. Locking the fact boundary to the project's canonical context sources
2. Filtering placeholders, teaching stubs, and non-factual noise
3. Producing one self-contained snapshot that can be understood without reopening the source repository
4. Adding structure-level knowledge such as global notes, section overviews, relationship indexes, merge notes, and explicit conflicts
5. Emitting stable identity, version, and diff semantics so repeated exports can be compared over time
6. Shaping the output into wiki-friendly knowledge units without performing downstream canonicalization on behalf of the wiki

The downstream wiki should only need to recognize that this artifact is
self-contained, traceable, and incrementally versioned. It should not need a
separate import-adapter layer that knows project-specific context internals.

## Core Contract

Produce exactly one primary output markdown file per export.

Default file naming pattern:

```text
<项目显示名或项目标识>-知识快照-<YYYY-MM-DD>-<commit短哈希>.md
```

If the user specifies a different output path or naming convention, follow that.

## Project Identity and Chinese Naming

Prefer a Chinese business-facing project name for snapshot titles and filenames.

If the project directory name is technical or unclear, do not let the directory
name become the human-facing snapshot name.

Preferred identity source order:

1. Explicit exporter CLI arguments
2. Existing `context/manifest.yml` only if the project already maintains one
3. Semantic inference from `context/tables.md`, `context/rules.md`, and `context/dictionary.md`
4. README H1 as a display-name fallback only
5. Project directory name

Do not add `context/manifest.yml` to a source project just to satisfy a one-off
export unless the user explicitly wants that project to maintain an identity
file.

Project identity is metadata for naming, tracing, and downstream search. It is
not part of the knowledge fact set. The fact boundary remains
`context/tables.md`, `context/rules.md`, and `context/dictionary.md`.

Default no-project-mutation command:

```powershell
$p = Get-Item -LiteralPath 'D:\path\to\project'
python scripts/export_context_snapshot.py --project-root $p.FullName
```

The exporter should infer a Chinese display name from the context files when
they contain stable semantic headings. For example, `营销域物理模型定义` and
`营销域业务逻辑库` imply `营销域数据分析项目`.

Explicit override command:

```powershell
$p = Get-Item -LiteralPath 'D:\path\to\project'
python scripts/export_context_snapshot.py `
  --project-root $p.FullName `
  --project-name '营销域数据分析项目' `
  --project-code 'data_project' `
  --snapshot-prefix '营销域数据分析项目' `
  --domain '营销域' `
  --alias 'data_project'
```

Use explicit CLI identity arguments only when the inferred name is wrong or the
user has provided a preferred name.

The Python exporter applies these values deterministically; do not ask the model
to freehand rewrite the final snapshot body after export.

Minimal manifest example:

```yaml
project_id: retail-marketing-data-workbench
project_name: 零售营销域数据分析工作台
project_short_name: 营销域数据工作台
project_code: data_project
snapshot_prefix: 零售营销域数据分析工作台
domain: 零售营销域
aliases:
  - data_project
  - 营销域数据项目
```

Use the reusable template in
[templates/项目身份清单模板.yml](templates/项目身份清单模板.yml) when initializing a
project manifest.

Field semantics:
- `project_id`: stable machine-readable identity; use ASCII when possible
- `project_name`: Chinese display name used in `title`, frontmatter, and H1
- `project_code`: technical project code or source repository name
- `snapshot_prefix`: filename prefix; defaults to `project_name`
- `domain`: business domain for later wiki classification
- `aliases`: Chinese and technical names that downstream wiki search may need

If no manifest exists, the exporter remains backward-compatible and falls back to
the project directory name.

## Required Inputs

All three files are required:
- `context/tables.md`
- `context/rules.md`
- `context/dictionary.md`

Optional project identity file:
- `context/manifest.yml`, `context/manifest.yaml`, or `context/manifest.json`

Optional project identity arguments:
- `--project-name`
- `--project-id`
- `--project-code`
- `--snapshot-prefix`
- `--domain`
- `--alias`

If any required file is missing, stop and report the gap clearly.

## Deterministic Execution Rule

Use the Python exporter in [scripts/export_context_snapshot.py](scripts/export_context_snapshot.py)
for the actual snapshot generation.

The script is the primary execution path. The model should not freehand-author the
final snapshot body when the script can run.

Preferred command pattern on this Windows machine:

```powershell
$p = Get-Item -LiteralPath 'D:\path\to\project'
python scripts/export_context_snapshot.py --project-root $p.FullName
```

Why:
- It keeps exports consistent across models
- It avoids lossy summarization caused by model compression
- It handles Chinese paths more reliably when PowerShell resolves the path first

Only fall back to a manual draft if the script is unavailable and the user still
wants a temporary prototype. If you do fall back, clearly label it as a temporary,
non-canonical export.

## Output Standard

The snapshot must be self-contained.

That means:
- A future wiki ingest should be possible from the snapshot alone
- `source_refs` are only for traceability, not for carrying missing meaning
- Each exported table, rule, and dictionary item must keep enough detail to stand alone

Bad output:
- A thin catalog that only lists names and says "see context/rules.md"
- A summary that drops SQL logic, matching logic, key fields, or important caveats
- A file that requires the downstream reader to reopen the original project to understand the facts

Good output:
- A single markdown file that preserves detailed table facts, rule facts, and dictionary facts
- A file that can be ingested into a wiki even if the original project is unavailable
- A file that still records source references for audit and traceability

## Anti-Compression Rule

The exporter must preserve facts, not just summaries.

Required behavior:
- Keep the original fact block for each table, rule, and dictionary item in `原始事实摘录`
- Add a compact `结构化事实` section, but do not let it replace the raw block
- Preserve repeated blocks when they add detail; merge only after checking content
- Do not rewrite a detailed rule into one sentence if the source contains SQL logic, caveats, mappings, or multiple conditions

Quick test:

If the downstream wiki only sees this one file, can it still understand the item
without reopening the source project?

If the answer is no, the export is too thin.

## Long-Term Snapshot Evolution

The exporter must support repeated snapshot generation over time.

Required behavior:
- Generate stable `project_id`, `snapshot_id`, and `source_content_hash`
- Detect the previous snapshot when available
- Emit a `与上一快照差异` section
- Mark current items with deterministic `change_type` values such as `baseline`, `new`, `updated`, or `unchanged`
- Keep removal information in the diff section instead of silently forgetting old knowledge

## Placeholder and Template Filtering

The exporter must detect and skip template placeholders, example skeletons, and
teaching stubs.

Common examples that must not appear in a canonical snapshot:
- `[表名] (中文名)`
- `Schema.TableName`
- `PK_Column`
- `Term_ID`
- `[R01] 规则名称 (Rule Name)`
- `一句话描述业务含义`
- `<key>: <value>`

If a source project mixes real knowledge with template examples:
- Keep the real knowledge
- Drop the placeholder blocks
- Record the filtering result in the export log when helpful

## Normalization Rules

Apply these rules during export:

1. Merge duplicates inside the same project snapshot
2. Do not silently delete conflicting definitions; surface them explicitly
3. Preserve stable identifiers from the source project whenever they exist
4. Preserve enough factual detail for standalone use
5. Prefer structured extraction over vague summaries

Identity rules:
- Tables use physical table names as primary identifiers
- Rules use rule IDs such as `R_Employee_Attribution`
- Dictionary items use namespace or term-group names such as `chn_num`

## Duplicate Handling

When the same logical item appears multiple times in one project:

- If the content is identical, keep one consolidated item and record all source refs
- If the content differs but is compatible, keep one consolidated item and preserve the extra detail in a `补充摘录` or `变体说明`
- If the content is incompatible, mark it under `冲突与待确认`

Never drop a repeated block without checking whether it adds detail.

## Cross-Project Safety Rule

This skill exports one project snapshot at a time.

It may merge duplicates inside one project, but it must not resolve
cross-project conflicts as if one project were globally authoritative.

When preparing content for later cross-project consolidation:
- Keep project identity in each item's metadata
- Use `exact`, `variant`, `conflict`, or `project-only` as status labels when helpful
- Leave final canonicalization to the downstream wiki workflow

## Recommended Snapshot Structure

The snapshot should contain:

1. Frontmatter manifest
2. Export boundary and source declaration
3. `项目级全局知识`
4. `知识结构导览`
5. `关系索引`
6. `与上一快照差异`
7. `Tables｜数据对象`
8. `Rules｜业务规则`
9. `Dictionary｜字典与术语`
10. `项目内重复合并说明`
11. `冲突与待确认`
12. `导出日志`

Use the template in [templates/项目知识快照模板.md](templates/项目知识快照模板.md).

## Required Frontmatter Fields

The snapshot frontmatter must include at least:
- `title`
- `type: project_context_snapshot`
- `project_id`
- `project_name`
- `project_code`
- `source_repo_name`
- `snapshot_prefix`
- `snapshot_id`
- `snapshot_date`
- `snapshot_sequence`
- `exported_at`
- `source_repo`
- `source_branch`
- `source_commit`
- `source_content_hash`
- `previous_snapshot`
- `supersedes`
- `source_files`
- `export_spec_version`
- `status`

`source_files` should normally list only the three context files.

When available, also include:
- `project_short_name`
- `domain`
- `project_aliases`

For non-git projects:
- `source_branch` may be `n/a`
- `source_commit` may be `no-git`
- `source_content_hash` becomes the primary version fingerprint

## Required Item Detail Level

### Tables

Each exported table item should preserve enough detail to answer:
- What is this table
- Which platform stores it
- What are the key fields
- What are the preset join paths
- What are the usage notes or restrictions

### Rules

Each exported rule item should preserve enough detail to answer:
- What the rule means
- When to use it
- What inputs and outputs matter
- What the key logic or SQL template is
- What caveats or special conditions apply

### Dictionary

Each exported dictionary item should preserve enough detail to answer:
- What namespace or term-group it defines
- Which representative values matter
- What matching or naming rules apply
- What constraints or usage notes matter

## Source Reference Format

Use source references only for traceability, for example:
- `context/rules.md#L120-L206`
- `context/tables.md :: [订单表] (DWD_CUST_PR_DTL_DI)`
- `context/dictionary.md :: 渠道编码 (chn_num)`

But remember:
- `source_refs` do not replace factual content
- The exported body must remain understandable without opening the source files

## Quality Gates

Before declaring the export complete, verify all of the following:

- No `supporting_files` field was added unless the user explicitly widened scope
- No placeholder blocks remain in the snapshot
- No item is reduced to a one-line summary plus `source_refs`
- The script generated the file successfully
- If a Chinese project name is supplied or inferred from context files, the output filename and frontmatter use it
- The output file can be opened and sampled locally

## Common Mistakes

- Treating `README.md` as an equal fact source
- Exporting a catalog instead of a fact-complete snapshot
- Dropping rule IDs or physical table names during summarization
- Keeping only one-line descriptions for complex rules
- Using `source_refs` as a substitute for the missing body of the rule
- Leaving template sample blocks in the final export
- Using a technical folder name such as `data_project` as the human-facing project name when a Chinese context-derived, CLI, manifest, or README name is available
- Adding `context/manifest.yml` to a source project when the user only wanted a one-off export identity

## Quick Decision Rule

When unsure whether the exported content is detailed enough, ask:

"If the downstream wiki only sees this one file, can it still understand the rule, object, or dictionary item without reopening the project?"

If the answer is no, the snapshot is too thin.
