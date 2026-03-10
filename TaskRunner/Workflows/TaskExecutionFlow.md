# TaskRunner Execution Workflow 任务执行工作流

**Version**: 1.0
**Purpose**: 完整的任务扫描、路由、执行流程实现

---

## Workflow Overview

```
User Request → Scan Inbox → Parse Tasks → Route to Skills →
Confirm Plan → Execute Sequentially → Update Status → Generate Logs
```

---

## Stage 1: Scan & Parse Implementation

### 1.1 扫描 Inbox 目录

```python
# Pseudocode for scanning logic
inbox_dir = "./Inbox/"
task_queue = []

for file in sorted(glob(inbox_dir + "*.md")):
    content = read_file(file)
    tasks = parse_unchecked_items(content)

    for task in tasks:
        task_queue.append({
            'file': file,
            'line': task.line_number,
            'content': task.text,
            'status': 'pending'
        })
```

### 1.2 解析 Checklist 语法

**Target Pattern**: `- [ ] Task description`

**Regex Pattern**:
```regex
^[\s]*-\s\[\s\]\s+(.+)$
```

**Ignore**:
- `- [x]` - 已完成任务
- `- [!]` - 失败任务（可选：重试）
- 非 checklist 行

---

## Stage 2: Intelligent Routing Implementation

### 2.1 Skill Registry 技能注册表

```yaml
skill_pool:
  BrightData:
    keywords: [抓取, 爬取, scrape, fetch, URL, 网页]
    patterns: [https?://]

  doc-coauthoring:
    keywords: [撰写, 写作, 文档, document, write, draft, 创作]
    patterns: [《.+》, .+\.md, proposal, spec]

  frontend-design:
    keywords: [设计, 界面, UI, 前端, design, interface, 网页设计]
    patterns: [dashboard, 仪表盘, 页面]
```

### 2.2 路由匹配逻辑

```python
def route_task(task_content):
    # 1. URL pattern matching
    if contains_url(task_content):
        if keyword_match(task_content, ['抓取', 'scrape', 'fetch']):
            return 'BrightData'

    # 2. Keyword matching
    for skill, config in skill_pool.items():
        score = calculate_match_score(task_content, config)
        if score > threshold:
            return skill

    # 3. Fallback: ask user
    return ask_user_for_skill(task_content)
```

### 2.3 匹配评分算法

**评分规则**:
- 关键词匹配: +10 分/词
- Pattern 匹配: +20 分
- 上下文相关性: +5 分

**阈值**: 25 分以上视为匹配成功

---

## Stage 3: Pre-flight Check Implementation

### 3.1 生成执行计划表

```python
def generate_execution_plan(task_queue):
    plan = "===== TaskRunner Execution Plan =====\n\n"

    grouped_tasks = group_by_file(task_queue)

    for file, tasks in grouped_tasks.items():
        plan += f"File: {file}\n"
        plan += "-" * 40 + "\n"

        for idx, task in enumerate(tasks, 1):
            plan += f"Task {idx}: {task['content']}\n"
            plan += f"  → Skill: {task['skill']}\n"
            plan += f"  → Action: {get_skill_description(task['skill'])}\n\n"

    plan += f"===== Total: {len(task_queue)} tasks from {len(grouped_tasks)} files =====\n"
    plan += "\nType 'Confirm' to proceed or 'Abort' to cancel."

    return plan
```

### 3.2 等待用户确认

```python
def wait_for_confirmation():
    user_input = get_user_input()

    if user_input.lower() in ['1', '确认', 'yes', 'y']:
        return True
    elif user_input.lower() in ['0', '取消', 'no', 'n']:
        return False
    else:
        print("Invalid input. Please type 'Confirm' or 'Abort'.")
        return wait_for_confirmation()
```

---

## Stage 4: Execution & State Management

### 4.1 顺序执行任务

```python
def execute_tasks(task_queue):
    execution_log = []
    current_file = None
    file_has_error = False

    for task in task_queue:
        # 如果当前文件有错误，跳过该文件的剩余任务
        if current_file != task['file']:
            current_file = task['file']
            file_has_error = False

        if file_has_error:
            skip_task(task)
            continue

        # 执行任务
        try:
            result = invoke_skill(task['skill'], task['content'])

            if result.success:
                update_task_status(task, 'completed')
                execution_log.append({
                    'task': task,
                    'status': 'SUCCESS',
                    'output': result.output,
                    'execution_time': result.time
                })
            else:
                update_task_status(task, 'failed', result.error)
                execution_log.append({
                    'task': task,
                    'status': 'FAILED',
                    'error': result.error
                })
                file_has_error = True  # 标记当前文件有错误

        except Exception as e:
            update_task_status(task, 'failed', str(e))
            execution_log.append({
                'task': task,
                'status': 'FAILED',
                'error': str(e)
            })
            file_has_error = True

    return execution_log
```

### 4.2 更新任务状态

```python
def update_task_status(task, status, error=None):
    file_path = task['file']
    line_number = task['line']

    # 读取文件内容
    lines = read_file_lines(file_path)

    # 更新对应行
    if status == 'completed':
        lines[line_number] = lines[line_number].replace('- [ ]', '- [x]')
    elif status == 'failed':
        error_msg = f" (Failed: {error})" if error else ""
        lines[line_number] = lines[line_number].replace('- [ ]', f'- [!]{error_msg}')

    # 写回文件
    write_file_lines(file_path, lines)
```

