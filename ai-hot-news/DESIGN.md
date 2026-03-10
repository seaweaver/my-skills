# AI 热门新闻聚合技能 (ai-hot-news) 设计方案

## 1. 目录结构设计

```
skills/ai-hot-news/
├── SKILL.md                    # 技能说明文档
├── config.yaml                 # 配置文件（数据源、关键词、输出格式）
├── main.py                     # 主入口，协调各模块
├── core/
│   ├── __init__.py
│   ├── provider_base.py        # Provider 基类/接口定义
│   ├── aggregator.py           # 聚合器：去重、排序、合并
│   ├── cache_manager.py        # 缓存管理：增量更新
│   └── deduplicator.py         # 去重机制：标题相似度检测
├── providers/
│   ├── __init__.py
│   ├── v2ex_provider.py        # V2EX 数据源实现
│   ├── linuxdo_provider.py     # Linux Do 论坛实现
│   └── hackernews_provider.py  # Hacker News 示例（待扩展）
├── utils/
│   ├── __init__.py
│   ├── http_client.py          # 统一 HTTP 客户端
│   ├── text_similarity.py      # 文本相似度计算
│   └── formatter.py            # 消息格式化
├── output/
│   ├── __init__.py
│   └── feishu_sender.py        # 飞书消息推送
├── tasks/
│   ├── cron_task.py            # Cron 定时任务入口
│   └── manual_task.py          # 手动触发入口
├── requirements.txt            # Python 依赖
├── run_cron.bat                # Windows 定时任务脚本
└── tests/
    ├── __init__.py
    ├── test_providers.py       # Provider 测试
    └── test_deduplication.py   # 去重测试
```

---

## 2. 核心接口定义

### 2.1 Provider 基类 (`core/provider_base.py`)

```python
#!/usr/bin/env python3
"""
Provider 基类 - 所有数据源必须实现此接口
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional
from datetime import datetime


@dataclass
class NewsItem:
    """新闻项数据结构"""
    id: str                    # 唯一标识（用于去重）
    title: str                 # 标题
    url: str                   # 原文链接
    source: str                # 来源平台（v2ex, linuxdo, hackernews）
    author: str                # 作者
    score: int                 # 热度分数（回复数/点赞数等）
    published_at: datetime     # 发布时间
    content_preview: str = ""  # 内容预览
    tags: list = None          # 标签列表
    
    def __post_init__(self):
        if self.tags is None:
            self.tags = []


class ProviderBase(ABC):
    """
    数据源 Provider 基类
    
    每个数据源需要实现三个核心方法：
    1. fetch: 抓取原始数据
    2. parse: 解析为标准 NewsItem 列表
    3. filter: 根据关键词筛选
    """
    
    def __init__(self, config: dict):
        """
        初始化 Provider
        
        Args:
            config: 配置字典，包含：
                - enabled: 是否启用
                - keywords: 筛选关键词列表
                - exclude_keywords: 排除关键词列表
                - limit: 返回数量限制
                - min_score: 最低热度分数
        """
        self.config = config
        self.name = self.__class__.__name__.replace('_provider', '').lower()
    
    @abstractmethod
    def fetch(self) -> Optional[any]:
        """
        抓取原始数据
        
        Returns:
            原始数据（通常是 JSON 或 HTML），失败返回 None
            
        注意：此方法不应抛出异常，内部处理错误并返回 None
        """
        pass
    
    @abstractmethod
    def parse(self, raw_data: any) -> list[NewsItem]:
        """
        解析原始数据为标准 NewsItem 列表
        
        Args:
            raw_data: fetch() 返回的原始数据
            
        Returns:
            NewsItem 列表
        """
        pass
    
    @abstractmethod
    def filter(self, items: list[NewsItem]) -> list[NewsItem]:
        """
        根据关键词筛选新闻
        
        Args:
            items: 解析后的 NewsItem 列表
            
        Returns:
            筛选后的 NewsItem 列表
        """
        pass
    
    def get_items(self) -> list[NewsItem]:
        """
        完整流程：fetch -> parse -> filter
        
        Returns:
            筛选后的 NewsItem 列表
        """
        try:
            raw_data = self.fetch()
            if raw_data is None:
                return []
            
            items = self.parse(raw_data)
            filtered = self.filter(items)
            
            # 应用数量限制
            limit = self.config.get('limit', 5)
            return filtered[:limit]
            
        except Exception as e:
            print(f"[{self.name}] Error: {e}")
            return []
    
    def _match_keywords(self, text: str, keywords: list[str]) -> bool:
        """检查文本是否匹配任意关键词"""
        text_lower = text.lower()
        for keyword in keywords:
            if keyword.lower() in text_lower or keyword in text:
                return True
        return False
    
    def _exclude_keywords(self, text: str, exclude_list: list[str]) -> bool:
        """检查文本是否包含排除关键词"""
        text_lower = text.lower()
        for keyword in exclude_list:
            if keyword.lower() in text_lower or keyword in text:
                return True
        return False
```

