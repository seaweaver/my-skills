---
name: cf-quant-web
description: Use when querying strategy positions, importing trading signals, looking up strategy metadata, checking performance metrics, or creating backups through the local cf_quant_web HTTP backend.
---

# CF Quant Web

## 概述

通过 HTTP 与本地 `cf_quant_web` 后端（FastAPI）交互。
Agent 与后端在同一台机器上运行时，使用本技能。

- 不要使用 MCP
- 不要直接访问数据库
- 无需认证，所有接口均为开放访问

## Base URL

```
http://127.0.0.1:8000
```

所有端点以 `/api` 开头，完整示例：`http://127.0.0.1:8000/api/positions`。

健康检查：`GET /api/health`

## 能力范围

| # | 能力 | 端点 |
|---|------|------|
| 1 | 查询策略持仓 | `GET /api/positions` |
| 2 | 导入交易信号 | `POST /api/signals/batch` 等 |
| 3 | 查询策略信息 | `GET /api/strategies` |
| 4 | 查看绩效指标 | `GET /api/performance/metrics/{strategy_id}` |
| 5 | 数据库备份 | `POST /api/backup` / `GET /api/backup/list` |

不要用本技能处理交割单导入、对账匹配或其他手工流程。

---

## 能力 1：查询策略持仓

`GET /api/positions`

### 参数

| 参数 | 类型 | 说明 |
|------|------|------|
| `strategy_id` | int | 策略 ID（与 strategy_code 二选一） |
| `strategy_code` | string | 策略代码（与 strategy_id 二选一） |
| `security_code` | string | 证券代码过滤（模糊匹配） |

仅返回 `quantity > 0` 的持仓。

### 示例

```bash
curl -s "http://127.0.0.1:8000/api/positions?strategy_code=nice-us"
```

### 响应结构

```json
[
  {
    "id": 1,
    "strategy_id": 1,
    "strategy_code": "nice-us",
    "strategy_name": "美股精选",
    "security_code": "NVDA",
    "security_name": "英伟达",
    "quantity": 100,
    "available_quantity": 100,
    "avg_cost": 110.25,
    "total_cost": 11025.00,
    "current_price": 120.50,
    "market_value": 12050.00,
    "unrealized_pnl": 1025.00,
    "entry_date": "2026-01-15",
    "last_updated": "2026-03-12T15:30:00"
  }
]
```

### 展示重点

向用户汇报时聚焦：`strategy_code`、`security_code`、`security_name`、`quantity`、`avg_cost`、`market_value`、`unrealized_pnl`。

### 其他持仓端点

| 端点 | 说明 |
|------|------|
| `GET /api/positions/summary?strategy_id=1` | 持仓汇总（持仓数、总成本、总市值、浮盈） |
| `GET /api/positions/history/{strategy_id}/{security_code}` | 单只证券的交易历史 |

---

## 能力 2：导入交易信号

三种导入方式，按优先级选择：

| 方式 | 端点 | 适用场景 |
|------|------|---------|
| JSON 批量 | `POST /api/signals/batch` | Agent 已解析好结构化数据，首选 |
| 文本粘贴 | `POST /api/signals/import-text` | 用户直接粘贴信号文本 |
| 文件上传 | `POST /api/signals/import` | 用户提供 txt/csv 文件 |

### 幂等导入硬规则

下面这些规则是强制项，不是建议项：

1. 导入前必须先查重，不能直接调用 `POST /api/signals/batch`、`POST /api/signals/import-text` 或 `POST /api/signals/import`。
2. 查重失败、策略不存在、或批内存在冲突时，必须停止导入并向用户说明原因。
3. 重复判定键固定为：`strategy_id + signal_date + security_code + direction`。
4. 只要后端已存在任意状态的同键信号（`PENDING`、`EXECUTED`、`CANCELLED` 等），就视为“已导入”，直接跳过，不要重复发送 `POST`。
5. 如果所有候选信号都已存在，允许“只查询、不导入”，并明确告诉用户：`已存在，未重复导入`。
6. Agent 对外汇报统一使用：
   - `已跳过 N 条重复`
   - `准备导入 M 条新增`
   - 如果 `M=0`，明确说 `已存在，未重复导入`

### 标准导入流程

无论最终使用 JSON、文本粘贴还是文件上传，都先按下面流程执行：

1. 如果用户只给了 `strategy_code`，先查策略：
   ```bash
   curl -s "http://127.0.0.1:8000/api/strategies/code/nice-us"
   ```
2. 取到 `strategy_id` 后，再处理候选信号；如果策略不存在，立即停止，不要猜。
3. 先把所有证券代码标准化后再查重，不要依赖后端兜底。
4. 先做批内去重和冲突检查。
5. 再调用 `GET /api/signals` 查询后端已有信号。
6. 只把未命中的增量信号组装进最终的导入请求。

### 批内去重与冲突处理

