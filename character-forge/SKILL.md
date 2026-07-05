---
name: character-forge
description: Modular character generation pipeline for creating stylized animation-ready human characters with Chinese-readable user-facing outputs. Use when Codex needs to generate a character profile, coordinate the 大门, 伯乐, 三宅, 托尼, 缪斯, 黑墙, and 阿佐特 modules, audit role/outfit/grooming consistency, review outfit quality before Blackwall, avoid forbidden occupation/material directions, and produce final English image-generation prompts plus Chinese summaries.
---

# Character Forge

## Overview

Use this skill as the mother dispatch console for a modular character generation system. Generate one character by running the modules in order, reporting progress after each module, and preserving a structured character record.

Default scope: build the character, audit it, produce image-generation prompts, apply the local Mirage / 蜃楼 floating scene-slice post-processor when available, call Image Gen with the configured reference image, then run a post-generation visual audit unless the user explicitly asks for text-only output. Do not try to create exhaustive lore, relationships, or full environments unless the user asks.

## Default Mirage Policy

When the user asks to create a character and does not explicitly request text-only output, use Mirage / 蜃楼 by default if `mirage/SKILL.md` exists in the workspace. This is not optional and does not require the user to repeat the floating-platform rules.

Mirage runs after Azoth prompt synthesis and before Image Gen. It adds one compact scene-slice paragraph and compact negative constraints: one coherent floating platform, solid themed ground, 2-3 dynamically selected rooted props, naturally broken edges fading into pure white, and no complete background, room, walls, ceiling, full landscape, scattered props, separated prop pack, or floating standalone props.

Mirage must not change the approved character, occupation, body, outfit anchors, black-market stock, hairstyle, eyebrows, pose, expression, or identity. If the user explicitly asks for a plain pure-white character with no platform, skip Mirage for that turn.

## Required Workflow

Read these references before generating a character:

1. `references/pipeline.md` for dispatch order, progress logs, reroutes, and final output.
2. `references/schema.md` for the shared character data shape.
3. `references/damen.md` for base character generation.
4. `references/bole.md` for occupation and gang matching.
5. `references/sanzhai.md` for work outfit matching.
   - When `../garment-grammar/SKILL.md` or workspace `garment-grammar/SKILL.md` exists, San Zhai must use it before designing clothing. It upgrades plain job clothing into no-skirt, no-apron garment construction language and passes professional keywords downstream.
   - When the black-market design grammar exists, San Zhai and all downstream audit/prompt modules should also use:
     - `../black-market/references/designer-methods.md`
     - `../black-market/references/design-operators.md`
     - `../black-market/references/base-garment-prototypes.md`
     - `../black-market/references/outer-shell-prototypes.md`
     - `../black-market/references/structural-events-and-material-behaviors.md`
     - `../black-market/references/pattern-and-cutting.md`
     - `../black-market/references/footwear-accessory-grammar.md`
6. `references/tony.md` for hairstyle, beard, and face matching.
7. `../muse/SKILL.md` or workspace `muse/SKILL.md` when it exists, for outfit and styling quality audit before Blackwall.
8. `references/blackwall.md` for design audit and forbidden directions.
9. `references/azoth.md` for prompt synthesis.
   - When Azoth composes prompts, load only the needed files from `references/prompt_blocks/` for fixed prompt blocks and final Image Gen wrapper assembly.

10. `../mirage/SKILL.md` or workspace `mirage/SKILL.md` when it exists, for default floating scene-slice composition before Image Gen.

Load library files only when the matching module needs them:

- `references/libraries/jobs.md` for Bo Le.
- `references/libraries/gangs.md` for Bo Le.
- `references/libraries/outfits.md` for San Zhai.
- `references/libraries/grooming.md` for Tony.
- `references/libraries/forbidden.md` for Blackwall.

## Dispatch Rules

Run the modules in this order:

```text
大门 -> 伯乐 -> 三宅(+服装语法) -> 托尼 -> 缪斯 -> 黑墙 -> 阿佐特 -> 蜃楼 -> 图像生成 -> 成图审核
```

Always show user-facing module names and outputs in Chinese. Internal schema keys may stay English for stability, but the final answer must use Chinese labels the user can read at a glance.

Use this dispatch log style:

