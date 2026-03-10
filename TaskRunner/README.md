# TaskRunner 使用指南

**版本**: 1.0
**最后更新**: 2026-01-28

---

## 快速开始

### 1️⃣ 创建任务文件

在 `Inbox/` 目录下创建 Markdown 文件，使用标准的 checklist 语法：

```markdown
# 我的任务清单

- [ ] 抓取 https://36kr.com/newsflashes 最新资讯
- [ ] 撰写《量化投资策略》技术文档
- [ ] 设计投资组合仪表盘界面
```

### 2️⃣ 触发 TaskRunner

在 Claude Code 中输入任何触发指令：

```
执行任务
```

或：

```
run tasks
```

### 3️⃣ 确认执行计划

TaskRunner 会显示执行计划：

```
===== TaskRunner Execution Plan =====

File: Inbox/我的任务清单.md
----------------------------------------
Task 1: 抓取 https://36kr.com/newsflashes 最新资讯
  → Skill: BrightData
  → Action: Progressive URL scraping

Task 2: 撰写《量化投资策略》技术文档
  → Skill: doc-coauthoring
  → Action: Structured document workflow

Task 3: 设计投资组合仪表盘界面
  → Skill: frontend-design
  → Action: Create frontend interface

===== Total: 3 tasks from 1 files =====

Type '1' to proceed or '0' to cancel.
```

输入 `1` 确认执行。

### 4️⃣ 查看结果

执行完成后：
- 任务状态会自动更新为 `- [x]`
- 执行日志保存到 `Outbox/` 目录
- 生成的内容也会保存到 `Outbox/`

---

## 文件组织

```
iCloudNote/
├── Inbox/                    # 任务输入目录
│   ├── research-tasks.md     # 研究任务
│   ├── daily-todos.md        # 日常待办
│   └── weekly-goals.md       # 周目标
│
├── Outbox/                   # 执行输出目录
│   ├── research-tasks-20260128-173015.log
│   ├── daily-todos-20260128-173215.log
│   └── 36kr-newsflashes.md   # 生成的内容
│
└── 1. AI-Skills/
    └── TaskRunner/
        ├── SKILL.md
        ├── README.md
        └── Workflows/
```

---

## 任务语法规则

### ✅ 支持的语法

**未完成任务** (会被执行):
```markdown
- [ ] Task description
```

**已完成任务** (会被跳过):
```markdown
- [x] Task description
```

**失败任务** (会被跳过，除非手动重置):
```markdown
- [!] Task description (Failed: Error message)
```

### 📝 任务描述建议

**Web 抓取任务**:
```markdown
- [ ] 抓取 https://example.com
- [ ] 获取 https://api.example.com/data
```

**文档撰写任务**:
```markdown
- [ ] 撰写《技术方案》文档
- [ ] 起草项目提案
- [ ] 写作《投资研究报告》
```

**前端设计任务**:
```markdown
- [ ] 设计登录页面
- [ ] 创建数据仪表盘界面
- [ ] 优化首页 UI
```

---

## 技能路由规则

TaskRunner 会根据关键词和模式自动将任务路由到合适的 Skill：

| 任务类型 | 关键词 | 路由到 |
|---------|--------|--------|
| Web 抓取 | 抓取、爬取、scrape、fetch、URL | BrightData |
| 文档撰写 | 撰写、写作、文档、draft、proposal | doc-coauthoring |
| 前端设计 | 设计、界面、UI、dashboard | frontend-design |

---

## 高级用法

### 任务依赖（未来功能）

如果任务之间有依赖关系，可以使用 `[depends:N]` 语法：

```markdown
- [ ] 抓取 https://example.com/data
- [ ] [depends:1] 分析抓取的数据并生成报告
- [ ] [depends:2] 发送报告邮件
```

### 重试失败任务

如果任务执行失败：

```markdown
- [!] 抓取 https://example.com (Failed: Timeout)
```

手动修改为 `- [ ]` 即可重新执行：

```markdown
- [ ] 抓取 https://example.com
```

### 批量处理

在 `Inbox/` 目录下创建多个文件，TaskRunner 会按文件名顺序依次处理：

```
Inbox/
├── 01-urgent.md      # 优先级最高
├── 02-important.md   # 优先级次之
└── 03-routine.md     # 常规任务
```

---

## 日志系统

### 日志文件命名

**成功日志**:
```
Outbox/[filename]-YYYYMMDD-HHMMSS.log
```

**错误日志**:
```
Outbox/[filename]-YYYYMMDD-HHMMSS-errors.log
```

### 日志内容示例

