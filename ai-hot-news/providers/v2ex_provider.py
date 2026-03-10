from __future__ import annotations

from datetime import datetime
import re

import requests

from core.provider_base import ProviderBase, Topic


class V2EXProvider(ProviderBase):
    source_name = "v2ex"
    api_url = "https://www.v2ex.com/api/topics/hot.json"

    keyword_high = [
        "ai", "人工智能", "llm", "gpt", "claude", "gemini", "copilot",
        "大模型", "agent", "rag", "prompt", "机器学习", "深度学习",
        "python", "javascript", "typescript", "java", "golang", "rust",
        "docker", "kubernetes", "k8s", "mcp", "cursor", "opencode", "codex",
    ]

    keyword_medium = [
        "开发", "编程", "代码", "后端", "前端", "全栈", "数据库",
        "api", "linux", "vscode", "devops", "架构", "工程",
    ]

    def get_topics(self, limit: int = 5) -> list[Topic]:
        try:
            response = requests.get(self.api_url, timeout=20)
            response.raise_for_status()
            items = response.json()
        except Exception:
            return []

        topics: list[Topic] = []
        for item in items:
            title = (item.get("title") or "").strip()
            content = (item.get("content") or "").strip()
            node_title = (item.get("node") or {}).get("title", "")
            raw_text = f"{title} {content} {node_title}".lower()

            score = self._score(raw_text)
            if score <= 0:
                continue

            created = item.get("created") or 0
            topic = Topic(
                title=title,
                url=(item.get("url") or "").strip(),
                author=(item.get("member") or {}).get("username", "anonymous"),
                replies=int(item.get("replies") or 0),
                created_at=datetime.fromtimestamp(created) if created else datetime.now(),
                source=self.source_name,
                excerpt=content,
                score=score,
            )
            topics.append(topic)

        topics.sort(key=lambda t: (t.score, t.replies, t.created_at), reverse=True)
        return topics[:limit]

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
