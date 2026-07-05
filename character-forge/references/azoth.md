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
4. Run the pre-Image-Gen prompt audit. The final prompt body must contain only imageable character, outfit, pose, expression, platform, rendering, lighting, and negative-output instructions. It must not contain inventory names, source labels, module names, selection reasoning, or stock provenance.

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
- Preserve every Blackwall-approved visible design domain as its own prompt material: body standard, occupation readability, outfit silhouette and layers, hairstyle, static eyebrow shape, selected pose description, selected expression description, rendering style, and single-character white-background constraints.
- Preserve the single approved `temperament` as a subtle character-owned variation layer inside `GROOMING_DYNAMIC` and, when useful, `EXPRESSION_DYNAMIC`. Translate it into visible stylized grooming, broad head silhouette, brow geometry, facial tension, and performance tone. Do not write it as an abstract label only.
- Convert `temperament` into one or two compact simile-like prompt phrases rather than showing it as a profile field. English prompt examples: `like a dependable neighborhood older brother`, `with the distant stillness of someone standing behind glass`, `like a bright outdoor worker who smiles before speaking`. Chinese prompt examples: `像可靠的邻家大哥一样`, `带着隔着玻璃看人的疏离感`, `像晒惯太阳的健康青年似的`. Keep these phrases imageable and character-owned; tie them to grooming, posture, facial tension, or expression.
- Expand approved visual details into concrete prompt language instead of compressing them into labels, summaries, or abstract traits.
- Translate San Zhai's `styling_algorithm`, `design_function_slots`, `replacement_slots_used`, `variation_matrix`, and `anti_default_decision` into visible outfit and accessory description. Do not put these internal field names or Chinese algorithm labels into the final prompt body.
- When Garment Grammar fields exist, consume `professional_keywords` as the primary clothing wording source and add `negative_clothing` to the compact negative constraints. Do not expose `garment_line`, `banned_shape_check`, or field names in the final prompt body.
- When `outer_shell_prototype`, `structural_event`, `material_behavior`, or `anti_shirt_jacket_default` exist, preserve their visible effect in `OUTFIT_DYNAMIC`. Do not collapse them into generic jacket, shirt, coat, vest, deconstruction, transparent material, or stylish details.
- Translate San Zhai's advanced design grammar fields into visible prompt material: `base_garment_prototype`, `designer_method_references`, `design_operators`, `panel_paths`, `pattern_strategy`, `craft_boundaries`, `body_fit_strategy`, `complexity_budget`, and `design_failure_avoidance`.
- If the user explicitly allowed designer names in prompts and San Zhai recorded `designer_prompt_references`, a short designer-method reference clause may appear in `OUTFIT_DYNAMIC`, but it must be subordinate to concrete construction and must never replace clothing detail. Prefer wording such as `with restrained design-method references to Issey Miyake garment pleating and Maison Margiela exposed construction`, then immediately describe the visible panel paths, piping, folds, or shoe structure.
- Do not write `in the style of <designer>` as the whole outfit direction. Designer names are allowed only as method references when requested, not as brand copying, source identity, or a substitute for panel paths and craft boundaries.
- Translate approved `world_context` only through visible character-bound details: garment construction, material zones, tools, tags, badges, bags, fasteners, cultural cut logic, civic devices, and Mirage platform props when active. Do not paste world-context field names or abstract setting labels into the prompt body.
- Remove only forbidden, contradictory, non-visual, or generation-harming phrases. Do not remove useful visual information merely because the prompt is already long.
- When a selected black-market pose or expression is used, translate its full `描述` into the English prompt unless a phrase must be trimmed for safety or direct contradiction.
- Keep the expanded prompt efficient: avoid meta-explanations such as `should read as`, `rather than`, `instead of`, `not posing for`, or repeated instructions about what the design is not.
- Prefer positive visual wording over negative prohibitions. Use one compact negative-constraint sentence near the end for banned output formats and forbidden rendering details.
- Split very long prompt sentences when they exceed roughly 35 English words, especially body-standard, pose, and expression sentences.
- Do not repeat the same visual adjective more than needed. If words such as `clean`, `practical`, `clear`, `shape`, or `stylized` recur heavily, merge or replace them with more specific visual language.
- Prefer visible details over abstract stats.
- Always include the fixed body standard in the prompt unless the user explicitly overrides it: width-first and grounded, around 6.2-6.6 heads tall, dramatically broad and heavy super-heavyweight fighting-game build, shoulder span much wider than the hips, short thick neck buried between huge traps, enormous rounded deltoids, huge chest shelf, thick barrel ribcage, powerful square torso, dense compact waist, giant upper arms, huge forearms, oversized heavy hands, very thick thighs, strong calves, large heavy feet, compact head, and stable heavy stance. Make clear that the first read is extreme horizontal muscle mass rather than height.
- Always insert the fixed torso base-layer anchor unless the user explicitly overrides the visible base layer, requests a bare torso, or requires fully covering armor or heavy outerwear that makes the torso invisible. The default visible base layer is a clean white fitted tank top or clean white fitted inner T-shirt, not a loose shirt.
- When the approved outfit includes shorts and plain white socks, explicitly preserve the pants-length guard: the shorts end above the knee, leaving the plain white socks clearly visible between the shorts and shoes. Keep the black belt readable when it is part of the approved outfit.
- When the approved outfit includes any non-short pants and visible plain white socks, describe them as 9-length pants regardless of style. Straight trousers, relaxed trousers, slacks, chinos, jeans-like work pants, uniform trousers, cargo pants, field trousers, service trousers, and every other non-short pant style must stop just above or lightly around the shoe collar, revealing a small clean glimpse of plain white sock. Do not describe full-length trousers, mid-calf capri pants, seven-tenths pants, pants tucked into socks, elastic cuffs, jogger cuffs, tight tapered hems, leggings-like pants, ribbed socks, vertical sock stripes, colored sock bands, or logos.
- Make clear that the chest and abdominal lines come from oversized muscle masses pressing through the fitted clothing, not from ordinary cloth folds, wrinkles, fabric bunching, or a smooth shirt surface.
- When the user asks for a white tank top, white fitted T-shirt, tucked undershirt, or similar base layer, preserve the fixed torso base-layer anchor verbatim and adapt only surrounding outfit details.
- Always specify a single full-body character standing alone on a pure white background.
- Always preserve face readability for the viewer: the head should be turned enough that the face is visible, and the eyes should look toward the screen, the camera, or very near the camera. Side-facing or side-body poses may keep the torso angled, but they still need a three-quarter head turn or camera-near gaze so the face does not disappear into a pure profile.
- Always include the fixed white-background lighting module unless the user explicitly asks for different lighting: one single soft neutral key light from upper left, mostly clean white with only a faint warm daylight tendency. Keep the lighting natural, restrained, and character-bound.
- Add very narrow pale cream-white lit-edge highlights only on the light-facing silhouette and surfaces, adapted to the current outfit and tools: hair tips, cheek edge, shoulder, collar edge, outer sleeve, forearm ridge, chest folds, belt buckle, badge or plastic card, trouser side folds, and boot leather edges. These highlights must look like painted cel-shading accents attached to the character surface, not glow.
- Keep the shadow side darker with only minimal ambient fill and no second rim light. Preserve the readable silhouette through crisp dark outer linework plus small neutral edge highlights.
- Strengthen the white-background constraint with: flat pure white background, no gradient, no vignette, no aura, no halo, no glow around the character, no visible light source, and no scenery.
- Avoid character sheet wording: no multiple characters, no multiple poses, no front-side-back turnaround, no panel layout, no split view, no callout boxes, no background scene unless the user explicitly asks.
- Keep daily-life occupation readable.
- Keep the no-skirt/no-apron preference visible in the final compact negative clothing clause when Garment Grammar is active: no skirt, no dress, no apron, no pinafore, no apron-like front panel.
- Do not copy broad styling labels such as urban, streetwear, city casual, casual, workwear, or light utility into the final prompt unless the user explicitly requested that style. If those labels come from outfit stock, translate them into concrete visual details such as silhouette, layering, color blocks, pocket placement, straps, footwear shape, or functional accessories.
- Do not copy styling algorithm labels such as `警示机能型`, `职业异化型`, `仪式宽体型`, `轻装装甲型`, or `权力套装型` into the prompt. Convert them into concrete construction: high-visibility trim, segmented outer shell, waist panels, wide sleeves, harness straps, protective plates, broad belt, hanging tags, transparent layer, tool pouches, heavy boots, or other approved visible elements.
- Do not copy world-context labels such as `时代背景`, `文化体系`, `文化阶段`, `市井特点`, `技术层级`, `秩序状态`, `材料生态`, `视觉禁忌`, `near-future`, `East Asian street market`, or `semi-regulated` as abstract labels. Convert them into visible prompt details, such as rainproof short jacket panels, arcade service tags, municipal badge tabs, clean metal buckles, transparent sleeve guards, compact repair pouch, or simple civic scanner.
- Include clean high-quality Japanese TV anime cel shading, crisp linework, fresh colors, tidy shadows, and clean stylized animation character design.
- Include Tony's `eyebrows` as static eyebrow-shape language when it is useful for character recognition. Keep it separate from expression acting.
- The final prompt may include broad stylized face-shape direction and simplified facial-proportion language when it comes from the approved character record or the target anime rendering style. This is allowed as design guidance. It must not become a copied reference-face identity, exact feature arrangement, recognizable likeness, celebrity/source-character match, or realistic face reconstruction.
- Preserve the WHOWHO anime eye read whenever face variation, high danger, strength, wildness, heroic weight, hard-edged temperament, heavy eyebrows, broad jaw language, tiredness, low tension, or quiet expressions appear. Add a compact eye-preservation clause in `GROOMING_DYNAMIC` or `EXPRESSION_DYNAMIC`: `large expressive eyes, same eye size, same anime eye style, wide eye opening, straight upper eyelids, firm lower eyelids, focused pupils, direct gaze, controlled highlights`. Use `angular almond-shaped eyes` only when it helps, and pair it with `wide eye opening` and `same eye size` so it does not become narrow. Do not express tiredness, calmness, cynicism, pressure, or low energy through half-lidded eyes, heavy-lidded eyes, droopy eyelids, sleepy eyes, squinting, or narrow slit eyes unless the user explicitly requests that eye state.
- Do not use abstract toughness labels in the final prompt body when they risk changing style. Avoid `tough guy`, `rugged man`, `hard-boiled man`, `masculine face`, `realistic rugged face`, `rough skin`, `weathered face`, and similar wording. Translate that intention into visible stylized structure: broad square jaw, wide lower face, solid blunt chin, full cheek structure, thick straight eyebrows, low-set brow pressure, firm mouth line, controlled eye highlights, squared posture, and grounded clothing mass.
- When face-shape wording is needed for a stronger male character, prefer broad and heavy terms over lean terms: `broad jaw`, `square jawline`, `wide lower face`, `solid blunt chin`, `full cheek structure`, `wide cheekbone support`, `balanced face length`, `broad nose bridge impression`, and `firm mouth line`. Avoid `pointed chin`, `V-shaped face`, `narrow face`, `narrow cheekbones`, `long face`, or `slender oval face` unless the user explicitly asks for a lean face.
- When reference images are used, include a character-owned face-diversity clause derived from `temperament` if needed, preferably as a compact simile-like phrase rather than a raw label. Keep this clause short and tied to visible grooming or expression; do not turn it into a detailed realistic feature list.
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
- `references/prompt_blocks/torso-base-layer-anchor.md`
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
- `ACCESSORY_DYNAMIC`: 40-80 words. Cover belts, bags, black-market-approved marker pieces, tools, jewelry, worn props, and carried props with position and attachment.
- `GROOMING_DYNAMIC`: 45-85 words. Cover hairstyle, static eyebrow shape, beard, broad stylized face shape, and the eye-preservation clause when needed, without beauty, complexion, makeup, or realistic feature reconstruction.
- `POSE_DYNAMIC`: 35-70 words. Cover body angle, weight shift, hand placement, prop interaction, and face readability.
- `EXPRESSION_DYNAMIC`: 30-60 words. Cover gaze, brow/eye state, mouth state, facial tension, controlled highlights when relevant, and acting intention; keep it separate from permanent face design.
- `PLATFORM_DYNAMIC_DECISIONS`: 25-50 words. Provide scene theme, solid ground material, and exactly 2-3 rooted props for Mirage to place into its fixed template.

