---
name: cf-quant-web
description: 查询量化策略持仓、导入交易信号、查看策略信息或绩效指标。Use when querying strategy positions, importing trading signals, looking up strategies, or checking performance metrics via the cf_quant_web local backend.
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
| JSON 批量 | `POST /api/signals/batch` | Agent 已解析好结构化数据 |
| 文本粘贴 | `POST /api/signals/import-text` | 用户直接粘贴信号文本 |
| 文件上传 | `POST /api/signals/import` | 用户提供 txt/csv 文件 |

### 前置准备

1. 如果只知道 `strategy_code`，先解析策略 ID：
   ```bash
   curl -s "http://127.0.0.1:8000/api/strategies/code/nice-us"
   ```
2. 标准化证券代码（见下方规则）
3. 构造请求体

### 方式 A：JSON 批量（`POST /api/signals/batch`）

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
| `security_code` | 是 | 证券代码 |
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

```bash
curl -s -X POST "http://127.0.0.1:8000/api/signals/batch" \
  -H "Content-Type: application/json" \
  -d '{"signals":[{"strategy_id":1,"signal_date":"2026-03-12","security_code":"NVDA","direction":"BUY","expected_price":120.5,"order_type":"LIMIT"}]}'
```

### 方式 B：文本粘贴（`POST /api/signals/import-text`）

```bash
curl -s -X POST "http://127.0.0.1:8000/api/signals/import-text" \
  -H "Content-Type: application/json" \
  -d '{"text":"NVDA BUY 120.5\nAAPL SELL 185.0"}'
```

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

### 信号管理端点

| 端点 | 说明 |
|------|------|
| `GET /api/signals?strategy_id=1&start_date=2026-03-01` | 查询信号列表（limit 默认 100，最大 1000） |
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

Agent 发送请求前应自行标准化代码，后端也会做一次：

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
| `600000`（纯 6 位） | `SH600000` | `6` 开头 → SH |
| `000001`（纯 6 位） | `SZ000001` | `0`/`3` 开头 → SZ |

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
- 源文件有歧义行 → 展示问题行让用户确认，不要自动跳过
- 批量导入部分失败 → 完整展示所有 error 项
