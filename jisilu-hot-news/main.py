import argparse
import sys
from datetime import date
from pathlib import Path


CURRENT_DIR = Path(__file__).resolve().parent
if str(CURRENT_DIR) not in sys.path:
    sys.path.insert(0, str(CURRENT_DIR))

from core.analyzer import analyze_topics, build_market_overview  # noqa: E402
from core.fetcher import build_runtime_manifest, fetch_html, fetch_topic_pages  # noqa: E402
from core.parser import parse_hot_topics_html, parse_topic_detail_html  # noqa: E402
from core.report import (  # noqa: E402
    build_concise_summary,
    build_failure_summary,
    build_full_report,
    resolve_report_output_path,
    write_json_file,
    write_text_file,
)


HOT_URL = "https://www.jisilu.cn/home/explore/sort_type-hot____day-7"


def parse_args():
    parser = argparse.ArgumentParser(description="Fetch and summarize Jisilu hot topics.")
    parser.add_argument("--max-topics", type=int, default=30, help="Maximum hot topics to fetch from the list page.")
    parser.add_argument("--max-selected", type=int, default=12, help="Maximum analyzed topics to include in the report.")
    parser.add_argument("--min-selected", type=int, default=10, help="Minimum desired high-value topics.")
    parser.add_argument("--model-name", default="nanobot", help="Model name suffix when the report path already exists.")
    parser.add_argument(
        "--output-dir",
        default=str(CURRENT_DIR / "out"),
        help="Directory used to save source json and draft report artifacts.",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    report_date = date.today().isoformat()
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    try:
        list_html = fetch_html(HOT_URL)
        topics = parse_hot_topics_html(list_html, max_topics=args.max_topics)
        topic_pages, topic_fetch_errors = fetch_topic_pages(topics)

        details = []
        parse_errors = []
        for item in topic_pages:
            try:
                details.append(parse_topic_detail_html(item["html"], item["topic"]))
            except Exception as exc:
                parse_errors.append(
                    {
                        "title": item["topic"].get("title", ""),
                        "url": item["topic"].get("url", ""),
                        "error": str(exc),
                    }
                )

        selected_topics = analyze_topics(details, min_topics=args.min_selected, max_topics=args.max_selected)
        overview = build_market_overview(selected_topics)

        report_path = resolve_report_output_path(report_date=report_date, model_name=args.model_name)
        full_report = build_full_report(report_date, overview, selected_topics, fetched_count=len(topics))
        concise_summary = build_concise_summary(report_date, len(topics), selected_topics, report_path)

        source_json_path = output_dir / f"{report_date}-jisilu-source.json"
        draft_report_path = output_dir / f"{report_date}-jisilu-draft.md"

        write_json_file(
            source_json_path,
            {
                "report_date": report_date,
                "fetched_count": len(topics),
                "selected_count": len(selected_topics),
                "overview": overview,
                "selected_topics": selected_topics,
                "topic_fetch_errors": topic_fetch_errors,
                "topic_parse_errors": parse_errors,
            },
        )
        write_text_file(draft_report_path, full_report)
        write_text_file(report_path, full_report)

        manifest = build_runtime_manifest(
            report_path=str(report_path),
            source_json_path=str(source_json_path),
            draft_path=str(draft_report_path),
            fetched_count=len(topics),
            selected_count=len(selected_topics),
        )
        write_json_file(output_dir / f"{report_date}-jisilu-manifest.json", manifest)

        print(concise_summary)
        return 0
    except Exception as exc:
        print(build_failure_summary("pipeline", str(exc)))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
