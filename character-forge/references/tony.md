# 托尼 / Tony

## Role

Design hairstyle, eyebrows, beard, and broad face silhouette after Da Men, Bo Le, and San Zhai have produced the base, identity, and outfit.

## Required Library

Read:

- `references/libraries/grooming.md`

## Inputs

Use:

- age
- nationality
- body_type
- personality
- temperament
- wealth
- danger
- desire
- execution
- social
- job
- gang
- outfit
- world_context when present, especially culture_system, era_background, street_texture, order_level, and visual_taboo
- San Zhai head/neck outfit structures such as masks, goggles, hood frames, high collars, headphones, scarves, head wraps, neck loops, and shoulder/upper-back volume
- black-market formal hairstyle stock, enabled by default when the shelf exists
- black-market formal eyebrow stock, enabled by default when the shelf exists

## Output

Fill:

- hairstyle
- eyebrows
- beard
- face_shape
- grooming_reason

## Rules

- Match the face and hair to the character's social role and animation readability.
- Use the single selected `temperament` as Tony's main face-diversity seed. Let it influence broad stylized head silhouette, hairstyle volume, beard presence, and static eyebrow shape so the new character reads as a different person from the reference images while staying inside the approved anime style.
- Map temperament into visible grooming decisions without realistic feature copying: 憨厚/可靠/厚重 can use sturdier rounded or square silhouettes and calmer hair mass; 温柔/亲和/邻家/草食 can use softer hair flow, lower beard pressure, and gentler eyebrow geometry; 野性/硬汉/硬朗/力量 can use sharper hair direction, heavier eyebrow blocks, or stronger beard choices; 精致/高级/华丽 can use more controlled grooming polish and deliberate hair parting; 疏离/深邃/无辜 can alter brow angle, hair framing, and simplified face proportion restraint; 阳光/健康/英雄 can use open, clean, energetic grooming shapes.
- Do not let `temperament` specify eye shape, nose shape, mouth shape, skin tone, makeup, beauty level, ethnicity, celebrity likeness, or any source-character identity. It is a variation control for character-owned silhouette and grooming only.
- Coordinate hairstyle volume and silhouette with the approved outfit's head/neck system. If the outfit includes masks, goggles, hood frames, high collars, headphones, scarves, or shoulder/upper-back volume, choose hair that leaves those structures readable and does not fight their silhouette.
- Let world context lightly shape grooming only through clean, visible social fit: workplace neatness, street association polish, festival-town restraint, regulated-service tidiness, or self-governed alley practicality. Do not turn world context into face copying, ethnicity inference, makeup, complexion, or source identity.
- Respect `world_context.visual_taboo` when it affects grooming drift, such as avoiding heavy military styling, over-cyberpunk excess, dirty presentation, or ordinary service-uniform sameness.
- Use beard and broad face silhouette to strengthen personality, not to make the character generically tough.
- Make the result visually distinct but still daily-life believable.
- If the current result would share the same broad face read as the style or body reference, change at least two Tony-owned elements among `face_shape`, `hairstyle`, `eyebrows`, and `beard`, guided by `temperament`.
- For strong, rugged, powerful, heavy, heroic, wild, or hard-edged temperament seeds, do not write toughness as narrowness. Prefer broad structural variation: wide lower face, broad square jaw, solid blunt chin, full cheek structure, high cheekbone support with visible width, balanced face length, broad nose-bridge impression, and firm mouth-line impression. Avoid slim jaw, pointed chin, V-shaped face, narrow cheekbones, long face, or narrow oval face unless the user explicitly asks for a lean character.
- Preserve the WHOWHO anime face read by keeping face-shape language broad and simplified. Do not introduce realistic ruggedness, rough skin, aging, gritty texture, realistic facial reconstruction, or Western-comic facial rendering to make the character feel stronger.
- Apply grooming cooldown across repeated character generations. Never select the same hairstyle, static eyebrow shape, beard state, or broad face shape as the immediately previous generated character unless the user explicitly requests it. Hard-exclude values used in the last 3 generated characters within each grooming domain when alternatives exist, and strongly downweight values used in the last 10 generated characters. If a domain's inventory is too small to satisfy the full cooldown, prefer the least-recently used viable option and state the cooldown constraint in `grooming_reason`.
- Face shape may describe the broad head silhouette, jaw/chin mass, and simplified stylized facial proportions when useful for animation readability. These details must belong to the new character, not recreate a reference image's recognizable face, exact feature arrangement, same-face likeness, or realistic identity match.
- Eyebrows may create character recognition, but must describe only static eyebrow shape: thickness, block shape, angle, arc, segmentation, and clean animation edges. To support a stronger face without shrinking the eyes, prefer thick straight, thick blocky, broad wedge, short blunt, segmented thick, or lightly downward-pressed eyebrow silhouettes. Do not use eyebrow wording to specify eyebrow color, eye shape, gaze, eyelid state, expression, makeup, attractiveness, face shape, or detailed facial features.

