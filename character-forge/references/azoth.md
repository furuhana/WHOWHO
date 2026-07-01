# 阿佐特 / Azoth

## Role

Merge the approved character record into image-generation prompts after Blackwall passes.

## Inputs

Use the full character record and Blackwall's `integrated_design`.

Use black-market formal expression and pose stock by default when the shelf exists, but only after Blackwall has approved the character design.

## Three Gates

1. Merge all useful information into one visual design summary.
2. Convert the visual summary into an English prompt that image2 can understand.
3. Audit whether each prompt phrase helps generation. Remove or translate abstract traits that do not help.

## Prompt Rules

- Write in English first.
- Translate the final English prompt into Chinese so the user can quickly inspect the result.
- Keep all non-prompt explanation in Chinese.
- Use `英文提示词`, `中文提示词`, and `提示词说明` as user-facing labels.
- Start `prompt_en` with an explicit image-generation instruction, preferably `Generate one image of ...`, so image2 treats the text as a direct image request instead of analysis material.
- Start `prompt_cn` with `生成一张图：` for the same reason; the Chinese version should read like a direct generation request, not a critique or explanation.
- Do not optimize the final prompt for brevity. The goal is a complete, imageable prompt, not a short prompt.
- Never compress, summarize, or omit prompt details to satisfy language or display checks. Fix wrong-language, empty, or misplaced sections by restoring the full completed prompt in the correct field.
- Default to omitting the character's personal name from `prompt_en` unless the user requests it or the name itself has visible design meaning. Keep names in the Chinese character record, not in the image prompt.
- Preserve every Blackwall-approved visible design domain as its own prompt material: body standard, occupation readability, outfit silhouette and layers, hairstyle, static eyebrow shape, selected pose stock, selected expression stock, rendering style, and single-character white-background constraints.
- Expand approved visual details into concrete prompt language instead of compressing them into labels, summaries, or abstract traits.
- Remove only forbidden, contradictory, non-visual, or generation-harming phrases. Do not remove useful visual information merely because the prompt is already long.
- When a selected black-market pose or expression is used, translate its full `描述` into the English prompt unless a phrase must be trimmed for safety or direct contradiction.
- Keep the expanded prompt efficient: avoid meta-explanations such as `should read as`, `rather than`, `instead of`, `not posing for`, or repeated instructions about what the design is not.
- Prefer positive visual wording over negative prohibitions. Use one compact negative-constraint sentence near the end for banned output formats and forbidden rendering details.
- Split very long prompt sentences when they exceed roughly 35 English words, especially body-standard, pose, and expression sentences.
- Do not repeat the same visual adjective more than needed. If words such as `clean`, `practical`, `clear`, `shape`, or `stylized` recur heavily, merge or replace them with more specific visual language.
- Prefer visible details over abstract stats.
- Always include the fixed body standard in the prompt unless the user explicitly overrides it: width-first and grounded, around 6.2-6.6 heads tall, dramatically broad and heavy super-heavyweight fighting-game build, shoulder span much wider than the hips, short thick neck buried between huge traps, enormous rounded deltoids, huge chest shelf, thick barrel ribcage, powerful square torso, dense compact waist, giant upper arms, huge forearms, oversized heavy hands, very thick thighs, strong calves, large heavy feet, compact head, and stable heavy stance. Make clear that the first read is extreme horizontal muscle mass rather than height.
- Always describe the inner base layer as fitted and stretched over the torso, visibly wrapping enormous pectorals, a deep lower-pectoral shelf, center chest divide, broad ribcage, thick side-ab planes, and large stacked blocky abdominal muscles with clean stylized contour lines, unless the user explicitly overrides this.
- When the approved outfit includes shorts and plain white socks, explicitly preserve the pants-length guard: the shorts end above the knee, leaving the plain white socks clearly visible between the shorts and shoes. Keep the black belt readable when it is part of the approved outfit.
- When the approved outfit includes long pants and visible plain white socks, describe the sock visibility as natural trouser length: straight or softly relaxed pant hems sit outside the ankle near the shoe opening, slightly above or around the shoe collar, revealing a small clean glimpse of plain white sock. Do not describe pants tucked into socks, elastic cuffs, jogger cuffs, tight tapered hems, leggings-like pants, ribbed socks, vertical sock stripes, colored sock bands, logos, or text.
- Make clear that the chest and abdominal lines come from oversized muscle masses pressing through the fitted clothing, not from ordinary cloth folds, wrinkles, fabric bunching, or a smooth shirt surface.
- When the user asks for a white tank top, white fitted T-shirt, tucked undershirt, or similar base layer, strengthen the prompt with explicit torso readability: the pectoral shelf, chest divide, upper-ab blocks, lower-ab blocks, and oblique side planes must be visible through the clean white fabric as simplified anime anatomy.
- Always specify a single full-body character standing alone on a pure white background.
- Always preserve face readability for the viewer: the head should be turned enough that the face is visible, and the eyes should look toward the screen, the camera, or very near the camera. Side-facing or side-body poses may keep the torso angled, but they still need a three-quarter head turn or camera-near gaze so the face does not disappear into a pure profile.
- Always include the fixed white-background lighting module unless the user explicitly asks for different lighting: one single soft neutral key light from upper left, mostly clean white with only a faint warm daylight tendency. Keep the lighting natural, restrained, and character-bound.
- Add very narrow pale cream-white lit-edge highlights only on the light-facing silhouette and surfaces, adapted to the current outfit and tools: hair tips, cheek edge, shoulder, collar edge, outer sleeve, forearm ridge, chest folds, belt buckle, badge or plastic card, trouser side folds, and boot leather edges. These highlights must look like painted cel-shading accents attached to the character surface, not glow.
- Keep the shadow side darker with only minimal ambient fill and no second rim light. Preserve the readable silhouette through crisp dark outer linework plus small neutral edge highlights.
- Strengthen the white-background constraint with: flat pure white background, no gradient, no vignette, no aura, no halo, no glow around the character, no visible light source, and no scenery.
- Avoid character sheet wording: no multiple characters, no multiple poses, no front-side-back turnaround, no panel layout, no split view, no callout boxes, no background scene unless the user explicitly asks.
- Keep daily-life occupation readable.
- Do not copy broad styling labels such as urban, streetwear, city casual, casual, workwear, or light utility into the final prompt unless the user explicitly requested that style. If those labels come from outfit stock, translate them into concrete visual details such as silhouette, layering, color blocks, pocket placement, straps, footwear shape, or functional accessories.
- Include clean high-quality Japanese TV anime cel shading, crisp linework, fresh colors, tidy shadows, and clean stylized animation character design.
- Include Tony's `eyebrows` as static eyebrow-shape language when it is useful for character recognition. Keep it separate from expression acting.
- The final prompt may include broad stylized face-shape direction and simplified facial-proportion language when it comes from the approved character record or the target anime rendering style. This is allowed as design guidance. It must not become a copied reference-face identity, exact feature arrangement, recognizable likeness, celebrity/source-character match, or realistic face reconstruction.
- Avoid overly specific realistic feature lists unless the user explicitly requests them. If facial wording is needed, keep it stylized and character-owned rather than source-owned.
- Use expression, gaze direction, brow tension, mouth state, and facial tension only when needed; these may describe the current performance, not permanent eye shape, permanent eyebrow shape, or facial structure.
- When combining static eyebrow shape with expression stock, preserve the selected eyebrow shape first, then add temporary brow movement only if it does not contradict that shape.
- Avoid forbidden directions even if earlier modules accidentally imply them.
- Do not ask for clothing material to be rendered through fine texture maps, tiny prints, micro-weave, speckles, or noisy surface detail.
- If mentioning cotton, linen, or similar fabrics, express them through color and clean shape language rather than visible grain or small texture.
- If white socks are present, keep them solid plain white. Add a compact negative phrase when needed: no striped socks, no ribbed vertical sock pattern, no colored sock bands, no pants tucked into socks, no jogger cuffs.

