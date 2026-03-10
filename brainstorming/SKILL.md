---
name: Brainstorming Ideas Into Designs 将想法转化为设计
description: 运用苏格拉底式方法进行互动式创意提炼，以形成完整设计方案
when_to_use: 当合作伙伴描述任何功能或项目创意时，在编写代码或实施方案之前
version: 2.2.0
---
# Brainstorming Ideas Into Designs

## Overview

通过结构化提问和替代方案探索，将初步构想转化为完整设计方案

核心原则：通过提问理解需求、探索替代方案、逐步呈现设计方案以供验证

开始前声明："我正在使用头脑风暴技能，将您的想法细化为设计方案。"

## 流程

### Phase 1: Understanding
- Ask ONE question at a time to refine the idea  
    每次只提一个问题来完善想法
- Prefer multiple choice when possible  
    尽可能提供多项选择
- Gather: Purpose, constraints, success criteria  
    收集：目的、限制条件、成功标准

### Phase 2: Exploration
- Propose 2-3 different approaches  
    提出 2-3 种不同的方案
- For each: Core architecture, trade-offs, complexity assessment  
    针对每种方案：核心架构、权衡取舍、复杂度评估
- Ask your human partner which approach resonates  
    询问你的合作伙伴哪种方案最合适

### Phase 3: Design Presentation
- Present in 200-300 word sections  
    以 200-300 字为单位进行呈现
- Cover: Architecture, components, data flow, error handling, testing  
    封面：架构、组件、数据流、错误处理、测试
- Ask after each section: "Does this look right so far?"  
    每个部分后询问："目前看起来正确吗？"

### Phase 4: Planning Handoff

询问："准备好创建实施计划了吗？"

当你的合作伙伴确认时（任何肯定回应）：

- 宣布：“我正在使用写作计划技能来制定实施方案。”
- 计划的标题要求：每个计划都必须以此开头
```
# [Feature Name] Implementation Plan

**Goal:** [One sentence describing what this builds]

**Architecture:** [2-3 sentences about approach]

**Tech Stack:** [Key technologies/libraries]

---
```

- 通过obsidian skill 将计划输出到笔记库的Outbox目录下

## 何时需要回顾早期阶段

**You can and should go backward when:**
**在以下情况下，你可以且应该返回之前的阶段：**
- Partner reveals new constraint during Phase 2 or 3 → Return to Phase 1 to understand it  
    合作伙伴在第二阶段或第三阶段提出新的限制条件 → 返回第一阶段以理解这些限制
- Validation shows fundamental gap in requirements → Return to Phase 1  
    验证显示需求存在根本性差距 → 返回第一阶段
- Partner questions approach during Phase 3 → Return to Phase 2 to explore alternatives  
    在第三阶段采用伙伴提问法 → 返回第二阶段探索替代方案
- Something doesn't make sense → Go back and clarify  
    某些环节不合逻辑 → 返回并澄清问题

**Don't force forward linearly** when going backward would give better results. 
当回溯能带来更好结果时，不要强行线性推进。

## Remember
- One question per message during Phase 1  
    第一阶段中每条消息只提一个问题
- Apply YAGNI ruthlessly  严格遵循 YAGNI 原则
- Explore 2-3 alternatives before settling  
    在确定方案前，先探索 2-3 种备选方案
- Present incrementally, validate as you go  
    逐步呈现，边做边验证
- Go backward when needed - flexibility > rigid progression  
    必要时可回溯调整——灵活性优于僵化推进
- Announce skill usage at start  
    在开始时声明技能使用