Dynamic slots may be written in `prompt_notes` for inspection when useful, but the final user-facing `英文提示词` must be the completed prompt, not a list of raw slots.

When drafting `OUTFIT_DYNAMIC` and `ACCESSORY_DYNAMIC`, consume the San Zhai styling-decision fields as follows:

- `professional_keywords`: preserve useful professional garment terms such as structured tailoring, offset placket, exposed facing, panelled technical pants, articulated knee seams, concealed closure, square shoulder, clean bound edge, matte fabric zones, sculptural sole sidewall, and load-bearing waist system.
- `outer_shell_prototype`: name the precise outer shell in imageable English, such as `hooded rain smock`, `field coat`, `long sleeveless coat`, `protective vest`, `pullover anorak`, `offset-placket jacket`, `inside-out shell`, or `sealed pocket shell`; never reduce it to `jacket`.
- `structural_event`: translate the event into visible mechanism: side entry, inactive sleeve opening, exposed facing, cutaway uniform front, sealed pocket blocks, single-sheet wrap shell, false sleeve layer, one hardware focal point, or heat-pressed fold planes.
- `material_behavior`: describe what the material does: reveals inner layers, seals objects, forms a rain shell, behaves as a second skin, supports semi-rigid volume, transfers weight, or compresses volume at cuffs/waist.
- `anti_shirt_jacket_default`: if shirt-like garments appear, explicitly show which non-shirt carrier owns the primary silhouette or memory point.
- `negative_clothing`: move banned clothing terms into the prompt's compact negative sentence; never describe the character as wearing a skirt, dress, apron, pinafore, wrap skirt, or apron-like panel unless the user explicitly overrode the rule.
- `styling_algorithm`: use it only to decide which visible systems deserve emphasis.
- `design_function_slots`: make each active slot visible through clothing construction, silhouette, attachment, exposure, concealment, material contrast, or motion release.
- `replacement_slots_used`: ensure the prompt names the replacement carriers, especially non-shirt carriers like waist system, outer volume, head/neck system, hand/arm system, leg system, or marker system.
- `variation_matrix`: express only visible consequences, such as off-duty looseness, formal structure, defensive concealment, action-ready mounting, ceremony drape, or repaired-but-clean construction.
- `anti_default_decision`: if a shirt-like base exists, describe the compensating structure that keeps the outfit from reading as a plain shirt outfit.
- `base_garment_prototype`: keep the readable starting garment visible before describing its modifications.
- `designer_method_references`: translate anonymous methods into visible operations, such as garment pleating, anatomical tailoring, exposed construction, controlled drape, sculptural sole logic, architectural shoe support, or performance footwear storytelling.
- `designer_prompt_references`: use designer names only when the user explicitly allowed them; keep the clause short and still describe all visible construction afterward.
- `design_operators`: name the visible effect, not the internal label. For example, write `an offset front placket` instead of `the operator is offset`.
- `panel_paths`: preserve start point, route, endpoint, and body rule in English prose. Example: `curved chest-side panels start below the shoulder peak, follow the outer pectoral mass, and end at the side waist`.
- `pattern_strategy`: describe pattern type, placement, and density. Use low-density edge trim, local emblems, interrupted side stripes, controlled plaid, radiating ribs, or heat-pressed fold lines; avoid all-over tiny pattern language.
- `craft_boundaries`: explicitly render piping, binding, topstitching, exposed seams, zipper teeth, buckle tabs, ribbed hems, drawcords, hard plate edges, or shoe sidewalls.
- `body_fit_strategy`: describe how the outfit reinforces width-first mass, chest/abdomen readability, giant arms, heavy hands, thick thighs, and stable footwear.
- `complexity_budget`: do not write the numeric budget into the final prompt unless useful; translate it into `large readable silhouette, controlled medium panels, sparse craft details, and very low-density markings`.
- `design_failure_avoidance`: use compact negative constraints only when needed: no random surface lines, no all-over tiny pattern, no cyber glow, no noisy fabric texture, no structureless thick soles.

