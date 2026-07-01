# Global Negative Constraints

Insert this compact negative block at the end of `prompt_en`, after the rendering and lighting blocks. Add pose-specific negatives only when Azoth selected a non-presentation pose that needs protection.

```text
No complete background, no full room, no walls, no ceiling, no complete landscape, no enclosed background, no crowded image, no scattered loose objects, no separated props, no floating asset pack, no multiple characters, no multiple poses, no front-side-back turnaround, no character sheet, no panel layout, no split view, no callout boxes, no readable text, no logos, no watermark, no 3D render, no toy figurine, no physical model base, no collectible statue, no miniature diorama render, no plastic or resin product photography; keep flat 2D anime cel-shading.
```
