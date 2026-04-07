---
name: jisilu-hot-news
description: Use when collecting and summarizing Jisilu hot topics from the last 7 days, especially for scheduled nanobot runs, investment discussion monitoring, hot post intelligence briefs, or when the user wants a full Jisilu report saved to Obsidian Clippings plus a short reply summary.
---

# Jisilu Hot News

Use this skill for scheduled Jisilu hot-topic collection and report generation.

## Workflow

1. Run `python .\jisilu-hot-news\main.py`.
2. Let the script fetch the last 7 days of hot topics, parse topic pages, rank high-value discussions, save the full Markdown report to Obsidian `Clippings`, and print a concise summary.
3. Return the script's concise summary to the user. Do not expand it unless the user explicitly asks for more.

## Boundaries

- Focus on investment-relevant information: convertible bonds, ETF/funds, arbitrage, stocks, asset allocation, yield/risk/rule-change discussions.
- Comments matter more than the original post.
- Low-signal topics may be skipped.
- The full report must be saved to the fixed `Clippings` path defined by the script.

## Nanobot

Recommended scheduled prompt:

```text
Run python .\jisilu-hot-news\main.py and return stdout only.
```
