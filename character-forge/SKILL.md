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

## Black-Market Stock

When the user provides a `黑商货单` or explicitly asks to use `@黑商` inventory, treat it as active external stock for the relevant modules. It is still subordinate to Blackwall safety and character fit, but the matching module must check it before falling back to the normal library.

Read only `正式入库` items from black-market stock. Use only each item's `名称`, `描述`, and `标签`. Never read or reconstruct `现场验货`, `常规描述`, raw reference-image analysis, makeup, facial features, complexion, or face-centered aesthetic judgments.

Use black-market stock only in modules that own the matching domain:

- San Zhai may use clothing, footwear, accessories, props, materials, colors, layering, or outfit relationships.
- Tony may use hairstyle stock for `hairstyle` and eyebrow stock for `eyebrows` only.

Use expression and pose stock only during Azoth prompt synthesis. Keep expression stock separate from face shape, features, or grooming; keep pose stock separate from outfit, anatomy redesign, multiple poses, character sheets, or background action.

## Black-Market Opening 1.0

When black-market formal stock is available in the conversation, or when the user explicitly asks to use black-market inventory, the mother pipeline should treat it as a small shop that relevant modules must visit at their own step:

- 三宅：during work-outfit design, check formal styling stock for complete outfits, clothing, footwear, accessories, carried props, worn props, materials, color relationships, and layering.
- 托尼：during head styling, check formal hairstyle stock for `hairstyle` and formal eyebrow stock for `eyebrows` only. Do not use black-market stock for beard, face shape, eye shape, facial features, makeup, complexion, or attractiveness.
- 阿佐特：during prompt synthesis, check formal pose stock for body angle, weight shift, hand placement, gesture, prop interaction, and action freeze-frame; then check formal expression stock for gaze, facial tension, mouth-corner state, emotional layer, and acting state. Pose should be selected first, expression second. Keep expression stock separate from face shape, grooming, and appearance judgments.
- 黑墙：audit any selected black-market stock after integration. Reject or reroute if the stock introduces forbidden directions, face-centered appearance judgments, makeup, complexion, dirty materials, noisy fabric texture, or any conflict with the fixed body and single-character prompt rules.

All modules must read only `正式入库`. `现场验货`, `常规描述`, source filenames, paths, and raw image analysis are never valid stock for the mother pipeline.

## Black-Market Shelf 1.2

Before running the module pipeline, check whether `black-market/inventory.md` exists as the shelf index. When the user asks to use black-market inventory, load external stock from the matching lane file before the normal library, and read only each file's `正式入库` section.

Shelf routing:

- 三宅 must check `black-market/inventory/styling.md` `造型库存 / 套装货` and `造型库存 / 单品货` for outfit, clothing, footwear, accessories, props, materials, color relationships, and layering.
- 托尼 must check `black-market/inventory/hairstyle.md` `发型库存` for hairstyle only and `black-market/inventory/eyebrow.md` `眉型库存` for static eyebrow shape only.
- 阿佐特 must check `black-market/inventory/pose.md` `姿势库存` for full-body pose and action language when the shelf exists, then check `black-market/inventory/expression.md` `表情库存` for expression and acting language only.
- 黑墙 must audit any selected shelf item using the same black-market rules.

If the shelf is empty, missing, or has no matching lane, say briefly in the dispatch log that no matching black-market stock was available, then continue with the normal libraries. If matching stock exists but a module rejects it, the module must name the rejected stock and give a short fit reason.

When black-market inventory is enabled, include a `黑商取货` note in the dispatch log or character record for each relevant module:

```text
[三宅] 黑商取货：
货道：<lane file and shelf>
候选：<1-3 formal stock names>
使用：<selected formal stock name or 未使用>
取货理由：<why this stock fits the current character>
未选理由：<why the other candidates were not selected>

[托尼] 黑商取货：
货道：<lane file and shelf>
候选：<1-3 formal stock names>
使用：<selected formal stock name or 未使用>
取货理由：<why this stock fits the current character>
未选理由：<why the other candidates were not selected>

[阿佐特] 黑商取货：
货道：<lane file and shelf>
候选：<1-3 formal stock names>
使用：<selected formal stock name or 未使用>
取货理由：<why this stock fits the current character>
未选理由：<why the other candidates were not selected>

[阿佐特] 表情姿势搭配：
组合：<pose stock name or 无> + <expression stock name or 无>
组合理由：<why the expression supports the selected full-body pose>
```

`黑商取货` is an inventory-level reasoning log. It may compare only formal stock fields such as `名称`, `类别`, `描述`, `标签`, and `包含单品`. It must not mention source images, filenames, paths, `现场验货`, `常规描述`, raw image analysis, facial features, complexion, makeup, attractiveness judgments, or identity/story inferred from the source.

## Output

Return these sections for each completed character:

1. 调度日志
2. 角色档案
3. 黑墙审核
4. 英文提示词
5. 中文提示词
6. 黑商商机

In `角色档案`, use Chinese field labels such as `名字`, `年龄`, `国籍`, `体型`, `性格`, `贫富值`, `危险值`, `欲望值`, `执行力`, `社交力`, `职业`, `帮派`, `工作服`, `发型`, `眉型`, `胡子`, and `脸型`.

Keep generated content grounded in daily-life occupations and clean, stylized animation character design.

## Black-Market Opportunities

After the final Chinese prompt, output `黑商商机` as a non-inventory procurement section.

Rules:

- Always provide exactly 10 numbered ideas when completing a character.
- These are ideas only. Do not write them to any `black-market/inventory/*` file and do not call them `正式入库`.
- Ideas should be inspired by the current character's occupation, gang, outfit, hairstyle, expression, stats, selected black-market stock, or gaps noticed during generation.
- Ideas may propose future styling, hairstyle, eyebrow shape, pose, expression, accessory, prop, material, color, layering, or full outfit stock.
- Each idea must name a suggested stock category such as `套装货`, `单品货`, `发型库存`, `眉型库存`, `姿势库存`, or `表情库存`.
- Keep each idea concrete enough that the user could search references or ask `@黑商` to turn it into stock later.
- Never include source image names, file paths, `现场验货`, `常规描述`, raw image analysis, makeup, facial features, face shape, complexion, skin texture, attractiveness judgments, or identity/story copied from a source.
- If an idea is based on a missing fit, phrase it as a procurement opportunity, not as a failed generation.

Use this shape:

```text
黑商商机
1. <category>: <concrete procurement idea and why it fits this character or occupation>
...
10. <category>: <concrete procurement idea and why it fits this character or occupation>
```
