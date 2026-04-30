---
name: BrightData
version: 2.3.0
description: 渐进式 URL 抓取，采用四层回退机制 - WebFetch、Curl、浏览器自动化、Bright Data MCP。适用于：抓取 URL、获取 URL 内容、网页抓取、应对反爬检测、无法访问网站的情况。Progressive URL scraping with four-tier fallback - WebFetch, Curl, Browser Automation, Bright Data MCP. USE WHEN scrape URL, fetch URL, web scraping, bot detection, can't access site.
---

# BrightData - Progressive URL Scraping  渐进式 URL 抓取

**Intelligent URL content retrieval with automatic fallback strategy.**

---

## Activation Triggers

### Direct Scraping Requests
- "scrape this URL", "scrape [URL]", "scrape this page"  
    "抓取此网址"、"抓取[网址]"、"抓取此页面"
- "fetch this URL", "fetch [URL]", "fetch this page"  
    "获取此网址"、"获取[网址]"、"获取此页面"
- "pull content from [URL]", "get content from [URL]"  
    "从[URL]拉取内容", "从[URL]获取内容"
- "retrieve [URL]", "download this page content"  
    "获取[URL]", "下载此页面内容"

### Access Issues
- "can't access this site", "site is blocking me"  
    "无法访问此网站", "网站屏蔽了我"
- "bot detection", "CAPTCHA", "403 error"  
    "机器人检测"、"验证码"、"403 错误"
- "this URL won't load"  
    "此 URL 无法加载"

### Explicit Tier Requests
- "use Bright Data to fetch [URL]" - Skip to Tier 4  
    "使用 Bright Data 抓取[URL]" - 跳转至第 4 级
- "use browser to scrape [URL]" - Skip to Tier 3  
    "使用浏览器抓取[URL]" - 跳转至第 3 级

---

## Core Capability

**Five-Step Progressive Escalation (with mirror fallback):**

```
START
  |
Tier 1 (WebFetch) --> Success? --> Return content
  |
  No
  |
Tier 2 (Curl) --> Success? --> Return content
  |
  No
  |
Tier 2.5 (Jina AI mirror) --> Success? --> Return content
  |
  No
  |
Tier 3 (Browser) --> Success? --> Return content
  |
  No
  |
Tier 4 (Bright Data) --> Success? --> Return content
  |
  No
  |
Report failure + alternatives
```

---

## Tier Details

### Tier 1: WebFetch (Built-in)
- **Tool:** Claude Code's WebFetch
- **Speed:** ~2-5 seconds
- **Cost:** Free
- **Works for:** Public sites, no bot detection

### Tier 2: Curl with Chrome Headers
- **Tool:** Bash curl with comprehensive browser headers
- **Speed:** ~3-7 seconds
- **Cost:** Free
- **Works for:** Sites with basic user-agent filtering

### Tier 2.5: Jina AI Mirror (`r.jina.ai`)
- **Tool:** HTTP fetch to `https://r.jina.ai/http://https://target-url`
- **Speed:** ~2-10 seconds
- **Cost:** Free
- **Works for:** Public forum/article pages when direct access is blocked by Cloudflare or anti-bot, but a readable mirrored markdown copy is available
- **Caveat:** May return partial page context or surrounding posts rather than a perfectly isolated target post; verify against nearby anchors/post numbers when precision matters

### Tier 3: Browser Automation (Playwright)
- **Tool:** Browser skill's Playwright automation
- **Speed:** ~10-20 seconds
- **Cost:** Free
- **Works for:** JavaScript SPAs, dynamic content

### Tier 4: Bright Data MCP
- **Tool:** `mcp__Brightdata__scrape_as_markdown`
- **Speed:** ~5-15 seconds
- **Cost:** Bright Data credits
- **Works for:** CAPTCHA, advanced bot detection, residential IPs

---

## Workflow Routing

**Default workflow for all URL scraping:**
- **Route to:** `Workflows/FourTierScrape.md`
- **Output:** URL content in markdown format

---

## Examples

### Example 1: Simple Site (Tier 1 Success)

**User:** "Scrape https://example.com"

**Process:**
1. Attempt Tier 1 (WebFetch)
2. Success in 3 seconds
3. Return markdown content

### Example 2: Cloudflare-Protected Forum Post (Tier 2.5 Success)

**User:** "Fetch https://linux.do/t/topic/1926833/1204"

**Process:**
1. Tier 1 fails (bot protection)
2. Tier 2 fails (403 / Cloudflare)
3. Tier 2.5 succeeds via `https://r.jina.ai/http://https://linux.do/t/topic/1926833/1204`
4. Extract target post from mirrored markdown and note any confidence limits
5. Return concise summary

### Example 3: JavaScript Site (Tier 3 Success)

**User:** "Fetch https://spa-app.com"

**Process:**
1. Tier 1 fails (blocked)
2. Tier 2 fails (JavaScript required)
3. Tier 3 succeeds with Playwright
4. Return markdown content

### Example 4: Protected Site (Tier 4 Success)

**User:** "Can't access https://protected-site.com"

**Process:**
1. Tier 1 fails (403)
2. Tier 2 fails (bot detection)
3. Tier 3 fails (CAPTCHA)
4. Tier 4 succeeds with Bright Data
5. Return markdown content

### Example 5: WeChat Article (mp.weixin.qq.com) Mobile-UA Shortcut

**User:** "Read this WeChat article https://mp.weixin.qq.com/s/..."

**Process:**
1. Browser / mirror may hit `环境异常` / CAPTCHA and look fully blocked.
2. Before escalating further, try **direct HTTP fetch with a mobile Safari UA** via terminal/Python requests.
3. Parse `#activity-name`, `meta[property="og:title"]`, `meta[name="description"]`, `#js_name`, `#js_author_name`, and `#js_content` from the returned HTML.
4. If article HTML loads, treat this as a successful retrieval even if browser automation is blocked.
5. Only escalate if the direct mobile-UA fetch also fails.

**Why this matters:** WeChat sometimes blocks browser automation and Jina mirror access with CAPTCHA, while the raw article HTML is still retrievable with a realistic mobile UA.

### Example 6: Direct Tier Request

**User:** "Use Bright Data to fetch https://any-site.com"

**Process:**
1. User explicitly requested Bright Data
2. Skip directly to Tier 4
3. Return markdown content

---

## Integration Points

- **WebFetch Tool** - Built-in Claude Code tool
- **Bash Tool** - For curl commands
- **Browser Skill** - For Playwright automation (requires pai-browser-skill)
- **Bright Data MCP** - For professional scraping

---

## Related Documentation

- `Workflows/FourTierScrape.md` - Complete workflow implementation
- `INSTALL.md` - Installation guide
- `VERIFY.md` - Verification checklist

**Last Updated:** 2026-01-14