---
name: mirage
description: "Floating scene-slice prompt post-processor for character generation. Use when Codex needs to convert an approved character prompt into a gacha-card style miniature platform: one coherent floating cross-section scene, solid themed ground, 2-3 rooted environmental props, pure white isolation, and negative constraints against complete backgrounds, rooms, walls, ceilings, scattered props, floating asset packs, or separated set dressing."
---

# 蜃楼 / Mirage

## Role

Use 蜃楼 after the character prompt is approved and before Image Gen. 蜃楼 is a composition post-processor, not a character module.

It converts the character's occupation or scene theme into a small, coherent floating platform for gacha-card presentation. It must not change the character's job, body, outfit anchors, black-market stock, grooming, pose, expression, or identity.

Recommended order with Character Forge:

```text
大门 -> 伯乐 -> 三宅 -> 托尼 -> 黑墙 -> 阿佐特 -> 蜃楼 -> Image Gen -> 成图审核
```

## Inputs

Use the approved character record and final prompt:

- occupation, gang, and role-readable props
- outfit anchors and selected black-market stock
- locked pose and expression
- Azoth `PLATFORM_DYNAMIC_DECISIONS`, when available
- user-provided `{{场景主题}}`, if any
- user environment rules, if any

If Azoth provides `PLATFORM_DYNAMIC_DECISIONS`, preserve those scene decisions unless they violate Mirage constraints. If neither Azoth nor the user provides a scene theme, infer one from the approved character. Do not use a fixed occupation-to-scene mapping table. Examples may help reasoning, but never encode them as mandatory pairs.

## Generation Logic

1. **Lock the character first**
   - Preserve the approved character prompt.
   - Do not rewrite role, clothing, pose, expression, body type, or selected inventory.
   - Keep the character as the visual priority.

2. **Infer the smallest recognizable scene slice**
   - Determine what compact local setting best identifies the role or user theme.
   - Prefer a counter, floor patch, booth edge, tabletop, station, display base, practice corner, service desk, stall slice, or other small local space when appropriate.
   - Avoid complete rooms, full landscapes, full storefronts, or wide establishing shots.

3. **Build one coherent floating platform**
   - The platform must be a single connected object the character can stand on.
   - Include solid themed ground, such as tile, wood, turf, pavement, carpet, dirt, matting, or another fitting surface.
   - The outer edge must naturally break into a few cross-section fragments and fade into a pure white background.
   - Allow only very few tiny fragments or subtle particles near the broken edge.

4. **Choose 2-3 rooted props dynamically**
   - Select props by role recognition, not by a fixed list.
   - Each prop must be physically connected, bolted, planted, embedded, built into, or firmly resting on the platform.
   - Choose medium-sized environmental anchors over scattered small items.
   - Props must support the current role and scene theme without stealing focus from the character.

5. **Compress the final prompt**
   - Add only one focused scene-platform paragraph plus one compact negative-constraint sentence unless the user asks for more detail.
   - Keep character-critical details intact.
   - Do not add examples or unused alternatives to the final prompt.

## Prompt Template

When used with Character Forge, load `character-forge/references/prompt_blocks/mirage-platform-template.md` and use that template as the stable platform wording. Replace only the bracketed fields.

Adapt this template to the current character. Replace bracketed text with concrete decisions:

```text
The character stands on one single coherent floating platform, a miniature cross-section slice of [scene theme]. The platform has solid [themed ground] and its outer edge naturally breaks into a few clean fragments that fade into a flat pure white background, with only a few tiny subtle particles nearby. Rooted into the platform are exactly [2-3] iconic environmental props: [prop 1], [prop 2], and [prop 3]. Every prop is fixed to, built into, planted in, or firmly resting on the same platform; no separated prop pack and no floating standalone props.
```

Compact negative sentence:

```text
No complete background, no full room, no walls, no ceiling, no complete landscape, no enclosed background, no crowded image, no scattered loose objects, no separated props, no floating asset pack, no multiple characters, no panels, no readable text, no logos, no watermark, no 3D render, no toy figurine, no physical model base, no collectible statue, no miniature diorama render, no plastic or resin product photography; keep flat 2D anime cel-shading.
```

## White-Sock Outfit Anchor

When the approved outfit or user preference includes the recurring outfit anchor, preserve these items in the final prompt:

```text
a clear black belt, visible long white socks, and a clean white fitted tank top or clean white fitted inner T-shirt
```

If the approved outfit naturally includes shorts, strengthen the sock visibility once:

```text
The shorts end above the knee, leaving the long white socks clearly visible between the shorts and shoes.
```

Use this as a sock-visibility and torso-readability guard. Do not force shorts, and do not turn the anchor into a new costume if the approved character explicitly requires different clothing. Preserve the white fitted torso base layer unless the approved character explicitly overrides it, has a bare torso, or uses fully covering armor or heavy outerwear.

## Output

Return:

- selected scene theme
- platform ground
- 2-3 rooted props
- final scene-platform prompt paragraph
- compact negative constraints

When used with Image Gen, merge the scene-platform paragraph into the final English prompt after the character description and before global rendering constraints.

## Audit

Before Image Gen, check:

- one single connected platform
- character standing on solid ground
- 2-3 rooted props, not scattered items
- pure white isolated background
- broken/fading outer edge
- no full room, wall, ceiling, complete landscape, or enclosed background
- no floating asset pack or separated prop collection
- no 3D render, toy figurine, physical model base, collectible statue, miniature diorama render, plastic/resin product photography, or non-flat cel-shading drift
- no unintended change to character, outfit anchors, pose, expression, or black-market stock
