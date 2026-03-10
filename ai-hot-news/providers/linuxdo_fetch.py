#!/usr/bin/env python3
"""
Linux Do 论坛话题抓取脚本
使用 Playwright 浏览器自动化抓取（绕过反爬）
可独立运行测试
"""
import sys
import json
from pathlib import Path
from datetime import datetime

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    print("ERROR: playwright not installed. Run: pip install playwright")
    sys.exit(1)


def fetch_linuxdo_topics(limit: int = 30, timeout: int = 30000):
    """
    使用 Playwright 抓取 Linux Do AI 板块话题
    
    Args:
        limit: 最大话题数量
        timeout: 页面加载超时时间（毫秒）
    
    Returns:
        话题列表 [{title, url, author, replies, created_at, excerpt}, ...]
    """
    topics = []
    
    try:
        with sync_playwright() as p:
            # 启动浏览器（headless 模式）
            browser = p.chromium.launch(headless=True, args=[
                '--no-sandbox',
                '--disable-setuid-sandbox',
                '--disable-dev-shm-usage'
            ])
            
            context = browser.new_context(
                user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
                viewport={'width': 1920, 'height': 1080}
            )
            
            page = context.new_page()
            
            # 访问 Linux Do AI 板块
            url = "https://linux.do/tag/444"
            print(f"[LinuxDo] Navigating to {url}...")
            
            try:
                page.goto(url, wait_until='networkidle', timeout=timeout)
            except Exception as e:
                print(f"[LinuxDo] Page load error: {e}")
                browser.close()
                return []
            
            # 等待话题列表加载
            page.wait_for_selector('tr.topic-list-item', timeout=10000)
            
            # 查找所有话题项
            topic_items = page.query_selector_all('tr.topic-list-item')
            print(f"[LinuxDo] Found {len(topic_items)} topic items")
            
            for i, item in enumerate(topic_items[:limit]):
                try:
                    # 提取标题和链接
                    title_elem = item.query_selector('a.title')
                    if not title_elem:
                        continue
                    
                    title = title_elem.inner_text().strip()
                    href = title_elem.get_attribute('href', '')
                    url = f"https://linux.do{href}" if href.startswith('/') else href
                    
                    # 提取作者
                    author_elem = item.query_selector('a[data-user-card]')
                    author = author_elem.get_attribute('data-user-card') if author_elem else 'anonymous'
                    
                    # 提取回复数
                    replies_elem = item.query_selector('td.num.replies') or item.query_selector('span.post-count')
                    replies_text = replies_elem.inner_text().strip() if replies_elem else '0'
                    try:
                        replies = int(replies_text)
                    except:
                        replies = 0
                    
                    # 提取创建时间
                    time_elem = item.query_selector('time')
                    created_at = datetime.now()
                    if time_elem:
                        datetime_str = time_elem.get_attribute('datetime')
                        if datetime_str:
                            try:
                                created_at = datetime.fromisoformat(datetime_str.replace('Z', '+00:00'))
                            except:
                                pass
                    
                    # 提取摘要
                    excerpt_elem = item.query_selector('div.topic-excerpt')
                    excerpt = excerpt_elem.inner_text().strip()[:200] if excerpt_elem else ''
                    
                    topics.append({
                        'title': title,
                        'url': url,
                        'author': author,
                        'replies': replies,
                        'created_at': created_at.isoformat(),
                        'excerpt': excerpt
                    })
                    
                except Exception as e:
                    print(f"[LinuxDo] Parse item {i} error: {e}")
                    continue
            
            browser.close()
            print(f"[LinuxDo] Successfully fetched {len(topics)} topics")
            
    except Exception as e:
        print(f"[LinuxDo] Browser error: {e}")
        return []
    
    return topics


def main():
    """主函数（独立运行时）"""
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else 30
    
    print(f"[LinuxDo] Fetching up to {limit} topics...")
    topics = fetch_linuxdo_topics(limit=limit)
    
    # 输出 JSON 格式结果
    print(json.dumps(topics, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
