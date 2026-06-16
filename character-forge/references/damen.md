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

- Height impression: very tall, imposing, about 7.5 to 8 heads tall in stylized animation proportions.
- Build: extremely broad shoulders, thick neck, wide chest, powerful torso, narrow but solid waist, and heavy limbs.
- Musculature: clearly muscular and heroic, with large arms, strong forearms, thick thighs, and a visible chest-and-ab structure when clothing allows it.
- Proportion language: oversized upper body and hands, stable stance, compact head relative to body, strong trapezius and deltoid silhouette.
- Body archetype references: use the shared physique language of Daemon Goro, Rugal Bernstein, Ryu, Zangief, Yashiro Nanakase, All Might, Rikido Sato, Endeavor, Reinhardt, Mauga, Elfman, and Alex Louis Armstrong as broad inspiration for scale, mass, heroic anatomy, and exaggerated animation readability. Do not copy any specific costume, face, hairstyle, symbol, or identity from those characters.
- Muscle shape language: the torso should feel built from very large simple anatomical masses: oversized pectorals, thick serratus/oblique side planes, stacked blocky abdominal muscles, heavy deltoids, and powerful trapezius forms.
- Outfit independence: clothing may change by job, but it must sit on this same tall, heavily built body type.
- Avoid changing the body into a slim, average, lanky, small, or lightly athletic figure.

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
