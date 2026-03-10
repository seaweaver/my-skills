from __future__ import annotations

import html
import re
from collections import defaultdict
from datetime import datetime

from .provider_base import Topic


class Aggregator:
    def __init__(self) -> None:
        self._topics_by_source: dict[str, list[Topic]] = defaultdict(list)

    def add_topics(self, source: str, topics: list[Topic]) -> None:
        self._topics_by_source[source].extend(topics)

    def _dedupe(self) -> dict[str, list[Topic]]:
        seen_keys: set[str] = set()
        result: dict[str, list[Topic]] = defaultdict(list)

        for source, topics in self._topics_by_source.items():
            for topic in topics:
                key = self._topic_key(topic)
                if key in seen_keys:
                    continue
                seen_keys.add(key)
                result[source].append(topic)

        return result

    @staticmethod
    def _topic_key(topic: Topic) -> str:
        clean_title = re.sub(r"\s+", "", topic.title).lower()
        clean_url = topic.url.strip().lower().rstrip("/")
        return clean_url if clean_url else clean_title

    @staticmethod
    def _source_display_name(source: str) -> str:
        mapping = {
            "v2ex": "V2EX",
            "linuxdo": "Linux Do",
        }
        return mapping.get(source.lower(), source)

    def format_for_feishu(self, limit_per_source: int = 5) -> str:
        grouped = self._dedupe()
        lines: list[str] = []

        lines.append("🤖 **AI 热门聚合日报**")
        lines.append(f"更新时间：{datetime.now().strftime('%Y-%m-%d %H:%M')}")

        total_count = 0
        for source in sorted(grouped.keys()):
            topics = sorted(
                grouped[source],
                key=lambda item: (item.score, item.replies, item.created_at),
                reverse=True,
            )[:limit_per_source]
            if not topics:
                continue

            total_count += len(topics)
            lines.append("\n---")
            lines.append(f"📌 **{self._source_display_name(source)} 热门话题**")

            for idx, topic in enumerate(topics, 1):
                title = html.unescape(topic.title).strip()
                excerpt = html.unescape(topic.excerpt).strip()
                if len(excerpt) > 100:
                    excerpt = excerpt[:100].rstrip() + "…"

                lines.append(f"\n{idx}. **{title}**")
                lines.append(f"   👤 {topic.author} | 💬 {topic.replies} | 🧮 分值 {topic.score}")
                lines.append(f"   🔗 {topic.url}")
                if excerpt:
                    lines.append(f"   📝 {excerpt}")

        if total_count == 0:
            return "🤖 **AI 热门聚合日报**\n\n⚠️ 本次未抓取到可用内容（V2EX/Linux Do）。"

        lines.append("\n---")
        lines.append(f"共输出 {total_count} 条（每源最多 {limit_per_source} 条）")
        return "\n".join(lines)

