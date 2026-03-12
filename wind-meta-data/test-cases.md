# Wind Meta Data Test Cases

## Overview

Use these cases to verify three things:

1. The skill is discoverable for the right prompts
2. The skill follows the L1 -> L2 -> L3 progressive lookup path
3. Query results are traceable to the current skill and knowledge-base versions

## Expected Baseline

Before running tests, confirm:

- `VERSION.json` exists and can be read
- `data/MANIFEST.json` includes all 6 packaged knowledge-base files
- `scripts/query_l3.py` runs with Python

## A. Trigger Tests

These prompts should trigger `wind-meta-data` automatically.

1. `Wind 里基金复权净值在哪张表？`
2. `中国共同基金基本资料的主键是什么？`
3. `998031.TX 的日行情查哪个表？`
4. `基金久期在 Wind 里有没有现成表？`
5. `某个指标字段名我忘了，帮我查一下`
6. `Wind 的 schema 里基金分类表怎么找？`
7. `Wind metadata 里公告正文字段在哪张表？`

Pass criteria:

- The skill is used without needing the user to say `fund` or `stock`
- The answer is clearly about Wind metadata rather than live data download

## B. L1 Lookup Tests

Use these prompts to verify that simple location queries can stop at L1.

1. `基金净值在哪张表？`
2. `基金分类表在哪？`
3. `公告文本在哪张表？`
4. `Wind 代码映射表是什么？`

Pass criteria:

- The answer recommends one or a few candidate tables
- The answer states it is based on L1 when that is enough
- It does not dump field lists

## C. L2 Lookup Tests

Use these prompts to verify that table description and key questions escalate to L2.

1. `ChinaMutualFundNAV 的主键和更新频率是什么？`
2. `中国共同基金净值这张表是干什么的？`
3. `AShareAnnText 的业务主键是什么？`
4. `基金分类表怎么用？`

Pass criteria:

- The answer includes table purpose
- The answer includes business key or join key
- The answer indicates the result came from L2 or L1+L2

## D. L3 Field Tests

Use these prompts to verify that exact field questions escalate to the script.

1. `ChinaMutualFundNAV 的复权单位净值字段叫什么？`
2. `中国共同基金净值里复权因子字段是什么？`
3. `AShareAnnText 里公告正文字段叫什么？`
4. `中国共同基金基本资料有哪些字段和成立日期有关？`

Recommended script checks:

```bash
python scripts/query_l3.py --domain fund --table "ChinaMutualFundNAV" --contains "复权"
python scripts/query_l3.py --domain stock --table "AShareAnnText" --contains "正文"
python scripts/query_l3.py --domain fund --table "中国共同基金基本资料" --contains "成立"
```

Pass criteria:

- Field names are returned exactly
- Field answers come from L3 output rather than guessing
- Output includes current version information

## E. Domain Routing Tests

Verify the skill can choose the correct domain automatically.

### Fund-first prompts

1. `基金分红字段在哪张表？`
2. `基金久期有没有现成字段？`
3. `共同基金净值主键是什么？`

### Stock-first prompts

1. `A股公告正文在哪张表？`
2. `行业代码表在哪里？`
3. `个股行情相关字段怎么找？`

### Cross-domain prompts

1. `Wind 代码映射表是什么？`
2. `指数日行情一般查哪个表？`
3. `元数据里主键怎么查？`

Pass criteria:

- Fund prompts prefer fund KB
- Stock prompts prefer stock KB
- Cross-domain prompts can inspect both sides before concluding

## F. Fallback And Ambiguity Tests

Use these prompts to verify graceful fallback.

1. `Wind 里有 alpha_exposure_7d 这个字段吗？`
2. `帮我找一个和收益很像的表`
3. `我要查那个表，就是你知道的那个`

Pass criteria:

- If not found, the answer explicitly says L1/L2/L3 did not confirm it
- The answer asks the user to narrow by metric, table, field keyword, or domain
- The answer does not invent tables or fields

## G. Version Traceability Tests

Use any successful query and verify that the answer includes:

- current `skill_version`
- current `kb_version`

Recommended checks:

1. `Wind 里基金复权净值在哪张表？`
2. `ChinaMutualFundNAV 的复权单位净值字段叫什么？`

Pass criteria:

- Every answer includes a version note
- L3 answers clearly indicate field-level results came from L3

## H. Regression Checklist

Run these checks after any knowledge-base update or skill change.

1. `VERSION.json` was updated correctly
2. `CHANGELOG.md` includes the new release note
3. `data/MANIFEST.json` reflects current file sizes and hashes
4. Fund L3 query still works
5. Stock L3 query still works
6. One L1-only prompt and one L2 prompt still behave as expected

## Suggested Smoke Test Commands

```bash
python scripts/query_l3.py --domain fund --table "ChinaMutualFundNAV" --contains "复权"
python scripts/query_l3.py --domain stock --table "AShareAnnText" --contains "正文"
python scripts/query_l3.py --domain fund --table "不存在的表"
```

Expected outcomes:

- First two commands return exact matches
- The third command returns a clear not-found message and version info
