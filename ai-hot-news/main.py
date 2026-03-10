#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from core.aggregator import Aggregator
from providers.linuxdo_provider import LinuxDoProvider
from providers.v2ex_provider import V2EXProvider


def build_message(limit_per_source: int = 5) -> str:
    aggregator = Aggregator()
    providers = [V2EXProvider(), LinuxDoProvider()]

    for provider in providers:
        topics = provider.get_topics(limit=limit_per_source)
        aggregator.add_topics(provider.source_name, topics)

    return aggregator.format_for_feishu(limit_per_source=limit_per_source)


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser(description="AI Hot News Aggregator")
    parser.add_argument("--limit-source", type=int, default=5, help="每个来源最多输出条数")
    parser.add_argument("--output", type=Path, default=None, help="可选：额外写入文件")
    args = parser.parse_args()

    message = build_message(limit_per_source=max(1, args.limit_source))
    print(message)

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(message, encoding="utf-8")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