```text
[母体] 启动角色生成流程
[大门] 已生成基础角色
[伯乐] 已匹配职业与帮派
[三宅] 已匹配工作服并应用服装语法
[托尼] 已匹配头脸造型
[缪斯] 审核通过
[黑墙] 审核通过
[阿佐特] 已生成英文提示词与中文提示词
[蜃楼] 已合成浮动底座
[图像生成] 已发送参考图并调用 Image Gen
[成图审核] 审核通过
[母体] 完成
```

If Muse fails, report the reason, reroute only the named modules, then run Muse again before Blackwall. Do not continue to Blackwall while Muse has unresolved outfit-quality issues. If Blackwall fails, report the reason, reroute only the named modules, then run Muse again only when outfit or grooming changed, then run Blackwall again before Azoth. Do not continue to Azoth while Blackwall has unresolved issues.

## Muse / 缪斯 Outfit Audit

When `muse/SKILL.md` exists in the workspace, run 缪斯 after Tony and before Blackwall. This is a trial integration: keep it lightweight, reversible, and subordinate to the mother pipeline.

缪斯 audits whether the outfit and styling read as a high-quality character design. It checks clothing, footwear, accessories, bags, carried or worn props, silhouette, layering, color, material, era, occupation fit, mixed-style control, visual-load distribution, runway-level design references, and animation/concept-art viability.

缪斯 must not evaluate face shape, facial features, complexion, skin texture, beauty, ugliness, makeup, attractiveness, identity, ethnicity, or source-character lore. 缪斯 may mention hairstyle only as outfit coordination.

Use these states in the dispatch log:

```text
[缪斯] 审核中
[缪斯] 审核通过
[缪斯] 勉强通过：<brief outfit issue and accepted reason>
[缪斯] 未通过：<brief reason>
```

If 缪斯 returns `需要重做`, reroute the smallest possible modules:

- outfit, layering, accessories, bag, prop, shoe, color, material, or silhouette issues: 打回三宅.
- hairstyle coordination issue only: 打回托尼.
- prompt wording issue only after design is otherwise approved: allow Blackwall to pass, then let Azoth phrase the design more clearly.

Do not let 缪斯 change the occupation chosen by Bo Le, selected black-market stock provenance, fixed body type, pose, expression, identity, or Blackwall safety rules. If 缪斯 suggests a stronger fashion direction, San Zhai may implement it only through the locked occupation and approved inventory/library materials.

When the design grammar files exist, 缪斯 should also audit whether San Zhai supplied:

- a readable `base_garment_prototype`
- a precise `outer_shell_prototype` when any outer layer exists
- one primary `structural_event` and zero or one supporting `material_behavior`
- `anti_shirt_jacket_default` when any shirt-like layer is present
- a `banned_shape_check` or equivalent proof that no skirt, dress, apron, pinafore, or apron-like lower/front garment was used
- anonymous `designer_method_references`, and optional `designer_prompt_references` only if the user allowed designer-name prompt testing
- concrete `design_operators`
- at least one `panel_paths` entry with start, route, endpoint, and body rule
- a controlled `pattern_strategy`
- visible `craft_boundaries`
- a `body_fit_strategy` that reinforces the WHOWHO width-first body
- a footwear/accessory structure that changes body reading or role readability
- a `complexity_budget` close to large silhouette 60 / medium panels 25 / small craft 10 / pattern-symbol 5
- explicit `design_failure_avoidance`

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

Read only `正式入库` items from black-market stock. Use only each item's formal reusable fields. For most stock this means `名称`, `描述`, and `标签`; for pose stock, Azoth may also use `姿势大类`, `身体朝向`, `重心高度`, `动势强度`, `手部策略`, and `展示风险` for selection, cooldown, and downweighting. Never read or reconstruct `现场验货`, `常规描述`, raw reference-image analysis, makeup, facial features, complexion, or face-centered aesthetic judgments.

Use black-market stock only in modules that own the matching domain:

- San Zhai may use clothing, footwear, accessories, props, materials, colors, layering, or outfit relationships. By default, San Zhai should scan `套装货` first for complete outfit structure, silhouette, layering, value-map logic, and accessory systems; then use `单品货` to adapt, complete, replace, or add individual assets. For the `pants` field, `black-market/inventory/styling/items/bottoms.md` is the canonical black-market leg-system pool: San Zhai must check it every character turn, either select/adapt one bottom item or record why no bottom item fit.
- Tony may use hairstyle stock for `hairstyle` and eyebrow stock for `eyebrows` only.
- Tony must apply grooming cooldown when selecting either black-market stock or normal grooming-library options: never repeat the immediately previous generated hairstyle, eyebrow shape, beard state, or face shape unless explicitly requested, hard-exclude the last 3 used values in each domain when alternatives exist, and strongly downweight the last 10.

