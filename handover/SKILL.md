---
name: handover
description: Use when handing off work between sessions in the same project, especially when the user says handover, resume from HANDOVER.md, continue a previous session, preserve next steps before context runs out, or carry stable learnings into AGENTS.md or README.md.
---

# Handover

Use this skill to standardize session handoff and resume work without re-scanning the whole project.

## Modes

- `handover write`
- `handover resume`
- `handover`

Use `write` when the current session is ending and you need to preserve state.
Use `resume` when a new session should continue from existing handoff files.
For plain `handover`, infer mode only if the signal is clear:

- active thread with real work already done -> `write`
- cold thread with existing `HANDOVER.md` -> `resume`
- mixed signal -> ask one short clarification instead of guessing

## Project Root

Use the current working directory as the project root by default.

If the current directory is only a child folder, first locate the nearest parent that contains one of these files:

- `AGENTS.md`
- `README.md`
- `.git`

Use that directory as the effective project root for all reads and writes.

## Write Mode

1. Read the project root `AGENTS.md` and `README.md` if they exist.
2. Check repository state with `git status --short` when the project is a Git repo.
3. Read only the most relevant files for the current task. Prefer changed files, files discussed in the session, and files named in the current plan.
4. Do **not** use old `HANDOVER.md` as source material for the new handover. Treat it as stale by default.
5. Build a fresh `HANDOVER.md` from:
   - the current thread context
   - current repository state
   - the most relevant files
   - decisions already made in this session
6. Overwrite the project root `HANDOVER.md` with the exact structure from [references/templates.md](references/templates.md).
7. If the session produced high-confidence, long-lived, reusable rules, update only the managed block in `AGENTS.md`.
8. If the session produced durable project design, implementation, or operation notes, update only the managed block in `README.md`.
9. Use `apply_patch` for all file edits. Do not rely on Python helper scripts.
10. Return only a concise status plus the next-session prompt.

## Resume Mode

1. Read `AGENTS.md` and `HANDOVER.md` from the project root.
2. Summarize the current goal, current status, important files, risks, and next best step.
3. Do not rewrite `HANDOVER.md`, `AGENTS.md`, or `README.md` unless the user explicitly asks.
4. Return a short resume brief and the immediate next step.

## Governance Boundaries

- `HANDOVER.md` is rolling state only. Keep only the latest chain.
- `AGENTS.md` only gets high-confidence, long-term, reusable rules.
- `README.md` only gets durable project notes. Use the managed block, never rewrite the whole file.
- If there is nothing durable to preserve, skip `AGENTS.md` or `README.md` updates.
- Never mix unrelated stale handover content into the new one.
- Do not delete or rewrite unrelated README or AGENTS content outside the managed blocks.

## Managed Blocks

When updating `AGENTS.md` or `README.md`, use these exact markers:

- `<!-- handover:agents:begin -->`
- `<!-- handover:agents:end -->`
- `<!-- handover:readme:begin -->`
- `<!-- handover:readme:end -->`

If the block already exists, replace only the block body.
If the block does not exist, append a new block at the end of the file.
Do not rewrite the rest of the file.

## Output

Follow [references/templates.md](references/templates.md) for:

- `HANDOVER.md` structure
- `AGENTS.md` managed block
- `README.md` managed block
- concise `write` / `resume` / failure outputs
