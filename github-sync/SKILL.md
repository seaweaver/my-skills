---
name: github-sync
description: Use when syncing multiple local Git repositories to GitHub, especially for scheduled automation, batch repository checks, auto-commit and push workflows, or when the user wants one final summary across several local repos.
---

# GitHub Sync

Use this skill for scheduled multi-repository Git sync on this Windows machine.

## Workflow

1. Run `powershell -ExecutionPolicy Bypass -File .\github-sync\scripts\sync_repos.ps1` from the repository root that contains this skill.
2. Let the script use its fixed repository list. Do not improvise extra repositories during the run.
3. Do not use `reset`, `rebase`, `merge`, `stash`, force-push, or any interactive repair step.
4. If a repository fails, report the failure exactly and continue with the remaining repositories.
5. Return only the final summary report.

## Boundaries

- The repository list is fixed in `scripts/sync_repos.ps1` for version 1.
- Repositories with merge, rebase, cherry-pick, revert, detached HEAD, or oversized-file states must be marked failed.
- Commit messages must stay single-line and must be derived only from Git status and diff skeletons.
- If the change skeleton is ambiguous, fall back to `chore: sync local changes`.

## Output

Follow [references/report-format.md](references/report-format.md) and keep the final answer concise.