---

## 3. 配置文件格式

### `config.yaml`

```yaml
# AI 热门新闻聚合技能配置

# 全局设置
global:
  output_format: "feishu"      # 输出格式：feishu, markdown, json
  timezone: "Asia/Shanghai"    # 时区
  language: "zh-CN"            # 语言

# 数据源配置
providers:
  v2ex:
    enabled: true
    api_url: "https://www.v2ex.com/api/topics/hot.json"
    limit: 5                   # 每个源最多返回的新闻数
    min_score: 0               # 最低回复数
    keywords:                  # 筛选关键词
      - AI
      - 人工智能
      - 大模型
      - LLM
      - GPT
      - Claude
      - 开发
      - 编程
      - 代码
      - Python
      - JavaScript
      - 机器学习
      - 深度学习
      - GitHub
      - 开源
      - 程序员
    exclude_keywords:          # 排除关键词
      - 问政
      - 二手
      - 交易
  
  linuxdo:
    enabled: true
    base_url: "https://linux.do"
    tag_id: 444                # AI 板块 tag ID
    limit: 5
    min_score: 0
    keywords:
      - AI
      - 人工智能
      - 大模型
      - LLM
      - 机器学习
      - 深度学习
      - Python
      - 开发
    exclude_keywords: []
  
  hackernews:
    enabled: false             # 默认禁用，按需开启
    api_url: "https://hacker-news.firebaseio.com/v0/topstories.json"
    limit: 5
    min_score: 10
    keywords:
      - AI
      - artificial intelligence
      - machine learning
      - LLM
      - GPT
      - Python
      - programming
    exclude_keywords: []

# 去重设置
deduplication:
  enabled: true
  method: "hybrid"             # similarity, url, hybrid
  similarity_threshold: 0.85   # 标题相似度阈值（0-1）
  time_window_hours: 24        # 多长时间内视为重复

# 缓存设置
cache:
  enabled: true
  ttl_seconds: 600             # 缓存过期时间（秒）
  file_path: "./cache/news_cache.json"

# 输出设置
output:
  feishu:
    webhook_url: "${FEISHU_WEBHOOK}"  # 支持环境变量
    mention_users: []          # 提及的用户 ID 列表
  max_items_total: 15          # 总输出数量上限
  include_source_icon: true    # 显示来源图标
```

---

## 4. 执行流程

### 4.1 流程图

```
┌─────────────────┐
│   触发技能      │
│ (cron/手动)     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  加载配置文件   │
│  (config.yaml)  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  初始化 Provider │
│  (根据 enabled)  │
└────────┬────────┘
         │
         ├──────────────────────┐
         │                      │
         ▼                      ▼
┌─────────────────┐   ┌─────────────────┐
│  Provider A     │   │  Provider B     │
│  (V2EX)         │   │  (LinuxDo)      │
│  fetch()        │   │  fetch()        │
│  parse()        │   │  parse()        │
│  filter()       │   │  filter()       │
└────────┬────────┘   └────────┬────────┘
         │                      │
         │    ┌─────────────────┘
         │    │
         ▼    ▼
┌─────────────────────────┐
│      缓存检查           │
│  (跳过未变更的数据)     │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│      合并所有结果       │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│      去重处理           │
│  (标题相似度 + URL)      │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│      按热度排序         │
│  (score 降序)           │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│      截取 Top N         │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│      格式化输出         │
│  (飞书卡片/Markdown)    │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│      推送到飞书         │
└─────────────────────────┘
```

### 4.2 伪代码

