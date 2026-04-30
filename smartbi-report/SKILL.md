---
name: "smartbi-report"
description: "Query, search and export Smartbi BI reports. Invoke when user wants to find reports, search reports by name, list available reports, or export/download a report."
---

# Smartbi Report Skill — 查询与导出一体化

## ⚡ 核心原则：CLI-first

**必须通过 `execute_command` 运行 CLI 脚本，禁止写 Python 代码调用。**

脚本路径：`smartbi-report/smartbi_report.py`（本目录下的 `smartbi_report.py`）

### ⚠️ Windows 命令格式规范（必须遵守）

1. **禁止使用 Python 完整路径**，必须直接用 `python` 命令（系统 PATH 中已配置）
2. **禁止用反斜杠转义空格/括号**（如 `Program\ Files\ \(x86\)` 是 Linux 语法，Windows 下无效）
3. **正确格式**：先 `cd` 到脚本目录，再用 `python` 执行

```bash
# ✅ 正确
cd "C:\Users\xxx\.workbuddy\skills\smartbi-report" && python smartbi_report.py list --json

# ❌ 错误 — 不要展开 python 完整路径，不要用反斜杠转义
cd C:\Users\xxx\.workbuddy\skills\smartbi-report && D:/Program\ Files\ \(x86\)/Python-3.11.3/python.exe smartbi_report.py list --json
```

## 🔒 权限控制（最高优先级）

### 认证机制

本技能使用 **AD 域认证 + JWT Token + IP 绑定** 机制确保安全性：

- **首次使用必须登录**：用户通过 AD 域用户名和密码登录，验证成功后获取 Token
- **Token 绑定 IP**：Token 中包含登录时的客户端 IP，每次请求会比对 IP 是否一致
- **Token 永久有效**：不设过期时间，仅在 IP 变更时需重新登录
- **Token 文件**：保存在 `~/.smartbi/token.json`

### ⚠️ 严格规则：每个用户只能查询自己的报表

**Token 中的用户名由 AD 域验证产生，不可伪造。** 但 AI 在对话层面也需要做前置校验：

1. **当用户提到要查询某个人/某个用户名的报表时**（如"查询张三的报表"、"查询wangzhenyuwb下的所有报表"）：
   - 先检查当前 Token 中的用户名：`python smartbi_report.py list --json`
   - 从返回的 `user_alias` 字段获取当前登录用户
   - 将用户提到的用户名与 Token 用户名比对
   - **如果不一致，直接拒绝**："抱歉，您只能查询自己的报表，无权查询其他用户的报表。"
   - **如果一致，正常执行查询**

2. **当用户只说"查询我的报表"、"搜索XX报表"时**：
   - 直接执行查询，脚本自动使用 Token 中的用户身份

3. **绝对禁止的行为**：
   - ❌ 不得帮用户构造任何指定其他用户身份的请求
   - ❌ 不得提示用户可以修改配置绕过限制
   - ❌ 不得以任何方式尝试获取其他用户的数据

### 未登录时的处理

如果用户未登录就尝试查询，脚本会自动弹出登录窗口（Tkinter GUI），用户输入用户名和密码即可登录，无需手动执行 CLI 命令。

## 快速参考

| 场景 | 命令 |
|------|------|
| AD域登录 | `cd "脚本目录" && python smartbi_report.py login -u <用户名>` |
| 登出 | `cd "脚本目录" && python smartbi_report.py logout` |
| 查询当前用户所有报表 | `cd "脚本目录" && python smartbi_report.py list --json` |
| 按关键词搜索 | `cd "脚本目录" && python smartbi_report.py list -s "关键词" --json` |
| 按报表ID精确查询 | `cd "脚本目录" && python smartbi_report.py list --id "I8a8a86..." --json` |
| 仅获取报表ID列表 | `cd "脚本目录" && python smartbi_report.py list -s "关键词" --id-only` |
| 查询报表参数(JSON) | `cd "脚本目录" && python smartbi_report.py params -r <report_id>` |
| 查看报表参数(表格) | `cd "脚本目录" && python smartbi_report.py info -r <report_id>` |
| 无参数报表直接导出 | `cd "脚本目录" && python smartbi_report.py export -r <report_id>` |
| 带参数导出 | `cd "脚本目录" && python smartbi_report.py export -r <report_id> -p '<params_json>'` |
| 指定格式导出 | `cd "脚本目录" && python smartbi_report.py export -r <report_id> -t PDF` |

