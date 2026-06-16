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
- Choose accessories that help image generation understand the character.
- Keep clothing plausible for daily life.

## Avoid

Avoid dirty, oily, stained, muddy, greasy, torn, or unclean materials. Avoid making muscular bodies automatically wear labor gear or gym wear.

## Library Writes

If the job is missing from the outfit library, propose a candidate outfit and ask the user before treating it as a library entry.