When drafting footwear, always cover:

- readable shoe prototype
- sole structure, such as sculptural sidewall, segmented outsole, flared sidewall, hollow heel, arch frame, or cushioning blocks
- upper cutting, such as toe cap, side wing, heel wrap, tongue, strap, or lace zone
- cuff/sock/trouser connection
- center-of-gravity or body-mass role

When drafting accessories, always cover:

- body location
- attachment method
- shape and volume
- body-reading role, such as widening shoulders, splitting waist, enlarging hands, weighting legs, framing head/neck, or adding occupation cue
- avoid work badges, chest cards, ID cards, name tags, staff passes, access cards, conference badges, and lanyards unless the approved San Zhai record explicitly says they are required

When consuming `world_context`, use it this way:

- `era_background`: visible era-specific garment rhythm and hardware, not a year label.
- `culture_system`: visible construction, tags, wrap logic, service markers, market objects, or association symbols.
- `culture_stage`: new issue, maintained remnant, self-modified, regulated, prosperous custom, or transitional mixed kit.
- `street_texture`: small character-bound objects and accessories, not a background scene.
- `technology_level`: amount and type of visible civilian hardware.
- `order_level`: concealment, patrol/service cues, association badges, number plates, color strips, or pocket markers.
- `material_ecology`: broad clean material zones.
- `visual_taboo`: negative and positive constraints that keep the prompt away from forbidden or overused directions.

