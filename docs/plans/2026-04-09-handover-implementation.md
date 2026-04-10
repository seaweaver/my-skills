# Handover Skill Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build a `handover` skill that writes a fresh `HANDOVER.md`, supports resume handoff, and manages stable knowledge updates for `AGENTS.md` and `README.md`.

**Architecture:** `SKILL.md` defines the write/resume/auto workflow and strict file-governance boundaries. The runtime path is pure skill execution: read current project files, inspect Git state, and edit `HANDOVER.md`, `AGENTS.md`, and `README.md` directly with `apply_patch`. The final delivered skill keeps only Markdown resources and no runtime Python dependency.

**Tech Stack:** Markdown, git status, apply_patch

---

### Task 1: Implement Runtime Rules

**Step 1: Define project discovery rules**

Define rules for:
- finding the effective project root
- locating `AGENTS.md`, `README.md`, `HANDOVER.md`
- collecting `git status --short` when available
- updating only the managed blocks in `AGENTS.md` and `README.md`

**Step 2: Encode these rules in `SKILL.md`**

Require:
- `write / resume / auto` mode handling
- no reuse of stale `HANDOVER.md` during write
- `apply_patch` only for file writes
- managed block marker usage

### Task 2: Write The Skill

**Files:**
- Create: `D:/Dropbox/Project/my-skills/handover/SKILL.md`
- Create: `D:/Dropbox/Project/my-skills/handover/references/templates.md`

**Step 1: Define triggering contract**

Include:
- explicit `write` and `resume` commands
- `auto` fallback rules
- governance rules for `AGENTS.md` and `README.md`

**Step 2: Define templates**

Document:
- `HANDOVER.md` template
- managed block examples for `AGENTS.md` and `README.md`
- concise output shapes for write/resume/failure

### Task 3: Validate

**Step 1: Validate the skill**

Run:

```powershell
python .system\skill-creator\scripts\quick_validate.py handover
```

Expected: `Skill is valid!`

### Task 4: Update Repo Index

**Files:**
- Modify: `D:/Dropbox/Project/my-skills/README.md`
- Modify: `D:/Dropbox/Project/my-skills/AGENTS.md`

**Step 1: Update top-level docs**

Add the new skill to:
- skill count in `README.md`
- skill table in `README.md`
- directory tree in `AGENTS.md`

**Step 2: Run final diff check**

Run:

```powershell
git diff --check -- handover README.md AGENTS.md docs/plans/2026-04-09-handover-design.md docs/plans/2026-04-09-handover-implementation.md
```

Expected: no diff-format errors
