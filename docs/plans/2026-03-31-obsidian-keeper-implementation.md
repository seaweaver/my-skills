# Obsidian Keeper Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Create an `obsidian-keeper` skill that can directly maintain a small Obsidian vault with full-vault scanning, safe classification, YAML governance for normal notes, and date-only daily note cleanup.

**Architecture:** The skill lives in `D:/Dropbox/Project/my-skills/obsidian-keeper/` and uses a two-file structure. `SKILL.md` defines activation, execution flow, and reporting expectations. `reference.md` stores the directory classification rules, YAML governance rules, and daily note rename/recycle rules so the main skill stays concise.

**Tech Stack:** Markdown skill files only

---

### Task 1: Create The Skill Skeleton

**Files:**
- Create: `D:/Dropbox/Project/my-skills/obsidian-keeper/SKILL.md`
- Create: `D:/Dropbox/Project/my-skills/obsidian-keeper/reference.md`

**Step 1: Define the activation contract**

Write frontmatter with:
- `name: obsidian-keeper`
- a description focused on when to use the skill: Obsidian vault maintenance, frontmatter governance, weekly cleanup, and date-only daily note cleanup

**Step 2: Define the execution flow**

In `SKILL.md`, describe:
- current working directory must be the vault root
- full-vault scan of Markdown files
- safe classification before editing
- direct execution without waiting for confirmation
- final summary output

**Step 3: Define detailed governance rules**

In `reference.md`, document:
- skipped system/output directories
- ordinary note YAML/tag/summary rules
- preservation of content after the second `---`
- daily note rename/recycle logic
- conflict and exception handling

### Task 2: Validate The Skill Shape

**Files:**
- Test: `D:/Dropbox/Project/my-skills/obsidian-keeper/SKILL.md`
- Test: `D:/Dropbox/Project/my-skills/obsidian-keeper/reference.md`

**Step 1: Read both files back**

Check that:
- the frontmatter is valid
- the description is trigger-oriented
- the rules match the approved design

**Step 2: Confirm the skill is automation-friendly**

Check that:
- it executes directly
- it does not depend on interactive clarification
- it returns a concise report with counts and skipped reasons
