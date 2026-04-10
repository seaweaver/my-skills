# Handover Templates

## `HANDOVER.md`

Always use this structure:

```md
# HANDOVER

## Goal
一句话说明当前线程真正要完成什么

## Current Status
- 已完成
- 已验证
- 未完成

## Key Decisions
- 已拍板方案
- 明确边界
- 明确不做

## Important Files
- `/abs/path/file` - 作用

## Next Best Step
新线程现在最该先做的一件事

## Risks
- 已知风险
- 尚未验证点
- 外部依赖

## What To Avoid
- 不要重复做的事
- 不要覆盖的内容
- 已知坑

## Knowledge To Preserve
### AGENTS.md Candidates
- 长期稳定、可复用规则

### README.md Candidates
- 长期有效的设计、实现、操作说明
```

## `AGENTS.md` Managed Block

Only write stable rules. Use this block body:

```md
## Handover Learned Rules
- 规则 1
- 规则 2
```

Markers:

```md
<!-- handover:agents:begin -->
...
<!-- handover:agents:end -->
```

## `README.md` Managed Block

Only write durable project notes. Use this block body:

```md
## Maintainer Notes

### Workflow Decisions
- ...

### Operation Notes
- ...

### Integration Notes
- ...
```

Markers:

```md
<!-- handover:readme:begin -->
...
<!-- handover:readme:end -->
```

## Concise Output

### Write

```text
# handover
- mode: write
- handover: updated
- agents: updated / unchanged
- readme: updated / unchanged

## next-session-prompt
Read AGENTS.md and HANDOVER.md first.
Then continue the Next Best Step in HANDOVER.md without redoing completed work.
```

### Resume

```text
# handover
- mode: resume
- goal: ...
- next: ...

## resume-brief
...
```

### Failure

```text
# handover
- mode: write|resume
- status: failed
- stage: ...
- error: ...
```