```python
# main.py 核心逻辑

def main(trigger_mode: str = "manual"):
    # 1. 加载配置
    config = load_config("config.yaml")
    
    # 2. 初始化启用的 Provider
    providers = []
    for name, provider_config in config['providers'].items():
        if provider_config.get('enabled', False):
            provider = create_provider(name, provider_config)
            providers.append(provider)
    
    # 3. 并行抓取所有数据源（错误隔离）
    all_items = []
    with ThreadPoolExecutor(max_workers=len(providers)) as executor:
        futures = {executor.submit(p.get_items): p for p in providers}
        for future in as_completed(futures):
            provider = futures[future]
            try:
                items = future.result()
                all_items.extend(items)
                log(f"[{provider.name}] 获取 {len(items)} 条新闻")
            except Exception as e:
                log(f"[{provider.name}] 失败：{e}")
                # 单个失败不影响其他
    
    # 4. 缓存检查与增量更新
    cache = CacheManager(config['cache'])
    new_items = cache.get_new_items(all_items)
    
    # 5. 去重
    if config['deduplication']['enabled']:
        deduplicator = Deduplicator(config['deduplication'])
        unique_items = deduplicator.deduplicate(new_items)
    else:
        unique_items = new_items
    
    # 6. 排序并截取
    sorted_items = sorted(unique_items, key=lambda x: x.score, reverse=True)
    top_items = sorted_items[:config['output']['max_items_total']]
    
    # 7. 格式化
    formatter = Formatter(config['output'])
    message = formatter.format(top_items)
    
    # 8. 推送
    if trigger_mode == "cron" and len(top_items) > 0:
        sender = FeishuSender(config['output']['feishu'])
        sender.send(message)
    
    return message
```

---

## 5. 扩展示例：添加 Hacker News

### 5.1 创建 Provider (`providers/hackernews_provider.py`)

```python
#!/usr/bin/env python3
"""
Hacker News Provider
"""

import json
import urllib.request
from datetime import datetime, timezone
from typing import Optional

from core.provider_base import ProviderBase, NewsItem


class HackernewsProvider(ProviderBase):
    """Hacker News 数据源实现"""
    
    def __init__(self, config: dict):
        super().__init__(config)
        self.api_url = config.get('api_url', 
            "https://hacker-news.firebaseio.com/v0/topstories.json")
        self.item_api = "https://hacker-news.firebaseio.com/v0/item/"
    
    def fetch(self) -> Optional[list[int]]:
        """获取热门帖子 ID 列表"""
        try:
            req = urllib.request.Request(
                self.api_url,
                headers={'User-Agent': 'AI-Hot-News/1.0'}
            )
            with urllib.request.urlopen(req, timeout=10) as response:
                data = json.loads(response.read().decode('utf-8'))
                return data[:30]  # 只取前 30 个 ID
        except Exception as e:
            print(f"[hackernews] Fetch error: {e}")
            return None
    
    def parse(self, raw_data: list[int]) -> list[NewsItem]:
        """解析帖子详情"""
        items = []
        
        for item_id in raw_data:
            try:
                url = f"{self.item_api}{item_id}.json"
                req = urllib.request.Request(
                    url,
                    headers={'User-Agent': 'AI-Hot-News/1.0'}
                )
                with urllib.request.urlopen(req, timeout=5) as response:
                    data = json.loads(response.read().decode('utf-8'))
                
                # 跳过没有分数的项目
                score = data.get('score', 0)
                if score < self.config.get('min_score', 0):
                    continue
                
                # 构建 NewsItem
                item = NewsItem(
                    id=f"hn_{item_id}",
                    title=data.get('title', 'No title'),
                    url=data.get('url') or f"https://news.ycombinator.com/item?id={item_id}",
                    source="hackernews",
                    author=data.get('by', 'unknown'),
                    score=score,
                    published_at=datetime.fromtimestamp(
                        data.get('time', 0), tz=timezone.utc
                    ),
                    content_preview="",
                    tags=["hackernews"]
                )
                items.append(item)
                
            except Exception as e:
                print(f"[hackernews] Parse error for item {item_id}: {e}")
                continue
        
        return items
    
    def filter(self, items: list[NewsItem]) -> list[NewsItem]:
        """根据关键词筛选"""
        keywords = self.config.get('keywords', [])
        exclude_list = self.config.get('exclude_keywords', [])
        
        if not keywords:
            return items
        
        filtered = []
        for item in items:
            text = f"{item.title}"
            
            # 检查排除词
            if self._exclude_keywords(text, exclude_list):
                continue
            
            # 检查关键词
            if self._match_keywords(text, keywords):
                filtered.append(item)
        
        return filtered
```

