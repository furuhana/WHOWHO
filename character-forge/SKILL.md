---
name: character-forge
description: Modular character generation pipeline for creating stylized animation-ready human characters with Chinese-readable user-facing outputs. Use when Codex needs to generate a character profile, coordinate the 大门, 伯乐, 三宅, 托尼, 黑墙, and 阿佐特 modules, audit role/outfit/grooming consistency, avoid forbidden occupation/material directions, and produce final English image-generation prompts plus Chinese summaries.
---

# Character Forge

## Overview

Use this skill as the mother dispatch console for a modular character generation system. Generate one character by running the modules in order, reporting progress after each module, and preserving a structured character record.

Default scope: build the character, audit it, produce image-generation prompts, call Image Gen with the configured reference image, then run a post-generation visual audit unless the user explicitly asks for text-only output. Do not try to create exhaustive lore, relationships, or environments unless the user asks.

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
大门 -> 伯乐 -> 三宅 -> 托尼 -> 黑墙 -> 阿佐特 -> 图像生成 -> 成图审核
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
[图像生成] 已发送参考图并调用 Image Gen
[成图审核] 审核通过
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

Black-market inventory is enabled by default whenever the shelf exists. When the user provides a `黑商货单`, explicitly asks to use `@黑商` inventory, or `black-market/inventory.md` exists in the workspace, treat it as active external stock for the relevant modules. It is still subordinate to Blackwall safety and character fit, but the matching module must check it before falling back to the normal library.

Read only `正式入库` items from black-market stock. Use only each item's `名称`, `描述`, and `标签`. Never read or reconstruct `现场验货`, `常规描述`, raw reference-image analysis, makeup, facial features, complexion, or face-centered aesthetic judgments.

Use black-market stock only in modules that own the matching domain:

- San Zhai may use clothing, footwear, accessories, props, materials, colors, layering, or outfit relationships. By default, San Zhai should directly try `单品货` first and integrate compatible individual assets into the current job outfit; use `套装货` only when a complete outfit naturally fits the already selected occupation or the user explicitly asks for a whole outfit.
- Tony may use hairstyle stock for `hairstyle` and eyebrow stock for `eyebrows` only.
- Tony must apply hairstyle cooldown when selecting either black-market hairstyle stock or normal grooming-library hairstyles: never repeat the immediately previous generated hairstyle unless explicitly requested, hard-exclude the last 3 used hairstyles when alternatives exist, and strongly downweight the last 10.

Use expression and pose stock only during Azoth prompt synthesis. Keep expression stock separate from face shape, features, or grooming; keep pose stock separate from outfit, anatomy redesign, multiple poses, character sheets, or background action.

Black-market stock must not influence occupation selection. Bo Le chooses the occupation first from the jobs library using user constraints and balanced random selection. The random draw is authoritative when the user does not specify an occupation: stats may explain and flavor the selected job, but they must not reroll it toward a more compatible role such as wedding photographer. San Zhai may then adapt compatible styling stock to that chosen job, but it must not change the job to match a better-stocked outfit.

## Black-Market Opening 1.0

When black-market formal stock is available in the conversation, when the shelf exists, or when the user explicitly asks to use black-market inventory, the mother pipeline should treat it as a small shop that relevant modules must visit at their own step:

- 三宅：during work-outfit design, check formal styling stock for clothing, footwear, accessories, carried props, worn props, materials, color relationships, and layering. Default to `单品货` selection; only use `套装货` when the whole outfit fits the locked occupation.
- 托尼：during head styling, check formal hairstyle stock for `hairstyle` and formal eyebrow stock for `eyebrows` only. Do not use black-market stock for beard, face shape, eye shape, facial features, makeup, complexion, or attractiveness.
- 阿佐特：during prompt synthesis, check formal pose stock for body angle, weight shift, hand placement, gesture, prop interaction, and action freeze-frame; then check formal expression stock for gaze, facial tension, mouth-corner state, emotional layer, and acting state. Pose should be selected first, expression second. Keep expression stock separate from face shape, grooming, and appearance judgments.
- 黑墙：audit any selected black-market stock after integration. Reject or reroute if the stock introduces forbidden directions, face-centered appearance judgments, makeup, complexion, dirty materials, noisy fabric texture, or any conflict with the fixed body and single-character prompt rules.