## Prompt Integrity Gate

Before returning Azoth output or handing off to Mirage/Image Gen, run this gate:

1. `prompt_en` must be non-empty, start with `Generate one image`, and be written as English prompt prose. It may contain only unavoidable proper nouns that are legitimate visual terms, character/job names requested by the user, or fixed rendering labels. It must not contain Chinese sentence blocks such as `生成一张图`, `已用于生成`, `单人全身`, or a translated Chinese prompt body.
2. `prompt_cn` must be non-empty, start with `生成一张图：`, and be a Chinese translation or inspection version of the completed English prompt.
3. The user-facing `英文提示词` section must display the full completed `prompt_en`, including dynamic slots, fixed prompt blocks, Mirage paragraph when active, and negative constraints. Do not replace it with a Chinese summary, a note that it was used, raw dynamic-slot names, or an omitted placeholder.
4. The user-facing `中文提示词` section must display the full completed `prompt_cn`, not a second copy of the English prompt.
5. Both user-facing prompt sections must wrap the prompt body in directly copyable fenced code blocks. Use exactly one ```text fence for the complete `prompt_en` under the English prompt heading, and exactly one ```text fence for the complete `prompt_cn` under the Chinese prompt heading. Long prompt prose outside a code fence fails this gate.
6. If any check fails, stop before Mirage or Image Gen, regenerate only the prompt fields from the approved character record, and run the gate again. Do not reroute earlier character modules unless the approved design itself changed.
7. This gate is a correctness check, not a shortening pass. Preserve the target slot lengths, all fixed blocks, selected pose/expression stock descriptions, outfit/accessory detail density, and required body/rendering/lighting constraints.

