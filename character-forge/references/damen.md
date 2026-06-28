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
- Musculature: clearly overloaded with muscle, heroic, and super-heavyweight, with enormous rounded deltoids, huge pectorals, thick barrel ribcage, large arms like pillars, huge forearms, oversized heavy hands, thick hips, very thick thighs, strong calves, and a highly visible chest-and-ab structure when clothing allows it. The torso must be the main visual priority: deep lower-pectoral shelf, center chest valley, broad ribcage pressure, thick serratus/side-ab planes, and large stacked blocky abdominal masses should read clearly through fitted clothing.
- Proportion language: prioritize width over height, compact head, thick short neck, massive trapezius and deltoid shelf, arms hanging wide away from the torso because of muscle mass, dense compact waist, natural but not long legs, and large heavy feet. Do not elongate the legs, do not make the character read as a tall slim giant, and do not let full-body framing make the body narrow.
- Body archetype references: use the shared heavyweight fighting-game physique language of Daemon Goro, Rugal Bernstein, Ryu, Zangief, Yashiro Nanakase, All Might, Rikido Sato, Endeavor, Reinhardt, Mauga, Elfman, and Alex Louis Armstrong as broad inspiration for scale, mass, heroic anatomy, and exaggerated animation readability. Prioritize the Daemon Goro / Rugal Bernstein / Zangief side of the spectrum for chest width, torso thickness, arm mass, and heavy stance. Do not copy any specific costume, face, hairstyle, symbol, pose, or identity from those characters.
- Muscle shape language: the torso should feel built from very large simple anatomical masses: oversized pectorals, deep pectoral shelf, center chest valley, thick serratus/oblique side planes, stacked blocky abdominal muscles, huge rounded deltoids, lat width, and powerful trapezius forms. The abdomen should not be smooth, hidden, or merely implied; it should show large simplified muscle blocks pressing the fitted base layer outward.
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
- wealth, 1-10
- danger, 1-10
- desire, 1-10
- execution, 1-10
- social, 1-10

## Guidance

Prefer concrete, daily-life-readable traits. Avoid making the default character automatically drift into dock, shipyard, cargo, manual labor, dirty material, or gym-trainer directions.

Keep the base compact. Later modules add identity, outfit, and grooming.
