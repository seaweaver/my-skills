---
name: self-improvement
description: Use when a command or tool fails, the user corrects the agent, knowledge is outdated, an external integration breaks, or a better recurring approach is discovered. Capture the learning in local `.learnings/` files and promote durable items to AGENTS.md, TOOLS.md, USER.md, MEMORY.md, HISTORY.md, CLAUDE.md, or Copilot instructions.
---

# Self-Improvement Skill

Capture repeatable learnings into local markdown files so future sessions stop repeating the same mistakes.

## Local-First Policy

- This skill is maintained locally at `D:\Dropbox\Project\my-skills\self-improving-agent`
- Do not auto-install or auto-update this skill with `git clone`, `git pull`, `clawdhub install`, package-manager commands, or network template downloads during normal use
- Upstream changes should be reviewed manually and merged into the local copy deliberately

## First-Use Initialisation

Before logging anything, ensure the current project or workspace root contains:

- `.learnings/LEARNINGS.md`
- `.learnings/ERRORS.md`
- `.learnings/FEATURE_REQUESTS.md`

If any file is missing, create it. Never overwrite existing files.

Only initialize `.learnings/` for the current active project or workspace when the skill is actually needed. Do not pre-create `.learnings/` across unrelated projects just because this skill exists.

Recommended file headers:

```markdown
# Learnings

Corrections, insights, knowledge gaps, and best practices.

**Categories**: correction | insight | knowledge_gap | best_practice

---
```

```markdown
# Errors

Command failures and integration errors.

---
```

```markdown
# Feature Requests

Capabilities requested by the user.

---
```

## Safety Rules

- Do not log secrets, tokens, private keys, cookies, environment variables, or full config/source files unless the user explicitly wants that level of detail
- Prefer concise summaries or redacted excerpts over raw tool output and full transcripts
- When recording command failures, keep only the error needed for future diagnosis
- When reusing learnings across sessions or agents, prefer sanitized summaries plus relevant file paths

## Quick Reference

| Situation | Action |
|-----------|--------|
| Command or operation failed unexpectedly | Log to `.learnings/ERRORS.md` |
| User corrected the agent | Log to `.learnings/LEARNINGS.md` with category `correction` |
| External API / tool / MCP failed | Log to `.learnings/ERRORS.md` |
| Knowledge was outdated | Log to `.learnings/LEARNINGS.md` with category `knowledge_gap` |
| Better recurring approach discovered | Log to `.learnings/LEARNINGS.md` with category `best_practice` or `insight` |
| User requested a missing capability | Log to `.learnings/FEATURE_REQUESTS.md` |
| Similar learning already exists | Update existing entry, link with `See Also`, or increase priority instead of creating near-duplicate entries |
| Durable workflow or tool rule emerged | Promote to prompt files instead of leaving it only in `.learnings/` |

## Workflow

1. Decide whether the event is an `ERROR`, `LEARNING`, or `FEATURE_REQUEST`
2. Check whether a semantically similar entry already exists
3. Append a concise, sanitized entry with a stable ID
4. If the learning is durable and broadly useful, promote it to the right prompt file

## Detection Triggers

Automatically consider this skill when you notice:

**Corrections** (log to `LEARNINGS.md` with category `correction`):
- English: "No, that's not right", "Actually, it should be", "You're wrong about", "That's outdated"
- 中文: “不对”, “你好像不对”, “你理解错了”, “不是这个意思”, “你搞反了”, “你这个说法不准确”, “实际应该是”, “这个已经过时了”, “我不是这个意思”

**Feature Requests** (log to `FEATURE_REQUESTS.md`):
- English: "Can you also", "I wish you could", "Is there a way to", "Why can't you"
- 中文: “能不能顺手支持”, “可不可以直接”, “最好还能”, “为什么不能”, “以后能不能自动”, “有没有办法直接”, “我希望你下次可以”

**Knowledge Gaps** (log to `LEARNINGS.md` with category `knowledge_gap`):
- The user provides information you did not know
- Documentation or release behavior differs from your understanding
- Local environment facts contradict your assumption
- 中文常见信号: “最新不是这样了”, “现在已经改了”, “官方文档变了”, “我本地不是这样”, “这个版本行为变了”

**Errors** (log to `ERRORS.md`):
- Command returns non-zero exit code
- Exception, traceback, timeout, connection failure, permission error
- Unexpected output or behavior after a supposedly successful step
- 中文常见信号: “报错了”, “超时了”, “没起起来”, “找不到”, “权限不够”, “连不上”, “没生效”, “执行失败”, “结果不对”

## Priority Guidelines

- `critical`: secrets leak risk, destructive mistake, or recurring high-cost failure
- `high`: blocks delivery, likely to recur, or caused incorrect conclusion
- `medium`: useful correction or workflow improvement with moderate reuse value
- `low`: minor polish, one-off preference, or weak signal not yet proven recurrent

## Promotion Targets