## Pre-Image-Gen Prompt Audit

Run this audit after assembling `prompt_en` and `prompt_cn`, before Mirage or Image Gen. This audit is stricter than the language-integrity gate: it checks whether the prompt is clean generation prose rather than a mixed workflow log.

Fail the audit if `prompt_en` or `prompt_cn` contains source/provenance wording in the prompt body, including:

- Provenance phrases such as `black-market`, `black market`, `inventory`, `shelf`, `lane`, `formal stock`, `based on the stock`, `uses the stock`, `use the stock`, `from the stock`, `adapted from the stock`, `selected stock`, `stock name`, `stock item`, `only for its mood`, or `not as a <stock item category>`. Do not fail legitimate visual words that merely contain the letters `stock`, such as `stocky`, `stockroom`, `livestock`, or `stock pot`, unless they are being used as inventory provenance.
- Chinese equivalents such as `库存`, `黑商`, `货架`, `货道`, `基于库存`, `使用库存`, `来自库存`, `采用库存`, `取货`, or `只取氛围`.
- Raw stock names inside the prompt body, even when surrounded by imageable description.
- Module names or workflow labels such as `San Zhai`, `Tony`, `Azoth`, `Blackwall`, `Muse`, `Mirage`, `三宅`, `托尼`, `阿佐特`, `黑墙`, `缪斯`, or `蜃楼`.
- Prompt notes, reasoning, rejection reasons, cooldown notes, candidate lists, or any explanation of why an item was selected.
- Internal styling-decision labels or field names such as `styling_algorithm`, `design_function_slots`, `replacement_slots_used`, `variation_matrix`, `anti_default_decision`, `造型算法`, `设计功能位`, `可替换位`, `变化矩阵`, `反默认判断`, or `反默认价值`.
- World-context field names or abstract labels such as `world_context`, `era_background`, `culture_system`, `culture_stage`, `street_texture`, `technology_level`, `order_level`, `material_ecology`, `visual_taboo`, `世界底盘`, `时代背景`, `文化体系`, `文化阶段`, `市井特点`, `技术层级`, `秩序状态`, `材料生态`, or `视觉禁忌`.
- Prompt-engineering instructions that read like rules instead of image prose, such as `For any non-short pants style`, `use 9-length pants only`, `Do not describe`, `must be written as`, `insert this`, or `apply this guard`. Rewrite those as direct visual description and compact negative image constraints.

Do not fail designer names solely because they are famous proper nouns when all of these are true:

- the user explicitly allowed testing designer references in prompts;
- the names appear as short `design-method references`, not as `in the style of` brand copying;
- the same prompt sentence or nearby sentence translates the reference into visible construction;
- no brand logo, exact product name, runway look, source character, or proprietary motif is requested.

Fail designer-name use when it replaces construction detail, requests brand imitation, or appears in stock provenance language.

Fail the audit if an inventory item is used only as abstract mood or category drift instead of visible material. Examples that must be rejected:

- A scarf stock becoming a jacket because it has a soft layered mood.
- A pose stock appearing as `black-market pose stock "<name>"` before the actual pose description.
- A hairstyle or eyebrow sentence that says `uses the stock "<name>"` before the translated visual description.
- An expression sentence that names a stock item instead of directly describing mouth, gaze, facial tension, and acting.

When the audit fails, do not continue to Mirage or Image Gen. Regenerate only `prompt_en`, `prompt_cn`, and `prompt_notes` from the approved character record. Preserve the same selected stock choices, but rewrite every affected sentence so the prompt body contains only the translated visual description and necessary character-owned adaptation. Put stock names and selection explanations only in `prompt_notes` / `提示词说明`.

## Outfit And Accessory Expansion

Do not reduce clothing to item labels such as `green jacket`, `white T-shirt`, or `olive trousers`. For every major garment, describe at least four imageable aspects:

- silhouette or fit
- material expressed through broad clean shape language
- construction such as panel seams, closures, pocket layout, cuffs, waistband, hems, or straps
- layering or body relationship
- color blocking or trim
- how the garment sits in the selected pose

