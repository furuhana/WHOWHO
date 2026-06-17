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
- Does the inner base layer visibly wrap the chest and abdominal muscle contour with clean animation lines, unless the user explicitly requested otherwise?
- Do the torso lines read as huge pectoral and abdominal anatomy pressing through the fitted base layer, rather than as generic fabric folds or bunched cloth?
- Is the composition a single full-body character on a pure white background, with no multi-character layout, panels, split views, turnarounds, callout boxes, or character-sheet structure?
- Is anything visually abrupt without a useful reason?
- Is the outfit clean and readable?
- Are there enough distinctive visual hooks for image generation?
- If black-market stock was used, did each module use only formal stock from its allowed category?

## Second Gate: Forbidden Directions

Reject or reroute if the result contains:

- shipbuilding-related occupations or visuals
- dock-related occupations or visuals
- cargo loading or unloading jobs
- hard manual labor / coolie-like direction
- fitness coach occupation
- slim, average, lanky, lightly athletic, or small body proportions when the fixed body standard should apply
- loose, boxy, or baggy inner base layers that hide the fixed chest and abdominal silhouette when no override was requested
- torso linework that reads mainly as cloth folds, wrinkles, or bunching instead of large underlying pectoral and abdominal muscle forms
- multiple characters, multiple poses, front-side-back turnarounds, segmented character sheets, panel layouts, callout boxes, background scenes, or non-white backgrounds unless the user explicitly asks for them
- dirty, oily, greasy, stained, muddy, or unclean materials
- clothing materials shown mainly through printed texture, dense texture maps, micro-weave details, small speckles, or other visual noise
- cotton, linen, or similar fabric described in a way that would create tiny noisy surface detail instead of clean animation shapes
- black-market `现场验货`, `常规描述`, source filenames, paths, or raw image analysis leaking into the character record or prompt
- `black-market/inventory.md` content outside `正式入库` being used as stock
- black-market styling stock used as expression, expression stock used as styling, or hairstyle stock used for beard, face shape, facial features, makeup, complexion, or attractiveness
- any black-market stock that introduces makeup, facial feature description, complexion, face-centered aesthetic judgment, dirty material, forbidden occupation, forbidden setting, or noisy texture detail

Important distinction: muscular or strongly built body types are allowed and may be preferred. Reject only when the system turns muscularity into forbidden jobs, dirty labor aesthetics, or gym-coach identity.

Material distinction: cotton, linen, and other natural fabric concepts are allowed only when expressed through color, simple silhouette, broad panels, and clean flat areas. Reject or reroute if the design asks image generation to render fine fabric grain, tiny prints, or texture-map-like surface detail on clothing.

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