## Fixed Prompt Blocks

Load these fixed prompt block files when synthesizing `prompt_en` or handing off to Image Gen. Fixed blocks are template resources, not prose suggestions; insert their text verbatim unless the user explicitly changes that constraint.

- `references/prompt_blocks/body-standard.md`
- `references/prompt_blocks/rendering-style.md`
- `references/prompt_blocks/lighting-white-background.md`
- `references/prompt_blocks/global-negative.md`
- `references/prompt_blocks/mirage-platform-template.md` when Mirage is active
- `references/prompt_blocks/sock-and-belt-guards.md`
- `references/prompt_blocks/imagegen-wrapper.md` for the final Image Gen handoff wrapper

Do not shorten dynamic clothing, accessory, grooming, pose, or expression blocks because fixed blocks are long. Fixed blocks do not count toward dynamic-section length targets.

## Dynamic Prompt Slots

Before writing the final `prompt_en`, draft these dynamic slots from the approved character record. Use only visible, image-helpful information.

```text
ROLE_VISUAL
OUTFIT_DYNAMIC
ACCESSORY_DYNAMIC
GROOMING_DYNAMIC
POSE_DYNAMIC
EXPRESSION_DYNAMIC
PLATFORM_DYNAMIC_DECISIONS
```

Use these target lengths for English dynamic slots. They are guidance for useful density, not a reason to pad with filler.

