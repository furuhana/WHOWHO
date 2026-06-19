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
- Does the body preserve the fixed standard: very tall, extremely broad-shouldered, heavily muscular, thick neck, powerful torso, large arms, heavy limbs, compact head relative to body?
- Does eyebrow language stay at static eyebrow shape, without turning into eye shape, gaze, expression acting, makeup, attractiveness, or detailed facial-feature wording?
- Does face-shape language stay at broad head silhouette and jaw/chin mass, without permanent eye shape or detailed facial-feature wording?
- Does the inner base layer visibly wrap the chest and abdominal muscle contour with clean animation lines, unless the user explicitly requested otherwise?
- Do the torso lines read as huge pectoral and abdominal anatomy pressing through the fitted base layer, rather than as generic fabric folds or bunched cloth?
- Is the composition a single full-body character on a pure white background, with no multi-character layout, panels, split views, turnarounds, callout boxes, or character-sheet structure?
- Is anything visually abrupt without a useful reason?
- Is the outfit clean and readable?
- Are there enough distinctive visual hooks for image generation?
- If black-market stock was used, did each module use only formal stock from its allowed category?
- If black-market inventory was enabled, did each relevant module provide a `黑商取货` log with lane, candidates, selected stock, selection reason, and rejection reason?
- If Azoth selected both pose and expression stock, do they support one coherent performance beat without conflicting body language or facial acting?
- If Azoth used black-market expression stock, preserve valid five-part expression descriptions as prompt-useful material when they contain mouth shape, eyebrow/eye state, gaze, facial tension, and reusable acting intention.
- If `黑商商机` is present, is it clearly non-inventory and free of black-market forbidden source or appearance leakage?

## Second Gate: Forbidden Directions

Reject or reroute if the result contains:

- shipbuilding-related occupations or visuals
- dock-related occupations or visuals
- cargo loading or unloading jobs
- hard manual labor / coolie-like direction
- fitness coach occupation
- slim, average, lanky, lightly athletic, or small body proportions when the fixed body standard should apply
- eyebrow wording that changes eye shape or face style, including willow-leaf eyebrows, thin eyebrows, long slender eyebrows, delicate eyebrows, realistic eyebrow hair flow, close-to-eye eyebrows, makes the eyes narrow, sharp eye shape, 柳叶眉, 细眉, 修长眉, 精致眉, 写实毛流, 贴眼眉, 让眼睛变窄, or 锐利眼型
- permanent eye shape or detailed face-shape wording that changes the base anime style, including long face, narrow eyes, small eyes, sharp nose, high cheekbones, thin lips, delicate features, realistic facial features, detailed facial structure, 长脸, 窄眼, 小眼, 尖鼻, 高颧骨, 薄唇, 精致五官, 写实五官, or 详细五官结构
- loose, boxy, or baggy inner base layers that hide the fixed chest and abdominal silhouette when no override was requested
- torso linework that reads mainly as cloth folds, wrinkles, or bunching instead of large underlying pectoral and abdominal muscle forms
- multiple characters, multiple poses, front-side-back turnarounds, segmented character sheets, panel layouts, callout boxes, background scenes, or non-white backgrounds unless the user explicitly asks for them
- dirty, oily, greasy, stained, muddy, or unclean materials
- clothing materials shown mainly through printed texture, dense texture maps, micro-weave details, small speckles, or other visual noise
- cotton, linen, or similar fabric described in a way that would create tiny noisy surface detail instead of clean animation shapes
- black-market `现场验货`, `常规描述`, source filenames, paths, or raw image analysis leaking into the character record or prompt
- black-market inventory content outside `正式入库` being used as stock
- black-market styling stock used as expression, expression stock used as styling or pose, pose stock used as styling or face design, hairstyle stock used for beard, eyebrows, face shape, facial features, makeup, complexion, or attractiveness, or eyebrow stock used for hairstyle, beard, eye shape, expression acting, face shape, facial features, makeup, complexion, or attractiveness
- black-market pose stock that creates multiple poses, front-side-back turnarounds, segmented character sheets, panel layouts, callout boxes, background scenes, anatomy redesign, or action clutter instead of one clear full-body pose
- any black-market stock that introduces makeup, facial feature description, complexion, face-centered aesthetic judgment, dirty material, forbidden occupation, forbidden setting, or noisy texture detail
- curly, curled, coiled, ringlet, wavy, wave-like, 卷发, 卷曲, 波浪发, or similar hairstyle directions; if Tony or black-market hairstyle stock selects curled/wavy hair, reject and reroute to Tony for a non-curly hairstyle
- `黑商取货` reasoning that mentions source images, filenames, paths, `现场验货`, `常规描述`, raw image analysis, facial features, complexion, makeup, attractiveness judgments, or identity/story inferred from the source
- Azoth expression and pose selection that visually contradict each other, unless the contradiction is explicit, useful, and still readable as one single-character performance
- `黑商商机` being described as already入库, `正式入库`, or using source images, filenames, paths, `现场验货`, `常规描述`, raw image analysis, facial features, complexion, makeup, attractiveness judgments, or identity/story inferred from a source

Important distinction: muscular or strongly built body types are allowed and may be preferred. Reject only when the system turns muscularity into forbidden jobs, dirty labor aesthetics, or gym-coach identity.

Material distinction: cotton, linen, and other natural fabric concepts are allowed only when expressed through color, simple silhouette, broad panels, and clean flat areas. Reject or reroute if the design asks image generation to render fine fabric grain, tiny prints, or texture-map-like surface detail on clothing.

Expression whitelist: black-market expression descriptions are not invalid just because they include acting phrases such as `像是在提醒`, `像是在读场`, `像是在讲解`, or `像是在护场`. Allow them when they are grounded in visible mouth shape, eyebrow/eye state, gaze, and facial tension, and when they do not introduce identity, source story, makeup, facial features, complexion, attractiveness judgments, multiple characters, background scenes, or forbidden occupations.

Expression distinction: allow temporary gaze, eyelid state, brow movement, mouth state, and facial tension as performance language. Reject only when expression wording becomes permanent eye shape, face shape, or detailed facial structure.

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