| Learning Type | Promote To |
|---------------|------------|
| Workflow, coordination, operating rules | `AGENTS.md` |
| Tool gotchas, environment constraints, path quirks | `TOOLS.md` |
| User style, tone, stable communication preferences | `USER.md` |
| Stable long-term facts that should auto-load | `MEMORY.md` |
| Dated events, transient status, investigation notes | `HISTORY.md` |
| Claude Code global or repo-specific guidance | `CLAUDE.md` |
| Copilot shared instructions | `.github/copilot-instructions.md` |

## Logging Format

### Learning Entry

Append to `.learnings/LEARNINGS.md`:

```markdown
## [LRN-YYYYMMDD-XXX] category

**Logged**: ISO-8601 timestamp
**Priority**: low | medium | high | critical
**Status**: pending
**Area**: frontend | backend | infra | tests | docs | config

### Summary
One-line description of what was learned

### Details
What happened, what was wrong, and what is correct now

### Suggested Action
Specific fix, prompt update, or workflow improvement

### Metadata
- Source: conversation | error | user_feedback | recurring_pattern
- Related Files: path/to/file.ext
- Tags: tag1, tag2
- See Also: LRN-20250110-001
- Pattern-Key: simplify.dead_code | harden.input_validation

---
```

### Error Entry

Append to `.learnings/ERRORS.md`:

```markdown
## [ERR-YYYYMMDD-XXX] command_or_tool

**Logged**: ISO-8601 timestamp
**Priority**: high
**Status**: pending
**Area**: frontend | backend | infra | tests | docs | config

### Summary
Brief description of what failed

### Error
Short error excerpt or redacted output

### Context
- Command or operation attempted
- Inputs or parameters used
- Environment details if relevant

### Suggested Fix
What will likely prevent recurrence

### Metadata
- Reproducible: yes | no | unknown
- Related Files: path/to/file.ext
- See Also: ERR-20250110-001

---
```

### Feature Request Entry

Append to `.learnings/FEATURE_REQUESTS.md`:

```markdown
## [FEAT-YYYYMMDD-XXX] capability_name

**Logged**: ISO-8601 timestamp
**Priority**: medium
**Status**: pending
**Area**: frontend | backend | infra | tests | docs | config

### Requested Capability
What the user wanted to do

### User Context
Why they needed it

### Suggested Implementation
How this might be implemented later

### Metadata
- Frequency: first_time | recurring
- Related Features: existing_feature_name

---
```

## ID Generation

Format: `TYPE-YYYYMMDD-XXX`

- `TYPE`: `LRN` (learning), `ERR` (error), `FEAT` (feature request)
- `YYYYMMDD`: current date
- `XXX`: sequential number or short random suffix such as `001` or `A7B`

Examples:

- `LRN-20260329-001`
- `ERR-20260329-A3F`
- `FEAT-20260329-002`

## Resolving Entries

When an issue is fixed or a learning has been promoted:

1. Update `Status`
2. Add a short resolution block

Resolution example:

```markdown
### Resolution
- **Resolved**: 2026-03-29T17:00:00+08:00
- **Commit/PR**: abc123 or #42
- **Notes**: Brief description of what changed
```

Common status values:

- `pending` - logged but not acted on yet
- `in_progress` - currently being handled
- `resolved` - fixed or addressed
- `wont_fix` - consciously not fixing
- `promoted` - moved into prompt files or durable project docs

## Best Practices

1. Log immediately while context is still fresh
2. Be specific enough that a future agent can act quickly
3. Include reproduction clues for errors when available
4. Link relevant files and commands, but keep the entry concise
5. Suggest a concrete fix instead of only saying “investigate”
6. Reuse consistent categories and IDs
7. Prefer updating an existing near-duplicate entry over adding another one
8. Promote durable learnings aggressively; do not leave high-value rules buried in `.learnings/`

## Agent-Specific Notes

### nanobot

- Keep `.learnings/` in the instance workspace root or active project root
- Rely on this skill's trigger description plus a short reminder in `AGENTS.md` to improve hit rate
- When promoting learnings, follow nanobot's split: stable facts -> `MEMORY.md`, dated events -> `HISTORY.md`

### Codex

- Keep the skill in the active skills directory or shared skill source used by Codex
- Add a short reminder in global or project `AGENTS.md` so failure/correction scenarios trigger this skill more reliably
- Prefer project-local `.learnings/` over global dumping

### Claude Code

- Keep the skill in Claude's skill path or project skill path
- Add a short reminder in `CLAUDE.md`
- Optional hooks can increase compliance, but the recommended default is activator-only setup

## Optional Hooks

- Hooks are opt-in, not required
- Recommended default: `UserPromptSubmit` activator only
- Enable `PostToolUse` only if you are comfortable with hook scripts inspecting command output for error patterns
- See `references/hooks-setup.md` for configuration details

## Optional OpenClaw Notes

- OpenClaw-specific cross-session tools are optional
- Only use cross-session sharing in trusted environments and only when cross-session context is actually needed
- Prefer short sanitized summaries and relevant file paths rather than raw transcripts

See `references/openclaw-integration.md` if you explicitly need that mode.
