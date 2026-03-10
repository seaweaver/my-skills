---
name: stockdata
version: 1.0.0
description: 本地股市数据读取指南（唯一事实源）。仅指导 Agent 读取本地行情，不联网、不造数。
---

# StockData

## 定位

`stockdata` 只负责一件事：为 Agent 提供**可追溯的本地行情数据读取规范**。

它不负责监控触发、阈值判断、消息通知、交易建议。

## 适用场景（Activation Triggers）

- 查询某个标的最新收盘价（例如：`162411`）
- 查询某个标的某个交易日的价格
- 查询最近 N 个交易日的 OHLCV
- 为其他 Agent 提供指标计算输入数据

## 硬约束（必须遵守）

1. **唯一事实源**：只能读取本地文件，禁止外部行情 API / 网页搜索。
2. **禁止造数**：读不到就报错，不允许“估算价格”或“补齐缺失值”。
3. **证据必带**：所有数值输出都要附 `source_file` 与 `trade_date`。
4. **先校验再返回**：必须校验文件存在、字段完整、数据非空。

## 数据源契约（Data Source Contract）

1. 首选读取 `D:\Dropbox\Project\cf_quant\config.yaml` 的 `data.base_dir`。
2. 如果配置不可用，默认使用 `D:\data`。
3. 目录约定：
   - A 股/ETF：`{base_dir}\stocks\{ts_code}.parquet`
   - 指数：`{base_dir}\indices\{ts_code}.parquet`
   - 美股：`{base_dir}\stocks_us\{ts_code}.parquet`
4. 推荐先检查更新状态：`{base_dir}\data_update_state.json`，期望 `status=SUCCESS`。

## 标的识别规则（Symbol Normalization）

1. 若输入已含后缀（如 `162411.SZ` / `000300.SH`），直接使用。
2. 若输入为纯数字（如 `162411`），按文件存在性探测：
   - 先试 `stocks\162411.SZ.parquet`
   - 再试 `stocks\162411.SH.parquet`
   - 仍不存在则报 `DATA_NOT_FOUND`
3. 若存在多个候选且冲突，报 `SYMBOL_AMBIGUOUS`，不得自行猜测。

## 数据读取流程（Agent 必须按顺序执行）

1. 确定 `base_dir` 与 `ts_code`。
2. 解析目标 `parquet` 文件，校验字段至少包含：
   - `ts_code`, `trade_date`, `close`
3. 按 `trade_date` 降序排序后再取最新值。
4. 如需涨跌信息，优先使用已有字段：`pre_close`, `change`, `pct_chg`。
5. 输出结构化结果，并附证据字段。

## 标准输出格式

### 成功

```json
{
  "ok": true,
  "symbol_input": "162411",
  "ts_code": "162411.SZ",
  "trade_date": "20260227",
  "close": 0.816,
  "pre_close": 0.821,
  "pct_chg": -0.609,
  "source_file": "D:\\data\\stocks\\162411.SZ.parquet",
  "source_type": "stocks",
  "data_status": "SUCCESS"
}
```

### 失败

```json
{
  "ok": false,
  "error_code": "DATA_NOT_FOUND",
  "error_message": "未找到标的对应本地行情文件",
  "symbol_input": "162411",
  "candidate_files": [
    "D:\\data\\stocks\\162411.SZ.parquet",
    "D:\\data\\stocks\\162411.SH.parquet"
  ]
}
```

## 失败处理规范

- `DATA_NOT_FOUND`：文件不存在
- `EMPTY_DATA`：文件存在但无行数据
- `COLUMN_MISSING`：缺少关键字段
- `STATE_NOT_SUCCESS`：`data_update_state.json` 非成功状态
- `SYMBOL_AMBIGUOUS`：标的映射冲突

出现以上任意错误时，必须停止并返回失败结构，不输出价格结论。

## Agent 使用提醒

当用户问“监控/提醒”时，`stockdata` 只提供数据，不负责触发逻辑。触发逻辑应由上层 Agent 处理，例如：

- 输入：`监控 162411，基准价 0.975，波动 ±5% 提醒`
- `stockdata` 输出：最新价与证据字段
- 上层 Agent 计算阈值并决定是否提醒

