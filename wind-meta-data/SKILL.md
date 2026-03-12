---
name: wind-meta-data
description: Use when querying Wind metadata, table names, field names, business keys, schema, or data-source mappings for funds, stocks, indices, or related cross-domain indicators.
---

# Wind Meta Data

## Overview

Use this skill to answer questions about Wind metadata rather than performing live Wind data extraction.

This skill is optimized for progressive lookup:
1. Use L1 indexes to locate candidate tables quickly
2. Use L2 summaries to confirm table purpose and business keys
3. Use the L3 script only when field-level detail is required

Always prefer the lightest layer that can answer the question.

## When To Use

Use this skill when the user asks any of the following:

- Which Wind table stores an indicator
- What a table or field means
- What the business key is for a table
- How to map a metric to a Wind schema
- Which fund or stock table should be used
- What field should be used for a specific metric
- Questions containing `Wind`, `schema`, `metadata`, `元数据`, `表结构`, `字段`, `主键`, `口径`

Do not use this skill for:

- Actually downloading Wind data
- Writing SQL or ETL logic unless the question is about schema mapping
- Non-Wind data providers

## Progressive Query Flow

1. First classify the query as `fund`, `stock`, or cross-domain.
2. For lookup-style questions, read only the relevant L1 index in `data/`.
3. If the answer needs table meaning, frequency, or business keys, then read the relevant L2 summary.
4. If the answer needs exact field names or field descriptions, run:

```bash
python scripts/query_l3.py --domain fund --table "中国共同基金净值"
python scripts/query_l3.py --domain stock --table "AShareAnnText"
python scripts/query_l3.py --domain fund --table "ChinaMutualFundNAV" --contains "复权"
```

5. Only cite field names that came from L2 text or the L3 script output.

## Domain Selection

Choose the default domain like this:

- Prefer `fund` for queries mentioning `基金`, `净值`, `分红`, `持仓`, `久期`, `共同基金`, `指数基金`
- Prefer `stock` for queries mentioning `A股`, `个股`, `公告`, `财报`, `行业`, `成分股`, `行情`
- For queries mentioning `指数`, `Wind代码`, `元数据`, `主键`, `取数口径`, start from both L1 indexes if needed

## Output Format

Answer in this order when possible:

1. Recommended table
2. Why this table fits
3. Key business key or join key
4. Key fields
5. Which knowledge layer was used: `L1`, `L2`, or `L3`
6. Version note, for example:
   `当前依据 wind-meta-data skill v1.0.0 / kb v1.0.0`

If the result is still ambiguous, ask the user to narrow one of:

- metric name
- table name
- field keyword
- domain (`fund` or `stock`)

## Common Queries

- `基金复权净值在哪张表？`
- `ChinaMutualFundNAV 的主键是什么？`
- `998031.TX 的日行情在哪张表？`
- `Wind 里基金久期有没有现成字段？`
- `某个字段是什么意思？`

## Files

- L1 indexes: `data/wind_fund_L1_index.md`, `data/wind_stock_L1_index.md`
- L2 summaries: `data/wind_fund_L2_summary.md`, `data/wind_stock_L2_summary.md`
- L3 full metadata: `data/wind_fund_L3_full.json`, `data/wind_stock_L3_full.json`
- Version file: `VERSION.json`
- File manifest: `data/MANIFEST.json`
- Test cases: `test-cases.md`

Use `reference.md` for detailed lookup guidance and edge cases.
Use `test-cases.md` for trigger checks, layered lookup validation, and regression tests.
