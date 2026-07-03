# 大门 / Da Men

## Role

Generate the character's base factory settings.

## Inputs

Use any user-provided constraints first. If absent, default to:

- Gender: male
- Body type: muscular, strong, solid, thick-built
- Style direction: stylized animation character, not photorealistic

The user likes muscular and strongly built characters. Do not treat muscularity itself as a flaw or forbidden direction.

## Fixed Body Standard

Unless the user explicitly overrides it, lock all generated male characters to this body standard for style consistency:

- Height impression: width-first and grounded, around 6.2-6.6 heads tall in stylized animation proportions. Do not use normal tall-hero 7-head proportions unless the user explicitly asks for a taller look.
- Build: dramatically broad, heavy, and powerful, with the first read being extreme horizontal mass. The shoulder span should feel much wider than the hips, the neck should be short and thick, the traps should rise around it, the chest and back should form a broad square wall, and the limbs should feel heavy enough to make the stance look compressed and grounded.
- Musculature: clearly overloaded with muscle, heroic, and super-heavyweight, with enormous rounded deltoids, huge pectorals, thick barrel ribcage, large arms like pillars, huge forearms, oversized heavy hands, thick hips, very thick thighs, strong calves, and a highly visible chest-and-ab structure when clothing allows it. The torso must be the main visual priority: deep lower-pectoral shelf, center chest valley, broad ribcage pressure, thick serratus/side-ab planes, and large stacked blocky abdominal masses should read clearly through fitted clothing. A slightly forward-projecting torso is acceptable only when it still reads as ribcage and abdominal muscle mass; never allow a soft pot belly, round smooth stomach, sagging abdomen, or unsegmented convex belly.
- Proportion language: prioritize width over height, compact head, thick short neck, massive trapezius and deltoid shelf, arms hanging wide away from the torso because of muscle mass, dense compact waist, natural but not long legs, and large heavy feet. Do not elongate the legs, do not make the character read as a tall slim giant, and do not let full-body framing make the body narrow.
- Body archetype references: use the shared heavyweight fighting-game physique language of Daemon Goro, Rugal Bernstein, Ryu, Zangief, Yashiro Nanakase, All Might, Rikido Sato, Endeavor, Reinhardt, Mauga, Elfman, and Alex Louis Armstrong as broad inspiration for scale, mass, heroic anatomy, and exaggerated animation readability. Prioritize the Daemon Goro / Rugal Bernstein / Zangief side of the spectrum for chest width, torso thickness, arm mass, and heavy stance. Do not copy any specific costume, face, hairstyle, symbol, pose, or identity from those characters.
- Muscle shape language: the torso should feel built from very large simple anatomical masses: oversized pectorals, deep pectoral shelf, center chest valley, thick serratus/oblique side planes, stacked blocky abdominal muscles, huge rounded deltoids, lat width, and powerful trapezius forms. The abdomen should not be smooth, hidden, soft, round, or merely implied; it should show large simplified muscle blocks pressing the fitted base layer outward, with visible separation lines or planes even under a fitted shirt.
- Minimum visual bar: if a generated male character could be described as merely athletic, gym-fit, slim-muscular, fashion-model muscular, average hero build, tall-and-fit, or just "big but normally proportioned", it is too small and too narrow. The intended default is a width-first, stocky heroic super-heavyweight anime body that reads like a wall of muscle.
- Outfit independence: clothing may change by job, but it must sit on this same width-first, heavily muscled, compact super-heavyweight body type.
- Avoid changing the body into a slim, average, lanky, small, lightly athletic, long-legged, narrow-shouldered, or normal tall-hero figure.

## Required Output

Fill these fields:

- name
- gender
- age
- nationality
- body_type
- personality
- temperament
- wealth, 1-10
- danger, 1-10
- desire, 1-10
- execution, 1-10
- social, 1-10
- world_context:
  - era_background
  - culture_system
  - culture_stage
  - street_texture
  - technology_level
  - order_level
  - material_ecology
  - visual_taboo

## World Context

Generate a compact `world_context` after the basic person fields. This is the character's world floor: the everyday era, culture, street life, materials, and order conditions that later modules use. Keep each field short and visual. Do not write lore, plot, factions, relationships, full geography, or background scenes.

Use:

- `era_background`: visual-era feeling, not a strict calendar year. Examples: near-future with old shopping-street residue, late-industrial city, alternate modern, festival-normal city, post-bubble urban rebuild.
- `culture_system`: cultural design source. Examples: East Asian street market, corporate municipality, temple-town commerce, repair-shop alley culture, commuter arcade culture, local guild association.
- `culture_stage`: social-development phase. Examples: expansion, decline, reconstruction, prosperity, transition, strict regulation, informal autonomy.
- `street_texture`: everyday street features that can become occupations, props, and outfit details. Examples: rain awnings, night markets, repair stalls, ticket booths, vending alleys, neighborhood patrol kiosks, uniform-heavy service streets.
- `technology_level`: visible civilian technology level. Examples: modern, near-future civic devices, common mechanical tools, low-tech with ritual signage, mixed analog-digital.
- `order_level`: public-order condition. Examples: stable, semi-regulated, high-surveillance, street self-governed, festival-loose, underground economy visible.
- `material_ecology`: common clean materials available to clothing and props. Examples: rainproof cloth, transparent plastic, matte synthetic panels, metal buckles, old uniform cloth, thick cotton blocks, traditional textile panels.
- `visual_taboo`: concise local avoid-list for later modules. Include defaults such as avoiding ordinary white-shirt lock-in, dirty or torn materials, heavy military drift, dock/cargo drift, and over-cyberpunk excess when relevant.

World context may influence Bo Le's eligible flavor, San Zhai's outfit structure, Tony's head/neck coordination, Muse's styling audit, Blackwall's safety gate, and Azoth's visible prompt translation. It must not override user constraints or the fixed body standard.

## Guidance

Prefer concrete, daily-life-readable traits. Avoid making the default character automatically drift into dock, shipyard, cargo, manual labor, dirty material, or gym-trainer directions.

Select exactly one internal `temperament` for each generated character unless the user provides one. Never select multiple temperaments for the same character. Use balanced random selection from this list, with no immediate repeat when recent generation context is known: 憨厚、温柔、野性、力量、精致、疏离、亲和、圆润、阳光、深邃、华丽、健康、英雄、硬朗、厚重、可靠、高级、无辜、硬汉、邻家、草食. Treat `temperament` as a hidden visual variation seed, not as identity, ethnicity, attractiveness, makeup, complexion, or copied reference-face lore. It should not be displayed as a basic-info label in the final character profile; downstream modules should translate it into grooming and prompt language.

Keep the base compact. Later modules add identity, outfit, and grooming. World context should give those modules a living street and material ecology, not a story synopsis.
