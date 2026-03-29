# 项目更新检查报告（2026-03-29）

## 摘要

本次更新的核心不是单一技能补丁，而是一次围绕“技能仓库治理”的集中增强。

- 新增系统级技能基础设施：`.system/skill-creator`、`.system/skill-installer`
- 新增 `obsidian-cli` 技能，补齐官方 Obsidian CLI 自动化能力
- 强化 `cf-quant-web` 的信号导入约束与数据库备份能力
- 重写 `self-improving-agent`，转为本地优先、脱敏记录、按需初始化
- 新增仓库级协作文档：`AGENTS.md`、`SKILL_USE_GUIDE.md`
- 为保证这批变更可验证，补修了 `.system/skill-creator/scripts/quick_validate.py` 的 Windows/UTF-8 兼容性，并新增回归测试

## 更新范围与影响

### 1. 系统技能基础设施

新增 `.system/skill-creator/` 与 `.system/skill-installer/` 两个系统技能目录，包含：

- `SKILL.md`
- `agents/openai.yaml`
- `scripts/`
- `assets/`
- `references/`

这意味着仓库开始同时覆盖：

- 技能创建与初始化
- OpenAI/Codex UI 元数据生成
- 技能快速校验
- 从 GitHub 或 curated 列表安装技能

对仓库定位的影响是：从“技能集合”进一步升级为“技能开发 + 技能分发”的工作台。

### 2. 新增 `obsidian-cli`

新增 `obsidian-cli/SKILL.md`，覆盖官方 Obsidian CLI（v1.12+）的主要能力，包括：

- vault 信息读取
- daily note 操作
- 文件读写与移动
- 搜索
- task 管理
- tags / properties / aliases
- links / backlinks / unresolved / outline
- bookmarks / bases / templates 等

这补齐了本仓库在 Obsidian 自动化方向的官方 CLI 方案。

### 3. `cf-quant-web` 能力增强

`cf-quant-web/SKILL.md` 本次有两类显著增强：

- 信号导入从“会导”升级为“幂等导入”
- 新增数据库备份能力

重点变化包括：

- 新增备份端点说明：`POST /api/backup`、`GET /api/backup/list`
- 明确导入前必须查重，禁止无脑重复提交
- 固化重复判定键：`strategy_id + signal_date + security_code + direction`
- 明确批内去重和冲突处理规则
- 强化证券代码标准化要求
- 补充“全部已存在时不重复导入”的对外汇报规范

这让 `cf-quant-web` 更接近可直接执行的操作规程，而不是接口备忘录。

### 4. `self-improving-agent` 本地化重构

`self-improving-agent` 是这次调整最大的单项更新之一，方向很明确：从“泛化说明”收敛到“本地维护、低风险、可沉淀”的工作流。

核心变化：

- frontmatter 描述改成更明确的触发条件与输出落点
- 引入 Local-First Policy，不在日常使用中自动联网安装/更新
- 改为按需初始化 `.learnings/`
- 强化脱敏与安全规则，避免记录 secrets、完整 transcript、敏感输出
- 细化 correction / feature request / knowledge gap / error 的触发信号
- 明确 durable learning 的提升目标：`AGENTS.md`、`TOOLS.md`、`USER.md`、`MEMORY.md`、`HISTORY.md`、`CLAUDE.md`
- 对 hooks 与 OpenClaw 跨会话能力增加“默认保守”的使用约束

同时新增：

- `self-improving-agent/README.md`
- `self-improving-agent/references/hooks-setup.md` 的安全补充
- `self-improving-agent/references/openclaw-integration.md` 的本地副本与脱敏补充

### 5. 仓库级协作文档补充

新增两个顶层文档：

- `AGENTS.md`
- `SKILL_USE_GUIDE.md`

其中：

- `AGENTS.md` 主要约束语言、沟通方式、风险确认、系统排查原则、记忆治理与本地技能维护规则
- `SKILL_USE_GUIDE.md` 主要沉淀 Skill 设计与使用最佳实践，偏方法论和团队规范

这两份文档对后续 AI Agent 在本仓库内的行为一致性有明显帮助。

## 本次补充修复

在检查更新时，发现仓库自带的 `.system/skill-creator/scripts/quick_validate.py` 存在两个会阻断当前提交质量的问题：

1. 在 Windows 上默认按系统编码读文件，校验 UTF-8 技能文档时会触发 `UnicodeDecodeError`
2. 对 frontmatter 的允许字段过严，无法通过新增 `obsidian-cli` 中常见的可选字段（如 `version`、`author`、`tags`、`triggers`）

因此本次额外补了两项修复：

- 修改 `quick_validate.py`，显式使用 `utf-8-sig` 读取 `SKILL.md`
- 放宽允许的 frontmatter 可选字段集合

并新增回归测试：

- `.system/skill-creator/tests/test_quick_validate.py`

覆盖场景：

- UTF-8 中文技能文档可被正常校验
- 常见可选 frontmatter 字段可通过校验
- 未知字段仍会被拦截

## 已执行验证

### 1. 回归测试

执行命令：

```powershell
python -m unittest discover -s .system\skill-creator\tests -p test_quick_validate.py -v
```

结果：

- 3 个测试全部通过

### 2. 技能快速校验

执行命令：

```powershell
python .system\skill-creator\scripts\quick_validate.py cf-quant-web
python .system\skill-creator\scripts\quick_validate.py self-improving-agent
python .system\skill-creator\scripts\quick_validate.py .system\skill-creator
python .system\skill-creator\scripts\quick_validate.py .system\skill-installer
python .system\skill-creator\scripts\quick_validate.py obsidian-cli
```

结果：

- 上述 5 个技能目录均返回 `Skill is valid!`

## 风险与后续建议

当前已完成的是“本次变更涉及目录”的针对性校验，不是整仓全量审计。

建议后续可继续做两件事：

1. 增加对全仓所有 `SKILL.md` 的批量校验脚本，避免只靠单目录手动检查
2. 单独评估根目录 `README.md` 的编码格式是否需要统一为 UTF-8，降低跨平台查看和编辑摩擦

## 结论

本次更新整体方向清晰，重点集中在：

- 技能工程化
- 本地优先与安全收敛
- 文档化约束增强
- 验证链补齐

在补上 `quick_validate.py` 兼容性修复后，这批改动已经具备可提交条件。
