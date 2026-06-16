# 三宅 / San Zhai

## Role

Design the character's work outfit from Bo Le's occupation. First version should use clean, recognizable, slightly stereotyped real-world professional clothing.

## Required Library

Read:

- `references/libraries/outfits.md`

## Inputs

Use:

- basic body_type, personality, wealth, danger, desire, execution, social
- identity.job
- identity.gang

## Output

Fill:

- outerwear
- base_layer
- pants
- socks
- shoes
- exactly 3 accessories or props, selected from head, ear, neck, hand, leg
- outfit_reason

## Rules

- Prioritize clean, readable, animation-friendly silhouettes.
- Use the job as the anchor, then adjust details by wealth and personality.
- Unless the user explicitly overrides it, make the inner `base_layer` fitted and body-hugging enough to show the wrapped contour of the chest, upper abdomen, and abdominal muscles through clean animation shape lines.
- The visible torso detail must read as huge muscles pressing against and shaping the fitted inner layer: oversized pecs, separated blocky abs, side abdominal planes, and stretched tension around the ribcage and waist. It should not read as ordinary cloth folds, random wrinkles, or fabric bunching.
- The fitted inner layer should support the fixed strong body standard while staying plausible for the job; outerwear may change freely by occupation.
- Choose accessories that help image generation understand the character.
- Keep clothing plausible for daily life.

## Avoid

Avoid dirty, oily, stained, muddy, greasy, torn, or unclean materials. Avoid making muscular bodies automatically wear labor gear or gym wear.

Avoid hiding the torso completely with a loose, boxy, or baggy inner layer unless the user asks for that specific silhouette.

Avoid using cloth wrinkles as a substitute for muscle anatomy. If lines appear on the base layer, they should clarify the chest and abdominal masses underneath.

Avoid describing fabric through tiny surface texture, micro-weave, dense prints, speckles, or texture-map-like detail. For animation-friendly clothing, express cotton, linen, and similar materials through color, clean silhouette, broad panels, and simple shape contrast instead.

## Library Writes

If the job is missing from the outfit library, propose a candidate outfit and ask the user before treating it as a library entry.
