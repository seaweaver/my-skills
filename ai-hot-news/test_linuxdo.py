#!/usr/bin/env python3
import sys

from providers.linuxdo_provider import LinuxDoProvider


def test() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    provider = LinuxDoProvider()
    topics = provider.get_topics(limit=5)

    print(f"source={provider.source_name} count={len(topics)}")
    for index, topic in enumerate(topics, 1):
        print(f"{index}. {topic.title}")
        print(f"   score={topic.score} replies={topic.replies} author={topic.author}")
        print(f"   {topic.url}")


if __name__ == "__main__":
    test()
