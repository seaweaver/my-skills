from __future__ import annotations

import json
from datetime import date
from pathlib import Path
from typing import Dict, List


OBSIDIAN_CLIPPINGS_DIR = Path(r"D:\iCloud\iCloudDrive\iCloud~md~obsidian\iCloudNote\Clippings")


def ensure_directory(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def resolve_report_output_path(report_date: str | None = None, model_name: str = "nanobot", root: Path | None = None) -> Path:
    if report_date is None:
        report_date = date.today().isoformat()
    root = root or OBSIDIAN_CLIPPINGS_DIR
    base = root / f"{report_date} jisilu_report.md"
    if not base.exists():
        return base
    return root / f"{report_date} jisilu_report_{model_name}.md"


def build_full_report(report_date: str, overview: Dict, selected_topics: List[Dict], fetched_count: int) -> str:
    lines = []
    lines.append(f"# 集思录 7 天热贴分析 - {report_date}")
    lines.append("")
    if len(selected_topics) < 10:
        lines.append("> 样本不足：本次高价值讨论少于 10 篇，已按当前可用高信号内容输出。")
        lines.append("")

    lines.append("## 1️⃣ 市场情绪与热点概览")
    recurring = "、".join(overview.get("recurring_keywords", [])[:6]) or "暂无明显重复关键词"
    lines.append(f"- 本周反复出现的关键词：{recurring}")
    for point in overview.get("consensus_points", []):
        lines.append(f"- 社区一致性判断：{point}")
    for topic in overview.get("divergent_topics", [])[:3]:
        lines.append(f"- 分歧最集中的话题：{topic}")

    lines.append("")
    lines.append(f"## 2️⃣ 高价值讨论（按信息密度排序，共 {len(selected_topics)} 篇，抓取主题 {fetched_count} 篇）")
    lines.append("")

    for topic in selected_topics:
        lines.append(f"### [{topic['title']}]({topic['url']})")
        lines.append(f"- 核心议题：{topic['core_issue']}")
        lines.append(f"- 楼主观点：{topic['op_summary'] or '主贴信息密度一般，主要价值来自评论区。'}")
        lines.append("- ⭐ 高赞评论摘要")
        if topic.get("top_comments"):
            for comment in topic["top_comments"][:3]:
                signal = max(comment.get("like_count", 0), comment.get("agree_user_count", 0))
                lines.append(f"  - {comment['author']}（热度 {signal}）：{comment['summary']}")
        else:
            lines.append("  - 本帖高赞评论有限，未发现明显高信号补充。")
        lines.append("- 分析师笔记")
        lines.append(f"  - 这个讨论能提供的决策价值：{topic['analyst_note']}")
        tags = "、".join(topic.get("tags", [])) or topic.get("category", "未分类")
        lines.append(f"  - 涉及标的或代码：{tags}")
        lines.append(f"  - 环境假设：依赖当前论坛讨论、条款/估值/规则背景仍然成立。")
        lines.append(f"  - 行动建议：先核对公告、价格、条款和仓位约束，再决定是否跟进。")
        lines.append("")

    return "\n".join(lines).strip() + "\n"


def build_concise_summary(report_date: str, fetched_count: int, selected_topics: List[Dict], final_path: Path) -> str:
    lines = []
    lines.append("# 集思录热帖简版")
    lines.append(f"- 日期: {report_date}")
    lines.append(f"- 抓取主题: {fetched_count}")
    lines.append(f"- 入选主题: {len(selected_topics)}")
    lines.append("- 核心结论:")
    for item in selected_topics[:5]:
        summary = item.get("top_comments", [{}])[0].get("summary") if item.get("top_comments") else item.get("analyst_note", "")
        if summary:
            lines.append(f"  - {item['title']}：{summary}")
        else:
            lines.append(f"  - {item['title']}")
    lines.append(f"- 完整报告: {final_path}")
    return "\n".join(lines)


def build_failure_summary(stage: str, error: str) -> str:
    lines = []
    lines.append("# 集思录热帖简版")
    lines.append(f"- 状态: failed")
    lines.append(f"- 阶段: {stage}")
    lines.append(f"- 错误: {error}")
    return "\n".join(lines)


def write_text_file(path: Path, content: str) -> Path:
    ensure_directory(path)
    path.write_text(content, encoding="utf-8")
    return path


def write_json_file(path: Path, payload: Dict) -> Path:
    ensure_directory(path)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    return path
