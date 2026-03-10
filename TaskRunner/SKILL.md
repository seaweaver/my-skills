---
name: TaskRunner
version: 1.0.0
description: 基于Obsidian知识库的任务执行器，采用智能路由机制自动分发任务到子Skill。适用于：批量任务执行、自动化工作流、任务调度、异步任务处理。Task executor based on Obsidian vault with intelligent routing to sub-skills. USE WHEN batch task execution, automated workflow, task scheduling, async task processing.
---

# TaskRunner - Asynchronous Task Scheduler 异步任务调度器

**Meta-Agent for intelligent task routing and execution with "Fire and Forget" experience.**

---

## Activation Triggers

### Direct Task Requests
- "执行任务", "运行任务", "执行待办清单"
  "execute tasks", "run tasks", "run todo list"
- "扫描任务清单", "检查任务"
  "scan task list", "check tasks"
- "清理任务", "批量执行任务"
  "cleanup tasks", "batch execute tasks"

### Workflow Management
- "自动化处理 Inbox", "处理待办事项"
  "automate Inbox processing", "process todo items"
- "开始任务队列", "启动任务执行器"
  "start task queue", "start task runner"

---

## Core Capability

**Four-Stage Task Execution Pipeline:**

```
START
  |
Stage 1: Scan & Parse
  ├─ Scan ./Inbox/*.md files
  ├─ Parse unchecked items: - [ ]
  └─ Build execution queue
  |
Stage 2: Intelligent Routing
  ├─ Analyze task semantics
  ├─ Match to available skills
  └─ Generate execution plan
  |
Stage 3: User Confirmation
  ├─ Display execution plan
  ├─ Wait for Confirm/Abort
  └─ Proceed or cancel
  |
Stage 4: Execute & Update
  ├─ Execute tasks sequentially
  ├─ Update status: [ ] → [x]
  ├─ Generate logs to ./Outbox/
  └─ Handle failures gracefully
```

---

## Stage Details

### Stage 1: Scan & Parse 扫描与解析

**Input:** `./Inbox/*.md` files
**Process:**
1. Traverse all Markdown files in `./Inbox/` directory
2. Parse file content for checklist syntax
3. **Target:** Only unchecked items `- [ ]`
4. **Ignore:** Checked items `- [x]` and other text
5. **Sorting:** Files by name/modification time, tasks by line number

**Output:** Task execution queue with metadata (file, line number, content)

**Example:**
```markdown
# Inbox/research-tasks.md
- [ ] 抓取 https://36kr.com/newsflashes 最新快讯
- [x] 整理投资笔记
- [ ] 撰写《动量因子研究》文档
```

**Parsed Queue:**
```
Task 1: [research-tasks.md:1] 抓取 https://36kr.com/newsflashes 最新快讯
Task 2: [research-tasks.md:3] 撰写《动量因子研究》文档
```

---

### Stage 2: Intelligent Routing 智能路由

**Skill Pool (能力池):**
- **BrightData**: Web scraping with four-tier fallback (WebFetch → Curl → Browser → Bright Data MCP)
- **doc-coauthoring**: Structured document co-authoring workflow
- **frontend-design**: Frontend interface creation and design
- **[扩展性]**: Future skills can be added to the pool

**Routing Logic:**
1. **Semantic Analysis**: Parse task description keywords and intent
2. **Pattern Matching**:
   - URL scraping patterns → BrightData
   - Document writing patterns → doc-coauthoring
   - Web/UI design patterns → frontend-design
3. **Fallback**: If no clear match, ask user for clarification

**Example Routing:**
```
"抓取 https://36kr.com/newsflashes 最新快讯"
  → Keyword: "抓取", "URL"
  → Match: BrightData

"撰写《动量因子研究》文档"
  → Keyword: "撰写", "文档"
  → Match: doc-coauthoring
```

---

### Stage 3: Pre-flight Check 预检表生成

**User Interaction:**

Before execution, display an execution plan table:

```
===== TaskRunner Execution Plan =====

File: Inbox/research-tasks.md
----------------------------------------
Task 1: 抓取 https://36kr.com/newsflashes 最新快讯
  → Skill: BrightData
  → Action: Progressive URL scraping

Task 2: 撰写《动量因子研究》文档
  → Skill: doc-coauthoring
  → Action: Structured document workflow

File: Inbox/daily-todos.md
----------------------------------------
Task 3: 优化首页设计
  → Skill: frontend-design
  → Action: Create frontend interface

===== Total: 3 tasks from 2 files =====

Type '1' to proceed or '0' to cancel.
```

**Wait for user confirmation** before proceeding.

---

### Stage 4: Execution & State Management 执行与状态管理

**Sequential Execution:**
1. Process tasks in queue order
2. For each task:
   - Invoke the matched Skill
   - Capture output and logs
   - Update task status in source file

**Status Update Logic:**

**Success:**
```markdown
Before: - [ ] 抓取 https://36kr.com/newsflashes 最新快讯
After:  - [x] 抓取 https://36kr.com/newsflashes 最新快讯
```

**Failure:**
```markdown
Before: - [ ] 抓取 https://example.com
After:  - [!] 抓取 https://example.com (Failed: Timeout)
```

**Failure Handling Strategy:**
- **Current file**: Stop processing remaining tasks in the same file
- **Other files**: Continue processing tasks from next file (prevent cascading failures)
- **Logging**: Record error details to `./Outbox/[filename]-errors.log`

---

## Logging System 日志输出

**Output Directory:** `./Outbox/`

