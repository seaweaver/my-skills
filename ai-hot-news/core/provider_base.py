from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Topic:
    title: str
    url: str
    author: str
    replies: int
    created_at: datetime
    source: str
    excerpt: str = ""
    score: int = 0
    tags: list[str] = field(default_factory=list)


class ProviderBase(ABC):
    source_name: str = "unknown"

    @abstractmethod
    def get_topics(self, limit: int = 5) -> list[Topic]:
        """返回过滤并排序后的话题。"""

