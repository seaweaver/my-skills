import time
from typing import Dict, List, Tuple

import requests


DEFAULT_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/123.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
}


class FetchError(RuntimeError):
    pass


def fetch_html(url: str, timeout: int = 20, retries: int = 2, sleep_seconds: float = 0.8) -> str:
    last_error = None
    for attempt in range(retries + 1):
        try:
            response = requests.get(url, headers=DEFAULT_HEADERS, timeout=timeout)
            response.raise_for_status()
            response.encoding = response.apparent_encoding or response.encoding or "utf-8"
            return response.text
        except requests.RequestException as exc:
            last_error = exc
            if attempt < retries:
                time.sleep(sleep_seconds)

    raise FetchError(f"failed to fetch {url}: {last_error}")


def fetch_topic_pages(topics, timeout: int = 20) -> Tuple[List[Dict], List[Dict]]:
    details = []
    errors = []
    for topic in topics:
        try:
            html = fetch_html(topic["url"], timeout=timeout)
            details.append({"topic": topic, "html": html})
        except FetchError as exc:
            errors.append({"title": topic.get("title", ""), "url": topic.get("url", ""), "error": str(exc)})
        time.sleep(0.5)

    return details, errors


def build_runtime_manifest(report_path: str, source_json_path: str, draft_path: str, fetched_count: int, selected_count: int) -> Dict[str, str]:
    return {
        "report_path": report_path,
        "source_json_path": source_json_path,
        "draft_path": draft_path,
        "fetched_count": str(fetched_count),
        "selected_count": str(selected_count),
    }
