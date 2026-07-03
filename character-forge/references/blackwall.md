# 黑墙 / Blackwall

## Role

Audit the combined character before prompt generation. Blackwall is a design gate, not a creativity module.

## Required Library

Read:

- `references/libraries/forbidden.md`

## Inputs

Use all fields from:

- Da Men
- Bo Le
- San Zhai
- Tony
- Muse / 缪斯

## First Gate: Reasonableness and Animation Design

Check:

- Does the character read as an animation character design rather than random real-life details?
- If Da Men provided `world_context`, did later modules use it as visible everyday-world guidance rather than lore, background scenery, or an excuse to change the character's occupation after selection?
- Do occupation, gang, outfit, hairstyle, beard, and face shape support the same character?
- Does the body preserve the fixed standard: width-first and grounded, around 6.2-6.6 heads tall, dramatically broad and heavily muscled, shoulder span much wider than hips, short thick neck buried between huge traps, enormous deltoids, huge chest shelf, thick barrel torso, large arms like pillars, huge forearms, oversized heavy hands, very thick thighs, natural but not long legs, large heavy feet, and a compact head?
- Does eyebrow language stay at static eyebrow shape, without turning into eye shape, gaze, expression acting, makeup, attractiveness, or detailed facial-feature wording?
- Does face-shape and facial-proportion language stay stylized, character-owned, and broad enough for animation design, without turning into copied reference-face identity, exact feature arrangement, recognizable likeness, or realistic face reconstruction?
- If `temperament` exists, did Tony use it to create character-owned face/grooming variation instead of leaving the broad face read too close to either reference image?
- If visible white socks are part of the outfit, are they plain solid white, and if any non-short pants are used, do the hems use a natural 9-length cut that reveals the socks at the shoe opening without becoming full-length trousers, mid-calf capri pants, seven-tenths pants, joggers, tight tapered hems, elastic cuffs, leggings-like pants, or pants tucked into socks?
- Does the final pose preserve face readability for the viewer, with the head turned enough to show the face and the eyes looking toward the screen, the camera, or very near the camera? Side-body, side-face, turning-back, walking-away, low, or action poses should still keep a readable three-quarter head angle unless the user explicitly requests a hidden-face or off-frame gaze.
- Does the inner base layer visibly wrap the chest and abdominal muscle contour with clean animation lines, unless the user explicitly requested otherwise?
- Do the torso lines read as huge pectoral and abdominal anatomy pressing through the fitted base layer, rather than as generic fabric folds or bunched cloth?
- Is the composition a single full-body character on a pure white background, with no multi-character layout, panels, split views, turnarounds, callout boxes, or character-sheet structure?
- If Mirage / 蜃楼 will be used after Azoth, does the planned platform language stay compatible with flat 2D anime cel-shading, without inducing a 3D render, toy figurine, physical model base, collectible statue, or miniature diorama render?
- Is anything visually abrupt without a useful reason?
- Is the outfit clean and readable?
- Does the outfit obey the Garment Grammar ban: no skirt, dress, apron, pinafore, wrap skirt, skirt-over-pants, or apron-like front panel unless the user explicitly overrode it?
- Are there enough distinctive visual hooks for image generation?
- Did San Zhai record a concrete `styling_algorithm`, active `design_function_slots`, `replacement_slots_used`, `variation_matrix`, and `anti_default_decision`?
- If Garment Grammar is available, did San Zhai record `garment_line`, `banned_shape_check`, `professional_keywords`, and `negative_clothing`?
- If the shared prototype libraries are available, did San Zhai record a precise `outer_shell_prototype` when any outer layer is present, rather than ending with generic jacket/coat/vest/hoodie/shirt-jacket wording?
- Did San Zhai record exactly one primary `structural_event` and zero or one supporting `material_behavior`, with visible part, mechanism, and body/role purpose?
- If a shirt-like garment is present, did San Zhai record `anti_shirt_jacket_default` naming the non-shirt carrier that prevents the design from collapsing into shirt/jacket print decoration?
- Did San Zhai record a readable `base_garment_prototype`, anonymous `designer_method_references`, concrete `design_operators`, `panel_paths`, `pattern_strategy`, `craft_boundaries`, `body_fit_strategy`, `complexity_budget`, and `design_failure_avoidance` when advanced design grammar is available?
- If the user allowed designer prompt references, are `designer_prompt_references` short, optional, and backed by visible construction rather than used as a substitute for garment detail?
- Does at least one clothing, footwear, or accessory element have a clear panel/cutting path with start point, route, endpoint, and rule?
- Is patterning controlled by placement and density rather than full-body tiny marks, random lines, or noisy texture?
- Do shoes include a readable prototype plus sole structure, upper cutting, cuff/sock/trouser connection, and center-of-gravity role rather than only being called thick shoes?
- Do accessories alter shoulder width, waist split, hand/arm mass, leg weight, head/neck frame, or role readability rather than floating as decorative extras?
- Does the outfit roughly preserve the complexity budget of large silhouette 60%, medium panels 25%, small craft 10%, and pattern/symbol 5%?
- If `world_context` exists, did San Zhai translate era, culture, street texture, technology, order, material ecology, and visual taboo into visible outfit decisions?
- If a shirt-like base layer is present, does another visible system carry the main outfit idea, such as outer volume, waist structure, head/neck structure, hand/arm gear, leg structure, markers, material contrast, or functional mounted objects?
- Did Muse explicitly pass or accept the outfit's styling algorithm, replacement-slot use, anti-default behavior, and world-context translation instead of only judging generic clothing coherence?
- If black-market stock was used, did each module use only formal stock from its allowed category?
- If 缪斯 was run, did it pass or explicitly accept only minor outfit-quality issues as `勉强通过` before Blackwall?
- If black-market inventory was enabled, did each relevant module provide a `黑商取货` log with lane, candidates, selected stock, selection reason, and rejection reason?
- If 三宅 used black-market styling stock, did the `黑商取货` log include a clear use strategy (`完整套装继承`, `局部单品借用`, `只继承搭配方法`, or `未使用`) and inherited outfit strengths based only on formal stock fields?
- Did San Zhai apply outfit cooldown before final styling selection, hard-excluding the last 3 recent set names and primary styling algorithms when alternatives exist, strongly downweighting the last 10, and recording cooldown handling in `黑商取货`?
- Did Bo Le choose the occupation before black-market inventory was considered?
- If no occupation was specified, did Bo Le preserve the fair random draw instead of rerolling toward a more compatible, easier, or recently repeated job?
- Did black-market styling stock serve the already selected occupation instead of causing the role to drift toward a better-stocked job?
- Did San Zhai apply footwear cooldown when viable alternatives exist, avoiding exact repeated shoe stock or specific shoe descriptions from recent generations while preserving occupation-needed footwear categories?
- If Azoth selected both pose and expression stock, do they support one coherent performance beat without conflicting body language or facial acting?
- If black-market pose stock exists, did Azoth select and lock one pose stock item before prompt writing, rather than inventing or defaulting to a generic display pose?
- Did Azoth record the selected pose stock name, broad pose category, cooldown handling, and prop-placement adaptation in the reasoning or prompt notes?
- If the selected pose is not a presentation pose, does the prompt preserve that body language and include a compact negative constraint against forward hand presentation, pointing at the viewer, or a hand extended toward the camera?
- If the selected pose angles the body sideways or away from the viewer, did Azoth add a head-and-gaze clause that keeps the face visible and keeps the eyes toward the viewer or just beside the camera?
- If Azoth used black-market expression stock, preserve valid five-part expression descriptions as prompt-useful material when they contain mouth shape, eyebrow/eye state, gaze, facial tension, and reusable acting intention.
- If `设计思路` is present, does it explain concrete design moves without becoming inventory procurement, source provenance, or appearance leakage?

