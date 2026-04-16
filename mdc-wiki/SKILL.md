---
name: mdc-wiki
description: Use when building, querying, ingesting, or maintaining a markdown-based knowledge wiki in a project, team repository, or company knowledge base, especially when knowledge should compound over time instead of being re-derived from raw sources in each session.
---

# MDC Wiki

Build and maintain a persistent, interlinked markdown knowledge base.
This skill packages the "LLM wiki" pattern into a tool-agnostic workflow that
works across coding agents, editors, and repository setups.

The core idea is simple: do not rediscover knowledge from scratch every session.
Capture it once, structure it, cross-link it, and keep it current.

## Overview

Use this skill to treat a markdown directory as a compounding knowledge system:
- Raw inputs are stored once and preserved
- Synthesized knowledge lives in curated wiki pages
- Navigation and activity are kept visible through `index.md` and `log.md`
- Future agents should orient themselves before making changes

This skill is intentionally not tied to a specific agent, editor, sync product,
or vendor config format. It should work with Codex, Claude Code, OpenCode, and
similar coding agents as long as they can read files, search text, and write
markdown.

## When to Use

Use this skill when the user:
- Wants to create a project wiki, research wiki, team knowledge base, or domain notebook
- Wants to ingest URLs, PDFs, pasted notes, meeting transcripts, or design docs into a markdown wiki
- Wants answers based on an existing markdown knowledge base rather than ad hoc browsing
- Wants to lint, audit, or health-check a wiki for broken links, stale pages, or missing structure
- Wants a portable wiki workflow that works in Git repos, shared folders, or editor vaults

Do not use this skill when:
- The task is a one-off summary with no need to preserve knowledge
- The output should live in a database or specialized CMS instead of markdown files
- The repository already has a different documented knowledge-management workflow that should be preserved

## Wiki Path Resolution

Resolve the wiki path in this order:

1. Use the path explicitly given by the user
2. Use the current project directory if the user wants the repository itself to be the wiki
3. Use a project or environment variable if one is already defined
4. Fall back to a sensible default such as `./wiki` or `~/wiki`

Do not assume a specific agent config file exists.
If a host platform injects skill config, that is optional and should be treated as one input source, not a requirement.

## Architecture

Recommended structure:

```text
wiki/
├── SCHEMA.md
├── index.md
├── log.md
├── raw/
│   ├── articles/
│   ├── papers/
│   ├── transcripts/
│   └── assets/
├── entities/
├── concepts/
├── comparisons/
├── queries/
└── _archive/
```

Three layers:
- Layer 1: `raw/` contains immutable source material
- Layer 2: wiki pages contain synthesized, cross-linked knowledge
- Layer 3: `SCHEMA.md` defines conventions, taxonomy, and update policy

## Session Start Rule

When a wiki already exists, always orient before doing anything else:

1. Read `SCHEMA.md`
2. Read `index.md`
3. Read the recent tail of `log.md`
4. Search the wiki for the current topic before creating new pages

This prevents duplicate pages, broken conventions, and repeated work.

## Agent Operating Rules

Any compatible coding agent should follow these rules:

1. Never edit files inside `raw/` after capture
2. Never create a wiki page without checking whether it already exists
3. Always update `index.md` when pages are created, moved, or archived
4. Always append meaningful actions to `log.md`
5. Prefer cross-links over isolated pages
6. Preserve contradictions explicitly instead of silently overwriting them
7. Ask before mass-updating many existing pages

Required capabilities are generic:
- Read files
- Search filenames and file contents
- Fetch or import source material
- Write markdown
- Run lightweight validation scripts when needed

Do not assume tool names such as `read_file`, `search_files`, or `web_extract`.
Use whatever the host agent provides to achieve those capabilities.

## Initializing a New Wiki

When asked to start a new wiki:

1. Determine the wiki path
2. Create the directory structure
3. Ask or infer the domain scope
4. Write `SCHEMA.md` customized for that domain
5. Write initial `index.md`
6. Write initial `log.md`
7. Confirm the wiki is ready and suggest the first sources to ingest

### SCHEMA.md Template

```markdown
# Wiki Schema

## Domain
[What this wiki covers]

## Conventions
- File names: lowercase, hyphens, no spaces
- Every wiki page starts with YAML frontmatter
- Use `[[wikilinks]]` between related pages
- When updating a page, always bump the `updated` date
- Every new page must be added to `index.md`
- Every action must be appended to `log.md`

## Frontmatter
```yaml
---
title: Page Title
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query | summary
tags: [from taxonomy below]
sources: [raw/articles/source-name.md]
---
```

## Tag Taxonomy
[Define the allowed tag set here before using new tags]

## Page Thresholds
- Create a page when a concept/entity is central to one source or recurring across sources
- Add to an existing page when a source expands something already covered
- Avoid new pages for passing mentions
- Split pages when they become too large to scan quickly
- Archive pages when fully superseded

## Update Policy
1. Check source dates
2. Preserve conflicting claims with dates and sources
3. Mark contradictions explicitly
4. Surface contradictions in lint output
```

### index.md Template

```markdown
# Wiki Index

> Content catalog. Every wiki page should appear here with a one-line summary.
> Last updated: YYYY-MM-DD | Total pages: N

## Entities

## Concepts

## Comparisons

## Queries
```

