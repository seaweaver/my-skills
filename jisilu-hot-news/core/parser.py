import re
from typing import Dict, List
from urllib.parse import urljoin

from bs4 import BeautifulSoup


BASE_URL = "https://www.jisilu.cn"


def normalize_text(value: str) -> str:
    text = re.sub(r"\s+", " ", value or "")
    return text.strip()


def extract_text(node) -> str:
    if node is None:
        return ""
    return normalize_text(node.get_text(" ", strip=True))


def parse_hot_topics_html(html: str, max_topics: int = 30) -> List[Dict]:
    soup = BeautifulSoup(html, "html.parser")
    topics = []

    for heading in soup.find_all("h4"):
        anchors = heading.find_all("a", href=True)
        if not anchors:
            continue

        main_link = None
        for anchor in anchors:
            href = anchor.get("href", "")
            if "/question/" in href:
                main_link = anchor
                break

        if main_link is None:
            continue

        reply_count = 0
        previous = heading.find_previous_sibling()
        while previous is not None:
            text = extract_text(previous)
            match = re.search(r"(\d+)\s*回复", text)
            if match:
                reply_count = int(match.group(1))
                break
            previous = previous.find_previous_sibling()

        meta_node = heading.find_next_sibling("span")
        meta_text = extract_text(meta_node)
        category = ""
        author = ""
        last_reply_at = ""
        views = 0
        if meta_text:
            parts = [part.strip() for part in meta_text.split("•") if part.strip()]
            if len(parts) >= 1:
                category = parts[0].replace("回复", "").strip()
            if len(parts) >= 2:
                author = parts[1].replace("回复", "").strip()
            if len(parts) >= 3:
                last_reply_at = parts[2].strip()
            view_match = re.search(r"(\d+)\s*次浏览", meta_text)
            if view_match:
                views = int(view_match.group(1))

        tags = []
        for anchor in anchors[1:]:
            tag_text = extract_text(anchor)
            if tag_text:
                tags.append(tag_text)

        title = extract_text(main_link)
        topics.append(
            {
                "title": title,
                "url": urljoin(BASE_URL, main_link["href"]),
                "reply_count": reply_count,
                "category": category,
                "author": author,
                "last_reply_at": last_reply_at,
                "views": views,
                "tags": tags,
            }
        )

        if len(topics) >= max_topics:
            break

    return topics


def parse_topic_detail_html(html: str, topic: Dict) -> Dict:
    soup = BeautifulSoup(html, "html.parser")
    title_node = soup.select_one("div.aw-question-detail-title h1")
    body_node = soup.select_one("div.aw-question-detail-txt.markitup-box")
    meta_spans = soup.select("div.aw-question-detail-meta span.aw-text-color-999")
    agree_node = soup.select_one("div.aw-question-detail-title p.aw-agree-by")

    topic_like_users = 0
    if agree_node is not None:
        topic_like_users = len(agree_node.select("a.aw-user-name"))

    published_at = ""
    location = ""
    if len(meta_spans) >= 1:
        published_at = extract_text(meta_spans[0]).replace("发表时间", "").strip()
    if len(meta_spans) >= 2:
        location = extract_text(meta_spans[1]).replace("来自", "").strip()

    comments = []
    for item in soup.select("div.aw-mod-body.aw-dynamic-topic > div.aw-item"):
        vote_node = item.select_one("em.aw-vote-count")
        publisher_node = item.select_one("p.publisher a.aw-user-name")
        agree_by_node = item.select_one("p.aw-agree-by")
        content_node = item.select_one("div.markitup-box")
        meta_node = item.select_one("div.aw-dynamic-topic-meta span.aw-text-color-999")

        if content_node is None or publisher_node is None:
            continue

        like_count = 0
        if vote_node is not None:
            vote_text = extract_text(vote_node)
            if vote_text.isdigit():
                like_count = int(vote_text)

        agree_user_count = 0
        if agree_by_node is not None:
            agree_user_count = len(agree_by_node.select("a.aw-user-name"))

        content_text = extract_text(content_node)
        if not content_text:
            continue

        comments.append(
            {
                "author": extract_text(publisher_node),
                "like_count": like_count,
                "agree_user_count": agree_user_count,
                "content": content_text,
                "published_info": extract_text(meta_node),
            }
        )

    return {
        "title": extract_text(title_node) or topic["title"],
        "url": topic["url"],
        "category": topic.get("category", ""),
        "tags": topic.get("tags", []),
        "reply_count": topic.get("reply_count", 0),
        "views": topic.get("views", 0),
        "author": topic.get("author", ""),
        "last_reply_at": topic.get("last_reply_at", ""),
        "body": extract_text(body_node),
        "published_at": published_at,
        "location": location,
        "topic_like_users": topic_like_users,
        "comments": comments,
    }