- `ROLE_VISUAL`: 15-30 words. Use occupation-readable visible cues only; do not include a personal name.
- `OUTFIT_DYNAMIC`: 120-180 words. Cover outerwear/top, base layer, pants/shorts, socks, and shoes as separate imageable material.
- `ACCESSORY_DYNAMIC`: 40-80 words. Cover belts, bags, ID cards, tools, jewelry, worn props, and carried props with position and attachment.
- `GROOMING_DYNAMIC`: 35-70 words. Cover hairstyle, static eyebrow shape, beard, and broad stylized face shape without beauty, complexion, makeup, or realistic feature reconstruction.
- `POSE_DYNAMIC`: 35-70 words. Cover body angle, weight shift, hand placement, prop interaction, and face readability.
- `EXPRESSION_DYNAMIC`: 25-50 words. Cover gaze, brow/eye state, mouth state, facial tension, and acting intention; keep it separate from permanent face design.
- `PLATFORM_DYNAMIC_DECISIONS`: 25-50 words. Provide scene theme, solid ground material, and exactly 2-3 rooted props for Mirage to place into its fixed template.

Dynamic slots may be written in `prompt_notes` for inspection when useful, but the final user-facing `英文提示词` must be the completed prompt, not a list of raw slots.

## Prompt Integrity Gate

Before returning Azoth output or handing off to Mirage/Image Gen, run this gate:

1. `prompt_en` must be non-empty, start with `Generate one image`, and be written as English prompt prose. It may contain only unavoidable proper nouns or fixed labels from approved stock; it must not contain Chinese sentence blocks such as `生成一张图`, `已用于生成`, `单人全身`, or a translated Chinese prompt body.
2. `prompt_cn` must be non-empty, start with `生成一张图：`, and be a Chinese translation or inspection version of the completed English prompt.
3. The user-facing `英文提示词` section must display the full completed `prompt_en`, including dynamic slots, fixed prompt blocks, Mirage paragraph when active, and negative constraints. Do not replace it with a Chinese summary, a note that it was used, raw dynamic-slot names, or an omitted placeholder.
4. The user-facing `中文提示词` section must display the full completed `prompt_cn`, not a second copy of the English prompt.
5. If any check fails, stop before Mirage or Image Gen, regenerate only the prompt fields from the approved character record, and run the gate again. Do not reroute earlier character modules unless the approved design itself changed.
6. This gate is a correctness check, not a shortening pass. Preserve the target slot lengths, all fixed blocks, selected pose/expression stock descriptions, outfit/accessory detail density, and required body/rendering/lighting constraints.

## Outfit And Accessory Expansion

Do not reduce clothing to item labels such as `green jacket`, `white T-shirt`, or `olive trousers`. For every major garment, describe at least four imageable aspects:

- silhouette or fit
- material expressed through broad clean shape language
- construction such as panel seams, closures, pocket layout, cuffs, waistband, hems, or straps
- layering or body relationship
- color blocking or trim
- how the garment sits in the selected pose

