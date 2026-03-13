# My Skills - Claude Code 技能库

## 项目概述

这是一个 Claude Code Agent Skills 集合仓库，每个子目录是一个独立的技能模块，通过 `SKILL.md` 文件定义技能的触发条件和执行逻辑。

## 目录结构

```
my-skills/
├── CLAUDE.md              # 项目级指令（本文件）
├── README.md
├── .system/               # 系统配置
│
├── # ─── 独立技能 ───
├── ai-hot-news/           # AI 热点新闻聚合（V2EX + Linux Do → 飞书）
├── BrightData/            # 四层回退网页抓取
├── cf-quant-web/          # 量化 Web 应用
├── doc-coauthoring/       # 文档合著工作流
├── docx/                  # Word 文档操作
├── frontend-design/       # 前端界面设计
├── pdf/                   # PDF 文件处理
├── pptx/                  # PowerPoint 演示文稿
├── prompt-engineering-patterns/  # 提示工程模式
├── self-improving-agent/  # 自改进智能体
├── skill-creator/         # 技能创建与优化
├── skill-writer/          # 技能编写指南
├── sql-optimization-patterns/   # SQL 优化模式
├── stockdata/             # 本地股市数据读取
├── TaskRunner/            # Obsidian 任务执行器
├── wind-meta-data/        # Wind 金融数据元信息
├── xlsx/                  # Excel 电子表格操作
│
├── # ─── Superpowers 增强技能集 ───
└── superpowers/
    ├── brainstorming/
    ├── dispatching-parallel-agents/
    ├── executing-plans/
    ├── finishing-a-development-branch/
    ├── receiving-code-review/
    ├── requesting-code-review/
    ├── subagent-driven-development/
    ├── systematic-debugging/
    ├── test-driven-development/
    ├── using-git-worktrees/
    ├── using-superpowers/
    ├── verification-before-completion/
    ├── writing-plans/
    └── writing-skills/
```

## 开发规范

- 每个技能目录必须包含 `SKILL.md`，使用 YAML frontmatter 定义 `name` 和 `description`
- 技能描述（description）决定触发准确性，应清晰描述触发场景
- 参考资料放在 `references/` 子目录，资源文件放在 `assets/` 子目录
- 工作流定义放在 `Workflows/` 子目录
- 中文优先，技术术语保留英文原文
