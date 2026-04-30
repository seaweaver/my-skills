---
name: my-wiki
description: "Karpathy's LLM Wiki — build and maintain a persistent, interlinked markdown knowledge base. Ingest sources, query compiled knowledge, and lint for consistency."
version: 2.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [wiki, knowledge-base, research, notes, markdown, rag-alternative]
    category: research
    related_skills: [obsidian, arxiv, agentic-research-ideas]
    config:
      - key: wiki.path
        description: Path to the LLM Wiki knowledge base directory
        default: "~/wiki"
        prompt: Wiki directory path
---

# Karpathy's LLM Wiki

Build and maintain a persistent, compounding knowledge base as interlinked markdown files.
Based on [Andrej Karpathy's LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

Unlike traditional RAG (which rediscovers knowledge from scratch per query), the wiki
compiles knowledge once and keeps it current. Cross-references are already there.
Contradictions have already been flagged. Synthesis reflects everything ingested.

**Division of labor:** The human curates sources and directs analysis. The agent
summarizes, cross-references, files, and maintains consistency.

## When This Skill Activates

Use this skill when the user:
- Asks to create, build, or start a wiki or knowledge base
- Asks to ingest, add, or process a source into their wiki
- Asks a question and an existing wiki is present at the configured path
- Asks to lint, audit, or health-check their wiki
- References their wiki, knowledge base, or "notes" in a research context

## Scope Boundary (when `mdc-wiki` also exists)

If both `llm-wiki` and `mdc-wiki` are installed, select by audience first:

- **`llm-wiki`**: personal knowledge management (single-owner wiki, optimized for the user's own decision loop)
- **`mdc-wiki`**: shared/team knowledge base (multi-reader collaboration and team governance)

Do not blend governance models in one operation. For personal wiki tasks, avoid applying team-oriented conventions unless explicitly requested.

## Locale and Naming Overrides (for Chinese-first personal wikis)

When the user explicitly requests Chinese-first conventions, override default naming/text style as follows:

- **Primary language:** Chinese for page titles, body text, TL;DR, structured sections, and log entries
- **English usage:** only for unavoidable technical terms, model names, code, or standard abbreviations (e.g., RAG/ETF/VaR)
- **Knowledge page filenames:** prefer **Chinese filenames** (can include digits and hyphens)
- **Forbidden filename chars (Windows-safe):** `/ \\ : * ? " < > |`
- **Raw source files:** keep original names by default (minimal intervention), only version suffix on conflict

### Retroactive migration (existing English filenames)

If the user asks to unify historical pages:

1. Build a rename map (old path -> new Chinese path)
2. Rename files across `entities/`, `concepts/`, `comparisons/`, `queries/`
3. Rewrite all `[[wikilinks]]` by target stem (support `[[name]]`, `[[name|alias]]`, `[[name#section]]`)
4. Update plain path mentions in `index.md`/`log.md` when present
5. Verify there are no stale old stems except in migration history lines
6. Append a migration entry to `log.md` with full rename mapping and touched files

Use this migration pattern to avoid link breakage during localization.

## Wiki Location

Configured via `skills.config.wiki.path` in `~/.hermes/config.yaml` (prompted
during `hermes config migrate` or `hermes setup`):

```yaml
skills:
  config:
    wiki:
      path: ~/wiki
```

Falls back to `~/wiki` default. The resolved path is injected when this
skill loads — check the `[Skill config: ...]` block above for the active value.

The wiki is just a directory of markdown files — open it in Obsidian, VS Code, or
any editor. No database, no special tooling required.

## Architecture: Three Layers

```
wiki/
├── SCHEMA.md           # Conventions, structure rules, domain config
├── index.md            # Sectioned content catalog with one-line summaries
├── log.md              # Chronological action log (append-only, rotated yearly)
├── raw/                # Layer 1: Immutable source material
│   ├── articles/       # Web articles, clippings
│   ├── papers/         # PDFs, arxiv papers
│   ├── transcripts/    # Meeting notes, interviews
│   └── assets/         # Images, diagrams referenced by sources
├── entities/           # Layer 2: Entity pages (people, orgs, products, models)
├── concepts/           # Layer 2: Concept/topic pages
├── comparisons/        # Layer 2: Side-by-side analyses
└── queries/            # Layer 2: Filed query results worth keeping
```

**Layer 1 — Raw Sources / Source Pointers:** Evidence sources. Prefer immutable copies in `raw/` for external material; for files already inside the same Obsidian vault, a source pointer path is allowed (no duplicate copy).
**Layer 2 — The Wiki:** Agent-owned markdown files. Created, updated, and
cross-referenced by the agent.
**Layer 3 — The Schema:** `SCHEMA.md` defines structure, conventions, and tag taxonomy.

## Resuming an Existing Wiki (CRITICAL — do this every session)

When the user has an existing wiki, **always orient yourself before doing anything**:

① **Read `SCHEMA.md`** — understand the domain, conventions, and tag taxonomy.
② **Read `index.md`** — learn what pages exist and their summaries.
③ **Scan recent `log.md`** — read the last 20-30 entries to understand recent activity.

```bash
WIKI="${wiki_path:-$HOME/wiki}"
# Orientation reads at session start
read_file "$WIKI/SCHEMA.md"
read_file "$WIKI/index.md"
read_file "$WIKI/log.md" offset=<last 30 lines>
```

Only after orientation should you ingest, query, or lint. This prevents:
- Creating duplicate pages for entities that already exist
- Missing cross-references to existing content
- Contradicting the schema's conventions
- Repeating work already logged

For large wikis (100+ pages), also run a quick `search_files` for the topic
at hand before creating anything new.

## Initializing a New Wiki

When the user asks to create or start a wiki:

1. Determine the wiki path (from config, env var, or ask the user; default `~/wiki`)
2. Create the directory structure above
3. Ask the user what domain the wiki covers — be specific
4. Write `SCHEMA.md` customized to the domain (see template below)
5. Write initial `index.md` with sectioned header
6. Write initial `log.md` with creation entry
7. Confirm the wiki is ready and suggest first sources to ingest

### SCHEMA.md Template

Adapt to the user's domain. The schema constrains agent behavior and ensures consistency:

```markdown
# Wiki Schema

## Domain
[What this wiki covers — e.g., "AI/ML research", "personal health", "startup intelligence"]

## Conventions
- File names: lowercase, hyphens, no spaces (e.g., `transformer-architecture.md`)
- Every wiki page starts with YAML frontmatter (see below)
- Use `[[wikilinks]]` to link between pages (minimum 2 outbound links per page)
- When updating a page, always bump the `updated` date
- Every new page must be added to `index.md` under the correct section
- Every action must be appended to `log.md`

- **model**: 实体定义、数据结构、关系图 (e.g., 广告计划字段)
- **decision**: 技术选型、架构决策及理由 (e.g., 为什么选事件驱动)
- **guideline**: 最佳实践 (recommend) 或禁止做法 (avoid)
- **pitfall**: 已知风险、故障模式、排查步骤 (e.g., 高并发超扣坑)
- **process**: 业务流程、操作步骤 (e.g., 审核流流程)

## Maturity & Decay (Optional)
- **draft**: initial capture
- **verified**: tested in 1 project
- **proven**: tested in 2+ projects
- **Decay**: entries not referenced for 6-12 months should be flagged for linting/archiving.
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
[Define 10-20 top-level tags for the domain. Add new tags here BEFORE using them.]

Example for AI/ML:
- Models: model, architecture, benchmark, training
- People/Orgs: person, company, lab, open-source
- Techniques: optimization, fine-tuning, inference, alignment, data
- Meta: comparison, timeline, controversy, prediction

Rule: every tag on a page must appear in this taxonomy. If a new tag is needed,
add it here first, then use it. This prevents tag sprawl.

## Page Thresholds
- **Create a page** when an entity/concept appears in 2+ sources OR is central to one source
- **Add to existing page** when a source mentions something already covered
- **DON'T create a page** for passing mentions, minor details, or things outside the domain
- **Split a page** when it exceeds ~200 lines — break into sub-topics with cross-links
- **Archive a page** when its content is fully superseded — move to `_archive/`, remove from index

## Entity Pages
One page per notable entity. Include:
- Overview / what it is
- Key facts and dates
- Relationships to other entities ([[wikilinks]])
- Source references

## Concept Pages
One page per concept or topic. Include:
- Definition / explanation
- Current state of knowledge
- Open questions or debates
- Related concepts ([[wikilinks]])

## Comparison Pages
Side-by-side analyses. Include:
- What is being compared and why
- Dimensions of comparison (table format preferred)
- Verdict or synthesis
- Sources

## Update Policy
When new information conflicts with existing content:
1. Check the dates — newer sources generally supersede older ones
2. If genuinely contradictory, note both positions with dates and sources
3. Mark the contradiction in frontmatter: `contradictions: [page-name]`
4. Flag for user review in the lint report
```

### index.md Template

The index is sectioned by type. Each entry is one line: wikilink + summary.

```markdown
# Wiki Index

> Content catalog. Every wiki page listed under its type with a one-line summary.
> Read this first to find relevant pages for any query.
> Last updated: YYYY-MM-DD | Total pages: N

## Entities
<!-- Alphabetical within section -->

## Concepts

## Comparisons

## Queries
```

**Scaling rule:** When any section exceeds 50 entries, split it into sub-sections
by first letter or sub-domain. When the index exceeds 200 entries total, create
a `_meta/topic-map.md` that groups pages by theme for faster navigation.

### log.md Template

```markdown
# Wiki Log

> Chronological record of all wiki actions. Append-only.
> Format: `## [YYYY-MM-DD] action | subject`
> Actions: ingest, update, query, lint, create, archive, delete
> When this file exceeds 500 entries, rotate: rename to log-YYYY.md, start fresh.

## [YYYY-MM-DD] create | Wiki initialized
- Domain: [domain]
- Structure created with SCHEMA.md, index.md, log.md
```

## Knowledge Classification (MECE)
Categorize info to prevent bloat:
- **model**: Definitions, schemas, entity relationships.
- **decision**: Architecture/logic choices and reasoning.
- **guideline**: Best practices (recommend/avoid).
- **pitfall**: Known risks, bugs, and edge-case "traps".
- **process**: Workflows, state machines, step-by-step logic.

### 1. Ingest

When the user provides a source (URL, file, paste), integrate it into the wiki:

⓪ **Domain-fit check (before writing pages):**
   - Compare source topic with `SCHEMA.md -> Domain`
   - If the source is outside current domain, do **not** silently mix taxonomies
   - Choose one path explicitly:
     1) Update `SCHEMA.md` domain/scope to include the new topic, or
     2) Keep source in `raw/` only, or
     3) Route to another wiki
   - Log the decision in `log.md` when scope is expanded

① **Capture source evidence (choose mode explicitly):**
   - **Snapshot mode (default for external sources):**
     - URL → use `web_extract` to get markdown, save to `raw/articles/`
     - PDF → use `web_extract` (handles PDFs), save to `raw/papers/`
     - Pasted text → save to appropriate `raw/` subdirectory
     - Name files descriptively: `raw/articles/karpathy-llm-wiki-2026.md`
   - **Source-pointer mode (default for same-vault local markdown):**
     - If the source `.md` already resides inside the same Obsidian vault/wiki domain, **do not duplicate into `raw/`**
     - Record the original absolute/relative path directly in page frontmatter `sources`
     - Recommended marker: `sources_mode: pointer` (optional but preferred for auditability)
     - **Obsidian link visibility:** in addition to frontmatter path, add at least one explicit wikilink in body (e.g., `原文：[[2-健康/xxx.md]]`) so Graph/Backlinks can see the source relationship
   - **Promotion rule:** if pointer source is moved outside vault scope, deleted risk is high, or strict reproducibility is required, promote to Snapshot mode by copying into `raw/` and update `sources`

② **Discuss takeaways** with the user — what's interesting, what matters for
   the domain. (Skip this in automated/cron contexts — proceed directly.)

③ **Check what already exists** — search index.md and use `search_files` to find
   existing pages for mentioned entities/concepts. This is the difference between
   a growing wiki and a pile of duplicates.

④ **Write or update wiki pages:**
   - **New entities/concepts:** Create pages only if they meet the Page Thresholds
     in SCHEMA.md (2+ source mentions, or central to one source)
   - **Existing pages:** Add new information, update facts, bump `updated` date.
     When new info contradicts existing content, follow the Update Policy.
   - **Cross-reference:** Every new or updated page must link to at least 2 other
     pages via `[[wikilinks]]`. Check that existing pages link back.
   - **Relevance-first linking (critical):** prioritize same-topic/same-domain links; do **not** add unrelated cross-domain links just to satisfy link count. If only one relevant wiki page exists, use source-pointer wikilinks to original Obsidian notes as supplemental links.
   - **Tags:** Only use tags from the taxonomy in SCHEMA.md

   **High-signal ingest pattern (recommended for mature personal wikis):**
   - Prefer **1 new distilled page + 2~4 targeted updates** to existing hub pages,
     instead of scattering many small pages.
   - For each touched existing page, do three things together: append source in
     `sources`, bump `updated`, and add one concise "来自<来源日期/主题>的补充" block.
   - This keeps knowledge compounding while preserving page stability and avoids
     index/log churn from over-fragmentation.

   **Preprocess-then-ingest pattern (for user-requested transformations):**
   - If the user requests a transformation first (e.g., bilingual rewrite, cleanup,
     OCR normalization), create a **derived source file** in the same vault folder
     and keep the original file untouched.
   - **Fidelity gate (critical):** when the user asks for “1:1”, “完整”, or explicitly says prior output lost details,
     switch to full-fidelity mode: preserve original structure/headings/order, avoid summarization/compression,
     and state scope explicitly (e.g., article body only vs body+comments).
   - Use the derived file as the ingest `source` (pointer mode for same-vault md),
     and log the preprocess step explicitly in `log.md` under `Preprocess:`.
   - In distilled pages, include explicit links to both files when useful:
     `原始摘录` + `整理版本` (or `bilingual`), so provenance and auditability stay clear.

⑤ **Update navigation:**
   - Add new pages to `index.md` under the correct section, alphabetically
   - Update the "Total pages" count and "Last updated" date in index header
   - Append to `log.md`: `## [YYYY-MM-DD] ingest | Source Title`
   - List every file created or updated in the log entry
   - If using pointer mode, log it explicitly (e.g., `Source (pointer mode)` and `Raw captured: skipped`) so future audits can distinguish pointer vs snapshot provenance

⑥ **Report what changed** — list every file created or updated to the user.

A single source can trigger updates across 5-15 wiki pages. This is normal
and desired — it's the compounding effect.

### 2. Query

When the user asks a question about the wiki's domain:

① **Read `index.md`** to identify relevant pages.
② **For wikis with 100+ pages**, also `search_files` across all `.md` files
   for key terms — the index alone may miss relevant content.
③ **Read the relevant pages** using `read_file`.
④ **Synthesize an answer** from the compiled knowledge. Cite the wiki pages
   you drew from: "Based on [[page-a]] and [[page-b]]..."
⑤ **File valuable answers back** — if the answer is a substantial comparison,
   deep dive, or novel synthesis, create a page in `queries/` or `comparisons/`.
   Don't file trivial lookups — only answers that would be painful to re-derive.
⑥ **Update log.md** with the query and whether it was filed.

### 3. Lint

When the user asks to lint, health-check, or audit the wiki:

① **Orphan pages:** Find pages with no inbound `[[wikilinks]]` from other pages.
```python
# Use execute_code for this — programmatic scan across all wiki pages
import os, re
from collections import defaultdict
wiki = "<WIKI_PATH>"
# Scan all .md files in entities/, concepts/, comparisons/, queries/
# Extract all [[wikilinks]] — build inbound link map
# Pages with zero inbound links are orphans
```

② **Broken wikilinks:** Find `[[links]]` that point to pages that don't exist.

③ **Index completeness:** Every wiki page should appear in `index.md`. Compare
   the filesystem against index entries.

④ **Frontmatter validation:** Every wiki page must have all required fields
   (title, created, updated, type, tags, sources). Tags must be in the taxonomy.

⑤ **Stale content:** Pages whose `updated` date is >90 days older than the most
   recent source that mentions the same entities.

⑥ **Contradictions:** Pages on the same topic with conflicting claims. Look for
   pages that share tags/entities but state different facts.

⑦ **Page size:** Flag pages over 200 lines — candidates for splitting.

⑧ **Tag audit:** List all tags in use, flag any not in the SCHEMA.md taxonomy.

⑨ **Pointer provenance audit (when using source-pointer mode):**
   - Pages with `sources_mode: pointer` must include at least one explicit body wikilink to the same source path (not only frontmatter text)
   - Flag pointer pages where source paths are plain text only (Graph/Backlinks blind spot)

⑩ **Cross-domain link drift audit:**
   - Flag unrelated cross-domain links added only to satisfy link-count rules
   - Suggested fix: replace with same-topic/same-folder (e.g., `2-健康/`) links or relevant wiki concept pages

⑪ **Log rotation:** If log.md exceeds 500 entries, rotate it.

⑫ **Report findings** with specific file paths and suggested actions, grouped by
   severity (broken links > orphans > stale content > style issues).

⑬ **Append to log.md:** `## [YYYY-MM-DD] lint | N issues found`

## Working with the Wiki

### Searching

```bash
# Find pages by content
search_files "transformer" path="$WIKI" file_glob="*.md"

# Find pages by filename
search_files "*.md" target="files" path="$WIKI"

# Find pages by tag
search_files "tags:.*alignment" path="$WIKI" file_glob="*.md"

# Recent activity
read_file "$WIKI/log.md" offset=<last 20 lines>
```

### Bulk Ingest

When ingesting multiple sources at once, batch the updates:
1. Read all sources first
2. Identify all entities and concepts across all sources
3. Check existing pages for all of them (one search pass, not N)
4. Create/update pages in one pass (avoids redundant updates)
5. Update index.md once at the end
6. Write a single log entry covering the batch

### Folder-wide ingest pattern (same-topic series)

When the user asks to ingest **all files in one folder** (e.g., monthly reports in `6-文章/`), prefer this pattern unless they explicitly want per-file wiki pages:

1. List all `.md` files in that folder and treat each as a source pointer when same-vault.
2. Build **one distilled hub page** under `concepts/` (or `queries/` if it's primarily Q&A output), not N fragmented pages.
3. Put the full file list in frontmatter `sources` and add explicit body wikilinks to each source file for Obsidian graph/backlinks visibility.
4. Extract a compact structured summary table when possible (e.g., month, strategy return, benchmark return) to make the hub operationally useful.
5. Update `index.md` once (single new entry) and append one batch `log.md` entry listing all source files.

Rationale: this preserves provenance for every source while avoiding index bloat and duplicate concept pages.

#### Variant: mixed-topic folders (e.g., `4-阅读/`)

If the folder is heterogeneous (investment + psychology + health + history, etc.), still keep the **single hub-page** approach, but replace numeric KPI tables with a **theme distribution block**:

- Add counts by topic cluster (e.g., 投资交易/心理沟通/健康/文学历史).
- Add 2-4 reusable cross-domain takeaways (high signal, action-oriented).
- Link only to genuinely relevant existing wiki pages (avoid forced cross-domain links just to satisfy link count).

This keeps ingestion scalable for messy real-world folders while maintaining navigability and semantic quality.

### Archiving

When content is fully superseded or the domain scope changes:
1. Create `_archive/` directory if it doesn't exist
2. Move the page to `_archive/` with its original path (e.g., `_archive/entities/old-page.md`)
3. Remove from `index.md`
4. Update any pages that linked to it — replace wikilink with plain text + "(archived)"
5. Log the archive action

### Obsidian Integration

The wiki directory works as an Obsidian vault out of the box:
- `[[wikilinks]]` render as clickable links
- Graph View visualizes the knowledge network
- YAML frontmatter powers Dataview queries
- The `raw/assets/` folder holds images referenced via `![[image.png]]`

For best results:
- Set Obsidian's attachment folder to `raw/assets/`
- Enable "Wikilinks" in Obsidian settings (usually on by default)
- Install Dataview plugin for queries like `TABLE tags FROM "entities" WHERE contains(tags, "company")`

If using the Obsidian skill alongside this one, set `OBSIDIAN_VAULT_PATH` to the
same directory as the wiki path.

### Obsidian Headless (servers and headless machines)

On machines without a display, use `obsidian-headless` instead of the desktop app.
It syncs vaults via Obsidian Sync without a GUI — perfect for agents running on
servers that write to the wiki while Obsidian desktop reads it on another device.

**Setup:**
```bash
# Requires Node.js 22+
npm install -g obsidian-headless

# Login (requires Obsidian account with Sync subscription)
ob login --email <email> --password '<password>'

# Create a remote vault for the wiki
ob sync-create-remote --name "LLM Wiki"

# Connect the wiki directory to the vault
cd ~/wiki
ob sync-setup --vault "<vault-id>"

# Initial sync
ob sync

# Continuous sync (foreground — use systemd for background)
ob sync --continuous
```

**Continuous background sync via systemd:**
```ini
# ~/.config/systemd/user/obsidian-wiki-sync.service
[Unit]
Description=Obsidian LLM Wiki Sync
After=network-online.target
Wants=network-online.target

[Service]
ExecStart=/path/to/ob sync --continuous
WorkingDirectory=/home/user/wiki
Restart=on-failure
RestartSec=10

[Install]
WantedBy=default.target
```

```bash
systemctl --user daemon-reload
systemctl --user enable --now obsidian-wiki-sync
# Enable linger so sync survives logout:
sudo loginctl enable-linger $USER
```

This lets the agent write to `~/wiki` on a server while you browse the same
vault in Obsidian on your laptop/phone — changes appear within seconds.

## Pitfalls

- **Never modify files in `raw/`** — sources are immutable. Corrections go in wiki pages.
- **Pointer mode is valid for same-vault markdown** — when source `.md` already lives in the same personal Obsidian vault, reference path directly instead of duplicating into `raw/`.
- **Always orient first** — read SCHEMA + index + recent log before any operation in a new session.
  Skipping this causes duplicates and missed cross-references.
- **Always update index.md and log.md** — skipping this makes the wiki degrade. These are the
  navigational backbone.
- **Don't create pages for passing mentions** — follow the Page Thresholds in SCHEMA.md. A name
  appearing once in a footnote doesn't warrant an entity page.
- **Don't create pages without cross-references** — isolated pages are invisible. Every page must
  link to at least 2 other pages.
- **Frontmatter is required** — it enables search, filtering, and staleness detection.
- **Tags must come from the taxonomy** — freeform tags decay into noise. Add new tags to SCHEMA.md
  first, then use them.
- **Keep pages scannable** — a wiki page should be readable in 30 seconds. Split pages over
  200 lines. Move detailed analysis to dedicated deep-dive pages.
- **Ask before mass-updating** — if an ingest would touch 10+ existing pages, confirm
  the scope with the user first.
- **Rotate the log** — when log.md exceeds 500 entries, rename it `log-YYYY.md` and start fresh.
  The agent should check log size during lint.
- **Handle contradictions explicitly** — don't silently overwrite. Note both claims with dates,
  mark in frontmatter, flag for user review.
