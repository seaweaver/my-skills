# my-skills

Claude Code Agent Skills 集合仓库 — 包含 21 个独立技能和 14 个 Superpowers 增强技能。

## 技能列表

| 技能 | 说明 |
|------|------|
| ai-hot-news | 聚合 V2EX + Linux Do 的 AI/开发热门话题 → 飞书消息 |
| BrightData | 渐进式四层回退 URL 抓取 |
| cf-quant-web | 量化 Web 应用 |
| doc-coauthoring | 结构化文档合著工作流 |
| docx | Word 文档创建/编辑/操作 |
| frontend-design | 高质量前端界面设计与生成 |
| github-sync | 多本地 Git 仓库批量同步到 GitHub |
| jisilu-hot-news | 集思录近 7 天热帖采集、研报落盘与简版摘要 |
| obsidian-cli | 官方 Obsidian CLI 自动化 |
| obsidian-keeper | Obsidian vault 治理与清理 |
| pdf | PDF 读取/合并/拆分/水印/OCR |
| pptx | PowerPoint 演示文稿操作 |
| prompt-engineering-patterns | 高级提示工程技巧 |
| self-improving-agent | 捕获学习与纠错的自改进智能体 |
| skill-creator | 技能创建、评测与优化 |
| skill-writer | 技能编写指南 |
| sql-optimization-patterns | SQL 查询优化与索引策略 |
| stockdata | 本地股市行情数据读取 |
| TaskRunner | 基于 Obsidian 的任务智能路由执行器 |
| wind-meta-data | Wind 金融数据表/字段/业务键查询 |
| xlsx | Excel 电子表格操作 |

## Superpowers 增强技能

位于 `superpowers/` 目录下，包含：brainstorming、dispatching-parallel-agents、executing-plans、finishing-a-development-branch、receiving-code-review、requesting-code-review、subagent-driven-development、systematic-debugging、test-driven-development、using-git-worktrees、using-superpowers、verification-before-completion、writing-plans、writing-skills。

## 使用方式

将本仓库中的技能目录链接或复制到 Claude Code 的 skills 路径即可自动加载。每个技能通过 `SKILL.md` 中的 `description` 字段自动匹配用户意图。