### 4.3 调用 Skill

```python
def invoke_skill(skill_name, task_content):
    if skill_name == 'BrightData':
        # 提取 URL
        url = extract_url(task_content)
        return execute_bright_data(url)

    elif skill_name == 'doc-coauthoring':
        # 启动文档协作流程
        return execute_doc_coauthoring(task_content)

    elif skill_name == 'frontend-design':
        # 启动前端设计流程
        return execute_frontend_design(task_content)

    else:
        raise UnknownSkillError(f"Skill '{skill_name}' not found")
```

---

## Stage 5: Logging & Output

### 5.1 生成执行日志

```python
def generate_log(execution_log, task_queue):
    timestamp = get_timestamp()
    log_content = f"""===== TaskRunner Execution Log =====
Execution Time: {timestamp}
Total Tasks: {len(task_queue)}
Success: {count_success(execution_log)}
Failed: {count_failed(execution_log)}

"""

    for idx, entry in enumerate(execution_log, 1):
        log_content += f"""----- Task {idx} -----
Status: {entry['status']}
Content: {entry['task']['content']}
Skill: {entry['task']['skill']}
"""

        if entry['status'] == 'SUCCESS':
            log_content += f"Execution: {entry.get('execution_time', 'N/A')}\n"
            log_content += f"Output: {entry.get('output', 'No output')}\n"
        else:
            log_content += f"Error: {entry.get('error', 'Unknown error')}\n"

        log_content += "\n"

    return log_content
```

### 5.2 保存日志文件

```python
def save_log(log_content, source_file):
    timestamp = get_timestamp_short()  # YYYYMMDD-HHMMSS
    filename = get_filename_without_ext(source_file)

    # 成功日志
    if has_success(log_content):
        log_path = f"./Outbox/{filename}-{timestamp}.log"
        write_file(log_path, log_content)

    # 错误日志
    if has_errors(log_content):
        error_log_path = f"./Outbox/{filename}-{timestamp}-errors.log"
        error_content = extract_error_entries(log_content)
        write_file(error_log_path, error_content)
```

---

## Error Handling & Recovery

### 容错策略

**Level 1: Task Level**
- Try-Catch 包裹每个任务执行
- 记录错误详情到日志
- 标记任务为 `- [!]`

**Level 2: File Level**
- 当前文件任务失败后，停止该文件的后续任务
- 继续处理下一个文件的任务

**Level 3: Global Level**
- TaskRunner 永不崩溃
- 所有异常都被捕获并记录
- 确保至少生成一份执行日志

### 重试机制

**手动重试**:
```markdown
- [!] 抓取 https://example.com (Failed: Timeout)
```

用户可以:
1. 修改为 `- [ ]` 重新标记为待执行
2. 再次运行 TaskRunner

**自动重试（未来功能）**:
```yaml
- [ ] [retry:3] 抓取 https://unstable-api.com
```

---

## Advanced Features (Optional)

### 任务依赖

**语法**: `- [ ] [depends:1,2] Task description`

**示例**:
```markdown
- [ ] 抓取 https://example.com/data        # Task 1
- [ ] 分析数据生成报告                      # Task 2
- [ ] [depends:1,2] 发送报告邮件           # Task 3 (依赖 1,2)
```

**实现**:
```python
def parse_dependencies(task_content):
    pattern = r'\[depends:([0-9,]+)\]'
    match = re.search(pattern, task_content)

    if match:
        dep_ids = [int(x) for x in match.group(1).split(',')]
        return dep_ids
    return []

def execute_with_dependencies(task_queue):
    # Build dependency graph
    # Execute in topological order
    # Pass outputs as context
```

---

## Performance Optimization

### 并行执行（未来功能）

```python
from concurrent.futures import ThreadPoolExecutor

def execute_tasks_parallel(task_queue):
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = []

        for task in task_queue:
            if not has_dependencies(task):
                future = executor.submit(execute_task, task)
                futures.append(future)

        results = [f.result() for f in futures]

    return results
```

**注意**: 并行执行需要处理文件写入冲突。

---

## Testing & Validation

### 单元测试

```python
def test_parse_unchecked_items():
    content = """
    - [ ] Task 1
    - [x] Task 2
    - [ ] Task 3
    """

    tasks = parse_unchecked_items(content)
    assert len(tasks) == 2
    assert tasks[0].text == "Task 1"
    assert tasks[1].text == "Task 3"
```

### 集成测试

```markdown
# Test Cases

## Case 1: Single file, single task
Input: Inbox/test.md with 1 unchecked task
Expected: Task executed, status updated, log generated

## Case 2: Multiple files, mixed tasks
Input: 3 files with total 10 tasks (3 BrightData, 4 doc-coauthoring, 3 frontend-design)
Expected: All routed correctly, executed sequentially, statuses updated

## Case 3: Failure handling
Input: 1 file with 3 tasks, Task 2 fails
Expected: Task 1 success, Task 2 failed, Task 3 skipped
```

---

## Related Files

- `../SKILL.md` - TaskRunner skill definition
- `../TaskRunner Skill 需求规格说明书.md` - Requirements specification

**Last Updated:** 2026-01-28
