from __future__ import annotations

import html
import re
import xml.etree.ElementTree as ET
from datetime import datetime, timezone

import requests

from core.provider_base import ProviderBase, Topic


class LinuxDoProvider(ProviderBase):
    source_name = "linuxdo"

    top_weekly_rss = "https://linux.do/top/weekly.rss"
    latest_rss = "https://linux.do/latest.rss"

    keyword_high = [
        "ai", "人工智能", "llm", "gpt", "claude", "gemini", "copilot", "openai",
        "大模型", "机器学习", "agent", "rag", "mcp", "提示词", "模型",
    ]

    keyword_medium = [
        "开发", "编程", "代码", "python", "javascript", "go", "rust",
        "api", "linux", "docker", "k8s", "后端", "前端", "工程",
    ]

    def get_topics(self, limit: int = 5) -> list[Topic]:
        raw_items = self._fetch_rss(self.top_weekly_rss)
        if not raw_items:
            raw_items = self._fetch_rss(self.latest_rss)

        topics: list[Topic] = []
        for item in raw_items:
            title = item.get("title", "").strip()
            description = self._strip_html(item.get("description", ""))
            categories = item.get("categories", [])

            text = f"{title} {description} {' '.join(categories)}".lower()
            score = self._score(text)
            if score <= 0:
                continue

            topic = Topic(
                title=title,
                url=item.get("link", "").strip(),
                author=item.get("creator", "anonymous").strip() or "anonymous",
                replies=item.get("comments", 0),
                created_at=item.get("pub_date", datetime.now(timezone.utc)),
                source=self.source_name,
                excerpt=description,
                score=score,
                tags=categories,
            )
            topics.append(topic)

        topics.sort(key=lambda t: (t.score, t.replies, t.created_at), reverse=True)
        return topics[:limit]

    def _fetch_rss(self, url: str) -> list[dict]:
        try:
            response = requests.get(
                url,
                timeout=20,
                headers={"User-Agent": "Mozilla/5.0"},
            )
            response.raise_for_status()
        except Exception:
            return []

        try:
            root = ET.fromstring(response.text)
        except ET.ParseError:
            return []

        channel = root.find("channel")
        if channel is None:
            return []

        items: list[dict] = []
        for item in channel.findall("item"):
            raw_pub_date = (item.findtext("pubDate") or "").strip()
            pub_date = self._parse_pub_date(raw_pub_date)

            slash_comments = item.find("{http://purl.org/rss/1.0/modules/slash/}comments")
            comments = 0
            if slash_comments is not None and (slash_comments.text or "").strip().isdigit():
                comments = int((slash_comments.text or "").strip())

            items.append(
                {
                    "title": html.unescape(item.findtext("title") or ""),
                    "link": item.findtext("link") or "",
                    "description": item.findtext("description") or "",
                    "creator": item.findtext("{http://purl.org/dc/elements/1.1/}creator") or "anonymous",
                    "categories": [(c.text or "").strip() for c in item.findall("category") if (c.text or "").strip()],
                    "pub_date": pub_date,
                    "comments": comments,
                }
            )

        return items

    @staticmethod
    def _parse_pub_date(raw: str) -> datetime:
        if not raw:
            return datetime.now(timezone.utc)
        try:
            return datetime.strptime(raw, "%a, %d %b %Y %H:%M:%S %z")
        except ValueError:
            return datetime.now(timezone.utc)

    @staticmethod
    def _strip_html(text: str) -> str:
        clean = re.sub(r"<[^>]+>", " ", text)
        clean = html.unescape(clean)
        clean = re.sub(r"\s+", " ", clean).strip()
        return clean

    def _score(self, text: str) -> int:
        score = 0
        if any(self._match_keyword(text, keyword) for keyword in self.keyword_high):
            score += 10
        if any(self._match_keyword(text, keyword) for keyword in self.keyword_medium):
            score += 4
        return score

    @staticmethod
    def _match_keyword(text: str, keyword: str) -> bool:
        normalized = keyword.lower().strip()
        if not normalized:
            return False

        if re.fullmatch(r"[a-z0-9+#._-]+", normalized):
            pattern = rf"(?<![a-z0-9]){re.escape(normalized)}(?![a-z0-9])"
            return re.search(pattern, text) is not None

        return normalized in text