### 5.2 注册 Provider (`providers/__init__.py`)

```python
from .v2ex_provider import V2exProvider
from .linuxdo_provider import LinuxdoProvider
from .hackernews_provider import HackernewsProvider

PROVIDER_REGISTRY = {
    'v2ex': V2exProvider,
    'linuxdo': LinuxdoProvider,
    'hackernews': HackernewsProvider,
}

def create_provider(name: str, config: dict):
    """工厂函数：根据名称创建 Provider 实例"""
    provider_class = PROVIDER_REGISTRY.get(name)
    if not provider_class:
        raise ValueError(f"Unknown provider: {name}")
    return provider_class(config)
```

### 5.3 更新配置

在 `config.yaml` 中启用 Hacker News：

```yaml
providers:
  hackernews:
    enabled: true  # 改为 true
    limit: 3
    min_score: 15
    keywords:
      - AI
      - machine learning
      - LLM
```

---

## 6. 依赖管理

### `requirements.txt`

```txt
# HTTP 请求
requests>=2.31.0

# YAML 配置解析
PyYAML>=6.0

# 文本相似度计算
thefuzz>=0.19.0
python-Levenshtein>=0.21.0

# 日期时间处理
python-dateutil>=2.8.2

# 异步支持（可选，用于并发抓取）
aiohttp>=3.9.0

# 测试
pytest>=7.4.0
pytest-asyncio>=0.21.0
```

### 依赖用途说明

| 库 | 用途 |
|----|------|
| `requests` | HTTP 请求，抓取 API 数据 |
| `PyYAML` | 解析 YAML 配置文件 |
| `thefuzz` | 计算标题字符串相似度（去重） |
| `python-Levenshtein` | thefuzz 的性能加速后端 |
| `python-dateutil` | 时区转换和日期解析 |
| `aiohttp` | 异步 HTTP，可选用于高并发场景 |
| `pytest` | 单元测试框架 |

---

## 7. 关键模块实现要点

### 7.1 去重机制 (`core/deduplicator.py`)

```python
from thefuzz import fuzz

class Deduplicator:
    def __init__(self, config: dict):
        self.threshold = config.get('similarity_threshold', 0.85)
        self.method = config.get('method', 'hybrid')
        self.seen_urls = set()
        self.seen_titles = []
    
    def deduplicate(self, items: list[NewsItem]) -> list[NewsItem]:
        result = []
        for item in items:
            if self._is_duplicate(item):
                continue
            result.append(item)
            self._mark_seen(item)
        return result
    
    def _is_duplicate(self, item: NewsItem) -> bool:
        # URL 去重
        if item.url in self.seen_urls:
            return True
        
        # 标题相似度去重
        for seen_title in self.seen_titles:
            ratio = fuzz.ratio(item.title.lower(), seen_title.lower())
            if ratio >= self.threshold * 100:
                return True
        
        return False
    
    def _mark_seen(self, item: NewsItem):
        self.seen_urls.add(item.url)
        self.seen_titles.append(item.title)
```

### 7.2 缓存管理 (`core/cache_manager.py`)

```python
import json
import hashlib
from pathlib import Path
from datetime import datetime, timedelta

class CacheManager:
    def __init__(self, config: dict):
        self.enabled = config.get('enabled', True)
        self.ttl = config.get('ttl_seconds', 600)
        self.cache_file = Path(config.get('file_path', './cache/cache.json'))
        self.cache = self._load_cache()
    
    def _load_cache(self) -> dict:
        if not self.enabled or not self.cache_file.exists():
            return {}
        try:
            with open(self.cache_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return {}
    
    def save_cache(self):
        if not self.enabled:
            return
        self.cache_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.cache_file, 'w', encoding='utf-8') as f:
            json.dump(self.cache, f, ensure_ascii=False, indent=2)
    
    def get_new_items(self, items: list[NewsItem]) -> list[NewsItem]:
        """返回相对于缓存的新增/变更项"""
        if not self.enabled:
            return items
        
        new_items = []
        for item in items:
            cache_key = f"{item.source}:{item.id}"
            cached = self.cache.get(cache_key)
            
            # 检查是否过期或变更
            if cached:
                cached_time = datetime.fromisoformat(cached['cached_at'])
                if datetime.now() - cached_time < timedelta(seconds=self.ttl):
                    if cached.get('score') == item.score:
                        continue  # 未变更，跳过
            
            new_items.append(item)
            self.cache[cache_key] = {
                'score': item.score,
                'title': item.title,
                'cached_at': datetime.now().isoformat()
            }
        
        self.save_cache()
        return new_items
```

