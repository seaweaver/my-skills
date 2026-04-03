# Obsidian Keeper Reference

## Vault Assumptions

- Vault root is the current working directory.
- The vault is small enough for a full Markdown scan each run.
- The skill is optimized for safety over maximum coverage.

## File Classification

### Daily note special case

Treat a file as a daily note special case only when both conditions are true:

- the file is inside `7-日记/`
- the filename matches `YYYY-MM-DD.md`

### Skipped directories

Skip all Markdown files inside these directories:

- `1-AIAgent/`
- `7-日记/` for YAML governance
- `9-附件/`
- `10-Memo/`
- `11-Inbox/`
- `12-Outbox/`
- `13-回收站/`
- `.learnings/`
- `.trash/`

### Ordinary note targets

Treat all other Markdown files as ordinary note candidates, with two exceptions:

- do not treat any file under `7-日记/` as an ordinary note
- do not treat Markdown files placed directly in the vault root as ordinary notes

Typical examples include:

- `Clippings/`
- `2-健康/`
- `3-工作/`
- `4-阅读/`
- `5-游戏/`
- `6-文章/`
- `8-投资/`
- any future Markdown directory not listed in skipped directories

### Batch order

Process ordinary note candidates in this order:

- sort by file last modified time, newest first
- process only the current batch window
- default batch size is 20 ordinary notes per run

## YAML Governance Rules

### Trigger conditions

Update an ordinary note when any of these is true:

- YAML frontmatter is missing
- `tags` is missing
- `tags` exists but does not follow the sandwich method
- `summary` is missing or clearly inconsistent with the length rules

### Hard limits

- Edit only the top YAML frontmatter block.
- Never edit content after the second `---`.
- Preserve custom fields such as `created`, `aliases`, `url`, `author`, `published`, or any other existing metadata.

### Standard shape

Use this logical structure:

```yaml
---
title: "Document title"
tags: [tag1, tag2, tag3]
summary: ""
---
```

### Title rule

- Reuse the existing frontmatter title when present and sensible.
- Otherwise derive the title from the filename without the `.md` extension.

### Tag rule

Generate or repair tags using the sandwich method:

- total tag count must be 3 to 7
- include 1 macro domain tag
- include 2 to 4 topic/entity tags
- optionally include 1 context/problem/scenario tag

If existing tags are partially useful:

- keep meaningful user tags
- add missing layers
- avoid deleting useful manual tags unless they are clearly broken noise

### Summary rule

- if body length is under 300 characters, keep `summary` empty
- if body length is 300 to 1000 characters, write one sentence
- if body length is above 1000 characters, write 3 to 5 concise bullet points

## Daily Note Handling

### Empty date-only daily notes

For `7-日记/YYYY-MM-DD.md`:

- treat the file as empty if the body becomes empty after trimming whitespace and blank lines
- move it to `13-回收站/`
- do not permanently delete it

### Non-empty date-only daily notes

For `7-日记/YYYY-MM-DD.md` with content:

- extract a concise title from the full diary content
- rename the file to `YYYY-MM-DD 标题.md`
- do not edit the body

### Title extraction method

Derive the title by summarizing the whole diary entry rather than copying the first line.

The title should:

- reflect the main topic of the entry
- be concise and filename-safe
- avoid copying raw URLs, placeholders, or fragments

When cleaning the final title:

- remove leading `#`
- remove leading list markers like `-`, `*`, `1.`
- remove task markers like `[ ]` and `[x]`
- trim whitespace
- remove Windows-invalid filename characters: `< > : " / \ | ? *`
- collapse repeated spaces
- keep the title concise rather than copying a full paragraph

### Low-quality title guardrail

Skip renaming and report the file when the derived title is clearly low quality, including cases such as:

- raw URL or URL-like text
- placeholder words such as `todo`
- very short abbreviations without clear meaning
- pure symbols or punctuation
- content that is too fragmentary to support a useful title

### Rename conflict handling

- if the target filename already exists, skip the file
- report the source file and the conflicting target path
- never overwrite an existing file automatically

## Failure Handling

Skip and report when any of these happens:

- malformed YAML that cannot be safely repaired
- file encoding problems
- unreadable file contents
- filename conflicts
- unclear classification

Do not stop the whole run because of one bad file.

## Final Report Checklist

At the end of each run, report:

- total Markdown files scanned
- ordinary notes updated
- ordinary note batch window used
- daily notes renamed
- empty daily notes moved to `13-回收站/`
- daily notes skipped for low-quality titles
- skipped files grouped by reason