Use expression and pose stock only during Azoth prompt synthesis. Keep expression stock separate from face shape, features, or grooming; keep pose stock separate from outfit, anatomy redesign, multiple poses, character sheets, or background action.

Pose diversity is mandatory when pose stock exists. Azoth must use a mandatory two-stage lock before prompt writing: first lock exactly one broad `姿势大类`, then filter `black-market/inventory/pose.md` to concrete stock items inside that exact family, then lock exactly one concrete pose item by `名称`. A broad family alone is not a valid pose selection. Azoth must not invent an unstocked pose after choosing a family, must not choose a concrete item from a different family, and must not write `POSE_DYNAMIC` until the concrete stock item's `描述` is locked for translation. Apply recent-pose cooldown, and adapt outfit props to the selected body language. Do not let occupational readability collapse the character back into a repeated one-hand-forward presentation pose. If a selected pose contains hand-on-hip, crossed legs, hip tilt, pelvis-forward lean, runway stance, S-curve body, arched-back fashion posture, or playful finger-flourish signals, keep the pose family but translate it into a grounded masculine version with squared hips, squared shoulders, planted feet, balanced weight, and belt-resting or low side-carry hand placement. Do not let `seated` become the default alternative to standing: seated poses require a believable support surface or rest/work beat, must never repeat back-to-back unless explicitly requested, and must be hard-excluded for the next 3 selections when the user complains that poses are always sitting.

Black-market stock must not influence occupation selection. Bo Le chooses the occupation first from the jobs library using user constraints and balanced random selection. The random draw is authoritative when the user does not specify an occupation: stats may explain and flavor the selected job, but they must not reroll it toward a more compatible role such as wedding photographer. San Zhai may then adapt compatible styling stock to that chosen job, but it must not change the job to match a better-stocked outfit.

## Face and Eye Preservation

When a character needs a stronger, heavier, heroic, wild, hard-edged, or high-pressure male read, do not use abstract labels such as `tough guy`, `rugged man`, `hard-boiled man`, or `masculine face` in the final prompt. These tend to push image generation toward realism, small eyes, rough skin, older faces, or Western-comic rendering.

Use module-owned structure instead:

- 托尼：translate the stronger read into broad stylized face silhouette, jaw/chin mass, hairstyle direction, static eyebrow shape, and beard pressure. Prefer wide lower face, broad square jaw, solid blunt chin, full cheek structure, balanced face length, thick straight/blocky eyebrows, and clean animation edges. Avoid pointed chin, V-shaped face, narrow cheekbones, long face, narrow oval face, realistic ruggedness, rough skin, and small-eye toughness.
- 三宅：support the read through clothing mass and stable silhouette: shoulder volume, waist systems, belts, gloves, arm gear, heavy footwear, head/neck structure, clean protective layers, and grounded accessory placement.
- 阿佐特：preserve WHOWHO anime eyes in the final prompt when adding brow pressure, stronger face structure, tiredness, low tension, or quiet expressions. Use compact protection such as `large expressive eyes, same eye size, same anime eye style, wide eye opening, straight upper eyelids, firm lower eyelids, focused pupils, direct gaze, controlled highlights`, plus negative constraints against small eyes, narrow slit eyes, squinting, half-lidded eyes, heavy-lidded eyes, droopy eyelids, sleepy eyes, realistic eyes, and style shift.
- 黑墙：reject any face or prompt wording that turns strength, tiredness, low tension, or quiet expression into facial slimming, small eyes, half-lidded eyes, sleepy eyes, rough realism, weathered skin, or non-WHOWHO art style unless the user explicitly asks for that exact direction.

## Black-Market Opening 1.0

When black-market formal stock is available in the conversation, when the shelf exists, or when the user explicitly asks to use black-market inventory, the mother pipeline should treat it as a small shop that relevant modules must visit at their own step:

