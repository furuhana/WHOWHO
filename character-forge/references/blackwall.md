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

## First Gate: Reasonableness and Animation Design

Check:

- Does the character read as an animation character design rather than random real-life details?
- Do occupation, gang, outfit, hairstyle, beard, and face shape support the same character?
- Does the body preserve the fixed standard: width-first and grounded, around 6.2-6.6 heads tall, dramatically broad and heavily muscled, shoulder span much wider than hips, short thick neck buried between huge traps, enormous deltoids, huge chest shelf, thick barrel torso, large arms like pillars, huge forearms, oversized heavy hands, very thick thighs, natural but not long legs, large heavy feet, and a compact head?
- Does eyebrow language stay at static eyebrow shape, without turning into eye shape, gaze, expression acting, makeup, attractiveness, or detailed facial-feature wording?
- Does face-shape and facial-proportion language stay stylized, character-owned, and broad enough for animation design, without turning into copied reference-face identity, exact feature arrangement, recognizable likeness, or realistic face reconstruction?
- If visible white socks are part of the outfit, are they plain solid white, and if long pants are used, do the trouser hems use a natural 9.5-length cut that reveals the socks at the shoe opening without becoming joggers, tight tapered hems, elastic cuffs, leggings-like pants, or pants tucked into socks?
- Does the final pose preserve face readability for the viewer, with the head turned enough to show the face and the eyes looking toward the screen, the camera, or very near the camera? Side-body, side-face, turning-back, walking-away, low, or action poses should still keep a readable three-quarter head angle unless the user explicitly requests a hidden-face or off-frame gaze.
- Does the inner base layer visibly wrap the chest and abdominal muscle contour with clean animation lines, unless the user explicitly requested otherwise?
- Do the torso lines read as huge pectoral and abdominal anatomy pressing through the fitted base layer, rather than as generic fabric folds or bunched cloth?
- Is the composition a single full-body character on a pure white background, with no multi-character layout, panels, split views, turnarounds, callout boxes, or character-sheet structure?
- If Mirage / 蜃楼 will be used after Azoth, does the planned platform language stay compatible with flat 2D anime cel-shading, without inducing a 3D render, toy figurine, physical model base, collectible statue, or miniature diorama render?
- Is anything visually abrupt without a useful reason?
- Is the outfit clean and readable?
- Are there enough distinctive visual hooks for image generation?
- If black-market stock was used, did each module use only formal stock from its allowed category?
- If black-market inventory was enabled, did each relevant module provide a `黑商取货` log with lane, candidates, selected stock, selection reason, and rejection reason?
- If 三宅 used black-market styling stock, did the `黑商取货` log include a clear use strategy (`完整套装继承`, `局部单品借用`, `只继承搭配方法`, or `未使用`) and inherited outfit strengths based only on formal stock fields?
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
- If `黑商商机` is present, is it clearly non-inventory and free of black-market forbidden source or appearance leakage?

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
- loose, boxy, or baggy inner base layers that hide the fixed chest and abdominal silhouette when no override was requested
- jogger cuffs, elastic ankle cuffs, overly tight tapered pants, pants tucked into socks, sock-like leggings, long pants hiding the socks completely instead of using a natural 9.5-length trouser break, striped white socks, ribbed vertical sock patterns, colored sock bands, sock logos, or sock text when the user only asked for visible white socks
- torso linework that reads mainly as cloth folds, wrinkles, or bunching instead of large underlying pectoral and abdominal muscle forms
- multiple characters, multiple poses, front-side-back turnarounds, segmented character sheets, panel layouts, callout boxes, background scenes, or non-white backgrounds unless the user explicitly asks for them
- Mirage / 蜃楼 platform wording that pushes the image toward 3D rendering, toy figurine presentation, physical model bases, collectible statues, miniature diorama renders, plastic/resin product photography, or any non-flat 2D anime cel-shading result
- dirty, oily, greasy, stained, muddy, or unclean materials
- clothing materials shown mainly through printed texture, dense texture maps, micro-weave details, small speckles, or other visual noise
- cotton, linen, or similar fabric described in a way that would create tiny noisy surface detail instead of clean animation shapes
- black-market `现场验货`, `常规描述`, source filenames, paths, or raw image analysis leaking into the character record or prompt
- black-market inventory content outside `正式入库` being used as stock
- black-market styling stock used as expression, expression stock used as styling or pose, pose stock used as styling or face design, hairstyle stock used for beard, eyebrows, face shape, facial features, makeup, complexion, or attractiveness, or eyebrow stock used for hairstyle, beard, eye shape, expression acting, face shape, facial features, makeup, complexion, or attractiveness
- black-market pose stock that creates multiple poses, front-side-back turnarounds, segmented character sheets, panel layouts, callout boxes, background scenes, anatomy redesign, or action clutter instead of one clear full-body pose
- black-market pose stock being available but Azoth omitting pose selection, failing to name the selected pose, or replacing the selected pose with generic prompt language
- repeated use of the same recent pose category when viable alternatives exist, especially one hand extended forward, open palm presenting, pointing, hand-forward small-object display, or chest-strap grip plus hand-forward presentation
- occupation props forcing the hands back into a forward display pose when the selected pose could carry props on the belt, backpack, strap, leg side, chest badge, neck loop, or neutral side carry
- any black-market stock that introduces makeup, facial feature description, complexion, face-centered aesthetic judgment, dirty material, forbidden occupation, forbidden setting, or noisy texture detail
- black-market styling stock deciding, boosting, replacing, or retroactively changing the occupation
- changing the occupation because a black-market outfit has a stronger fit to another job
- rerolling an unspecified random occupation because the character stats, outfit library, or prompt clarity make another job easier
- repeating the same exact shoe stock or specific shoe description from recent generations when viable alternatives exist, especially repeated default white sneakers or thick-soled shoes, unless the user explicitly requests that shoe or the job has no believable alternative
- repeating `wedding photographer`, `photographer`, or `婚庆摄影师` during recent-history cooldown unless the user explicitly names that job
- curly, curled, coiled, ringlet, wavy, wave-like, 卷发, 卷曲, 波浪发, or similar hairstyle directions; if Tony or black-market hairstyle stock selects curled/wavy hair, reject and reroute to Tony for a non-curly hairstyle
- `黑商取货` reasoning that mentions source images, filenames, paths, `现场验货`, `常规描述`, raw image analysis, facial features, complexion, makeup, attractiveness judgments, or identity/story inferred from the source
- 三宅 `黑商取货` reasoning that invents outfit strengths from source context instead of deriving them from formal stock fields such as `名称`, `类别`, `描述`, `标签`, and `包含单品`
- Azoth expression and pose selection that visually contradict each other, unless the contradiction is explicit, useful, and still readable as one single-character performance
- `黑商商机` being described as already入库, `正式入库`, or using source images, filenames, paths, `现场验货`, `常规描述`, raw image analysis, facial features, complexion, makeup, attractiveness judgments, or identity/story inferred from a source

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
    - module: bole|sanzhai|tony|azoth|multiple
      reason:
      reroute_to:
  integrated_design:
```

If failed, give precise reroute instructions. Do not rewrite every module when only one module caused the issue.
