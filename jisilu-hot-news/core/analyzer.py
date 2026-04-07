import math
import re
from collections import Counter
from typing import Dict, List


INVESTMENT_KEYWORDS = [
    "转债",
    "可转债",
    "基金",
    "etf",
    "套利",
    "股票",
    "银行",
    "股息",
    "收益",
    "估值",
    "折价",
    "溢价",
    "下修",
    "赎回",
    "回售",
    "仓位",
    "调仓",
    "新股",
    "北交所",
    "债",
    "资产配置",
    "存款",
    "保险",
    "风险",
]

THEME_RULES = {
    "convertible-bond": ["转债", "下修", "赎回", "转股", "回售", "溢价"],
    "fund-etf": ["基金", "etf", "指数", "净值", "仓位"],
    "arbitrage": ["套利", "折价", "溢价", "价差"],
    "dividend-income": ["银行", "股息", "吃息", "分红"],
    "new-share": ["新股", "北交所"],
    "asset-allocation": ["存款", "保险", "现金管理", "资产配置"],
    "stock-strategy": ["股票", "微盘", "消费", "猪", "收益"],
}


def normalize(value: str) -> str:
    return (value or "").strip().lower()


def sentence_snippet(text: str, max_length: int = 120) -> str:
    text = (text or "").strip()
    if not text:
        return ""
    text = re.sub(r"\s+", " ", text)
    for splitter in ["。", "！", "？", "\n"]:
        parts = [part.strip() for part in text.split(splitter) if part.strip()]
        if parts:
            snippet = parts[0]
            if len(snippet) <= max_length:
                return snippet
            return snippet[:max_length].rstrip("，,；;") + "..."
    return text[:max_length].rstrip("，,；;") + ("..." if len(text) > max_length else "")


def detect_themes(text: str) -> List[str]:
    lowered = normalize(text)
    themes = []
    for theme, keywords in THEME_RULES.items():
        if any(keyword in lowered for keyword in keywords):
            themes.append(theme)
    return themes