- 三宅：during work-outfit design, check formal styling stock for clothing, footwear, accessories, carried props, worn props, materials, color relationships, and layering. Default to scanning `套装货` first for complete structure; use `单品货` afterward for component-level adaptation and mix-and-match. Always check `items/bottoms.md` before finalizing `pants`; if a selected套装 has a generic or recently repeated leg system, replace or mutate it with a compatible bottom item. Apply outfit cooldown before final scoring: hard-exclude the last 3 selected set stock names and main styling algorithms when alternatives exist, strongly downweight the last 10, and vary the primary visual carrier across outer volume, waist system, armor/protection, leg system, head/neck system, hand/arm system, marker system, footwear, and accessory system.
- 托尼：during head styling, check formal hairstyle stock for `hairstyle` and formal eyebrow stock for `eyebrows` only. Do not use black-market stock for beard, face shape, eye shape, facial features, makeup, complexion, or attractiveness.
- 阿佐特：during prompt synthesis, check formal pose stock for body angle, weight shift, hand placement, gesture, prop interaction, and action freeze-frame; then check formal expression stock for gaze, facial tension, mouth-corner state, emotional layer, and acting state. Pose must be selected and locked first, expression second. Pose selection must be two-stage: lock a broad `姿势大类`, filter to concrete items from that exact family, and lock one concrete `名称` plus `描述`; if the family has no viable concrete item, reject that family and reroll/reselect another family before writing the prompt. Apply pose cooldown: hard-exclude the last 3 used pose categories when alternatives exist, strongly downweight the last 10, avoid repeated hand-forward presentation patterns unless explicitly required, and convert seductive-fashion pose signals into grounded masculine body language instead of deleting the pose. Apply expression cooldown after the pose is locked: hard-exclude the last 3 used expression stock names and near-duplicate performance beats when alternatives exist, strongly downweight the last 10, and prefer an expression that supports the selected pose without repeating the same mouth/gaze/tension pattern. Treat seated as a low-frequency family: only use it when the role naturally supports a seated/resting/workstation beat, never repeat it back-to-back unless requested, and hard-exclude it for the next 3 selections after a sitting-sameness complaint. Keep expression stock separate from face shape, grooming, and appearance judgments.
- 黑墙：audit any selected black-market stock after integration. Reject or reroute if the stock introduces forbidden directions, face-centered appearance judgments, makeup, complexion, dirty materials, noisy fabric texture, or any conflict with the fixed body and single-character prompt rules.

All modules must read only `正式入库`. `现场验货`, `常规描述`, source filenames, paths, and raw image analysis are never valid stock for the mother pipeline.

## Black-Market Shelf 1.2

Before running the module pipeline, check whether `black-market/inventory.md` exists as the shelf index. If it exists, load external stock from the matching lane file before the normal library by default, and read only each file's `正式入库` section. The user no longer needs to say `@黑商` for the mother pipeline to shop from stock.

Shelf routing:

- 三宅 must check `black-market/inventory/styling/sets.md` first for `造型库存 / 套装货`, then check `black-market/inventory/styling/items/*.md` for `造型库存 / 单品货` when it needs adaptation, replacement, mix-and-match, or extra accessories/props.
- 三宅 must treat `black-market/inventory/styling/items/bottoms.md` as mandatory for the `pants` lane. The character record's `裤子 / pants` row should be derived from a selected bottom stock item when compatible, or from a set leg system explicitly improved with bottom-stock fields. The `黑商取货` log must name the bottom candidate when it affects `pants`.
- 托尼 must check `black-market/inventory/hairstyle.md` `发型库存` for hairstyle only and `black-market/inventory/eyebrow.md` `眉型库存` for static eyebrow shape only.
- 阿佐特 must check `black-market/inventory/pose.md` `姿势库存` for full-body pose and action language when the shelf exists, select a broad pose category, lock one concrete pose, then check `black-market/inventory/expression.md` `表情库存` for expression and acting language only. If the locked pose is not a presentation pose, occupational tools should be placed on belts, packs, straps, leg sides, badges, neck loops, or neutral side carry instead of forcing a forward hand display.
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

`黑商取货` is an inventory-level reasoning log. It may compare only formal stock fields such as `名称`, `类别`, `描述`, `标签`, and `包含单品`; for pose stock, it may also compare `姿势大类`, `身体朝向`, `重心高度`, `动势强度`, `手部策略`, and `展示风险`. For 三宅 styling stock, it may also summarize inherited outfit strengths derived from those formal fields, such as silhouette, color, material, layering, and role-fit logic. It must not mention source images, filenames, paths, `现场验货`, `常规描述`, raw image analysis, facial features, complexion, makeup, attractiveness judgments, or identity/story inferred from the source.

## Output

Return these sections for each completed character:

1. 调度日志
2. 角色档案
3. 缪斯审核
4. 黑墙审核
5. 英文提示词
6. 中文提示词
7. 设计思路
8. 图像生成
9. 成图审核
10. 文件归档

In `角色档案`, use Chinese field labels such as `名字`, `年龄`, `国籍`, `体型`, `性格`, `贫富值`, `危险值`, `欲望值`, `执行力`, `社交力`, `世界底盘`, `时代背景`, `文化体系`, `文化阶段`, `市井特点`, `技术层级`, `秩序状态`, `材料生态`, `视觉禁忌`, `职业`, `帮派`, `工作服`, `发型`, `眉型`, `胡子`, and `脸型`.

### 角色档案表格格式

Default to Markdown tables inside `角色档案` for scanability. Use compact two-group side-by-side tables for short sections, and use normal one-group tables when the content is too long for side-by-side layout.

Use these defaults:

- `基础信息`: two-group table. Put identity fields on the left (`名字`, `性别`, `年龄`, `国籍`, `体型`, `性格`) and score fields on the right (`贫富值`, `危险值`, `欲望值`, `执行力`, `社交力`). Do not show the internal `temperament` field as a basic-info row; let Azoth translate it into the prompt instead.
- `世界底盘`: two-group table. Left group: `时代背景`, `文化体系`, `文化阶段`, `市井特点`. Right group: `技术层级`, `秩序状态`, `材料生态`, `视觉禁忌`.
- `社会身份 + 头脸造型`: two-group table when both are compact. Left group: `职业`, `帮派`, `匹配理由`. Right group: `发型`, `眉型`, `胡子`, `脸型`, `造型理由`.
- `工作服`: use a one-group table or short grouped list because clothing fields can be long. Include `外套`, `打底`, `裤子`, `袜子`, `鞋子`, `饰品/道具`, `造型算法`, `服装线`, `禁用形态检查`, `专业关键词`, `基础款原型`, `外层原型`, `结构事件`, `材质行为`, `衬衫夹克默认规避`, `匿名设计方法`, `设计师提示引用` when user allowed it, `设计操作符`, `裁片路径`, `图案策略`, `工艺边界`, `身体适配`, `鞋饰结构`, `复杂度配额`, `失败规避`, `可替换位`, `世界底盘继承`, `反默认判断`, and `服装理由` when available.
- If any cell would become too long and make the table hard to read, switch only that section to a single two-column table (`字段 | 内容`) or a short list.
- Do not put English prompt bodies, Chinese prompt bodies, or long audits into tables. Keep prompt bodies in fenced code blocks.

Example shape:

```markdown
| 基础信息 | 内容 | 能力数值 | 内容 |
|---|---|---|---|
| 名字 | ... | 贫富值 | ... |
| 年龄 | ... | 危险值 | ... |

| 世界底盘 | 内容 | 世界底盘 | 内容 |
|---|---|---|---|
| 时代背景 | ... | 技术层级 | ... |
| 文化体系 | ... | 秩序状态 | ... |
```

Keep generated content grounded in daily-life occupations and clean, stylized animation character design.

Before any `图像生成` step, enforce prompt visibility and language integrity:

- `英文提示词` must show the full completed English prompt from Azoth. It must be non-empty, start with `Generate one image`, and not be replaced by Chinese text, a summary, a hidden handoff note, or raw slot labels.
- `中文提示词` must show the full completed Chinese inspection prompt. It must be non-empty and start with `生成一张图：`.
- Every user-facing prompt body must be wrapped in a directly copyable fenced code block. Under `英文提示词`, put only the complete English prompt inside one ```text code fence. Under `中文提示词`, put only the complete Chinese prompt inside one ```text code fence. Do not print long prompt prose outside a code fence.
- If the two sections are swapped, empty, truncated into summaries, or written in the wrong language, stop before Mirage/Image Gen and ask Azoth to regenerate only `prompt_en` and `prompt_cn` from the approved character record.
- If either prompt body contains stock provenance, inventory names, module names, selection reasoning, or abstract mood-borrowing, stop before Mirage/Image Gen and ask Azoth to regenerate only `prompt_en`, `prompt_cn`, and `prompt_notes` from the approved character record. Forbidden prompt-body wording includes `black-market`, `inventory`, `based on the stock`, `uses the stock`, `from the stock`, `adapted from the stock`, `selected stock`, `stock name`, `库存`, `黑商`, `取货`, raw stock names, `only for its mood`, and phrases such as `not as a scarf`. Do not fail legitimate visual words such as `stocky`, `stockroom`, `livestock`, or `stock pot` unless they are being used as inventory provenance.
- This check must not compress the prompt. Preserve the full dynamic slot detail, fixed body/rendering/lighting/negative blocks, selected pose and expression descriptions, Mirage paragraph when active, and all generation-critical constraints.