**Naming Convention:**
- Success logs: `[original-filename]-YYYYMMDD-HHMMSS.log`
- Error logs: `[original-filename]-YYYYMMDD-HHMMSS-errors.log`

**Log Content:**
```
===== TaskRunner Execution Log =====
Source File: Inbox/research-tasks.md
Execution Time: 2026-01-28 17:30:15
Total Tasks: 2
Success: 1
Failed: 1

----- Task 1 -----
Status: SUCCESS
Content: 抓取 https://36kr.com/newsflashes 最新快讯
Skill: BrightData
Execution: Tier 1 (WebFetch) succeeded in 3.2s
Output: [Markdown content saved to ./Outbox/36kr-newsflashes.md]

----- Task 2 -----
Status: FAILED
Content: 撰写《动量因子研究》文档
Skill: doc-coauthoring
Error: User aborted during context gathering phase
```

---

## Task Atomicity & Context Isolation

### Atomic Tasks 任务原子性
- Each `- [ ]` item is treated as an **atomic task**
- TaskRunner handles **"who does what"**, not **"how to do it"**
- Skills are responsible for actual execution logic

### Context Isolation 上下文隔离
**Default behavior**: Tasks are independent

**Advanced feature (optional)**:
- If tasks in the same file depend on previous outputs
- TaskRunner can pass previous Skill output as context to next Skill
- Enable with special syntax: `- [ ] [depends:1] Task description`

**Example:**
```markdown
- [ ] 抓取 https://example.com/data
- [ ] [depends:1] 分析抓取的数据并生成报告
```

---

## Fault Tolerance 容错机制

**Error Handling:**
- Network timeouts, Skill errors should NOT crash TaskRunner
- Use Try-Catch logic to capture and log errors
- Continue processing next file after current file failure

**Recovery Strategy:**
- Failed tasks remain as `- [!]` for manual review
- Re-running TaskRunner will skip `- [x]` and retry `- [!]`
- User can manually reset `- [!]` to `- [ ]` for retry

---

## Integration Points

### Available Skills
- **BrightData** - Web scraping (四层回退机制)
- **doc-coauthoring** - Document co-authoring workflow
- **frontend-design** - Frontend interface creation
- **[Extensible]** - New skills can be registered to the pool

### File System Structure
```
./Inbox/           # Task input directory
  ├── research-tasks.md
  ├── daily-todos.md
  └── weekly-goals.md

./Outbox/          # Execution log output
  ├── research-tasks-20260128-173015.log
  ├── daily-todos-20260128-173215.log
  └── 36kr-newsflashes.md (generated content)
```

---

## Usage Examples

### Example 1: Web Scraping Task

**User:** "执行任务"

**Inbox/research.md:**
```markdown
- [ ] 抓取 https://36kr.com/newsflashes
- [ ] 抓取 https://geekpark.net
```

**Process:**
1. Scan: 2 tasks found
2. Route: Both → BrightData
3. Confirm: User types 'Confirm'
4. Execute:
   - Task 1: Success (Tier 1, 3s)
   - Task 2: Success (Tier 2, 5s)
5. Update: Both marked as `- [x]`
6. Log: Saved to `./Outbox/research-20260128-173015.log`

---

### Example 2: Mixed Task Types

**Inbox/weekly-plan.md:**
```markdown
- [ ] 抓取集思录热帖 https://jisilu.cn
- [ ] 撰写《量化策略优化》技术文档
- [ ] 设计投资组合仪表盘界面
```

**Process:**
1. Scan: 3 tasks found
2. Route:
   - Task 1 → BrightData
   - Task 2 → doc-coauthoring
   - Task 3 → frontend-design
3. Confirm: Display execution plan, wait for user
4. Execute: Sequential processing
5. Update: Status written back to source file
6. Log: Comprehensive execution log in Outbox

---

### Example 3: Failure Handling

**Inbox/tasks.md:**
```markdown
- [ ] 抓取受保护网站 https://protected-site.com
- [ ] 分析抓取数据
```

**Process:**
1. Execute Task 1: FAILED (Tier 4 exhausted, CAPTCHA)
2. Mark: `- [!] 抓取受保护网站... (Failed: CAPTCHA)`
3. Strategy: Stop processing remaining tasks in tasks.md
4. Log: Error details saved to `tasks-20260128-errors.log`
5. User can manually review and retry

---

## Workflow Philosophy

### "Fire and Forget" Experience
1. **User writes tasks** in Inbox Markdown files
2. **User triggers** TaskRunner: "执行任务"
3. **TaskRunner handles everything**:
   - Scanning
   - Routing
   - Execution
   - Status updates
   - Logging
4. **User reviews results** in Outbox logs

### Zero Context Friction
- No need to open new sessions for each task
- No need to repeat context
- No need to manually track progress
- TaskRunner is the "meta-layer" that orchestrates everything

---

## Configuration (Future)

**Optional `taskrunner.config.md` in Inbox root:**

```yaml
---
routing:
  url_scraping: BrightData
  document_writing: doc-coauthoring
  web_design: frontend-design

execution:
  parallel: false  # Sequential execution
  stop_on_error: file  # file | all | none

logging:
  level: detailed  # detailed | summary
  output_dir: ./Outbox/
---
```

---

## Related Documentation

- `TaskRunner Skill 需求规格说明书.md` - Complete requirements specification
- `../BrightData/SKILL.md` - Web scraping skill
- `../doc-coauthoring/SKILL.md` - Document co-authoring skill
- `../frontend-design/SKILL.md` - Frontend design skill

**Last Updated:** 2026-01-28
