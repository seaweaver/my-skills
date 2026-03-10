---
name: ai-hot-news
description: 聚合 V2EX + Linux Do 的 AI/开发热门话题，并输出飞书可读消息
---

# AI Hot News

## 功能
- 抓取 V2EX 热门话题（API）
- 抓取 Linux Do 热门话题（RSS，优先 weekly top）
- 用统一关键词打分筛选 AI/开发内容
- 生成可直接投递到飞书的 Markdown 文本

## 运行

```bash
python main.py --limit-source 5
```

可选参数：

```bash
python main.py --limit-source 5 --output .\last_report.md
```

## 定时任务推荐触发方式

Cron 任务消息建议固定为：

1. 运行 `E:\nanobot\.venv\Scripts\python.exe C:\Users\zhuhaibo\.nanobot\workspace\skills\ai-hot-news\main.py --limit-source 5`
2. 将标准输出原样作为回复

这样可减少模型自由发挥，提升确定性。