## Design Thinking

After the final Chinese prompt, output `设计思路` as a user-facing design explanation section.

Rules:

- Always provide 6-10 numbered design notes when completing a character.
- These notes explain the current character design. Do not phrase them as future procurement leads, stock requests, or `正式入库`.
- Focus on concrete styling thinking: cutting and pattern paths, material replacement, structural deconstruction, accessory pairing, silhouette tricks, layering method, color/value organization, craft boundaries, and how the outfit is meant to be used or worn.
- Each note should connect a design move to a visible body or outfit result, such as widening the shoulder, freeing the arm, lowering the center of gravity, breaking up a plain torso, replacing a normal shirt, or turning an accessory into a structural anchor.
- Prefer actionable design vocabulary such as `裁剪`, `裁片路径`, `材质替换`, `结构事件`, `解构`, `饰品搭配`, `层次关系`, `搭配方式`, `使用方式`, `巧思`, `身体适配`, `轮廓重心`, and `复杂度控制`.
- Include at least one note about clothing structure, one about material behavior, one about accessories or props, and one about how the pieces are matched or used together.
- Keep the notes grounded in the approved character record and final prompts. Do not invent new identity, story, source provenance, or hidden image-analysis details.
- Never include source image names, file paths, `现场验货`, `常规描述`, raw image analysis, makeup, facial features, face shape, complexion, skin texture, attractiveness judgments, or identity/story copied from a source.

Use this shape:

```text
设计思路
1. <design move>: <how it changes the outfit, body reading, material behavior, accessory role, or matching method>
...
6-10. <design move>: <same format>
```

## Image Generation Tail Step

After preserving all text sections above, the mother pipeline must run one final `图像生成` step unless the user explicitly asks for text only.

For any non-text-only character generation, run the local `mirage` / `蜃楼` skill after Azoth and before Image Gen when that skill is available, unless the user explicitly asks for no platform or a plain character-only white background. Mirage may add only the scene-platform paragraph and compact negative constraints. It must not change the approved character, body, occupation, outfit anchors, black-market stock, grooming, pose, or expression.

Use the built-in Image Gen path. Before every Image Gen call, load both local reference images with `view_image` so they are visible in the conversation context, then send them with the final English prompt from `英文提示词`:

Do not call Image Gen with a prompt that is only stored in the tool call or hidden from the user. The completed English prompt must already be visible under `英文提示词` inside a ```text fenced code block; if it is missing, print the full prompt first in one copyable code block without shortening it, then continue. Before the Image Gen call, run the prompt clean-audit one final time. If the visible prompt still contains stock provenance, raw stock names, module names, selection notes, or abstract mood-borrowing, stop and have Azoth rewrite only the prompt fields; do not send that dirty prompt to Image Gen.

```text
Input image 1 / style reference:
character-forge/references/assets/style_reference.png