def topic_relevance_score(topic: Dict) -> int:
    combined_text = " ".join(
        [
            topic.get("title", ""),
            topic.get("category", ""),
            " ".join(topic.get("tags", [])),
            topic.get("body", ""),
        ]
    )
    lowered = normalize(combined_text)

    keyword_hits = sum(1 for keyword in INVESTMENT_KEYWORDS if keyword in lowered)
    category_bonus = 0
    if topic.get("category") in {"债券/可转债", "基金", "套利", "新股", "股票"}:
        category_bonus = 12
    elif keyword_hits >= 2:
        category_bonus = 6

    topic_like_score = min(topic.get("topic_like_users", 0), 30)
    reply_score = min(topic.get("reply_count", 0) // 4, 25)
    top_comment_score = 0
    for comment in topic.get("comments", []):
        signal = max(comment.get("like_count", 0), comment.get("agree_user_count", 0))
        top_comment_score = max(top_comment_score, min(signal * 2, 20))

    signal_comment_count = 0
    for comment in topic.get("comments", []):
        signal = max(comment.get("like_count", 0), comment.get("agree_user_count", 0))
        if signal >= 2:
            signal_comment_count += 1

    return category_bonus + keyword_hits * 3 + topic_like_score + reply_score + top_comment_score + signal_comment_count * 2


def classify_action_note(topic: Dict) -> str:
    combined = " ".join(
        [
            topic.get("title", ""),
            topic.get("body", ""),
            " ".join(comment.get("content", "") for comment in topic.get("top_comments", [])),
        ]
    )
    themes = detect_themes(combined)

    if "convertible-bond" in themes:
        return "重点是条款、下修、赎回或价格博弈。行动上应跟踪公告、转股价值、溢价率与触发条件，避免只看情绪。"
    if "arbitrage" in themes:
        return "重点是价差与规则约束。行动上应核对交易成本、容量、资金占用和规则变化，而不是只看静态收益。"
    if "dividend-income" in themes:
        return "重点是高股息策略的风险收益匹配。行动上应检查盈利稳定性、估值、监管风险和利率环境。"
    if "fund-etf" in themes:
        return "重点是配置逻辑与持仓承受力。行动上应核对估值区间、行业暴露和回撤假设。"
    if "new-share" in themes:
        return "重点是估值与流动性。行动上应核对发行定价、换手、可比标的和短期情绪波动。"
    if "asset-allocation" in themes:
        return "重点是保守配置与资金安全。行动上应结合利率、存款保险边界和资金使用期限。"
    return "这类讨论更适合作为风险提示或情绪观察。行动上应回到数据、规则和仓位管理，不直接追随论坛热度。"


def pick_top_comments(topic: Dict, limit: int = 3) -> List[Dict]:
    ranked = []
    for comment in topic.get("comments", []):
        signal = max(comment.get("like_count", 0), comment.get("agree_user_count", 0))
        if signal < 2:
            continue
        ranked.append((signal, len(comment.get("content", "")), comment))

    ranked.sort(key=lambda item: (item[0], item[1]), reverse=True)
    selected = []
    for _, _, comment in ranked[:limit]:
        selected.append(
            {
                "author": comment.get("author", ""),
                "like_count": comment.get("like_count", 0),
                "agree_user_count": comment.get("agree_user_count", 0),
                "summary": sentence_snippet(comment.get("content", ""), max_length=110),
                "published_info": comment.get("published_info", ""),
            }
        )
    return selected


def is_low_signal(topic: Dict) -> bool:
    lowered = normalize(
        " ".join(
            [
                topic.get("title", ""),
                topic.get("body", ""),
                " ".join(topic.get("tags", [])),
            ]
        )
    )
    keyword_hits = sum(1 for keyword in INVESTMENT_KEYWORDS if keyword in lowered)
    signal_comment_count = sum(
        1 for comment in topic.get("comments", []) if max(comment.get("like_count", 0), comment.get("agree_user_count", 0)) >= 2
    )
    return keyword_hits < 1 and signal_comment_count == 0 and topic.get("category", "") == "其他"


def analyze_topics(topic_details: List[Dict], min_topics: int = 10, max_topics: int = 12) -> List[Dict]:
    analyzed = []
    for topic in topic_details:
        if is_low_signal(topic):
            continue

        score = topic_relevance_score(topic)
        top_comments = pick_top_comments(topic)
        entry = {
            "title": topic.get("title", ""),
            "url": topic.get("url", ""),
            "category": topic.get("category", ""),
            "tags": topic.get("tags", []),
            "reply_count": topic.get("reply_count", 0),
            "views": topic.get("views", 0),
            "topic_like_users": topic.get("topic_like_users", 0),
            "score": score,
            "core_issue": sentence_snippet(topic.get("title", ""), max_length=80),
            "op_summary": sentence_snippet(topic.get("body", ""), max_length=140),
            "top_comments": top_comments,
            "analyst_note": classify_action_note({"title": topic.get("title", ""), "body": topic.get("body", ""), "top_comments": top_comments}),
            "themes": detect_themes(" ".join([topic.get("title", ""), topic.get("body", ""), " ".join(topic.get("tags", []))])),
            "published_at": topic.get("published_at", ""),
        }
        analyzed.append(entry)

    analyzed.sort(key=lambda item: (item["score"], item["reply_count"], item["topic_like_users"]), reverse=True)
    selected = analyzed[:max_topics]
    if len(selected) < min_topics:
        return analyzed[:max(min_topics, len(selected))]
    return selected


def build_market_overview(selected_topics: List[Dict]) -> Dict[str, List[str]]:
    keyword_counter = Counter()
    consensus = []
    disagreements = []

    for topic in selected_topics:
        for theme in topic.get("themes", []):
            keyword_counter[theme] += 1
        for tag in topic.get("tags", []):
            if len(tag) >= 2:
                keyword_counter[tag] += 1

    recurring = []
    for keyword, _ in keyword_counter.most_common(6):
        recurring.append(keyword)

    if any("convertible-bond" in topic.get("themes", []) for topic in selected_topics):
        consensus.append("可转债条款博弈、下修和风险识别仍是社区最稳定的高频主题。")
    if any("dividend-income" in topic.get("themes", []) for topic in selected_topics):
        consensus.append("高股息与吃息策略讨论明显增多，核心分歧在于安全性与估值。")
    if any("asset-allocation" in topic.get("themes", []) for topic in selected_topics):
        consensus.append("保守理财、存款与资金安全话题明显升温。")

    sorted_by_reply = sorted(selected_topics, key=lambda item: item.get("reply_count", 0), reverse=True)
    for topic in sorted_by_reply[:3]:
        disagreements.append(topic["title"])

    return {
        "recurring_keywords": recurring,
        "consensus_points": consensus[:3],
        "divergent_topics": disagreements,
    }


def extract_core_conclusions(selected_topics: List[Dict], limit: int = 5) -> List[str]:
    conclusions = []
    for topic in selected_topics[:limit]:
        if topic.get("top_comments"):
            comment = topic["top_comments"][0]["summary"]
            conclusions.append(f"{topic['title']}：{comment}")
        else:
            conclusions.append(f"{topic['title']}：{topic['analyst_note']}")
    return conclusions[:limit]