批内先按同一组 key：`strategy_id + signal_date + security_code + direction` 分组。

- 同键且 `expected_price`、`expected_quantity`、`signal_name`、`scale`、`remark` 全部一致：折叠为 1 条。
- 同键但上述字段有任意不一致：视为冲突，必须停止并让用户确认，不能私自选一条继续导入。
- 对文本粘贴或文件导入，先完成解析和标准化，再应用同一套规则。

### 导入前查重步骤

对每一条候选信号，按下面顺序执行：

1. 获取或确认 `strategy_id`
2. 标准化 `security_code`
3. 查询：
   ```bash
   curl -s "http://127.0.0.1:8000/api/signals?strategy_id=1&signal_date=2026-03-12&security_code=NVDA&limit=1000"
   ```
4. 在返回结果里按 `direction` 精确比对
5. 命中同键同方向记录则跳过；未命中才允许进入导入请求

> `GET /api/signals` 的查询参数里没有单独的 `direction` 过滤，所以必须先按 `strategy_id + signal_date + security_code` 查询，再在返回结果里按 `direction` 做精确匹配。

### 方式 A：JSON 批量（`POST /api/signals/batch`）

JSON 批量是首选。只有在完成上面的查重步骤后，才允许提交增量数据。

请求体：

```json
{
  "signals": [
    {
      "strategy_id": 1,
      "signal_date": "2026-03-12",
      "security_code": "NVDA",
      "direction": "BUY",
      "expected_price": 120.5,
      "order_type": "LIMIT"
    }
  ]
}
```

**字段说明：**

| 字段 | 必填 | 说明 |
|------|------|------|
| `strategy_id` | 是 | 策略 ID |
| `signal_date` | 是 | 信号日期 YYYY-MM-DD |
| `security_code` | 是 | 证券代码，必须先由 Agent 标准化 |
| `direction` | 是 | `BUY` 或 `SELL` |
| `expected_price` | 否 | 预期价格 |
| `expected_quantity` | 否 | 预期数量 |
| `order_type` | 否 | 默认 `LIMIT` |
| `target_amount` | 否 | 目标金额 |
| `security_name` | 否 | 证券名称 |
| `signal_name` | 否 | 信号名称 |
| `scale` | 否 | 默认 `Daily` |
| `remark` | 否 | 备注 |

> **自动计算数量**：如果提供了 `expected_price` 但未提供 `expected_quantity`，后端会用 `策略.position_size / expected_price` 自动计算，并按市场规则取整（A 股取整到 100，美股取整到 1）。

增量导入示例：

```bash
curl -s -X POST "http://127.0.0.1:8000/api/signals/batch" \
  -H "Content-Type: application/json" \
  -d '{"signals":[{"strategy_id":1,"signal_date":"2026-03-12","security_code":"NVDA","direction":"BUY","expected_price":120.5,"order_type":"LIMIT"}]}'
```

### 方式 B：文本粘贴（`POST /api/signals/import-text`）

仅当用户给的是原始文本，且你无法先转成结构化 JSON 时使用。即便走文本入口，也必须先做：

1. 解析出候选信号
2. 标准化证券代码
3. 批内去重
4. 查询已有信号
5. 只有确认存在新增时才执行导入

```bash
curl -s -X POST "http://127.0.0.1:8000/api/signals/import-text" \
  -H "Content-Type: application/json" \
  -d '{"text":"NVDA BUY 120.5\nAAPL SELL 185.0"}'
```

### 方式 C：文件上传（`POST /api/signals/import`）

仅当用户明确提供 txt/csv 文件且不适合先转结构化 JSON 时使用。文件内容同样要先执行“解析 -> 标准化 -> 批内去重 -> 查询已有 -> 仅导入增量”。

### 响应结构（三种方式通用）

```json
{
  "success": true,
  "message": "成功创建 2 条信号，0 条失败",
  "data": {
    "created": 2,
    "errors": []
  }
}
```

部分失败时 `errors` 会包含具体错误信息（最多 10 条）。

### 幂等导入示例

示例 1：同一信号二次执行

1. 第一次查询未命中，导入 1 条新增。
2. 第二次查询命中同键同方向信号。
3. 不再调用 `POST`，直接汇报：`已跳过 1 条重复，已存在，未重复导入`。

示例 2：混合批次部分已存在

1. 候选信号共 5 条。
2. 查重后发现 2 条已存在，3 条为新增。
3. 最终只提交这 3 条新增。
4. 对外汇报：`已跳过 2 条重复，准备导入 3 条新增`。

### 信号管理端点

| 端点 | 说明 |
|------|------|
| `GET /api/signals?strategy_id=1&start_date=2026-03-01` | 查询信号列表（limit 默认 100，最大 1000） |
| `GET /api/signals?strategy_id=1&signal_date=2026-03-12&security_code=NVDA&limit=1000` | 导入前查重的推荐查询方式 |
| `POST /api/signals/{id}/cancel` | 取消待执行信号（仅 PENDING） |
| `DELETE /api/signals/{id}` | 删除信号（仅 PENDING/EXECUTED） |