Main outerwear or upper-body garments should usually be 35-60 English words each. Pants or shorts should usually be 30-55 words. Shoes and socks should usually be 18-35 words. Bags, belts, IDs, tools, and small accessories should usually be 12-30 words each.

Accessories must state where they sit on the body, how they attach or hang, their readable shape, and one or two clean construction details. For example, use `a compact rectangular side bag hanging close to the hip from a short shoulder strap, with a flap closure and flat buckle tabs`, not only `side bag`.

Use clean durability language by default: `reinforced stitching`, `panel seams`, `matte fabric`, `sturdy waistband`, `crisp cuffs`, `flat buckle tabs`, `clean edge lines`, and `structured pockets`.

Avoid default outfit language that implies dirty, damaged, gritty, aged, or noisy texture: `faded`, `worn`, `weathered`, `scuffed`, `dusty`, `stained`, `frayed`, `grimy`, `oily`, `torn`, `distressed`, `rough texture`, `visible fabric grain`, `micro-weave`, `speckled`, or `noisy texture`. Use these only when the user explicitly asks and Blackwall accepts the direction.

## Final Prompt Assembly

Assemble `prompt_en` in this order:

```text
Generate one image of a single full-body original male Japanese TV anime [ROLE_VISUAL], standing alone on a flat pure white background.

[BODY_STANDARD fixed block]

[OUTFIT_DYNAMIC]

[ACCESSORY_DYNAMIC]

[GROOMING_DYNAMIC]

[POSE_DYNAMIC]

[EXPRESSION_DYNAMIC]

[MIRAGE_PLATFORM paragraph generated from PLATFORM_DYNAMIC_DECISIONS, when Mirage is active]

[RENDERING_STYLE fixed block]

[LIGHTING_WHITE_BACKGROUND fixed block]

[GLOBAL_NEGATIVE fixed block plus any pose-specific compact negative]
```

If Mirage is active, Azoth should output `PLATFORM_DYNAMIC_DECISIONS` in `prompt_notes` so Mirage can fill its template without changing character details.

## Black-Market Stock

If `黑商货单` formal stock is available, the user asks to use black-market inventory, or `black-market/inventory.md` exists, Azoth must shop from `正式入库` for expression and pose stock before final prompt synthesis.

Also check these shelves before prompt synthesis, when they exist:

- `black-market/inventory/pose.md`: read only `正式入库 -> 姿势库存`.
- `black-market/inventory/expression.md`: read only `正式入库 -> 表情库存`.

Azoth is a selector and prompt synthesizer, not the original pose director or expression designer. It may choose, combine, adapt lightly for prompt clarity, and translate approved stock into the final English and Chinese prompts. It must not invent a new pose system, rewrite stock into permanent identity, or treat expression as face design.

## Pose Diversity Gate

When black-market pose stock exists, Azoth must run pose selection before writing any prompt prose. Treat the selected pose as the locked full-body action skeleton for the current character. Outfit details, carried props, worn props, and expression must adapt to that locked pose; they must not pull the body language back to a generic front-facing presentation pose.

Pose selection must follow this order:

1. Identify the broad pose category for each viable pose candidate, such as `standing`, `walking`, `seated`, `low seated`, `crouching`, `kneeling`, `half-reclining`, `leaning`, `arms crossed`, `hands on hips`, `shoulder-carried prop`, `low center of gravity`, or `action freeze`.
2. Apply recent-pose cooldown before scoring job fit. Hard-exclude the last 3 used pose categories when alternatives exist. Strongly downweight the last 10 used pose categories.
3. Hard-exclude recent or overused hand-display patterns when alternatives exist: one hand extended forward, open palm presenting, pointing at the viewer, one hand holding a small object forward, or one hand gripping a chest strap while the other hand presents forward.
4. Choose the pose category first, then choose one concrete pose stock item within that category.
5. After choosing a pose, normalize face visibility without changing the locked body action: add a head-and-gaze clause that keeps the face readable to the viewer. For side-body, angled, walking-away, turning-back, low, or action poses, require the head to turn toward the camera in a three-quarter view and the eyes to look toward the screen/camera area. Do not let profile, looking far off-frame, looking down, or looking fully away hide the face unless the user explicitly requests that mood.
6. If the selected pose is not a presentation pose, keep occupational props on the belt, backpack, shoulder strap, leg side, chest badge, neck loop, or carried neutrally at the side instead of forcing a hand-forward display.
7. If all viable pose stock is recently used, select the least-recently used category and state the cooldown limitation in the pose reasoning log.