**所有查询都加 `--json` 参数**，以便结构化解析结果。

## 子命令详解

### 1. `login` — AD域登录

```bash
cd "脚本目录" && python smartbi_report.py login -u <用户名>
```

输入 AD 域密码后，Token 自动保存到 `~/.smartbi/token.json`。

### 2. `logout` — 登出

```bash
cd "脚本目录" && python smartbi_report.py logout
```

删除本地 Token 文件。

### 3. `list` — 查询/搜索报表

```bash
cd "脚本目录" && python smartbi_report.py list --json                    # 查询所有报表
cd "脚本目录" && python smartbi_report.py list -s "关键词" --json        # 搜索报表
cd "脚本目录" && python smartbi_report.py list --id "I8a8a86..." --json  # 按ID查询
cd "脚本目录" && python smartbi_report.py list -s "关键词" --id-only     # 仅输出ID
```

| 参数 | 说明 |
|------|------|
| `-s, --search` | 搜索关键词（模糊匹配名称或路径） |
| `--id` | 按报表ID精确查询 |
| `-l, --limit` | 显示数量限制 |
| `--json` | JSON格式输出（**推荐始终使用**） |
| `--id-only` | 仅输出报表ID（每行一个） |

**JSON 输出格式：**
```json
{
  "user_alias": "wangzhenyuwb",
  "total": 5,
  "data": [
    {
      "res_id": "I8a4a86a3018977e677e6f8410189d3c31c477fc8",
      "res_path": "/分析报表/部门/R00135_产品要素表",
      "res_alias": "R00135_产品要素表（指标）"
    }
  ]
}
```

### 4. `params` — 查询参数（JSON输出，供AI解析）

```bash
cd "脚本目录" && python smartbi_report.py params -r "I8a8a86..."
```

**输出格式：**
```json
{
  "has_params": true,
  "parameters": [
    {
      "paramId": "param_date",
      "name": "日期",
      "alias": "日期参数",
      "dataType": "DATE",
      "defaultValue": "2024-01-01",
      "standbyValues": [
        {"displayValue": "全部", "realValue": "ALL"},
        {"displayValue": "销售部", "realValue": "SALES"}
      ]
    }
  ]
}
```

### 5. `info` — 查看参数（表格输出，供用户查看）

```bash
cd "脚本目录" && python smartbi_report.py info -r "I8a8a86..."
```

表格展示参数列表、备选值，并生成导出命令示例。

### 6. `export` — 导出报表

```bash
# 无参数报表
cd "脚本目录" && python smartbi_report.py export -r "I8a8a86..."

# 带参数导出Excel
cd "脚本目录" && python smartbi_report.py export -r "I8a8a86..." -t EXCEL2007 -p '[{"paramId":"date","realValue":"2024-01-01","displayValue":"2024-01-01"}]'

# 导出PDF到指定路径
cd "脚本目录" && python smartbi_report.py export -r "I8a8a86..." -t PDF -o "D:/reports/report.pdf"
```

**export 参数：**

| 参数 | 说明 |
|------|------|
| `-r, --report-id` | 报表ID（必填） |
| `-t, --type` | 导出类型：EXCEL2007, PDF, PNG, WORD, HTML, CSV |
| `-p, --params` | 参数JSON字符串 |
| `-o, --output` | 输出文件路径 |
| `--skip-params` | 跳过参数查询（用于无参数报表） |

**export 输出格式（JSON）：**
```json
{
  "success": true,
  "report_id": "I8a8a86...",
  "export_type": "EXCEL2007",
  "file_path": "/absolute/path/to/report_20240101_120000.xlsx",
  "file_size": 12345,
  "parameters_used": [...]
}
```