Main outerwear or upper-body garments should usually be 35-60 English words each. Pants or shorts should usually be 30-55 words. Shoes and socks should usually be 18-35 words. Bags, belts, IDs, tools, and small accessories should usually be 12-30 words each.

When advanced design grammar is present, major outfit descriptions should preserve:

- the base garment prototype
- one or two visible operations
- one panel path with start/route/endpoint
- one craft boundary
- controlled pattern or marking placement
- the body-fit purpose

Do not reduce `panel_paths` to `complex lines`, `stylish cuts`, `geometric details`, or `decorative panels`.

Accessories must state where they sit on the body, how they attach or hang, their readable shape, and one or two clean construction details. For example, use `a compact rectangular side bag hanging close to the hip from a short shoulder strap, with a flap closure and flat buckle tabs`, not only `side bag`.

Use clean durability language by default: `reinforced stitching`, `panel seams`, `matte fabric`, `sturdy waistband`, `crisp cuffs`, `flat buckle tabs`, `clean edge lines`, and `structured pockets`.

Avoid default outfit language that implies dirty, damaged, gritty, aged, or noisy texture: `faded`, `worn`, `weathered`, `scuffed`, `dusty`, `stained`, `frayed`, `grimy`, `oily`, `torn`, `distressed`, `rough texture`, `visible fabric grain`, `micro-weave`, `speckled`, or `noisy texture`. Use these only when the user explicitly asks and Blackwall accepts the direction.

Avoid fake advanced-design prompt language:

- `complex outfit` without structure
- `detailed patterns` without placement and density
- `futuristic glowing lines`
- `thick shoes` without sole architecture
- `many accessories` without attachment and body role
- `designer-inspired` without visible construction
- `apron-like` or `skirt-like` as a workaround for the no-skirt/no-apron rule

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

Pose selection is a mandatory two-stage lock, not a one-step category choice. Azoth must first lock exactly one broad `姿势大类`, then filter the pose stock to items whose `姿势大类` exactly matches that locked family, then lock exactly one concrete stock item from that filtered list. The final pose prose must be translated from the locked item's `描述`. Azoth must not stop after selecting only a broad family, must not invent an unstocked pose inside the family, and must not choose a concrete item from a different family after the broad family is locked. If the locked family has no viable concrete item, Azoth must explicitly reject that family, return to broad-family selection, and lock a different family before prompt writing.

Pose selection must follow this order:

1. Read the stock's structure fields when present: `姿势大类`, `身体朝向`, `重心高度`, `动势强度`, `手部策略`, and `展示风险`. If an older stock item lacks them, infer these fields from `名称`, `描述`, and `标签`.
2. Treat `姿势大类` as a broad silhouette family, not a micro-label. Valid broad families include `standing`, `walking`, `seated`, `crouching`, `kneeling`, `airborne`, `kick`, `fighting`, `lunge`, `leaning`, `shoulder_prop`, `turning_guard`, `victory`, `retreat`, and `tired`.
3. Build a family index from the available pose stock: group every concrete stock item under its exact `姿势大类`. Broad-family selection may only choose from families that have at least one concrete stock item available after hard exclusions.
4. Roll or choose the broad pose family before scoring job fit. Draw across available `姿势大类` families, not across individual stock names. This keeps the first decision about silhouette, height, and motion instead of occupation convenience.
5. Apply recent-pose cooldown to `姿势大类` before scoring job fit. Hard-exclude the last 3 used pose families when alternatives exist. Strongly downweight the last 10 used pose families.
6. Downweight `standing` as a family unless the user explicitly asks for a plain standing pose, the job absolutely needs a neutral display, or all viable non-standing families are exhausted. If the user has complained about pose sameness, side-standing, or basic standing in the current request or recent context, hard-exclude `standing` for the next pose selection when any non-standing family is viable. Do not treat side-standing, hand-on-hip, strap-holding, object-display, and relaxed-standing as meaningful pose variety from each other.
7. Treat `seated` as a special low-frequency family, not the default cure for pose sameness. Only select `seated` when the job, mood, or scene naturally provides a believable support surface or rest/work beat. If the user has complained that poses are always sitting, hard-exclude `seated` for the next 3 pose selections when alternatives exist, and strongly downweight it for the next 10. Never choose two seated poses in a row unless the user explicitly asks for sitting.
8. Downweight `展示风险: "high"` and overused hand-display strategies when alternatives exist: `forward_display`, `object_display`, `garment_display`, `pointing`, `forward_reach`, one hand extended forward, open palm presenting, pointing at the viewer, one hand holding a small object forward, or one hand gripping a chest strap while the other hand presents forward.
9. If a viable pose contains seductive-fashion signals such as hand-on-hip, hip tilt, hip cocked, crossed legs, runway pose, S-curve body, arched back, pelvis pushed forward, elegant feminine stance, or playful finger flourish, do not delete the pose outright. Translate it into a grounded masculine version: squared hips, squared shoulders, planted feet, balanced weight, no crossed legs, no exaggerated hip tilt, hand resting on belt or thumb hooked on belt instead of a fashion hand-on-hip, and stern composed body language.
10. Give priority to visibly different structures when the job allows it: `crouching`, `kneeling`, `airborne`, `kick`, `fighting`, `lunge`, `turning_guard`, `retreat`, `walking`, `shoulder_prop`, `victory`, `tired`, and only context-justified `seated`. Prefer low, airborne, kicking, crouched, turning-back, walking, or full-body action silhouettes over another side-standing or seated-rest variant.
11. After the broad family is locked, list the concrete candidates inside only that family, score 1-3 best items for job fit, cooldown, hand strategy, support-surface needs, prop compatibility, and face readability, then lock exactly one concrete stock item by `名称`. If no item inside the locked family is viable, discard the family and repeat from broad-family selection; do not fill the gap with an invented pose.
12. After choosing a concrete pose item, normalize face visibility without changing the locked body action: add a head-and-gaze clause that keeps the face readable to the viewer. For side-body, angled, walking-away, turning-back, low, or action poses, require the head to turn toward the camera in a three-quarter view and the eyes to look toward the screen/camera area. Do not let profile, looking far off-frame, looking down, or looking fully away hide the face unless the user explicitly requests that mood.
13. If the selected pose is not a presentation pose, keep occupational props on the belt, backpack, shoulder strap, leg side, chest badge, neck loop, or carried neutrally at the side instead of forcing a hand-forward display.
14. If all viable pose stock is recently used, select the least-recently used non-standing and non-seated family first; use `standing` only when every stronger silhouette is incompatible, and use `seated` only when a support surface or rest/work beat is genuinely appropriate. State the limitation in the pose reasoning log.

