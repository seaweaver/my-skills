# Jisilu Hot News Design

**目标**

创建一个名为 `jisilu-hot-news` 的 skill，供 nanobot 定时抓取集思录近 7 天热门主题，提取对投资决策有参考价值的信息，生成完整版研报并保存到 Obsidian `Clippings`，同时向 nanobot 返回简版摘要。

**输入源**

- 热帖入口：`https://www.jisilu.cn/home/explore/sort_type-hot____day-7`
- 帖子内容：主题页正文与评论区

**核心分析原则**

- 评论区优先于主贴
- 点赞是硬门槛
- 情绪化、宣泄式、无数据支持内容自动降权
- 允许跳过信息密度极低的话题
- 高价值讨论至少 10 篇；不足时在报告中标记样本不足

**输出**

1. 完整版 Markdown 研报
   - 保存到：
     `D:\iCloud\iCloudDrive\iCloud~md~obsidian\iCloudNote\Clippings\YYYY-MM-DD jisilu_report.md`
   - 如重名，文件名追加模型名

2. 简版摘要
   - 只用于 nanobot 回复
   - 包含：
     - 日期
     - 抓取主题数
     - 入选高价值主题数
     - 3-5 条核心结论
     - 完整文件路径

**目录结构**

```text
jisilu-hot-news/
├── SKILL.md
├── main.py
├── core/
│   ├── fetcher.py
│   ├── parser.py
│   ├── analyzer.py
│   └── report.py
├── references/
│   └── analysis-rules.md
└── tests/
    └── test_jisilu_hot_news.py
```

**实现边界**

- 第一版使用 `requests + BeautifulSoup`
- 不依赖登录态
- 不做浏览器自动化
- 不接飞书
- 不做数据库

**失败处理**

- 单篇帖子抓取失败可跳过
- 整体抓取失败时返回错误摘要，不写空报告
- 单帖解析异常不影响剩余帖子
