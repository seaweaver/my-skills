# Jisilu Hot News Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build a `jisilu-hot-news` skill that fetches Jisilu hot posts for the last 7 days, writes a full Markdown report to Obsidian `Clippings`, and returns a concise summary for nanobot.

**Architecture:** `main.py` orchestrates the workflow. `core/fetcher.py` pulls list and topic pages, `core/parser.py` extracts posts and liked comments, `core/analyzer.py` filters and structures high-value items, and `core/report.py` writes the full report plus concise summary. `SKILL.md` defines the trigger contract and nanobot usage. Tests cover parsing and report formatting with fixed sample inputs so the skill stays stable without requiring live network access.

**Tech Stack:** Python 3.11, requests, BeautifulSoup, unittest, Markdown

---

### Task 1: Create Skill Skeleton

**Files:**
- Create: `D:/Dropbox/Project/my-skills/jisilu-hot-news/SKILL.md`
- Create: `D:/Dropbox/Project/my-skills/jisilu-hot-news/references/analysis-rules.md`
- Create: `D:/Dropbox/Project/my-skills/jisilu-hot-news/core/fetcher.py`
- Create: `D:/Dropbox/Project/my-skills/jisilu-hot-news/core/parser.py`
- Create: `D:/Dropbox/Project/my-skills/jisilu-hot-news/core/analyzer.py`
- Create: `D:/Dropbox/Project/my-skills/jisilu-hot-news/core/report.py`
- Create: `D:/Dropbox/Project/my-skills/jisilu-hot-news/main.py`
- Create: `D:/Dropbox/Project/my-skills/jisilu-hot-news/tests/test_jisilu_hot_news.py`

**Step 1: Define the trigger contract**

Write `SKILL.md` with:
- `name: jisilu-hot-news`
- a description focused on scheduled Jisilu hot-topic collection, investment discussion extraction, report generation, and concise nanobot reply

**Step 2: Define the analysis rules**

Write `references/analysis-rules.md` with:
- comment-first rule
- like threshold rule
- low-signal skip rule
- full report structure
- concise reply structure

### Task 2: Write Failing Tests

**Files:**
- Test: `D:/Dropbox/Project/my-skills/jisilu-hot-news/tests/test_jisilu_hot_news.py`

**Step 1: Write a parsing test**

Use fixed sample HTML to verify:
- topic title extraction
- topic URL extraction
- reply count extraction
- comment like count extraction

**Step 2: Write a summary formatting test**

Verify concise output contains:
- date
- fetched topic count
- selected topic count
- 3-5 bullet conclusions
- saved file path

**Step 3: Run the tests to verify they fail**

Run:

```powershell
python -m unittest jisilu-hot-news.tests.test_jisilu_hot_news -v
```

Expected: fail because parser and report helpers do not exist yet.

### Task 3: Implement Parser And Report Logic

**Files:**
- Modify: `D:/Dropbox/Project/my-skills/jisilu-hot-news/core/parser.py`
- Modify: `D:/Dropbox/Project/my-skills/jisilu-hot-news/core/report.py`

**Step 1: Implement HTML parsing helpers**

Add functions for:
- hot-list extraction
- topic content extraction
- liked-comment extraction

**Step 2: Implement report builders**

Add functions for:
- full report markdown generation
- concise summary generation
- output path generation with collision-safe suffix

### Task 4: Implement Fetch And Analysis Flow

**Files:**
- Modify: `D:/Dropbox/Project/my-skills/jisilu-hot-news/core/fetcher.py`
- Modify: `D:/Dropbox/Project/my-skills/jisilu-hot-news/core/analyzer.py`
- Modify: `D:/Dropbox/Project/my-skills/jisilu-hot-news/main.py`

**Step 1: Implement HTTP fetching**

Use:
- stable headers
- request timeout
- simple retry behavior

**Step 2: Implement selection logic**

Select candidate discussions by:
- category relevance
- reply count
- like count
- comment information density

**Step 3: Implement end-to-end command**

Run the whole pipeline:
- fetch list
- fetch details
- analyze
- write full report
- print concise summary only

### Task 5: Verify And Update Repo Index

**Files:**
- Modify: `D:/Dropbox/Project/my-skills/README.md`
- Modify: `D:/Dropbox/Project/my-skills/AGENTS.md`

**Step 1: Run tests to verify they pass**

Run:

```powershell
python -m unittest discover -s .\jisilu-hot-news\tests -p test_jisilu_hot_news.py -v
```

Expected: PASS

**Step 2: Validate the skill**

Run:

```powershell
python .system\skill-creator\scripts\quick_validate.py jisilu-hot-news
```

Expected: `Skill is valid!`

**Step 3: Update top-level docs**

Add the new skill to:
- `README.md`
- `AGENTS.md`