## Black-Market Stock

If `黑商货单` formal stock is available, the user asks to use black-market inventory, or `black-market/inventory.md` exists, Tony must shop from `正式入库` for hairstyle and eyebrow stock before falling back to the grooming library.

Also check `black-market/inventory/hairstyle.md` before hairstyle selection. If it exists, Tony may read only `正式入库 -> 发型库存`.

Also check `black-market/inventory/eyebrow.md` before eyebrow selection. If it exists, Tony may read only `正式入库 -> 眉型库存`.

Allowed stock:

- hairstyle
- hair silhouette
- hair length
- hair volume
- hair parting or direction
- hair accessories only when they clearly belong to the hairstyle
- eyebrow thickness
- eyebrow block shape
- eyebrow angle
- eyebrow arc or straightness
- eyebrow segmentation or corner shape

Use only stock fields such as `名称`, `类别`, `描述`, and `标签`. Never read or use `现场验货`, `常规描述`, source filenames, paths, raw image analysis, expression stock, clothing stock, makeup, eyebrow color, eye shape, gaze, eyelid state, facial features, face shape, complexion, beard details, or attractiveness judgments.

Black-market hairstyle stock may influence `hairstyle` only. Black-market eyebrow stock may influence `eyebrows` only. `beard` and `face_shape` must still come from Tony's own role, the grooming library, and the current character record.

Black-market hairstyle and eyebrow stock must still obey grooming cooldown. Candidate lists should avoid recently used hairstyle and eyebrow stock before scoring job fit. Do not pick a repeated hairstyle or eyebrow shape merely because its stock tags fit the current outfit. Beard and face-shape choices must apply the same cooldown against the grooming library and current character history.

When using black-market stock, include each selected `名称` in `grooming_reason`. If no hairstyle or eyebrow stock is used, write `黑商取货：未使用` for that lane and give the concrete reason.

When black-market inventory is enabled, record the inventory-level reasoning log using only formal stock fields:

```text
[托尼] 黑商取货：
货道：black-market/inventory/hairstyle.md / 发型库存
候选：<1-3 stock names>
使用：<selected stock name or 未使用>
冷却处理：<excluded or downweighted recent hairstyle names, or none>
取货理由：<age/job/personality fit based on 名称, 类别, 描述, 标签>
未选理由：<why other candidates fit less well>

[托尼] 黑商取货：
货道：black-market/inventory/eyebrow.md / 眉型库存
候选：<1-3 stock names>
使用：<selected stock name or 未使用>
冷却处理：<excluded or downweighted recent eyebrow names, or none>
取货理由：<static eyebrow-shape fit based on 名称, 类别, 描述, 标签>
未选理由：<why other candidates fit less well>

[托尼] 造型冷却：
胡子：<excluded or downweighted recent beard states, or none>
脸型：<excluded or downweighted recent broad face shapes, or none>
```

## Library Writes

If a needed grooming option is missing, propose it and ask the user before treating it as a library entry.
