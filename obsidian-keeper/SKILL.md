---
name: obsidian-keeper
description: Use when maintaining a small Obsidian vault, doing weekly knowledge-base cleanup, normalizing YAML frontmatter/tags/summaries across Markdown notes, or cleaning date-only daily notes in 7-日记.
---

# Obsidian Keeper

## Overview

Use this skill to run a direct maintenance pass over the current Obsidian vault.

This skill is designed for small personal vaults. It scans the whole vault, classifies Markdown files safely, edits only allowed targets, and finishes with a concise report. Do not wait for confirmation unless the vault root is unclear or a truly blocking error appears.

Detailed rules live in [reference.md](reference.md).

## Preconditions

- The current working directory must be the Obsidian vault root.
- Treat this as a maintenance run, not a brainstorming session.
- Default to direct execution.

## Execution Flow

1. Confirm the current working directory is the vault root.
2. Scan all Markdown files in the vault.
3. Classify files before changing anything:
   - `7-日记/YYYY-MM-DD.md` -> daily note special case
   - ordinary notes outside skipped directories, outside `7-日记/`, and outside the vault root -> YAML governance target
   - files in skipped directories -> skip and report
4. Process ordinary notes:
   - sort candidates by last modified time, newest first
   - process only the current batch window, newest first
   - add or repair YAML frontmatter
   - repair `tags` using the sandwich method
   - add or repair `summary` using the length rules
   - preserve all custom frontmatter fields
   - never edit content after the second `---`
5. Process daily note special cases:
   - if the body is empty after trimming whitespace, move the file to `13-回收站/`
   - if the body has content, derive a concise title from the full diary content and rename the file to `YYYY-MM-DD 标题.md`
   - if the derived title is low quality, skip and report the file
   - never rewrite the diary body
6. Skip conflicts, malformed files, and encoding problems without stopping the whole run.
7. Finish with a concise report.

## Guardrails

- Scan the whole vault, but do not treat every Markdown file as an editable note.
- Always classify first, then edit.
- Skip system, output, attachment, recycle, maintenance, diary, and vault-root files listed in [reference.md](reference.md).
- Do not delete files permanently.
- Do not overwrite an existing target filename during daily note renaming.
- If a case is ambiguous, skip it and report why.
- Default batch size for ordinary notes is 20 unless the user explicitly changes it.

## Report Format

Return a short Markdown summary with:

- total Markdown files scanned
- ordinary notes updated
- ordinary note batch window used
- daily notes renamed
- empty daily notes moved to recycle
- daily notes skipped for low-quality titles
- skipped files and reasons

## Automation Use

This skill is suitable for scheduled runs.

For automation prompts, keep the instruction short and outcome-focused, for example:

1. Use `obsidian-keeper` on the current vault.
2. Run one maintenance pass.
3. Return only the final summary.
