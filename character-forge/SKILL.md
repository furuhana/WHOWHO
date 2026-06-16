---
name: character-forge
description: Modular character generation pipeline for creating stylized animation-ready human characters with Chinese-readable user-facing outputs. Use when Codex needs to generate a character profile, coordinate the 大门, 伯乐, 三宅, 托尼, 黑墙, and 阿佐特 modules, audit role/outfit/grooming consistency, avoid forbidden occupation/material directions, and produce final English image-generation prompts plus Chinese summaries.
---

# Character Forge

## Overview

Use this skill as the mother dispatch console for a modular character generation system. Generate one character by running the modules in order, reporting progress after each module, and preserving a structured character record.

First version scope: build the character, audit it, and produce image-generation prompts. Do not try to create exhaustive lore, relationships, environments, or images unless the user asks.

## Required Workflow

Read these references before generating a character:

1. `references/pipeline.md` for dispatch order, progress logs, reroutes, and final output.
2. `references/schema.md` for the shared character data shape.
3. `references/damen.md` for base character generation.
4. `references/bole.md` for occupation and gang matching.
5. `references/sanzhai.md` for work outfit matching.
6. `references/tony.md` for hairstyle, beard, and face matching.
7. `references/blackwall.md` for design audit and forbidden directions.
8. `references/azoth.md` for prompt synthesis.

Load library files only when the matching module needs them:

- `references/libraries/jobs.md` for Bo Le.
- `references/libraries/gangs.md` for Bo Le.
- `references/libraries/outfits.md` for San Zhai.
- `references/libraries/grooming.md` for Tony.
- `references/libraries/forbidden.md` for Blackwall.

## Dispatch Rules

Run the modules in this order:

```text
大门 -> 伯乐 -> 三宅 -> 托尼 -> 黑墙 -> 阿佐特
```

Always show user-facing module names and outputs in Chinese. Internal schema keys may stay English for stability, but the final answer must use Chinese labels the user can read at a glance.

Use this dispatch log style:

```text
[母体] 启动角色生成流程
[大门] 已生成基础角色
[伯乐] 已匹配职业与帮派
[三宅] 已匹配工作服
[托尼] 已匹配头脸造型
[黑墙] 审核通过
[阿佐特] 已生成英文提示词与中文提示词
[母体] 完成
```

If Blackwall fails, report the reason, reroute only the named modules, then run Blackwall again before Azoth. Do not continue to Azoth while Blackwall has unresolved issues.

## User-Controlled Library Writes

When proposing new library entries, show them as candidates first. Do not claim they are written into the library unless the user explicitly approves writing them.

Use this format:

```text
[待确认写入]
- 素材库：工作服
- 条目：...
- 原因：...
```

## Output

Return these sections for each completed character:

1. 调度日志
2. 角色档案
3. 黑墙审核
4. 英文提示词
5. 中文提示词

In `角色档案`, use Chinese field labels such as `名字`, `年龄`, `国籍`, `体型`, `性格`, `贫富值`, `危险值`, `欲望值`, `执行力`, `社交力`, `职业`, `帮派`, `工作服`, `发型`, `胡子`, and `脸型`.

Keep generated content grounded in daily-life occupations and clean, stylized animation character design.
