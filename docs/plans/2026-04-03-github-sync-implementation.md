# GitHub Sync Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build a `github-sync` skill that batch-syncs a fixed set of local Git repositories and returns one concise final report.

**Architecture:** The skill lives in `D:/Dropbox/Project/my-skills/github-sync/`. `SKILL.md` defines trigger conditions, safety boundaries, and usage. `scripts/sync_repos.ps1` performs deterministic repository checks, commit message generation, commit, push, and report aggregation. A small PowerShell test script validates the pure helper functions for commit message generation and report formatting.

**Tech Stack:** Markdown skill files, PowerShell 5.1-compatible script, plain PowerShell test script

---

### Task 1: Add Design And Reference Files

**Files:**
- Create: `D:/Dropbox/Project/my-skills/github-sync/SKILL.md`
- Create: `D:/Dropbox/Project/my-skills/github-sync/references/report-format.md`
- Create: `D:/Dropbox/Project/my-skills/github-sync/assets/repo-list.example.txt`

**Step 1: Write the skill frontmatter and trigger contract**

Define:
- `name: github-sync`
- a description focused on multi-repo GitHub sync, scheduled automation, batch checks, auto-commit and push, and final summary reporting

**Step 2: Write the execution contract**

Describe:
- fixed repository list in script
- no dangerous Git repair actions
- concise final report only
- nanobot-friendly direct execution

**Step 3: Write the report format reference**

Document the final report sections and example output.

### Task 2: Write The Failing Test Script

**Files:**
- Create: `D:/Dropbox/Project/my-skills/github-sync/tests/github-sync.tests.ps1`
- Test: `D:/Dropbox/Project/my-skills/github-sync/scripts/sync_repos.ps1`

**Step 1: Write a failing test for commit message generation**

Test that a docs-only change summary yields:

```powershell
docs: update documentation
```

**Step 2: Write a failing test for concise report formatting**

Test that a mixed result set outputs:
- one `Summary` block
- succeeded items as `repo | branch | message | hash`
- failed items as `repo | stage | error`

**Step 3: Run the test script to verify it fails**

Run:

```powershell
powershell -ExecutionPolicy Bypass -File .\github-sync\tests\github-sync.tests.ps1
```

Expected: fail because helper functions do not exist yet.

### Task 3: Implement The Sync Script

**Files:**
- Create: `D:/Dropbox/Project/my-skills/github-sync/scripts/sync_repos.ps1`

**Step 1: Implement fixed repo configuration and helper functions**

Add functions for:
- configured repo list
- safe-state checks
- large-file checks
- change summary classification
- commit message generation
- final report formatting

**Step 2: Implement the per-repo execution flow**

Implement:
- path validation
- Git validation
- repo safety checks
- status/diff collection
- `git add --all`
- `git commit`
- `git push`
- result aggregation with isolated error handling

**Step 3: Keep PowerShell 5.1 compatibility**

Avoid:
- PowerShell 7-only syntax
- fragile shell escaping
- interactive prompts

### Task 4: Verify And Update Repository Metadata

**Files:**
- Modify: `D:/Dropbox/Project/my-skills/README.md`
- Modify: `D:/Dropbox/Project/my-skills/AGENTS.md`

**Step 1: Run the test script to verify it passes**

Run:

```powershell
powershell -ExecutionPolicy Bypass -File .\github-sync\tests\github-sync.tests.ps1
```

Expected: PASS

**Step 2: Validate the new skill**

Run:

```powershell
python .system\skill-creator\scripts\quick_validate.py github-sync
```

Expected: `Skill is valid!`

**Step 3: Update top-level docs**

Add `github-sync` to:
- `README.md`
- `AGENTS.md`

Keep counts and directory listings accurate.