```
===== TaskRunner Execution Log =====
Source File: Inbox/research-tasks.md
Execution Time: 2026-01-28 17:30:15
Total Tasks: 3
Success: 2
Failed: 1

----- Task 1 -----
Status: SUCCESS
Content: 抓取 https://36kr.com/newsflashes 最新快讯
Skill: BrightData
Execution: Tier 1 (WebFetch) succeeded in 3.2s
Output: [Markdown content saved to ./Outbox/36kr-newsflashes.md]

----- Task 2 -----
Status: SUCCESS
Content: 撰写《动量因子研究》文档
Skill: doc-coauthoring
Execution: Document created successfully
Output: [Document saved to ./8. 投资/动量因子研究.md]

----- Task 3 -----
Status: FAILED
Content: 设计投资仪表盘
Skill: frontend-design
Error: User aborted during design phase
```

---

## 故障排除

### 问题 1: TaskRunner 没有识别我的任务

**原因**: Checklist 语法不正确

**解决**:
- 确保使用 `- [ ]` (中括号内有空格)
- 不要使用 `- []` 或 `- [  ]`

### 问题 2: 任务被路由到错误的 Skill

**原因**: 关键词不明确

**解决**:
- 使用更明确的关键词
- 例如：不要只写 "处理数据"，而是写 "抓取 https://... 数据" 或 "撰写数据分析文档"

### 问题 3: 任务执行失败

**原因**: 多种可能

**解决**:
1. 查看 `Outbox/` 中的错误日志
2. 根据错误信息调整任务描述
3. 手动将 `- [!]` 改为 `- [ ]` 重试

---

## 最佳实践

### ✅ 推荐做法

1. **清晰的任务描述**: 明确说明要做什么
   ```markdown
   - [ ] 抓取集思录热帖 https://jisilu.cn/question/hot
   ```

2. **一个任务一个行**: 不要在一行中包含多个任务
   ```markdown
   ✅ 正确:
   - [ ] 抓取 36kr 资讯
   - [ ] 抓取极客公园资讯

   ❌ 错误:
   - [ ] 抓取 36kr 和极客公园资讯
   ```

3. **合理分组**: 相关任务放在同一个文件
   ```markdown
   # research-tasks.md
   - [ ] 抓取研究资料
   - [ ] 分析数据
   - [ ] 撰写研究报告
   ```

4. **定期清理**: 将已完成的任务归档或删除

### ❌ 避免做法

1. **模糊的任务描述**:
   ```markdown
   - [ ] 做点研究  (太模糊，无法路由)
   ```

2. **过于复杂的任务**:
   ```markdown
   - [ ] 抓取 10 个网站、分析数据、生成报告并发送邮件
   (应该拆分成 4 个独立任务)
   ```

3. **混乱的文件组织**:
   ```markdown
   - [ ] 抓取网站
   - [ ] 买菜
   - [ ] 撰写文档
   - [ ] 看电影
   (任务类型混杂，建议分文件)
   ```

---

## 示例场景

### 场景 1: 投资研究工作流

```markdown
# Inbox/investment-research.md

- [ ] 抓取集思录 7 天热帖 https://jisilu.cn/question/hot
- [ ] 抓取雪球热门文章 https://xueqiu.com/hots
- [ ] 撰写《A股市场周报》文档
```

**执行**: `执行任务` → Confirm → 自动完成

**结果**:
- ✅ 所有任务标记为 `- [x]`
- 📄 热帖内容保存到 `Outbox/`
- 📊 周报文档创建完成

### 场景 2: 前端开发工作流

```markdown
# Inbox/frontend-tasks.md

- [ ] 设计登录页面
- [ ] 设计用户仪表盘
- [ ] 设计数据可视化界面
```

**执行**: `run tasks` → Confirm → 自动完成

**结果**:
- 🎨 所有设计任务完成
- 💾 HTML/CSS 代码生成到 `Outbox/`

### 场景 3: 内容创作工作流

```markdown
# Inbox/content-creation.md

- [ ] 抓取最新科技新闻 https://36kr.com/newsflashes
- [ ] 撰写《AI 发展趋势》分析文章
```

**执行**: `执行任务` → Confirm → 自动完成

**结果**:
- 📰 新闻内容抓取完成
- ✍️ 文章撰写完成

---

## 配置（未来功能）

可以在 `Inbox/taskrunner.config.md` 中自定义配置：

```yaml
---
routing:
  url_scraping: BrightData
  document_writing: doc-coauthoring
  web_design: frontend-design

execution:
  parallel: false  # 顺序执行
  stop_on_error: file  # 文件级别停止

logging:
  level: detailed  # 详细日志
  output_dir: ./Outbox/
---
```

---

## 相关资源

- **Skill 定义**: `SKILL.md`
- **需求规格**: `TaskRunner Skill 需求规格说明书.md`
- **工作流实现**: `Workflows/TaskExecutionFlow.md`
- **子 Skill 文档**:
  - `../BrightData/SKILL.md`
  - `../doc-coauthoring/SKILL.md`
  - `../frontend-design/SKILL.md`

---

## 反馈与贡献

如有问题或建议，请在 Obsidian 笔记中记录或直接与开发者沟通。

**享受 "Fire and Forget" 的高效体验！** 🚀
