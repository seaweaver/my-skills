# Skill 使用指南 - 基于 Anthropic 最佳实践

> 本文档基于 Anthropic 团队《Lessons from Building Claude Code: How We Use Skills》整理，结合创金零售数据组实际工作场景编写。
>
> **最后更新**: 2026-03-19
> **来源**: https://www.techtwitter.com/articles/lessons-from-building-claude-code-how-we-use-skills

---

## 📚 目录

1. [什么是 Skill](#什么是-skill)
2. [9 种 Skill 类型](#9 种 skill 类型)
3. [编写 Skill 的最佳实践](#编写-skill 的最佳实践)
4. [Skill 分发与协作](#skill 分发与协作)
5. [我们的行动清单](#我们的行动清单)

---

## 什么是 Skill

**核心认知**：
- ❌ Skill 不只是 markdown 文件
- ✅ Skill 是一个**文件夹**，可以包含脚本、资产、数据等
- ✅ Skill 是**上下文工程**的工具，通过文件系统实现渐进式披露

**Skill 的能力**：
- 注册动态 hooks（PreToolUse、PostToolUse 等）
- 包含可执行脚本供 Agent 调用
- 存储结构化数据（配置、日志、缓存）
- 与其他 Skill 或 MCP 组合使用

---

## 9 种 Skill 类型

Anthropic 团队将 Skill 分为 9 类，每类有明确的用途和最佳实践。

### 1️⃣ 库与 API 参考 (Library & API Reference)

**用途**：解释如何正确使用库、CLI、SDK（内部或外部）

**典型内容**：
- 参考代码片段
- 常见陷阱 (Gotchas) 列表
- 使用场景说明

**示例**：
```
wind-meta-data/          # 万得元数据查询 Skill
├── SKILL.md            # 主文档（L1/L2/L3 渐进式披露）
├── references/
│   ├── fund_tables.md  # 基金表大全
│   └── api_gotchas.md  # Wind API 常见陷阱
└── examples/
    └── query_fund.py   # 查询示例代码
```

**我们的场景**：
- `wind-meta-data` Skill（已实现）
- 内部数据服务 CLI 的用法说明
- Oracle/ClickHouse 查询规范

---

### 2️⃣ 产品验证 (Product Verification)

**用途**：描述如何测试或验证代码是否正常工作

**关键技巧**：
- 配合外部工具（Playwright、tmux 等）
- 让 Agent 录制测试视频
- 在每一步强制执行程序化断言

**示例**：
```
signup-flow-driver/
├── SKILL.md
├── scripts/
│   ├── drive_signup.py     # 自动化注册流程
│   └── verify_email.py     # 验证邮件发送
└── assertions/
    └── check_state.json    # 每步的状态检查点
```

**我们的场景**：
- TA6.1 数据检查项自动化验证
- 零售线日报数据准确性校验
- 蚂蚁入池产品的上下架流程验证

---

### 3️⃣ 数据获取与分析 (Data Fetching & Analysis)

**用途**：连接数据和监控栈，提供数据查询能力

**典型内容**：
- 数据源认证信息（加密存储）
- Dashboard ID 映射表
- 常见问题 → SQL 查询映射

**示例**：
```
funnel-query/
├── SKILL.md
├── config.json             # 数据源配置（加密）
├── queries/
│   ├── activation.sql      # 激活漏斗 SQL
│   └── retention.sql       # 留存分析 SQL
└── mappings/
    └── dashboard_ids.md    # Grafana Dashboard 映射
```

**我们的场景**：
- 零售线业绩查询 Skill
- 客户持有分析 Skill
- 数据质量检查 Skill

---

### 4️⃣ 业务流程与团队自动化 (Business Process & Team Automation)

**用途**：将重复性工作流封装成一条命令

**关键技巧**：
- 保存历史执行结果到日志文件
- Agent 可以反思之前的执行记录
- 依赖其他 Skill 或 MCP

**示例**：
```
standup-post/
├── SKILL.md
├── standups.log            # 历史站会记录（append-only）
└── scripts/
    └── aggregate.py        # 聚合 Jira/GitHub/Slack 活动
```

**我们的场景**：
- 每日工作流（已实现：AI 热点聚合 + 飞书推送）
- 周报自动生成
- 会议纪要整理 + 待办提取

---

### 5️⃣ 代码脚手架与模板 (Code Scaffolding & Templates)

**用途**：为特定框架/函数生成样板代码

**优势**：
- 处理自然语言需求（纯代码模板无法覆盖的场景）
- 可组合的脚本
- 内置组织规范

**示例**：
```
new-etl-workflow/
├── SKILL.md
├── templates/
│   ├── workflow.py.jinja   # 工作流模板
│   └── config.yaml.jinja   # 配置模板
└── scripts/
    └── scaffold.py         # 脚手架生成器
```

**我们的场景**：
- 新建 ETL 任务脚手架
- 数据视图开发模板
- MCP Server 快速生成

---

### 6️⃣ 代码质量与审查 (Code Quality & Review)

**用途**：执行代码质量检查和审查

**典型内容**：
- 确定性脚本（最大鲁棒性）
- 对抗性审查 Agent
- 测试规范

**示例**：
```
adversarial-review/
├── SKILL.md
└── scripts/
    └── critique.py         #  spawned subagent 批判代码
```

**我们的场景**：
- SQL 代码风格检查
- Python 代码规范审查
- 数据模型设计评审清单

---

### 7️⃣ CI/CD 与部署 (CI/CD & Deployment)

**用途**：帮助获取、推送、部署代码

**典型功能**：
- 监控 PR → 重试不稳定 CI → 解决合并冲突
- 构建 → 冒烟测试 → 灰度发布 → 自动回滚
- Cherry-pick 到生产分支

**我们的场景**：
- LOFTA 项目自动化部署
- 数据视图发布流程
- 配置文件变更审核流

---

### 8️⃣ 运行手册 (Runbooks)

**用途**：从症状出发，执行多工具调查，生成结构化报告

**典型流程**：
```
症状 (Slack/告警/错误签名)
  ↓
多工具调查 (日志/指标/追踪)
  ↓
结构化报告
```

**示例**：
```
oncall-runner/
├── SKILL.md
├── playbooks/
│   ├── high_cpu.md       # CPU 告警排查手册
│   └── data_lag.md       # 数据延迟排查手册
└── scripts/
    └── correlate.py      # 跨系统日志关联
```

**我们的场景**：
- TA6.1 数据异常排查
- 零售线日报缺失应急处理
- 数据库性能问题诊断

---

### 9️⃣ 基础设施运维 (Infrastructure Operations)

**用途**：执行例行维护和操作程序（包括破坏性操作）

**关键特性**：
- 防护栏 (Guardrails) 防止误操作
- 浸泡期 (Soak Period) 让用户确认
- 级联清理流程

**示例**：
```
resource-orphans/
├── SKILL.md
└── scripts/
    └── cleanup.py        # 查找孤儿资源 → Slack 通知 → 确认后清理
```

**我们的场景**：
- 孤儿数据表清理
- 过期备份文件归档
- 数据库索引优化

---

## 编写 Skill 的最佳实践

### ✅ DO（推荐做法）

#### 1. 不要陈述显而易见的内容
> Claude Code 对你的代码库已经了解很多。Skill 应该专注于**推动 Claude 跳出默认思维模式**的信息。

**反例**：
```markdown
## 如何使用 pandas
pandas 是一个 Python 数据分析库...
```

**正例**：
```markdown
## 我们团队的 pandas 使用规范
- 禁止使用 `df.apply()`，改用向量化操作（性能差 100 倍）
- 日期列统一用 `pd.to_datetime(utc=True)`，避免时区问题
- 读取 Parquet 时必须指定 `columns=` 参数，防止加载不必要列
```

#### 2. 建立 Gotchas 章节
> Skill 中信号最强的内容是 **Gotchas 章节**，应基于 Claude 使用 Skill 时的常见失败点持续更新。

**示例结构**：
```markdown
## ⚠️ Gotchas

### 1. Wind API 限流问题
- 现象：连续查询 3 次后返回 `429 Too Many Requests`
- 原因：Wind 免费版限制 2 次/分钟
- 解决方案：使用 `time.sleep(30)` 间隔，或升级到机构版

### 2. 基金代码后缀问题
- 现象：查询 `001234` 返回空结果
- 原因：Wind 需要 `.OF` 后缀（场外基金）
- 正确写法：`001234.OF`
```

#### 3. 利用文件系统和渐进式披露
> Skill 是文件夹，不是单个文件。将整个文件系统视为**上下文工程**工具。

**推荐结构**：
```
my-skill/
├── SKILL.md                # L1: 概述和触发条件
├── guides/
│   ├── quickstart.md       # L2: 快速入门
│   └── advanced.md         # L3: 高级用法
├── references/
│   ├── api.md              # API 参考（按需读取）
│   └── schema.json         # 数据结构定义
├── examples/
│   ├── basic.py            # 基础示例
│   └── complex.py          # 复杂示例
├── scripts/
│   └── helper.py           # 辅助脚本
└── assets/
    └── template.md         # 输出模板
```

**SKILL.md 中的渐进式披露**：
```markdown
# Skill 名称

## 何时使用我
（一句话描述触发条件）

## 快速开始
```bash
执行命令 xxx
```

## 详细内容
详细指南请参考 [guides/advanced.md](guides/advanced.md)

## API 参考
完整 API 文档请参考 [references/api.md](references/api.md)
```

#### 4. 避免过度限制 (Railroading)
> 给 Claude 所需的信息，但保留适应情况的灵活性。

**反例**：
```markdown
你必须按以下步骤执行：
1. 先执行 A
2. 再执行 B
3. 最后执行 C
如果出错，重试 3 次后放弃
```

**正例**：
```markdown
推荐流程：A → B → C，但可根据实际情况调整顺序。
如遇错误，分析原因后决定重试或寻求人工介入。
```

#### 5. 预先考虑设置 (Setup) 需求
> 某些 Skill 需要用户先提供上下文信息。

**推荐模式**：
- 在 Skill 目录中存放 `config.json`
- 如配置未设置，Agent 主动询问用户
- 使用 `AskUserQuestion` 工具提供结构化选择题

**示例**：
```json
// config.json
{
  "slack_channel": "",
  "data_source": "production",
  "notification_enabled": true
}
```

```markdown
## 首次使用
如 `config.json` 未配置，我会问你以下问题：
1. 要发布到哪个 Slack 频道？
2. 使用哪个数据源？（production / staging）
```

#### 6. Description 字段是写给模型看的
> Claude Code 启动时会扫描所有 Skill 的 description 来决定是否使用该 Skill。

**反例**：
```yaml
description: "这个 Skill 用于查询万得基金元数据"
```

**正例**：
```yaml
description: "当用户查询基金名称、代码、规模、经理、费率等 Wind 元数据时使用。支持模糊搜索和批量查询。"
```

**技巧**：
- 包含触发关键词（基金、代码、规模、经理...）
- 说明支持的查询类型
- 提及特殊能力（模糊搜索、批量查询）

#### 7. 在 Skill 中存储记忆
> Skill 可以包含某种形式的记忆，从简单的追加日志到 SQLite 数据库。

**示例**：
```python
# standup-post Skill 的执行逻辑
def generate_standup():
    # 读取历史日志
    history = read_log("standups.log")

    # 对比昨天，找出变化
    today = fetch_today_activity()
    delta = compute_delta(today, history[-1])

    # 生成站会并追加到日志
    post = format_standup(delta)
    append_log("standups.log", post)

    return post
```

**存储位置**：
- ⚠️ Skill 目录中的数据可能在升级时被删除
- ✅ 使用稳定目录：`${CLAUDE_PLUGIN_DATA}`（每个插件的独立数据目录）

#### 8. 存储脚本并生成代码
> 给 Claude 脚本和库，让它专注于**组合决策**而非重建样板代码。

**示例**：
```python
# scripts/data_fetcher.py
def fetch_fund_nav(code: str, start_date: str, end_date: str):
    """获取基金净值数据"""
    # ... 封装复杂的 Wind API 调用

def fetch_fund_holdings(code: str, quarter: str):
    """获取基金持仓数据"""
    # ...

def calculate_sharpe(returns: pd.Series):
    """计算夏普比率"""
    # ...
```

**Claude 可以这样组合使用**：
```python
# Agent 生成的分析脚本
from data_fetcher import fetch_fund_nav, calculate_sharpe

nav = fetch_fund_nav("001234.OF", "2025-01-01", "2025-12-31")
sharpe = calculate_sharpe(nav['nav'].pct_change())
print(f"夏普比率：{sharpe:.2f}")
```

#### 9. 使用 On-Demand Hooks
> Skill 可以包含仅在调用时激活的 hooks，适用于有意见但不想一直开启的场景。

**示例**：
```yaml
hooks:
  - name: careful-mode
    trigger: "/careful"
    type: PreToolUse
    matcher:
      bash: ["rm -rf", "DROP TABLE", "force-push", "kubectl delete"]
    action: block_with_confirmation
```

**使用场景**：
- `/careful`：只在触碰生产环境时启用危险操作拦截
- `/freeze`：调试时禁止修改特定目录外的文件

---

### ❌ DON'T（避免做法）

| 错误做法 | 正确做法 |
|----------|----------|
| 陈述显而易见的内容 | 专注于推动 Claude 跳出默认思维 |
| 过度具体的指令 | 给信息 + 保留灵活性 |
| 单一 markdown 文件 | 利用文件系统做渐进式披露 |
| 忽略配置需求 | 预先考虑 setup，使用 config.json |
| Description 写成摘要 | Description 写成触发条件描述 |
| 不存储历史数据 | 用日志文件实现记忆和反思 |
| 让 Claude 从头写 boilerplate | 提供脚本库供组合使用 |
| 全局启用 opinionated hooks | 用 on-demand hooks 按需激活 |

---

## Skill 分发与协作

### 两种分发方式

| 方式 | 适用场景 | 优点 | 缺点 |
|------|----------|------|------|
| **检入代码库** (`./.claude/skills`) | 小团队、少代码库 | 简单直接、版本可控 | 增加模型上下文、难以跨团队共享 |
| **内部插件市场** | 大团队、多代码库 | 集中管理、按需安装、有机生长 | 需要基础设施、需要审核机制 |

### 我们的建议路径

**阶段 1（当前）**：检入个人代码库
- 路径：`C:\Users\Dell\.nanobot-cici\workspace\skills\{skill-name}`
- 适合：个人使用、快速迭代

**阶段 2（未来 3-6 个月）**：建立团队技能库
- 路径：`D:\Dropbox\Project\my-skills`（共享目录）
- 适合：数据组内部共享、乐乐等同事使用

**阶段 3（长期）**：公司内部插件市场
- 参考 Anthropic 的 sandbox → marketplace 流程
- 适合：全公司范围推广、跨部门协作

### 有机生长流程

```
个人 Skill (sandbox)
    ↓
Slack/飞书分享 → 收集反馈
    ↓
有人主动安装使用 → 验证价值
    ↓
提交 PR 进入团队技能库
    ↓
持续迭代优化
```

### 审核与质量控制

> ⚠️ 警告：很容易创建糟糕或冗余的 Skill，发布前必须有审核机制。

**审核清单**：
- [ ] 是否有清晰的触发条件描述？
- [ ] 是否有 Gotchas 章节？
- [ ] 是否避免了显而易见的内容？
- [ ] 是否利用了渐进式披露？
- [ ] 是否有示例代码或使用场景？
- [ ] 是否考虑了配置需求？
- [ ] 是否与现有 Skill 重复？

---

## 我们的行动清单

### 🎯 短期（本周）

1. **优化现有 Skill**
   - [ ] `wind-meta-data`: 添加 Gotchas 章节（基于实际使用反馈）
   - [ ] `ai-hot-news`: 改进 description 字段，明确触发条件
   - [ ] `cf-quant-web`: 增加配置管理（config.json）

2. **新建高价值 Skill**（按优先级）
   - [ ] `retail-daily`: 零售线日报查询（类型 3: 数据获取）
   - [ ] `data-quality-check`: 数据质量检查（类型 2: 产品验证）
   - [ ] `sql-style-guide`: SQL 代码规范（类型 6: 代码质量）

3. **文档完善**
   - [ ] 为每个 Skill 添加 `references/api.md`
   - [ ] 建立 `examples/` 目录存放示例代码
   - [ ] 开始记录 `standups.log` 风格的执行日志

### 📅 中期（本月）

1. **乐乐的任务扩展**
   - 研究 Wind 基金查询接口 MCP 实现
   - 同时研究如何将内部数据服务 CLI 化
   - 对比 MCP vs CLI vs Skill 三种交付模式

2. **黄总邮件需求响应**
   - 用 Skill 封装「六棵树」查询能力
   - 实现 `data-cli tree org`、`data-cli label order` 等命令

3. **AI 转型会议分享**
   - 准备双周会材料：「知识抽取→Context 沉淀→Skill 变聪明」链路
   - 展示 `wind-meta-data` Skill 的 L1/L2/L3架构
   - 演示 Skill 如何支撑业务需求（黄总邮件场景）

### 🚀 长期（本季度）

1. **建立团队技能库**
   - 路径：`D:\Dropbox\Project\my-skills`
   - 制定审核流程和标准
   - 鼓励团队成员贡献 Skill

2. **Skill + MCP 双轮驱动**
   - MCP 层：封装原子数据/API 接口
   - Skill 层：封装交互指引/复杂逻辑
   - Agent 层：自然语言调用

3. **度量与优化**
   - 实现 Skill 使用日志（PreToolUse hook）
   - 识别高频 Skill 和低效 Skill
   - 持续迭代优化

---

## 📎 附录：Skill 模板

### 基础模板

```markdown
---
name: {skill-name}
description: {当用户做什么事情时触发此 Skill，包含关键词和场景}
version: 1.0.0
author: {你的名字}
tags:
  - {标签 1}
  - {标签 2}
triggers:
  - {触发词 1}
  - {触发词 2}
---

# {Skill 名称}

## 何时使用我
（一句话描述触发条件，包含关键词）

## 快速开始
```bash
{执行命令或操作步骤}
```

## 核心功能
- 功能 1
- 功能 2
- 功能 3

## ⚠️ Gotchas
（基于实际使用反馈持续更新）

### 1. {常见问题 1}
- **现象**：...
- **原因**：...
- **解决方案**：...

## 进阶使用
详细指南请参考 [guides/advanced.md](guides/advanced.md)

## API 参考
完整 API 文档请参考 [references/api.md](references/api.md)

## 示例
更多示例请参考 [examples/](examples/) 目录
```

### 目录结构模板

```
{skill-name}/
├── SKILL.md                 # 主文档（L1 概述）
├── guides/
│   ├── quickstart.md        # L2 快速入门
│   └── advanced.md          # L3 高级用法
├── references/
│   ├── api.md               # API 参考
│   └── schema.json          # 数据结构
├── examples/
│   ├── basic.py             # 基础示例
│   └── complex.py           # 复杂示例
├── scripts/
│   └── helper.py            # 辅助脚本
├── assets/
│   └── template.md          # 输出模板
├── config.json              # 配置（如有需要）
└── {skill-name}.log         # 执行日志（append-only）
```

---

## 🔗 参考资料

- 原文：[Lessons from Building Claude Code: How We Use Skills](https://www.techtwitter.com/articles/lessons-from-building-claude-code-how-we-use-skills)
- Anthropic 官方文档：[Claude Code Skills](https://docs.anthropic.com/claude-code/skills)
- Skill Creator Skill：帮助快速创建新 Skill
- Self-Improving Agent Skill：持续迭代优化 Skill

---

*本文档由 Cici 基于 Anthropic 最佳实践整理，结合创金零售数据组实际场景编写。*