The selected pose stock must be visibly present in `prompt_en` and `prompt_cn`. If the character's job requires a prop, the prop placement must preserve the locked pose. Do not replace the selected pose with generic phrasing such as `standing naturally with one hand forward` unless that exact pose stock was selected and is not under cooldown.

When the selected pose is not a hand-forward presentation pose, add a compact negative constraint to `prompt_en`, such as `no forward presenting hand, no pointing at the viewer, no hand extended toward the camera`, while keeping the rest of the prompt positive and imageable.

When the selected pose turns the body sideways or away from the viewer, add positive prompt language such as `his head turns back toward the camera in a readable three-quarter view, eyes looking toward the viewer or just beside the camera`. If an expression stock says the gaze is to one side, adapt it to `slightly beside the camera` rather than far off-frame, unless the user explicitly asks for an avoidant or hidden-face look.

Allowed expression stock:

- gaze direction and intensity
- eyebrow or eye state
- mouth-corner state
- facial tension
- emotional layer
- camera-facing performance
- acting state

Allowed pose stock:

- standing pose
- weight shift
- body angle
- arm and hand placement
- gesture
- prop interaction
- body language
- action freeze-frame

Use only stock fields such as `名称`, `描述`, and `标签`. Never read or use `现场验货`, `常规描述`, source filenames, paths, raw image analysis, styling stock, makeup, facial features, face shape, complexion, grooming, or attractiveness judgments.

For the final prompt body, translate and use the selected stock's `描述`, not its `名称` or `标签`. `名称` and `标签` are for selection, matching, logs, and `提示词说明` only.

Expression stock should appear as prompt-level performance language, not as permanent identity, face design, grooming, or beauty description.

Expression descriptions that follow the black-market five-part structure are valid prompt material: mouth shape, eyebrow/eye state, gaze, facial tension, and a reusable acting intention. Keep enough of that structure in the English prompt for the image model to perform the face; do not compress it into only the stock name.

Pose stock should appear as full-body performance language, not as clothing, anatomy redesign, multiple poses, character-sheet structure, or background action.

When both pose and expression stock are available, choose pose first, then choose an expression that supports the pose. The final combination should feel like one coherent performance beat. If they conflict, prefer the pose and select a quieter or more compatible expression.

The pose reasoning log must name the selected pose category, note any cooldown exclusion or downweighting, and explain how occupational props were placed without overriding the locked pose. If Azoth chooses a hand-forward presentation pose, it must explicitly justify why no non-presentation candidate fit the character better.

When using black-market stock, include each selected `名称` in `提示词说明`. If no matching pose or expression stock is used, write `黑商取货：未使用` for that lane and give the concrete reason.

When black-market inventory is enabled, record the inventory-level reasoning log using only formal stock fields:

```text
[阿佐特] 黑商取货：
货道：black-market/inventory/pose.md / 姿势库存
候选：<1-3 pose stock names or 无可用库存>
使用：<selected pose stock name or 未使用>
姿势大类：<selected broad pose category>
冷却处理：<excluded or downweighted recent pose categories, or none>
道具适配：<how job props preserve the locked pose instead of forcing a hand-forward display>
取货理由：<body-performance fit based on 名称, 描述, 标签>
未选理由：<why other candidates fit less well>

[阿佐特] 黑商取货：
货道：black-market/inventory/expression.md / 表情库存
候选：<1-3 expression stock names or 无可用库存>
使用：<selected expression stock name or 未使用>
取货理由：<expression-performance fit based on 名称, 描述, 标签 and selected pose>
未选理由：<why other candidates fit less well>

[阿佐特] 表情姿势搭配：
组合：<pose stock name or 无> + <expression stock name or 无>
组合理由：<why the face performance supports the full-body pose>
```