## Second Gate: Forbidden Directions

Reject or reroute if the result contains:

- shipbuilding-related occupations or visuals
- dock-related occupations or visuals
- cargo loading or unloading jobs
- hard manual labor / coolie-like direction
- fitness coach occupation
- slim, average, lanky, lightly athletic, small, tall-and-fit, normally proportioned hero, or merely athletic body proportions when the fixed body standard should apply
- pure side profile, hidden face, head turned fully away, eyes looking far off-frame, sustained downward gaze hiding the eyes, or any side-body pose that fails to add a readable three-quarter face and camera-near gaze, unless the user explicitly asks for a hidden-face or avoidant-gaze image
- overly tall, towering-giant, stretched vertical proportions, normal 7-head tall hero proportions, narrow shoulders, insufficient chest/back width, excessively long legs, or an excessively shrunken head when the fixed width-first super-heavyweight body standard should apply
- eyebrow wording that changes eye shape or face style, or that specifies eyebrow color, including willow-leaf eyebrows, thin eyebrows, long slender eyebrows, delicate eyebrows, realistic eyebrow hair flow, close-to-eye eyebrows, makes the eyes narrow, sharp eye shape, white eyebrows, black eyebrows, blond eyebrows, gray eyebrows, 柳叶眉, 细眉, 修长眉, 精致眉, 写实毛流, 贴眼眉, 让眼睛变窄, 锐利眼型, 白眉, 白色眉, 黑眉, 金眉, 灰眉, or any eyebrow color label
- facial wording that copies a reference face as the same recognizable person, exact feature arrangement, source-character likeness, celebrity likeness, identity match, or realistic face reconstruction. Broad stylized face shape and simplified facial proportions are allowed when they belong to the approved character design instead of the reference identity.
- missing, ignored, or purely abstract `temperament` when the generated face/grooming would otherwise read too close to the reference face; reroute to Tony or Azoth to translate temperament into broad face silhouette, hairstyle, static eyebrow shape, beard pressure, or expression performance
- loose, boxy, or baggy inner base layers that hide the fixed chest and abdominal silhouette when no override was requested
- jogger cuffs, elastic ankle cuffs, overly tight tapered pants, pants tucked into socks, sock-like leggings, full-length trousers, mid-calf capri pants, seven-tenths pants, non-short pants hiding the socks completely instead of using a natural 9-length trouser break, striped white socks, ribbed vertical sock patterns, colored sock bands, or sock logos when the user only asked for visible white socks
- torso linework that reads mainly as cloth folds, wrinkles, or bunching instead of large underlying pectoral and abdominal muscle forms
- multiple characters, multiple poses, front-side-back turnarounds, segmented character sheets, panel layouts, callout boxes, background scenes, or non-white backgrounds unless the user explicitly asks for them
- Mirage / 蜃楼 platform wording that pushes the image toward 3D rendering, toy figurine presentation, physical model bases, collectible statues, miniature diorama renders, plastic/resin product photography, or any non-flat 2D anime cel-shading result
- dirty, oily, greasy, stained, muddy, or unclean materials
- skirts, dresses, aprons, pinafores, wrap skirts, skirt-over-pants structures, apron-like front panels, maid outfits, school uniform skirts, or any lower/front garment described with skirt/apron language, unless the user explicitly overrides the no-skirt/no-apron rule
- default outfit wording that implies aged, damaged, gritty, or worn-down clothing, including faded, worn, weathered, scuffed, dusty, frayed, distressed, rough texture, visible fabric grain, speckled surface, or noisy weave, unless the user explicitly requests that direction and it remains clean enough for flat anime cel-shading
- clothing materials shown mainly through printed texture, dense texture maps, micro-weave details, small speckles, or other visual noise
- cotton, linen, or similar fabric described in a way that would create tiny noisy surface detail instead of clean animation shapes
- black-market `现场验货`, `常规描述`, source filenames, paths, or raw image analysis leaking into the character record or prompt
- black-market inventory content outside `正式入库` being used as stock
- black-market styling stock used as expression, expression stock used as styling or pose, pose stock used as styling or face design, hairstyle stock used for beard, eyebrows, face shape, facial features, makeup, complexion, or attractiveness, or eyebrow stock used for hairstyle, beard, eye shape, expression acting, face shape, facial features, makeup, complexion, or attractiveness
- San Zhai output that lacks a styling algorithm, lacks functional-slot reasoning, or cannot explain why this outfit is not just another occupation-locked shirt formula
- San Zhai output that uses `shirt`, `jacket`, `coat`, `vest`, `hoodie`, `pants`, `shoes`, or `bag` as final prototypes instead of precise base and outer-shell prototypes, unless the user explicitly requested plain clothing
- San Zhai output with an outer layer but no precise `outer_shell_prototype`, or a final outer layer that remains a generic jacket/coat/vest/hoodie/shirt-jacket
- San Zhai output that claims deconstruction, structural fashion, or material replacement but lacks a named `structural_event` and `material_behavior` with visible mechanism
- San Zhai output that uses transparent material as the entire material idea without saying what the transparent layer reveals, seals, supports, protects, or changes
- San Zhai output that stacks multiple primary structure events, such as offset entry plus inside-out plus sealed pockets plus single-sheet wrap plus body hardware focal point, until the outfit becomes unreadable
- San Zhai output that uses an apron as the default solution for service, food, craft, vendor, or workshop jobs instead of replacing that function with a vest, belt, harness, structured overshirt, protective placket, trouser pouch, or crossbody tool bag
- San Zhai output that uses designer names as the actual design instead of anonymous methods and visible construction, unless the user explicitly allowed short designer prompt references and the outfit still has full structural description
- San Zhai output that records designer prompt references but lacks concrete design operators, panel paths, craft boundaries, footwear structure, or body-fit strategy
- San Zhai output that claims complex cutting, paneling, trimming, patterning, deconstruction, pleating, drape, or sculptural footwear but cannot name where it starts, how it travels, where it ends, and what body or role function it serves
- outfit complexity that reads as full-body random lines, all-over tiny patterns, fake cyber glow, texture-map fabric, equal-detail noise, or surface graphics pasted over joints
- panel lines that cut across elbows, knees, ankles, chest, or abdomen as unbroken surface graphics instead of breaking, turning, or serving body structure
- footwear that is only described as thick-soled, heavy, futuristic, or stylish without sole sidewall, outsole segmentation, heel/arch structure, upper paneling, or trouser/sock connection
- accessories that are only decorative hanging objects without a clear attachment point, shape, body-reading role, or occupation cue
- complexity budget missing or obviously inverted so that tiny marks and symbols dominate the outfit while silhouette and medium panel structure disappear
- `world_context` used as lore, background scenery, source identity, or faction story instead of compact everyday-world constraints
- `world_context` causing Bo Le to invent jobs outside the jobs library, reroll a fair job draw, or drift into forbidden dock, cargo, heavy manual labor, or fitness-coach directions
- `world_context.visual_taboo` being ignored when it bans ordinary shirt lock-in, dirty materials, heavy military drift, dock/cargo drift, over-cyberpunk excess, or other local constraints
- San Zhai outfit output that receives world context but shows no visible translation through material ecology, street accessories, order markers, cultural construction, technology level, or taboo avoidance
- a shirt, button-up, T-shirt, polo, undershirt, or service-uniform shirt becoming the primary visual when no compensating outerwear, harness, armor, vest, structured overshirt, waist system, head/neck system, hand/arm system, leg system, marker system, material contrast, or prop system carries the design
- `anti_default_decision` that merely says the job requires a shirt without naming visible compensating structures, unless the user explicitly requested a plain shirt outfit
- `variation_matrix` missing from San Zhai when the outfit otherwise collapses into the same occupational default
- black-market pose stock that creates multiple poses, front-side-back turnarounds, segmented character sheets, panel layouts, callout boxes, background scenes, anatomy redesign, or action clutter instead of one clear full-body pose
- black-market pose stock being available but Azoth omitting pose selection, failing to name the selected pose, or replacing the selected pose with generic prompt language
- repeated use of the same recent pose category when viable alternatives exist, especially one hand extended forward, open palm presenting, pointing, hand-forward small-object display, or chest-strap grip plus hand-forward presentation
- occupation props forcing the hands back into a forward display pose when the selected pose could carry props on the belt, backpack, strap, leg side, chest badge, neck loop, or neutral side carry
- any black-market stock that introduces makeup, facial feature description, complexion, face-centered aesthetic judgment, dirty material, forbidden occupation, forbidden setting, or noisy texture detail
- black-market styling stock deciding, boosting, replacing, or retroactively changing the occupation
- changing the occupation because a black-market outfit has a stronger fit to another job
- repeating the same recent black-market套装货 name, primary styling algorithm, or primary visual carrier while viable alternatives exist, or omitting outfit cooldown handling from `黑商取货`
- rerolling an unspecified random occupation because the character stats, outfit library, or prompt clarity make another job easier
- repeating the same exact shoe stock or specific shoe description from recent generations when viable alternatives exist, especially repeated default white sneakers or thick-soled shoes, unless the user explicitly requests that shoe or the job has no believable alternative
- repeating `wedding photographer`, `photographer`, or `婚庆摄影师` during recent-history cooldown unless the user explicitly names that job
- curly, curled, coiled, ringlet, wavy, wave-like, 卷发, 卷曲, 波浪发, or similar hairstyle directions; if Tony or black-market hairstyle stock selects curled/wavy hair, reject and reroute to Tony for a non-curly hairstyle
- `黑商取货` reasoning that mentions source images, filenames, paths, `现场验货`, `常规描述`, raw image analysis, facial features, complexion, makeup, attractiveness judgments, or identity/story inferred from the source
- 三宅 `黑商取货` reasoning that invents outfit strengths from source context instead of deriving them from formal stock fields such as `名称`, `类别`, `描述`, `标签`, and `包含单品`
- Azoth expression and pose selection that visually contradict each other, unless the contradiction is explicit, useful, and still readable as one single-character performance
- `设计思路` being described as already入库, `正式入库`, future procurement leads, or using source images, filenames, paths, `现场验货`, `常规描述`, raw image analysis, facial features, complexion, makeup, attractiveness judgments, or identity/story inferred from a source