---

## 能力 3：查询策略信息

| 端点 | 说明 |
|------|------|
| `GET /api/strategies` | 策略列表（可选 `is_active`、`keyword`） |
| `GET /api/strategies/{strategy_id}` | 按 ID 查策略 |
| `GET /api/strategies/code/{code}` | 按 code 查策略 |

### 响应结构

```json
{
  "id": 1,
  "name": "美股精选",
  "code": "nice-us",
  "description": "...",
  "virtual_capital": 1000000.00,
  "position_size": 35000.00,
  "position_ratio": 4.00,
  "is_active": true,
  "created_at": "2026-01-01T00:00:00",
  "updated_at": "2026-03-12T10:00:00"
}
```

> `position_size` 是每笔交易的目标金额，信号导入时用于自动计算数量。

---

## 能力 4：查看绩效指标

`GET /api/performance/metrics/{strategy_id}`

可选参数：`start_date`、`end_date`

```bash
curl -s "http://127.0.0.1:8000/api/performance/metrics/1"
```

### 其他绩效端点

| 端点 | 说明 |
|------|------|
| `GET /api/performance/summary` | 全策略绩效摘要 |
| `GET /api/performance/ranking` | 策略排名 |
| `GET /api/performance/nav/{strategy_id}` | 净值曲线 |
| `GET /api/performance/trades/{strategy_id}` | 交易明细与汇总 |
| `GET /api/performance/comparison?strategy_ids=1,2` | 多策略对比 |

---

## 证券代码标准化规则

Agent 在导入前必须先自行标准化代码，再做查重；不要依赖后端兜底。

### 美股

| 输入 | 存储为 | 规则 |
|------|--------|------|
| `74NVDA` | `NVDA` | 剥离 `74` 前缀 |
| `nvda` | `NVDA` | 转大写 |
| `GOOG` | `GOOG` | 1-5 位大写字母原样保留 |

### A 股

| 输入 | 存储为 | 规则 |
|------|--------|------|
| `000001.XSHE` | `SZ000001` | `.XSHE` → `SZ` 前缀 |
| `600000.XSHG` | `SH600000` | `.XSHG` → `SH` 前缀 |
| `SZ000001` | `SZ000001` | 已有前缀则保留 |
| `SH600000` | `SH600000` | 已有前缀则保留 |
| `600000`（纯 6 位） | `SH600000` | `6` 开头 → SH |
| `000001`（纯 6 位） | `SZ000001` | `0`/`3` 开头 → SZ |

导入前查重时，必须使用标准化后的结果作为 key。例如：

- `74NVDA`、`nvda`、`NVDA` 统一按 `NVDA` 查重
- `002694.XSHE`、`SZ002694` 统一按 `SZ002694` 查重

---

## 错误处理

### 两种错误响应格式

**格式 1 — 标准 HTTP 错误**（404/400/500）：

```json
{"detail": "策略不存在"}
```

**格式 2 — 批量操作部分失败**：

```json
{
  "success": false,
  "message": "成功创建 1 条信号，2 条失败",
  "data": {"created": 1, "errors": ["第2行: 证券代码为空", "第3行: 日期格式错误"]}
}
```

### 处理策略

- 后端不可用 → 报告具体的连接错误
- 策略代码不存在 → 停止操作，报告给用户，不要猜测
- 查重接口失败 → 停止导入，报告给用户，不要在未知状态下继续
- 批内同键冲突 → 停止导入，列出冲突项让用户确认
- 源文件有歧义行 → 展示问题行让用户确认，不要自动跳过
- 批量导入部分失败 → 完整展示所有 error 项

---

## 能力 5：数据库备份

### 触发备份

`POST /api/backup`

无需请求体。后端调用 mysqldump 导出整个 pms 数据库为 SQL 文件。

```bash
curl -s -X POST "http://127.0.0.1:8000/api/backup"
```

#### 响应结构

```json
{
  "success": true,
  "message": "备份完成: pms_2026-03-13_221500.sql",
  "data": {
    "filename": "pms_2026-03-13_221500.sql",
    "path": "D:/Dropbox/Project/cf_quant_web/pms_2026-03-13_221500.sql",
    "size_kb": 142.5,
    "elapsed_seconds": 1.23
  }
}
```

### 列出已有备份

`GET /api/backup/list`

```bash
curl -s "http://127.0.0.1:8000/api/backup/list"
```

#### 响应结构

```json
{
  "total": 3,
  "backups": [
    {
      "filename": "pms_2026-03-13_221500.sql",
      "size_kb": 142.5,
      "modified_at": "2026-03-13 22:15:00"
    }
  ]
}
```

### 展示重点

向用户汇报时聚焦：`filename`、`size_kb`、备份是否成功。列表展示时用表格呈现。