The selected pose description must be visibly present in `prompt_en` and `prompt_cn`. If the character's job requires a prop, the prop placement must preserve the locked pose. Do not replace the selected pose with generic phrasing such as `standing naturally with one hand forward` unless that exact pose description was selected and is not under cooldown. Keep the pose stock name in reasoning or `prompt_notes`, not in the prompt body.

When the selected pose is not a hand-forward presentation pose, add a compact negative constraint to `prompt_en`, such as `no forward presenting hand, no pointing at the viewer, no hand extended toward the camera`, while keeping the rest of the prompt positive and imageable.

When the selected pose needed the grounded-masculine correction, preserve its action but add a compact positive correction clause to `POSE_DYNAMIC`: `squared hips and shoulders, planted feet, balanced weight, stern composed stance`. Also add compact negatives: `no crossed legs, no runway pose, no S-curve body, no exaggerated hip tilt, no arched-back fashion pose`.

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
- pose structure metadata: `姿势大类`, `身体朝向`, `重心高度`, `动势强度`, `手部策略`, `展示风险`
- arm and hand placement
- gesture
- prop interaction
- body language
- action freeze-frame

Use only stock fields such as `名称`, `描述`, `标签`, `姿势大类`, `身体朝向`, `重心高度`, `动势强度`, `手部策略`, and `展示风险`. Never read or use `现场验货`, `常规描述`, source filenames, paths, raw image analysis, styling stock, makeup, facial features, face shape, complexion, grooming, or attractiveness judgments.

For the final prompt body, translate and use the selected stock's `描述`, not its `名称`, `标签`, or structure metadata. `名称`, `标签`, `姿势大类`, `身体朝向`, `重心高度`, `动势强度`, `手部策略`, and `展示风险` are for selection, matching, logs, and `提示词说明` only.

This rule applies to every final prompt body, including grooming, outfit, pose, expression, and Mirage-related prose. The final prompt must never say `uses the stock`, `based on the stock`, `from the stock`, `black-market stock`, or similar provenance wording. A clean sentence says `His hair is short, straight, fragmented, thickly lifted on top, and tightened at the sides`; it does not say `His hairstyle uses the stock "厚蓬碎短发"`.

Expression stock should appear as prompt-level performance language, not as permanent identity, face design, grooming, or beauty description.

Expression descriptions that follow the black-market five-part structure are valid prompt material: mouth shape, eyebrow/eye state, gaze, facial tension, and a reusable acting intention. Keep enough of that structure in the English prompt for the image model to perform the face; do not compress it into only the stock name.

Pose stock should appear as full-body performance language, not as clothing, anatomy redesign, multiple poses, character-sheet structure, or background action.

