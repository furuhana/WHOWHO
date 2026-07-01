# Pipeline

## Order

Run each module in strict order:

```text
1. 大门 / Da Men
2. 伯乐 / Bo Le
3. 三宅 / San Zhai
4. 托尼 / Tony
5. 缪斯 / Muse
6. 黑墙 / Blackwall
7. 阿佐特 / Azoth
8. 蜃楼 / Mirage, when available and not explicitly skipped
9. 图像生成 / Image Gen
10. 成图审核 / Post-Generation Visual Audit
```

Use the Chinese names in user-facing responses. The English aliases exist only to keep file names and internal references stable.

## Progress Logging

Report progress as each module completes. Keep logs short and visible to the user.

Use these canonical states:

```text
[母体] 启动角色生成流程
[大门] 已生成基础角色
[伯乐] 已匹配职业与帮派
[三宅] 已匹配工作服
[托尼] 已匹配头脸造型
[缪斯] 审核中
[缪斯] 审核通过
[缪斯] 勉强通过：<brief outfit issue and accepted reason>
[缪斯] 未通过：<reason>
[黑墙] 审核中
[黑墙] 审核通过
[黑墙] 未通过：<reason>
[母体] 打回：<中文模块名列表>
[阿佐特] 已生成英文提示词与中文提示词
[蜃楼] 已合成浮动底座
[图像生成] 已发送参考图并调用 Image Gen
[成图审核] 审核通过
[母体] 完成
```

## Reroute Logic

If 缪斯 finds outfit-quality issues, reroute the smallest possible set of modules before Blackwall:

- 工作服、外层、层次、鞋履、饰品、包具、道具、色彩、材质、轮廓问题：打回三宅。
- 仅发型与穿搭协调问题：打回托尼。
- 仅提示词表达问题：设计通过后交给阿佐特写清楚。

Run 缪斯 again after rerouted modules finish. Continue to 黑墙 only when 缪斯 passes or explicitly accepts a minor issue as `勉强通过`.

If 黑墙 finds issues, reroute the smallest possible set of modules:

- 职业或帮派问题：打回伯乐，必要时再跑三宅、托尼。
- 工作服问题：打回三宅。
- 发型、胡子或脸型问题：打回托尼。
- 仅提示词问题：黑墙通过后打回阿佐特。

Run 缪斯 again after rerouted modules finish if outfit or grooming changed, then run 黑墙 again. Continue only when 黑墙 passes.

## Prompt Composition

Azoth drafts variable prompt content as dynamic slots, then assembles `prompt_en` with fixed blocks from `references/prompt_blocks/`. Fixed blocks cover the body standard, rendering style, lighting and white background, global negative constraints, sock/belt guards, Mirage platform template, and Image Gen wrapper. Insert fixed blocks verbatim unless the user explicitly changes that constraint.

The fixed blocks do not count toward dynamic-section length targets. Do not compress `OUTFIT_DYNAMIC`, `ACCESSORY_DYNAMIC`, `GROOMING_DYNAMIC`, `POSE_DYNAMIC`, or `EXPRESSION_DYNAMIC` because the fixed prefix, suffix, or wrapper is long.

## Final Response Shape

Use this final structure. Keep headings and labels in Chinese except the English prompt body itself:

```text
调度日志
...

角色档案
...

缪斯审核
...

黑墙审核
...

英文提示词
...

中文提示词
...

黑商商机
...

图像生成
...

成图审核
...
```

## Image Generation Tail Step

After all previous text sections are produced, keep them intact and run one final Image Gen step unless the user explicitly asks for text-only output.

Before every Image Gen call, load both local reference images with `view_image` so they are visible in the conversation context, then attach them as `Input image 1` and `Input image 2`:

```text
Input image 1 / style reference:
character-forge/references/assets/style_reference.png

Input image 2 / body reference:
character-forge/references/assets/width_first_body_reference.png
```

Resolve both paths relative to the workspace root when possible. If the agent is running from inside `character-forge/`, use `references/assets/style_reference.png` and `references/assets/width_first_body_reference.png`. Do not fall back to external sync folders or Windows drive paths unless the local asset is genuinely missing.