Input image 2 / body reference:
character-forge/references/assets/width_first_body_reference.png
```

Resolve both paths relative to the workspace root when possible. If the agent is running from inside `character-forge/`, use `references/assets/style_reference.png` and `references/assets/width_first_body_reference.png`. Do not fall back to external sync folders or Windows drive paths unless the local asset is genuinely missing.

Treat `Input image 1` as the style and rendering reference only, not as identity, costume, exact character copying, or body-proportion authority. Treat `Input image 2` as the body-proportion and muscle-mass reference only, not as identity, costume, hairstyle, or exact character copying. Broad stylized face-shape direction and simplified facial proportions may follow the approved character prompt and anime style, but neither input may cause the result to copy the same recognizable face, exact feature arrangement, or identity likeness. The generated image must follow the current character's approved prompt while matching these reference-image qualities as closely as the model allows:

- clean Japanese TV anime cel-shading, crisp dark outer linework, tidy internal contour lines, smooth flat color blocks, soft but controlled shadow shapes, and minimal background noise
- width-first grounded body proportion, around 6.2-6.6 heads tall, dramatically broad super-heavyweight fighting-game mass, compact head, short thick neck buried between huge traps, enormous deltoids, huge chest shelf, thick barrel ribcage, giant upper arms, huge forearms, oversized heavy hands, very thick thighs, strong calves, large heavy boots or feet, and stable full-body presentation. The first read must be extreme horizontal muscle mass rather than height.
- torso anatomy expressed through large simplified muscle masses and clean stylized shape lines, with a clean white fitted tank top or clean white fitted inner T-shirt visibly wrapping the torso by default; the pectoral shelf, center chest divide, stacked abdominal blocks, firm upper-ab wall, and side-ab planes must press through the white fabric unless the user explicitly overrides the base layer, requests a bare torso, or requires fully covering armor or heavy outerwear; even a slightly forward-projecting torso must read as ribcage pressure and abdominal muscle blocks, never as a soft pot belly, round smooth stomach, sagging abdomen, unsegmented convex belly, loose undershirt, or smooth torso shirt; not realistic skin texture or painterly rendering
- single full-body character, centered on a flat pure white background, with no scene, props display, panels, turnarounds, gradient, vignette, aura, halo, glow, or extra characters
- one single soft neutral key light from upper left, mostly clean white with only a faint warm daylight tendency; very narrow pale cream-white painted cel-shading lit-edge highlights only on the light-facing silhouette and surfaces; no second rim light, no colored dual rim light, and no glow around the character

Add the Image Gen prompt wrapper from `references/prompt_blocks/imagegen-wrapper.md` around the final English prompt:

```text
<the exact wrapper from references/prompt_blocks/imagegen-wrapper.md>
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
- `体块一致性`: shoulders, chest, traps, neck, back width, arms, forearms, hands, waist, thighs, calves, and boots/feet must visibly carry super-heavyweight mass. The silhouette should read like a wall of muscle with shoulder span much wider than hips, short thick neck, giant arms, huge forearms, oversized hands, very thick thighs, and large heavy feet. By default, the torso must show a clean white fitted tank top or clean white fitted inner T-shirt wrapping large simple pectoral and abdominal masses unless the prompt explicitly overrides the base layer, uses a bare torso, or fully covers the torso with armor or heavy outerwear. The pectoral shelf, center chest divide, stacked abdominal blocks, firm upper-ab wall, and side-ab planes must press through the white fabric; a smooth torso shirt, loose undershirt, or hidden abdomen fails. Reject any soft pot belly, round smooth stomach, sagging abdomen, or unsegmented convex belly, even if the character is otherwise broad and heavy.
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

Then run one corrective Image Gen attempt using the same approved character record, but strengthen only the failed constraints. For body failures, the corrective prompt must explicitly prioritize `width-first super-heavyweight fighting-game anime body`, `around 6.2-6.6 heads tall`, `dramatically wider and thicker than a normal tall hero`, `shoulder span much wider than hips`, `short thick neck buried between huge traps`, `enormous rounded deltoids`, `huge chest shelf`, `thick barrel ribcage`, `clean white fitted tank top or clean white fitted inner T-shirt`, `deep pectoral shelf pressing through white fabric`, `visible center chest valley`, `large stacked blocky abs pressing through the fitted white base layer`, `firm upper-ab wall`, `thick oblique side planes`, `giant upper arms`, `huge forearms`, `oversized heavy hands`, `very thick thighs`, `strong calves`, `large heavy feet`, and `wall of muscle silhouette`, and must explicitly avoid `slim`, `narrow shoulders`, `long legs`, `7-head tall normal hero proportions`, `fashion-model proportions`, `smooth torso shirt`, `loose undershirt`, `baggy base layer`, `soft pot belly`, `round smooth stomach`, `sagging abdomen`, `unsegmented convex belly`, `lightly athletic build`, and `merely tall and muscular`.

After the corrective attempt, audit again. If it still fails, show the best image but clearly write:

```text
成图审核：未通过，原因：<brief reason>。已保留当前生成结果，建议下一轮使用更强参考或更硬体型提示词。
```

## No Filesystem Archive

Do not create a desktop `GP` folder, character subfolder, `prompts.md`, `image-unavailable.txt`, or any other local archive file after generation. The previous Desktop GP archive step is disabled by default because it slows the workflow.

Keep the generated image, English prompt, Chinese prompt, audits, and logs visible in the conversation only. In the final `文件归档` section, write `未归档：已按当前规则跳过本地文件保存。` Do not report a folder path or created files unless the user explicitly asks to save or export the result in that turn.