## Useful Visual Conversions

- `wealth`: convert to fabric quality, accessory polish, and overall neatness.
- `danger`: use it to choose compatible approved pose/expression stock, and otherwise convert it only to silhouette pressure or visual restraint.
- `desire`: use it to choose compatible approved pose/expression stock, and otherwise convert it only to ambition, vanity, restlessness, or showy styling details.
- `execution`: convert to controlled posture, prepared tools, and organized styling.
- `social`: use it to choose compatible approved pose/expression stock, and otherwise convert it only to approachable or closed overall body language.
- material: convert cotton, linen, and similar fabric ideas into clean colors, broad panels, simple silhouettes, and matte flat areas; remove fine-grain texture wording.

Do not invent named expression beats from abstract scores. If no matching expression stock is available or selected, use only minimal neutral prompt language such as `neutral steady expression`, `calm face`, or omit face performance entirely.

## Output

Fill:

```yaml
azoth:
  dynamic_slots:
    role_visual:
    outfit_dynamic:
    accessory_dynamic:
    grooming_dynamic:
    pose_dynamic:
    expression_dynamic:
    platform_dynamic_decisions:
  prompt_en:
  prompt_cn:
  prompt_notes:
```

`prompt_notes` should mention which abstract details were translated or removed.

`prompt_notes` must also include `本轮姿势库存：<selected pose stock name>` and `姿势大类：<selected pose category>`. If no pose stock was used, explain why in one sentence. If a non-presentation pose was selected, mention the anti-presentation constraint added to `prompt_en`.

## Black-Market Opportunities

After `prompt_cn`, generate a user-facing `黑商商机` section with exactly 10 numbered procurement ideas.

These ideas are not inventory and must not be treated as `正式入库`. They are future stock leads for the user to search, discuss, or pass to `@黑商` later.

Use the completed character record, Blackwall-approved design, selected black-market stock, and final prompts to suggest concrete future stock. Cover a useful mix of:

- `套装货`
- `单品货`
- `发型库存`
- `姿势库存`
- `表情库存`

Ideas should be specific, imageable, and useful for the current character's occupation, gang, stats, outfit, hairstyle, or performance direction.

Never include source image names, file paths, `现场验货`, `常规描述`, raw image analysis, makeup, facial features, face shape, complexion, skin texture, attractiveness judgments, or source-derived identity/story.

## Image Generation Handoff

After `黑商商机`, hand the final English prompt to the mother pipeline's Image Gen tail step and later desktop archive step. Do not remove or shorten the previous text sections.

Before Image Gen runs, the mother pipeline must load both local reference images with `view_image` and pass them as `Input image 1` and `Input image 2`:

```text
Input image 1 / style reference:
character-forge/references/assets/style_reference.png

Input image 2 / body reference:
character-forge/references/assets/width_first_body_reference.png
```

Resolve both paths relative to the workspace root when possible. If the agent is running from inside `character-forge/`, use `references/assets/style_reference.png` and `references/assets/width_first_body_reference.png`. Do not fall back to external sync folders or Windows drive paths unless the local asset is genuinely missing.

Input image 1 is allowed to guide rendering style, full-body framing, line weight, flat cel-shading, clean white background, and crisp anime readability. Input image 2 is allowed to guide width-first grounded body proportion, simplified muscle anatomy, stable stance, broad muscle mass, and compact heavy silhouette. Neither reference may override the approved character record, selected black-market stock, outfit, grooming, expression, prompt content, or source-character separation. Broad face-shape direction and simplified facial proportions may be style-adjacent, but the generated face must read as a new person, not the same face or a recognizable identity match to either reference.

When handing off to Image Gen, wrap `prompt_en` with:

```text
<the exact wrapper from references/prompt_blocks/imagegen-wrapper.md>
```

Keep `prompt_en` compatible with that wrapper: avoid painterly, semi-realistic, rendered, detailed skin, gritty, textured, cinematic, volumetric, or realistic material language unless the user explicitly asks for that style.