Use the final English prompt as the generation prompt, wrapped with the exact block in `references/prompt_blocks/imagegen-wrapper.md`:

```text
<the exact wrapper from references/prompt_blocks/imagegen-wrapper.md>
```

Input image 1 must guide clean Japanese TV anime cel-shading, crisp dark outer linework, tidy internal contour lines, smooth flat color blocks, soft controlled shadow shapes, centered full-body framing, and pure white background. Input image 2 must guide width-first super-heavyweight mass, oversized arms and hands, heavy lower body, compact proportions, and muscle-block readability. Neither reference may override the current character's approved identity, outfit, grooming, pose, expression, or source character separation. Face shape and facial proportions may be style-adjacent, but must resolve as a new person rather than a clone or recognizable match to either reference face.

If Image Gen succeeds, show the generated image under `图像生成`. If Image Gen is unavailable or fails, preserve the text output and write `图像生成：未完成，原因：<brief reason>`.

## Post-Generation Visual Audit

After every successful Image Gen call, inspect the generated image before completing the character.

Mandatory checks:

- Style: must match clean Japanese TV anime cel-shading, crisp dark outer linework, flat color blocks, tidy internal contour lines, controlled shadows, and pure white background. Fail if it drifts into painterly, semi-realistic, gritty, 3D, fashion-illustration, or noisy texture rendering.
- Body: male characters must remain width-first, grounded, and visually extremely broad, thick, heavy, and powerful. Fail if the result becomes slim, narrow-shouldered, lanky, long-legged, fashion-model-like, lightly athletic, small-armed, small-handed, vertically stretched, normally 7-head heroic, or merely tall and muscular.
- Mass: shoulders, chest, traps, neck, back width, arms, forearms, hands, waist, thighs, calves, and boots/feet must visibly carry super-heavyweight mass. The silhouette should read like a wall of muscle with shoulder span much wider than hips, short thick neck, giant arms, huge forearms, oversized hands, very thick thighs, and large heavy feet. When a fitted base layer is visible, the torso must show large simple pectoral and abdominal masses pressing through it, not ordinary wrinkles. The pectoral shelf, center chest divide, stacked abdominal blocks, and side-ab planes must be readable; fail smooth white tank tops or T-shirts that hide the chest and abdomen.
- Character: occupation, outfit, grooming, pose, expression, selected black-market stock, single-character framing, and white background must match the approved prompt.
- Forbidden outputs: fail multiple characters, multiple poses, turnarounds, character sheets, panels, callout boxes, background scenes, dirty/oily/stained clothing, dense prints, micro-weave/noisy fabric detail, realistic skin texture, or forbidden occupation drift.

If the audit passes, add this log and final section:

```text
[成图审核] 审核通过
成图审核：通过。画风、体型、职业识别、单人白底构图均符合。
```

If the audit fails, add:

```text
[成图审核] 未通过：<brief reason>
```

Then run one corrective Image Gen attempt using the same approved character record. Strengthen only the failed constraints. For body failures, the corrective prompt must explicitly prioritize `width-first super-heavyweight fighting-game anime body`, `around 6.2-6.6 heads tall`, `dramatically wider and thicker than a normal tall hero`, `shoulder span much wider than hips`, `short thick neck buried between huge traps`, `enormous rounded deltoids`, `huge chest shelf`, `thick barrel ribcage`, `deep pectoral shelf`, `visible center chest valley`, `large stacked blocky abs pressing through the fitted shirt`, `thick oblique side planes`, `giant upper arms`, `huge forearms`, `oversized heavy hands`, `very thick thighs`, `strong calves`, `large heavy feet`, and `wall of muscle silhouette`, and must explicitly avoid `slim`, `narrow shoulders`, `long legs`, `7-head tall normal hero proportions`, `fashion-model proportions`, `smooth torso shirt`, `lightly athletic build`, and `merely tall and muscular`.

After the corrective attempt, audit again. If it still fails, show the best image but clearly write:

```text
成图审核：未通过，原因：<brief reason>。已保留当前生成结果，建议下一轮使用更强参考或更硬体型提示词。
```