Important distinction: muscular or strongly built body types are allowed and may be preferred. Reject only when the system turns muscularity into forbidden jobs, dirty labor aesthetics, or gym-coach identity.

Material distinction: cotton, linen, and other natural fabric concepts are allowed only when expressed through color, simple silhouette, broad panels, and clean flat areas. Reject or reroute if the design asks image generation to render fine fabric grain, tiny prints, or texture-map-like surface detail on clothing.

Expression whitelist: black-market expression descriptions are not invalid just because they include acting phrases such as `像是在提醒`, `像是在读场`, `像是在讲解`, or `像是在护场`. Allow them when they are grounded in visible mouth shape, eyebrow/eye state, gaze, and facial tension, and when they do not introduce identity, source story, makeup, facial features, complexion, attractiveness judgments, multiple characters, background scenes, or forbidden occupations.

Expression distinction: allow temporary gaze, eyelid state, brow movement, mouth state, and facial tension as performance language. Reject only when expression wording becomes permanent identity copying, source-face likeness, or detailed realistic facial reconstruction.

Eyebrow distinction: allow static eyebrow shape from Tony or `眉型库存`, and allow temporary brow movement from expression stock. Reject only when eyebrow wording becomes eye shape, makeup, attractiveness, thin/willow-leaf styling, realistic hair-flow detail, or detailed facial-feature structure.

## Output

Fill:

```yaml
blackwall:
  passed: true/false
  issues:
    - module: bole|sanzhai|tony|muse|azoth|multiple
      reason:
      reroute_to:
  integrated_design:
```

If failed, give precise reroute instructions. Do not rewrite every module when only one module caused the issue.
