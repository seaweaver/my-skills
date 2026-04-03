# GitHub Sync Design

**目标**

创建一个名为 `github-sync` 的 skill，供 nanobot 在固定仓库列表上执行批量 Git 同步。第一版面向本机固定仓库，不做外部配置系统，不做交互式确认。

**适用场景**

- 多个本地 Git 仓库的定时自动提交与推送
- 批量检查仓库是否有变更
- 需要统一最终汇总报告，而不是逐仓库长日志

**职责边界**

- 输入：脚本中写死的仓库绝对路径列表
- 处理：逐仓库检查、提交信息生成、提交、推送、结果汇总
- 输出：一份简洁总报告

**明确不做**

- `reset / rebase / merge / stash`
- 冲突修复
- 远程仓库地址修改
- 交互式确认
- 动态仓库配置系统

**目录结构**

```text
github-sync/
├── SKILL.md
├── scripts/
│   └── sync_repos.ps1
├── references/
│   └── report-format.md
└── assets/
    └── repo-list.example.txt
```

**执行流程**

每个仓库按以下顺序执行：

1. 路径存在性检查
2. Git 仓库有效性检查
3. 安全状态检查
4. 变更检查
5. 大文件检查
6. 生成单行 commit message
7. `git add --all`
8. `git commit -m`
9. `git push`
10. 记录结果

**失败隔离**

- 单仓库失败不得中断整批
- 每个仓库在独立的错误处理块中执行
- 最终统一输出成功、跳过、失败的汇总

**提交信息策略**

采用混合式骨架摘要：

- 骨架来源限制为：
  - `git status --short`
  - `git diff --name-status`
  - `git diff --stat`
- 只允许根据文件类型、主要目录、增删改情况生成单行消息
- 信息不足时降级到：`chore: sync local changes`

**报告格式**

最终报告尽可能简洁：

- `Summary`：`total / succeeded / skipped / failed`
- `Succeeded`：`repo | branch | message | hash`
- `Failed`：`repo | stage | error`
- `Skipped`：默认只输出数量，不展开明细

**nanobot 调用方式**

```text
Run the github-sync skill for the configured repositories.
Return only the final summary report.
```

**固定仓库列表**

- `D:\Dropbox\Project\my-skills`
- `D:\iCloud\iCloudDrive\iCloud~md~obsidian\iCloudNote`
- `D:\Dropbox\Project\cf_quant`
- `D:\Dropbox\Project\cf_quant_web`
- `D:\Dropbox\Project\cf_quant_weixin`
- `D:\Dropbox\Project\data_project`