When both pose and expression stock are available, choose pose first, then choose an expression that supports the pose. The final combination should feel like one coherent performance beat. If they conflict, prefer the pose and select a quieter or more compatible expression.

Expression selection must apply recent-expression cooldown after the pose is locked. Never repeat the immediately previous expression stock name or near-duplicate performance beat unless the user explicitly requests it. Hard-exclude expression stock names used in the last 3 generated characters when alternatives exist, and strongly downweight expression stock names used in the last 10 generated characters. Treat strongly overlapping mouth shape, gaze direction, facial tension, and acting intention as the same performance family for downweighting, even when the stock names differ.

The pose reasoning log must name the selected pose category, note any cooldown exclusion or downweighting, and explain how occupational props were placed without overriding the locked pose. If Azoth chooses a hand-forward presentation pose, it must explicitly justify why no non-presentation candidate fit the character better.

When using black-market stock, include each selected `名称` in `提示词说明`. If no matching pose or expression stock is used, write `黑商取货：未使用` for that lane and give the concrete reason.

When black-market inventory is enabled, record the inventory-level reasoning log using only formal stock fields:

```text
[阿佐特] 黑商取货：
货道：black-market/inventory/pose.md / 姿势库存
锁定大类：<selected broad pose category>
大类内候选：<1-3 concrete pose stock names from the locked category only, or 无可用库存>
使用：<selected pose stock name or 未使用>
姿势大类：<selected broad pose category>
结构抽选：<身体朝向 / 重心高度 / 动势强度 / 手部策略 / 展示风险>
冷却处理：<excluded or downweighted recent pose categories, or none>
道具适配：<how job props preserve the locked pose instead of forcing a hand-forward display>
取货理由：<body-performance fit based on 名称, 描述, 标签, and structure metadata>
未选理由：<why other candidates fit less well>

[阿佐特] 黑商取货：
货道：black-market/inventory/expression.md / 表情库存
候选：<1-3 expression stock names or 无可用库存>
使用：<selected expression stock name or 未使用>
冷却处理：<excluded or downweighted recent expression names or performance families, or none>
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

## Design Thinking

After `prompt_cn`, generate a user-facing `设计思路` section with 6-10 numbered design notes.

These notes explain the approved design. They are not inventory, procurement leads, or `正式入库`.

Use the completed character record, Blackwall-approved design, selected black-market stock, and final prompts to describe concrete design thinking. Cover a useful mix of:

- `裁剪` / `裁片路径`
- `材质替换` / `材质行为`
- `结构事件` / `解构`
- `饰品搭配` / `道具用法`
- `层次关系` / `搭配方式`
- `巧思` / `身体适配` / `复杂度控制`

Notes should be specific, imageable, and useful for understanding why the current outfit, accessories, material choices, hairstyle, pose, or expression work together.

Never include source image names, file paths, `现场验货`, `常规描述`, raw image analysis, makeup, facial features, face shape, complexion, skin texture, attractiveness judgments, or source-derived identity/story.

## Image Generation Handoff

After `设计思路`, hand the final English prompt to the mother pipeline's Image Gen tail step. Do not remove or shorten the previous text sections.

Before Image Gen runs, the mother pipeline must load both local reference images with `view_image` and pass them as `Input image 1` and `Input image 2`:

```text
Input image 1 / style reference:
character-forge/references/assets/style_reference.png

Input image 2 / body reference:
character-forge/references/assets/width_first_body_reference.png
```

Resolve both paths relative to the workspace root when possible. If the agent is running from inside `character-forge/`, use `references/assets/style_reference.png` and `references/assets/width_first_body_reference.png`. Do not fall back to external sync folders or Windows drive paths unless the local asset is genuinely missing.

Input image 1 is allowed to guide rendering style, full-body framing, line weight, flat cel-shading, clean white background, and crisp anime readability. Input image 2 is allowed to guide width-first grounded body proportion, simplified muscle anatomy, stable stance, broad muscle mass, compact heavy silhouette, and a hard segmented abdominal read. Neither reference may override the approved character record, selected black-market stock, outfit, temperament, grooming, pose, expression, prompt content, or source-character separation. Broad face-shape direction and simplified facial proportions may be style-adjacent, but the generated face must read as a new person, not the same face or a recognizable identity match to either reference. If the torso projects forward, it must still read as ribcage pressure and stacked abdominal blocks, never as a soft pot belly, round smooth stomach, sagging abdomen, or unsegmented convex belly.

When handing off to Image Gen, wrap `prompt_en` with:

```text
<the exact wrapper from references/prompt_blocks/imagegen-wrapper.md>
```

Keep `prompt_en` compatible with that wrapper: avoid painterly, semi-realistic, rendered, detailed skin, gritty, textured, cinematic, volumetric, or realistic material language unless the user explicitly asks for that style.