### log.md Template

```markdown
# Wiki Log

> Chronological record of wiki actions
> Format: `## [YYYY-MM-DD] action | subject`

## [YYYY-MM-DD] create | Wiki initialized
- Domain: [domain]
- Structure created with SCHEMA.md, index.md, log.md
```

## Core Operation: Ingest

When the user provides a source:

1. Capture the raw source into `raw/`
2. Keep the raw copy immutable
3. Identify entities, concepts, decisions, and open questions
4. Check what already exists in the wiki
5. Create or update wiki pages according to `SCHEMA.md`
6. Add cross-links
7. Update `index.md`
8. Append an entry to `log.md`
9. Report which files changed

Examples of raw source capture:
- URL to `raw/articles/`
- PDF to `raw/papers/`
- Transcript or pasted notes to `raw/transcripts/`
- Images and diagrams to `raw/assets/`

If a single ingest would touch many existing pages, pause and confirm scope first.

## Core Operation: Query

When the user asks a question against the wiki:

1. Read `index.md`
2. Search relevant `.md` files when the wiki is large
3. Read the most relevant pages
4. Synthesize the answer from compiled knowledge
5. Cite the pages used in the synthesis
6. File the answer back into `queries/` or `comparisons/` only if it is worth preserving
7. Append the action to `log.md`

Do not file trivial answers back into the wiki.
Store only the kinds of synthesis that would be painful to reconstruct later.

## Core Operation: Lint

When the user asks for a health check, audit, or lint:

Check for:
- Orphan pages with no inbound wikilinks
- Broken wikilinks
- Pages missing from `index.md`
- Missing or invalid frontmatter
- Tags not defined in `SCHEMA.md`
- Contradictory claims on related pages
- Oversized pages that should be split
- Stale pages that lag behind their newest cited sources
- `log.md` files large enough to rotate

Report findings grouped by severity:
- Broken links and missing structure
- Contradictions and stale knowledge
- Style, size, and taxonomy issues

Append the lint action to `log.md`.

## Searching and Validation

Use the host agent's native file and text search capabilities.
Typical operations include:
- Find pages by filename
- Find pages by content
- Find pages by tag
- Read the last section of `log.md`
- Run a small script to validate links and frontmatter

Prefer simple, repeatable checks over clever one-off automation.

## Archiving

When content is fully superseded:

1. Move the page under `_archive/`
2. Remove it from `index.md`
3. Update or soften links from active pages
4. Append the archive action to `log.md`

Do not silently delete knowledge that may still matter historically.

## Optional Integrations

This workflow works with many environments:
- Git repositories
- Shared folders
- VS Code workspaces
- Obsidian vaults
- Other markdown editors or sync tools

Optional editor features that can help:
- Wikilink navigation
- Graph view
- YAML frontmatter queries
- Full-text search
- Attachment previews

Obsidian is a useful option, not a requirement.
If a team uses Obsidian, the wiki directory can double as a vault.
If a team uses plain Git plus VS Code, that is equally valid.

## Platform Compatibility Notes

### Codex

- Prefer the current repository or user-specified folder as the wiki root
- Use shell/file tools for search, reading, and linting
- Keep changes explicit and traceable in markdown files

### Claude Code

- Follow the same orientation rule at session start
- Use repository search before creating new pages
- Maintain `index.md` and `log.md` as first-class navigation files

### OpenCode and similar agents

- Map this workflow onto whatever file, search, and fetch tools are available
- Preserve the method even if the tool names differ
- Avoid vendor-specific assumptions in generated content

### Hermes or other host-specific systems

- Host-specific config injection is optional
- If a platform provides a configured wiki path, use it
- If not, fall back to the generic path resolution order above

## Team and Company Recommendations

For data teams and internal company use, prefer these conventions:

1. Keep the wiki inside a Git-managed project or a clearly versioned shared directory
2. Use the project directory itself as the wiki root when the repository is already knowledge-centric
3. Require `SCHEMA.md`, `index.md`, and `log.md` from day one
4. Keep raw evidence and synthesized knowledge separate
5. Make major updates auditable through commits and log entries
6. Prefer incremental maintenance over periodic rewrites
7. Treat contradictions, unknowns, and `null` findings as valid knowledge states
8. Use markdown and csv-first workflows where possible for portability and batch validation

Recommended team scenarios:
- Research and vendor due-diligence notes
- Data lineage and metric definition knowledge
- Source-system quirks and field interpretation notes
- Incident learnings and investigation trails
- Strategy, architecture, and design decision records

## Common Mistakes

- Treating the wiki like a dumping ground instead of a curated system
- Skipping orientation at the start of a session
- Creating duplicate pages for the same concept
- Forgetting to update `index.md`
- Forgetting to append `log.md`
- Using freeform tags without updating the taxonomy
- Silently overwriting contradictions
- Binding the workflow to a single editor, agent, or proprietary config path

## Bottom Line

This skill is a portable operating model for markdown knowledge systems.
The durable value is not a specific agent integration.
The durable value is the discipline:
- preserve raw evidence
- synthesize into pages
- cross-link aggressively
- keep navigation current
- make updates auditable

If a coding agent can read, search, and write markdown, it can use this skill.