All modules must read only `正式入库`. `现场验货`, `常规描述`, source filenames, paths, and raw image analysis are never valid stock for the mother pipeline.

## Black-Market Shelf 1.2

Before running the module pipeline, check whether `black-market/inventory.md` exists as the shelf index. If it exists, load external stock from the matching lane file before the normal library by default, and read only each file's `正式入库` section. The user no longer needs to say `@黑商` for the mother pipeline to shop from stock.

Shelf routing:

- 三宅 must check `black-market/inventory/styling.md` `造型库存 / 单品货` first for outfit components, clothing, footwear, accessories, props, materials, color relationships, and layering. It may then check `造型库存 / 套装货` only when no direct single item fits or a complete outfit is naturally compatible.
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
使用策略：<完整套装继承 / 局部单品借用 / 只继承搭配方法 / 未使用>
取货理由：<why this stock fits the current character>
继承优点：<silhouette, color, material, layering, or role-fit strengths inherited from the selected stock>
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

`黑商取货` is an inventory-level reasoning log. It may compare only formal stock fields such as `名称`, `类别`, `描述`, `标签`, and `包含单品`. For 三宅 styling stock, it may also summarize inherited outfit strengths derived from those formal fields, such as silhouette, color, material, layering, and role-fit logic. It must not mention source images, filenames, paths, `现场验货`, `常规描述`, raw image analysis, facial features, complexion, makeup, attractiveness judgments, or identity/story inferred from the source.

## Output

Return these sections for each completed character:

1. 调度日志
2. 角色档案
3. 黑墙审核
4. 英文提示词
5. 中文提示词
6. 黑商商机
7. 图像生成
8. 成图审核

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

## Image Generation Tail Step

After preserving all text sections above, the mother pipeline must run one final `图像生成` step unless the user explicitly asks for text only.

Use the built-in Image Gen path. Before every Image Gen call, load both local reference images with `view_image` so they are visible in the conversation context, then send them with the final English prompt from `英文提示词`:

```text
Input image 1 / style reference:
E:\sw\eagle\BaiduSyncdisk\A.library\images\MKXONR4EBPO4Z.info\0_0.png

Input image 2 / body reference:
E:\wk\GitHub\WHOWHO\character-forge\references\assets\width_first_body_reference.png
```

Treat `Input image 1` as the style and rendering reference only, not as identity, costume, face, exact character copying, or body-proportion authority. Treat `Input image 2` as the body-proportion and muscle-mass reference only, not as identity, costume, face, hairstyle, or exact character copying. The generated image must follow the current character's approved prompt while matching these reference-image qualities as closely as the model allows:

- clean Japanese TV anime cel-shading, crisp dark outer linework, tidy internal contour lines, smooth flat color blocks, soft but controlled shadow shapes, and minimal background noise
- width-first grounded body proportion, around 6.2-6.6 heads tall, dramatically broad super-heavyweight fighting-game mass, compact head, short thick neck buried between huge traps, enormous deltoids, huge chest shelf, thick barrel ribcage, giant upper arms, huge forearms, oversized heavy hands, very thick thighs, strong calves, large heavy boots or feet, and stable full-body presentation. The first read must be extreme horizontal muscle mass rather than height.
- torso anatomy expressed through large simplified muscle masses and clean stylized shape lines, with the pectoral shelf, center chest divide, stacked abdominal blocks, and side-ab planes visibly pressing through fitted tank tops, fitted T-shirts, or tucked undershirts; not realistic skin texture or painterly rendering
- single full-body character, centered on a flat pure white background, with no scene, props display, panels, turnarounds, gradient, vignette, aura, halo, glow, or extra characters
- one single soft neutral key light from upper left, mostly clean white with only a faint warm daylight tendency; very narrow pale cream-white painted cel-shading lit-edge highlights only on the light-facing silhouette and surfaces; no second rim light, no colored dual rim light, and no glow around the character

Add this Image Gen prompt wrapper around the final English prompt:

```text
Use Input image 1 as the mandatory visual reference for rendering style, full-body framing, line weight, flat cel-shading, tidy contour lines, smooth color blocks, and clean white-background presentation. Use Input image 2 as the mandatory visual reference for width-first grounded super-heavyweight body proportion, simplified muscle anatomy, extreme horizontal muscle mass, 6.2-6.6 head proportions, very wide shoulders, huge traps, huge chest and back, giant arms, oversized hands, very thick thighs, and large heavy feet. Keep the new character's identity, outfit, job, grooming, pose, and expression from the prompt below. Preserve one single soft neutral upper-left key light with very narrow pale cream-white painted cel-shading lit-edge highlights only on the light-facing silhouette and surfaces. Keep the background flat pure white with no gradient, vignette, aura, halo, glow, visible light source, or scenery. Do not copy either reference character's exact face, clothing, identity, or any overly tall vertical proportion.

<final English prompt>
```

Add this log line after the call:

```text
[图像生成] 已发送参考图并调用 Image Gen
```

If Image Gen is unavailable or fails, keep all text output unchanged and add `图像生成：未完成，原因：<brief reason>` instead of retrying with a different generation path.

## Post-Generation Visual Audit

After every successful Image Gen call, inspect the generated image before marking the character complete. The audit is mandatory for all non-text-only character generations.

Check these items:

- `画风一致性`: clean Japanese TV anime cel-shading, crisp dark outer linework, flat color blocks, tidy shadow shapes, flat pure white background, and no painterly, semi-realistic, gritty, 3D, fashion-illustration, or noisy-texture drift.
- `光源一致性`: one single soft neutral upper-left key light, natural and restrained; narrow pale cream-white lit-edge highlights should appear only on the light-facing silhouette and surfaces as painted cel-shading accents. Reject obvious dual-sided rim lights, blue-red colored rim lights, neon glow, aura, halo, visible light source, gray background gradient, or vignette.
- `体型一致性`: male characters must remain width-first, grounded, very broad, thick, heavy, and powerful; reject if the result becomes slim, narrow-shouldered, lanky, long-legged, fashion-model-like, lightly athletic, small-armed, small-handed, normally 7-head heroic, merely tall and muscular, or has a shrunken/over-elongated body.
- `体块一致性`: shoulders, chest, traps, neck, back width, arms, forearms, hands, waist, thighs, calves, and boots/feet must visibly carry super-heavyweight mass. The silhouette should read like a wall of muscle with shoulder span much wider than hips, short thick neck, giant arms, huge forearms, oversized hands, very thick thighs, and large heavy feet. The torso must show large simple pectoral and abdominal masses pressing through the fitted base layer when clothing allows it. For white tank tops, fitted T-shirts, or tucked undershirts, the pectoral shelf, center chest divide, stacked abdominal blocks, and side-ab planes must be clear; a smooth torso shirt fails.
- `角色一致性`: occupation, outfit, grooming, pose, expression, selected black-market stock, and single-character white-background framing must match the approved prompt.
- `禁区复查`: reject multiple characters, character sheets, turnarounds, panels, callout boxes, background scenes, dirty or oily clothing, dense prints, micro-weave/noisy fabric detail, realistic skin texture, or forbidden occupation drift.

If the audit passes, add:

```text
[成图审核] 审核通过
成图审核：通过。画风、体型、职业识别、单人白底构图均符合。
```

If the audit fails, do not claim the character is complete. Add:

```text
[成图审核] 未通过：<brief reason>
```

Then run one corrective Image Gen attempt using the same approved character record, but strengthen only the failed constraints. For body failures, the corrective prompt must explicitly prioritize `width-first super-heavyweight fighting-game anime body`, `around 6.2-6.6 heads tall`, `dramatically wider and thicker than a normal tall hero`, `shoulder span much wider than hips`, `short thick neck buried between huge traps`, `enormous rounded deltoids`, `huge chest shelf`, `thick barrel ribcage`, `deep pectoral shelf`, `visible center chest valley`, `large stacked blocky abs pressing through the fitted shirt`, `thick oblique side planes`, `giant upper arms`, `huge forearms`, `oversized heavy hands`, `very thick thighs`, `strong calves`, `large heavy feet`, and `wall of muscle silhouette`, and must explicitly avoid `slim`, `narrow shoulders`, `long legs`, `7-head tall normal hero proportions`, `fashion-model proportions`, `smooth torso shirt`, `lightly athletic build`, and `merely tall and muscular`.

After the corrective attempt, audit again. If it still fails, show the best image but clearly write:

```text
成图审核：未通过，原因：<brief reason>。已保留当前生成结果，建议下一轮使用更强参考或更硬体型提示词。
```
