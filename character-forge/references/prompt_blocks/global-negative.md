# Global Negative Constraints

Insert this compact negative block at the end of `prompt_en`, after the rendering and lighting blocks. Add pose-specific negatives only when Azoth selected a non-presentation pose that needs protection.

```text
No complete background, no full room, no walls, no ceiling, no complete landscape, no enclosed background, no crowded image, no scattered loose objects, no separated props, no floating asset pack, no multiple characters, no multiple poses, no front-side-back turnaround, no character sheet, no panel layout, no split view, no callout boxes, no readable text, no logos, no watermark, no 3D render, no toy figurine, no physical model base, no collectible statue, no miniature diorama render, no plastic or resin product photography, no small eyes, no narrow slit eyes, no squinting eyes, no half-lidded eyes, no heavy-lidded eyes, no droopy eyelids, no sleepy eyes, no tiny pupils, no realistic eyes, no pointed chin, no V-shaped face, no narrow face, no narrow cheekbones, no long face, no realistic rugged face, no rough skin texture, no Western comic face style, no soft pot belly, no round smooth stomach, no unsegmented convex belly, no hidden abdominal structure; keep flat 2D anime cel-shading and the same WHOWHO anime eye style with normal-open readable eyes.
```
