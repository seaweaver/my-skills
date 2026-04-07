import sys
import tempfile
import unittest
from pathlib import Path


SKILL_DIR = Path(__file__).resolve().parents[1]
if str(SKILL_DIR) not in sys.path:
    sys.path.insert(0, str(SKILL_DIR))

from core.analyzer import analyze_topics  # noqa: E402
from core.parser import parse_hot_topics_html, parse_topic_detail_html  # noqa: E402
from core.report import build_concise_summary, resolve_report_output_path  # noqa: E402


HOT_LIST_HTML = """
<html><body>
<h4><a href="/question/123456">龙大再分析！下修条款宽松，随时可再次计时下修</a><a href="/tag/转债">龙大转债</a></h4>
<p class="pull-right">贡献 :</p>
<span class="aw-text-color-999">债券/可转债 • 销户保平安 回复 • 2026-04-07 09:24 • 7622 次浏览</span>
</body></html>
"""


TOPIC_DETAIL_HTML = """
<html><body>
<div class="aw-mod aw-item aw-question-detail-title">
  <div class="aw-mod-head"><h1>龙大再分析！下修条款宽松，随时可再次计时下修</h1></div>
  <div class="aw-mod-body">
    <div class="aw-question-detail-txt markitup-box">核心是下修条款宽松，市场在重新评估条款博弈空间。</div>
    <div class="aw-question-detail-meta">
      <div>
        <span class="aw-text-color-999">发表时间 2026-04-07 09:24</span>
        <span class="aw-text-color-999">来自北京</span>
      </div>
      <p class="aw-text-color-999 aw-agree-by">
        赞同来自:
        <a class="aw-user-name" href="/people/a">甲</a>
        <a class="aw-user-name" href="/people/b">乙</a>
      </p>
    </div>
  </div>
</div>
<div class="aw-mod-body aw-dynamic-topic">
  <div class="aw-item" id="answer_list_1">
    <div class="aw-mod-body clearfix">
      <em class="aw-border-radius-5 aw-vote-count pull-left disable">7</em>
      <div class="pull-left aw-dynamic-topic-content">
        <div>
          <p class="publisher"><a class="aw-user-name" href="/people/user1">评论员A</a></p>
          <p class="aw-text-color-999 aw-agree-by">赞同来自: <a class="aw-user-name" href="/people/c">丙</a></p>
          <div class="markitup-box">下修条款宽松意味着博弈时间窗口更长，关键要看公告和正股修复。</div>
        </div>
        <div class="aw-dynamic-topic-meta"><span class="pull-left aw-text-color-999">2026-04-07 10:01 来自上海</span></div>
      </div>
    </div>
  </div>
</div>
</body></html>
"""


class JisiluHotNewsTests(unittest.TestCase):
    def test_parse_hot_topics_html(self):
        topics = parse_hot_topics_html(HOT_LIST_HTML, max_topics=5)
        self.assertEqual(len(topics), 1)
        self.assertEqual(topics[0]["title"], "龙大再分析！下修条款宽松，随时可再次计时下修")
        self.assertEqual(topics[0]["reply_count"], 0)
        self.assertEqual(topics[0]["category"], "债券/可转债")
        self.assertEqual(topics[0]["views"], 7622)

    def test_parse_topic_detail_html(self):
        topic = {
            "title": "龙大再分析！下修条款宽松，随时可再次计时下修",
            "url": "https://www.jisilu.cn/question/123456",
            "category": "债券/可转债",
            "tags": ["龙大转债"],
            "reply_count": 44,
            "views": 7622,
        }
        detail = parse_topic_detail_html(TOPIC_DETAIL_HTML, topic)
        self.assertEqual(detail["title"], topic["title"])
        self.assertEqual(detail["topic_like_users"], 2)
        self.assertEqual(len(detail["comments"]), 1)
        self.assertEqual(detail["comments"][0]["author"], "评论员A")
        self.assertEqual(detail["comments"][0]["like_count"], 7)

    def test_build_concise_summary_and_output_path(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            first_path = resolve_report_output_path("2026-04-07", model_name="nanobot", root=root)
            first_path.write_text("x", encoding="utf-8")
            second_path = resolve_report_output_path("2026-04-07", model_name="nanobot", root=root)
            self.assertTrue(str(second_path).endswith("2026-04-07 jisilu_report_nanobot.md"))

            selected_topics = analyze_topics(
                [
                    {
                        "title": "龙大再分析！下修条款宽松，随时可再次计时下修",
                        "url": "https://www.jisilu.cn/question/123456",
                        "category": "债券/可转债",
                        "tags": ["龙大转债"],
                        "reply_count": 44,
                        "views": 7622,
                        "body": "核心是下修条款宽松，市场在重新评估条款博弈空间。",
                        "topic_like_users": 2,
                        "comments": [
                            {
                                "author": "评论员A",
                                "like_count": 7,
                                "agree_user_count": 1,
                                "content": "下修条款宽松意味着博弈时间窗口更长，关键要看公告和正股修复。",
                                "published_info": "2026-04-07 10:01 来自上海",
                            }
                        ],
                    }
                ],
                min_topics=1,
                max_topics=3,
            )
            summary = build_concise_summary("2026-04-07", 12, selected_topics, second_path)
            self.assertIn("- 日期: 2026-04-07", summary)
            self.assertIn("- 抓取主题: 12", summary)
            self.assertIn("- 入选主题: 1", summary)
            self.assertIn("龙大再分析", summary)
            self.assertIn(str(second_path), summary)


if __name__ == "__main__":
    unittest.main()