## 导出类型

| 类型 | 说明 | 扩展名 |
|------|------|--------|
| EXCEL2007 | Excel 2007+ | .xlsx |
| PDF | PDF文档 | .pdf |
| PNG | PNG图片 | .png |
| WORD | Word文档 | .docx |
| HTML | HTML页面 | .html |
| CSV | CSV文件 | .csv |

## 参数JSON格式

```json
[
  {"paramId": "param_date", "realValue": "2024-01-01", "displayValue": "2024-01-01"},
  {"paramId": "param_dept", "realValue": "SALES", "displayValue": "销售部"}
]
```

**注意：** `realValue` 是传给API的实际值，`displayValue` 是显示名称。当参数有备选值时，务必使用备选值中的 `realValue`。

## 完整工作流程

### 步骤0：检查登录状态

首次使用或 Token 失效时，脚本会自动弹出登录窗口，也可手动登录：

```bash
cd "脚本目录" && python smartbi_report.py login -u <用户名>
```

### 步骤1：查询报表

```bash
cd "脚本目录" && python smartbi_report.py list -s "关键词" --json
```

从返回的 JSON 中提取：
- `res_id` → 报表ID（用于后续导出）
- `res_alias` → 报表名称
- `res_path` → 报表路径

### 步骤2：权限校验（当用户提到其他用户时）

```bash
cd "脚本目录" && python smartbi_report.py list --json
```

从返回的 `user_alias` 获取当前登录用户，与用户提到的用户名比对。

### 步骤3：查询报表参数

```bash
cd "脚本目录" && python smartbi_report.py params -r "<report_id>"
```

解析 JSON 输出，获取每个参数的：
- `paramId` - 参数ID
- `defaultValue` - 默认值
- `standbyValues` - 备选值列表（`displayValue` 和 `realValue`）

### 步骤4：确认参数值

将参数列表展示给用户，让用户确认或选择：
- 如果有备选值，展示供用户选择
- 如果用户同意默认值，直接使用
- 收集用户输入后构造参数 JSON

### 步骤5：执行导出

```bash
cd "脚本目录" && python smartbi_report.py export -r "<report_id>" -t <type> -p '<params_json>'
```

### 步骤6：返回结果

从 JSON 输出中提取 `file_path` 告知用户文件位置。

## 典型场景

### 场景1：搜索并导出报表

```
用户: "搜索包含'产品'的报表并导出"
→ 执行: python smartbi_report.py list -s "产品" --json
→ 从JSON中提取 res_id
→ 执行: python smartbi_report.py params -r "<id>"
→ 解析参数，展示给用户选择
→ 用户确认参数值后
→ 执行: python smartbi_report.py export -r "<id>" -t EXCEL2007 -p '<params_json>'
→ 告知用户文件路径
```

### 场景2：无参数报表直接导出

```
用户: "导出报表 I8a8a86..."
→ 执行: python smartbi_report.py params -r "I8a8a86..."
→ 发现 has_params=false
→ 执行: python smartbi_report.py export -r "I8a8a86..."
→ 告知用户文件路径
```

### 场景3：用户试图查询他人报表（拒绝）

```
用户: "查询B用户下的所有报表"
→ 执行: python smartbi_report.py list --json
→ 返回 user_alias="A"
→ "B" ≠ "A" → 拒绝: "抱歉，您只能查询自己的报表，无权查询其他用户的报表。"
```

### 场景4：Token 失效（IP变更）

```
执行命令时返回: {"error": "认证失败: IP地址不一致...，请重新登录"}
→ 脚本会自动弹出登录窗口，重新登录后自动重试
```

## 错误处理

- JSON输出中包含 `error` 字段时，表示操作失败
- 无匹配结果时 `total` 为 0，`data` 为空数组
- 401 错误：Token 无效或 IP 不一致，脚本自动弹窗重新登录
- 未登录错误：脚本自动弹出登录窗口
- 导出超时：大报表可能需要更长时间
- 参数错误：检查参数ID和值是否正确