### 7.3 飞书推送 (`output/feishu_sender.py`)

```python
import json
import requests
import os

class FeishuSender:
    def __init__(self, config: dict):
        self.webhook_url = config.get('webhook_url', '')
        # 支持环境变量替换
        if self.webhook_url.startswith('${'):
            env_var = self.webhook_url.strip('${}')
            self.webhook_url = os.environ.get(env_var, '')
    
    def send(self, message: str):
        """发送 Markdown 格式消息到飞书"""
        payload = {
            "msg_type": "interactive",
            "card": {
                "config": {
                    "wide_screen_mode": True
                },
                "elements": [
                    {
                        "tag": "markdown",
                        "content": message
                    }
                ]
            }
        }
        
        try:
            response = requests.post(
                self.webhook_url,
                json=payload,
                headers={'Content-Type': 'application/json'},
                timeout=10
            )
            response.raise_for_status()
            return True
        except Exception as e:
            print(f"Feishu send error: {e}")
            return False
```

---

## 8. 运行模式

### 8.1 手动触发 (`tasks/manual_task.py`)

```python
#!/usr/bin/env python3
"""手动触发入口 - 供 nanobot 直接调用"""

import sys
sys.path.insert(0, '..')

from main import main

if __name__ == "__main__":
    result = main(trigger_mode="manual")
    print(result)
```

### 8.2 Cron 定时任务 (`tasks/cron_task.py`)

```python
#!/usr/bin/env python3
"""Cron 定时任务入口"""

import sys
sys.path.insert(0, '..')

from main import main

if __name__ == "__main__":
    main(trigger_mode="cron")
```

### 8.3 Windows 定时任务脚本 (`run_cron.bat`)

```batch
@echo off
cd /d "%~dp0"
python tasks\cron_task.py >> logs\cron.log 2>&1
```

---

## 9. 错误隔离策略

```python
# 在 main.py 中的并发处理
from concurrent.futures import ThreadPoolExecutor, as_completed

def fetch_all_providers(providers: list) -> list[NewsItem]:
    """并行抓取，单个失败不影响整体"""
    all_items = []
    
    with ThreadPoolExecutor(max_workers=len(providers)) as executor:
        # 提交所有任务
        future_to_provider = {
            executor.submit(p.get_items): p for p in providers
        }
        
        # 收集结果
        for future in as_completed(future_to_provider):
            provider = future_to_provider[future]
            try:
                items = future.result(timeout=30)
                all_items.extend(items)
                logger.info(f"[{provider.name}] Success: {len(items)} items")
            except TimeoutError:
                logger.error(f"[{provider.name}] Timeout")
            except Exception as e:
                logger.error(f"[{provider.name}] Error: {e}")
                # 继续处理其他 provider
    
    return all_items
```

---

## 10. 总结

### 设计特点

1. **插件化架构**：每个数据源独立实现 Provider 接口，易于扩展
2. **配置驱动**：通过 YAML 控制启用的数据源、关键词、输出格式
3. **错误隔离**：单个数据源失败不影响整体流程
4. **智能去重**：基于 URL + 标题相似度的混合去重
5. **增量缓存**：避免重复抓取相同内容
6. **双模式运行**：支持 cron 定时和手动触发

### 扩展新数据源的步骤

1. 在 `providers/` 目录创建新的 `xxx_provider.py`
2. 继承 `ProviderBase` 并实现 `fetch`, `parse`, `filter`
3. 在 `providers/__init__.py` 注册 Provider
4. 在 `config.yaml` 添加配置
5. 完成！

### 文件路径

本设计方案已保存为：`C:\Users\zhuhaibo\.nanobot\workspace\skills\ai-hot-news\DESIGN.md`
