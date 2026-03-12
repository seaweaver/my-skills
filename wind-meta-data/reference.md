# Wind Meta Data Reference

## Query Strategy

### L1: fast table discovery

Use L1 when the user asks:

- 哪张表
- 有没有现成表
- 某个指标在哪
- 哪个表更合适

Goal:

- locate 1 to 3 candidate tables quickly

### L2: table semantics and business keys

Use L2 when the user asks:

- 表的用途
- 更新频率
- 是否全量产品
- 业务主键
- 表之间如何初步关联

Goal:

- confirm the best table
- provide business key or join key
- avoid escalating to L3 unless needed

### L3: exact fields

Use L3 only when the user asks:

- 字段名是什么
- 某字段中文含义
- 这个表都有哪些字段
- 要精确到字段级 mapping

Goal:

- return exact field-level evidence

## Recommended Answer Style

Prefer this template:

```text
推荐表：<中文表名> (<英文表名>)
原因：<为什么选这张表>
主键/连接键：<业务主键>
关键字段：<字段列表>
依据层级：L1 / L2 / L3
版本：wind-meta-data skill vX.Y.Z / kb vA.B.C
```

If multiple tables are plausible:

1. state the top recommendation
2. list 1 to 2 alternatives
3. explain the selection difference

## L3 Script Notes

Examples:

```bash
python scripts/query_l3.py --domain fund --table "中国共同基金净值"
python scripts/query_l3.py --domain fund --table "ChinaMutualFundNAV"
python scripts/query_l3.py --domain fund --table "ChinaMutualFundNAV" --contains "复权"
python scripts/query_l3.py --domain stock --table "AShareAnnText" --contains "正文"
```

Matching order:

1. exact Chinese table name
2. exact English table name
3. Chinese name contains the query
4. English name contains the query

If there are too many matches:

- tell the user to provide a more exact table name or field keyword

## Known Boundaries

- This skill does not execute Wind terminal downloads.
- This skill only explains metadata, schema, mappings, and table usage.
- If L1 and L2 disagree with user expectation, trust the knowledge base files rather than guessing.
- If a field is not found in L3, say so explicitly.

## Versioning

- `VERSION.json` is the source of truth for current skill and KB versions.
- `data/MANIFEST.json` is the source of truth for packaged knowledge-base files.
- `CHANGELOG.md` records release history.
- `test-cases.md` records recommended manual and script-level validation scenarios.
