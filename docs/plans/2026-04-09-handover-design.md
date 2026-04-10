# Handover Skill Design

**目标**

创建一个名为 `handover` 的 skill，用于在上下文接近耗尽或用户显式要求时，生成并覆盖项目根目录 `HANDOVER.md`，同时做轻量知识沉淀，并为新 session 提供最短可执行接力入口。

**核心模式**

1. `write`
   - 用于当前 session 即将结束时
   - 不读取旧 `HANDOVER.md` 作为生成输入
   - 基于当前 session 上下文、工作区状态、关键文件和 Git 状态生成新的 handover
   - 滚动覆盖 `HANDOVER.md`
   - 视内容质量决定是否更新 `AGENTS.md` 与 `README.md`

2. `resume`
   - 用于新 session 接力
   - 读取 `AGENTS.md` 与 `HANDOVER.md`
   - 输出接力摘要和下一步
   - 默认不重写文件

3. `auto`
   - 优先尊重显式命令
   - 无显式命令时，若线程已有明显工作产出则判定为 `write`
   - 若线程接近冷启动且存在 `HANDOVER.md`，则判定为 `resume`
   - 若信号冲突，则只问一句短确认

**文件落点**

- `HANDOVER.md`
  - 只保留当前接力所需的最新状态
  - 每次写入滚动覆盖
- `AGENTS.md`
  - 只写高置信度、长期稳定、可复用规则
- `README.md`
  - 只写项目长期有用的设计、实现或操作说明
  - 通过受控标记块维护，避免污染正文

**实现方式**

- `SKILL.md` 负责触发条件、模式判断、更新边界、输出格式
- skill 本身负责根据当前线程上下文完成总结、治理和写入动作
- 项目快照、`HANDOVER.md` 覆盖写入、`AGENTS.md` 与 `README.md` 受控块更新，统一由模型直接读文件、读 Git 状态并使用 `apply_patch` 完成

**2026-04-10 修订**

- 去掉 `handover` 对 `python .\handover\main.py` 的运行时依赖
- 改为纯 `SKILL.md` 工作流，避免 agent 在不同项目里误判 `main.py` 路径
- 删除旧 helper 与测试文件，只保留纯 Markdown skill 结构

**目录结构**

```text
handover/
├── SKILL.md
├── references/
│   └── templates.md
```

**受控标记块**

- `AGENTS.md`
  - `<!-- handover:agents:begin -->`
  - `<!-- handover:agents:end -->`
- `README.md`
  - `<!-- handover:readme:begin -->`
  - `<!-- handover:readme:end -->`

**失败策略**

- 不能确定模式时，不自动覆盖 `HANDOVER.md`
- `resume` 模式缺少 `HANDOVER.md` 时，返回短错误
- `write` 模式更新 README/AGENTS 失败时，不影响 `HANDOVER.md` 生成，但要在输出中明确标注

**验证**

- skill 校验：
  - `python .system\skill-creator\scripts\quick_validate.py handover`
