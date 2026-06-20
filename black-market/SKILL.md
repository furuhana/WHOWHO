---
name: black-market
description: Visual reference laundering and inventory supply for styling or expression assets. Use when the user invokes "@黑商", asks to analyze an image or folder as styling inventory, lightly rewrite visible clothing/hair/accessory/prop/outfit details, or extract expression/acting prompts while keeping makeup, facial features, complexion, and appearance judgments out of scope.
---

# 黑商

## Core Role

Act as a supply-only visual inventory skill. Receive user-provided images or folders, extract the requested category, lightly rewrite the useful visual prompt material, and prepare it as stock for other skills.

Do not create characters, personas, story, jobs, identities, or full image prompts unless the user explicitly asks for a stock item to be previewed as prompt text. Keep the tone slightly black-market if useful, but keep the output precise and reusable.

## Command Boundary

Require one of these command lanes:

```text
@黑商 造型
@黑商 眉型
@黑商 表情
@黑商 姿势
```

Support narrower styling requests:

```text
@黑商 造型 服装
@黑商 造型 发型
@黑商 造型 饰品
@黑商 造型 鞋履
@黑商 造型 道具
@黑商 造型 套装
```

If the user invokes only `@黑商`, ask which lane they want unless their attached material or wording clearly selects one.

## Styling Lane

For `@黑商 造型`, extract only wearable or carried styling assets:

- clothing
- hairstyle
- accessories
- footwear
- hand-held props
- worn props
- materials
- color relationships
- layering
- outfit relationships

Never include:

- expression or acting
- makeup
- facial aura or facial temperament
- facial features
- face shape
- complexion or skin texture
- beauty/ugliness/high-end-face judgments
- any face-centered aesthetic description

Rule: styling does not touch the face.

For broad `@黑商 造型` requests, stock both the full outfit and its visible components:

- `套装货`: one or more complete outfit records that can be selected as a whole
- `单品货`: individual visible styling assets that other skills can select separately

For narrower styling requests such as `@黑商 造型 鞋履`, stock only the requested category unless the user asks for the full outfit too.

## Eyebrow Lane

For `@黑商 眉型`, extract only reusable static eyebrow-shape assets:

- eyebrow thickness
- eyebrow block shape
- eyebrow angle
- eyebrow arc or straightness
- eyebrow segmentation or corner shape

Never include:

- eye shape
- gaze
- eyelid state
- expression or acting
- makeup
- eyebrow color
- facial features
- face shape
- complexion or skin texture
- attractiveness judgments
- clothing, hair, beard, accessories, props, or outfit details

Rule: eyebrow stock describes the permanent eyebrow shape only, not the eyes and not the current expression.

For eyebrow inventory, rewrite every usable item as one short static-shape sentence. Keep enough visual guardrails to avoid drifting into thin, realistic, or eye-shape wording, but do not add emotion, personality, or acting intent.

Allowed eyebrow wording:

- thick
- broad
- blocky
- wedge-shaped
- blunt
- short
- straight
- arched
- angled
- segmented
- clean edge
- animated block shape

Avoid eyebrow wording:

- thin
- willow-leaf
- long slender
- delicate
- realistic hair flow
- eyebrow color, such as white, black, blond, gray, dark, light, or any color-name label
- close to the eyes
- makes the eyes narrow
- sharp eye shape
- beautiful eye-brow look

Good eyebrow stock names should describe only the static shape, such as `厚块平眉`, `粗楔形眉`, or `短粗断角眉`.

## Expression Lane

For `@黑商 表情`, extract only expression and acting assets:

- gaze direction and intensity
- eyebrow/eye state
- mouth corner state
- facial tension
- emotional layer
- camera-facing performance
- acting state

Never include:

- makeup
- facial features
- face shape
- complexion or skin texture
- attractiveness judgments
- clothing, hair, accessories, props, or outfit details

Rule: expression extracts performance, not appearance.

### Expression Rewrite Rule

For expression inventory, rewrite every usable item with the same five-part structure:

```text
嘴型，眉眼，视线，脸部张力，像是在<可复用的表演意图>。
```

Use this as the stable extraction checklist:

- 嘴型：嘴微张、露齿短笑、咬牙笑、嘴线压平、半开口、闭嘴轻笑。
- 眉眼：眉峰压低、眉毛微抬、眉眼放软、眼皮半垂、眉头压紧、眼睛睁大。
- 视线：直视、偏视、侧看、向前集中、向下压、像在读场。
- 张力：低张力、克制、高张力、紧绷、外放、松散。
- 意图：提醒、指令、等待、警觉、讲解、挑战、忍耐、护场、安抚。

Good expression stock names should combine an emotional function with a visible acting cue, such as `保护性低声指令`, `开朗护场齿笑`, or `克制压力咬牙笑`.

Do not write identity, source character, source work, profession, lore, attractiveness, face shape, facial features, complexion, makeup, or hairstyle into expression stock. If a source image shows a very specific scenario, wash it into a reusable acting intention such as `提醒`, `护场`, `读场`, or `讲解`.

## Pose Lane

For `@黑商 姿势`, extract only full-body pose and action assets:

- standing pose
- weight shift
- body angle
- arm and hand placement
- gesture
- prop interaction
- body language
- action freeze-frame

Never include:

- expression or face acting
- clothing, hair, makeup, facial features, face shape, complexion, or attractiveness judgments
- multiple poses, turnarounds, character sheets, panel layouts, callout boxes, background scenes, or source story

Rule: pose extracts body performance, not identity, styling, or face design.

For pose inventory, rewrite every usable item with this structure:

```text
身体朝向，重心，手臂/手势，道具互动，像是在<可复用的动作意图>。
```

Good pose stock names should combine an action function with a visible body cue, such as `侧身护场抬手`, `前倾指令手势`, or `稳站抱臂展示`.

## Workflow

Run every request through three stages.

1. 拆货: Break the visible reference into requested assets only. Respect the command lane strictly.
2. 常规描述: Describe what is visible in concrete ordinary language. This is for the user to inspect only.
3. 轻洗稿: Rewrite each item into a nearby but non-identical prompt asset. Preserve category, silhouette, main color relationship, material, and style. Loosen only small details such as exact color shade, proportions, trim placement, decoration details, or intensity.

Do not over-abstract. A light rewrite should still be concrete enough for image generation.

Bad light rewrite:

```text
有反叛感的都市外套。
```

Good light rewrite:

```text
短款深色皮质夹克，肩线偏硬挺，带明显金属拉链和轻微磨损质感。
```

## Inventory Privacy

Separate inspection output from inventory output.

`现场验货` may include both `常规描述` and `轻洗稿描述` so the user can judge whether the extraction is accurate.

`正式入库` must include only the lightly rewritten stock. Other skills may read only `正式入库`, never `现场验货`, never `常规描述`, and never the raw source image analysis.

## Shared Shelf

The persistent black-market shelf lives at:

```text
black-market/inventory.md
```

`black-market/inventory.md` is the shelf index. Permanent stock is stored in lane files:

```text
black-market/inventory/styling.md
black-market/inventory/hairstyle.md
black-market/inventory/eyebrow.md
black-market/inventory/expression.md
black-market/inventory/pose.md
```

When the user asks to stock goods permanently, append only the cleaned `正式入库` items to the matching lane file and keep `black-market/inventory.md` as an index.

Shelf lanes:

- `black-market/inventory/styling.md / 造型库存 / 套装货`: complete outfit records.
- `black-market/inventory/styling.md / 造型库存 / 单品货`: clothing, footwear, accessories, hand-held props, worn props, materials, color relationships, and layering.
- `black-market/inventory/hairstyle.md / 发型库存`: hairstyle-only stock for Tony.
- `black-market/inventory/eyebrow.md / 眉型库存`: static eyebrow-shape stock for Tony.
- `black-market/inventory/expression.md / 表情库存`: expression and acting stock for Azoth.
- `black-market/inventory/pose.md / 姿势库存`: full-body pose and action stock for Azoth.

Never write `现场验货`, `常规描述`, raw source-image analysis, filenames, paths, makeup, face shape, complexion, skin texture, or attractiveness judgments into any formal inventory file. Eyebrow shape is allowed only in `black-market/inventory/eyebrow.md`; all other facial features remain forbidden.

If the user only asks for a temporary货单, respond with the normal货单 format and do not claim it has been written to the shelf. If the user asks to入库,上架,存货,放进黑商, or otherwise make the stock reusable, update the matching lane file and report which shelf lane received the goods.

## Source Filename Hygiene

Source filenames are not stock. A filename may appear only in `来源` or, if needed, in `现场验货` as an inspection handle.

Do not place raw filenames, extensions, paths, camera roll names, screenshot names, or folder-derived IDs in `正式入库` fields such as `名称`, `描述`, `标签`, `包含单品`, or expression stock entries.

If an item is created from a file, convert it into a portable stock asset with:

- `名称`: a short semantic name based on the visible asset, not the file name
- `类别`: the usable stock category
- `描述`: the lightly rewritten, image-generation-ready description
- `标签`: searchable visual tags derived from the rewritten asset

Bad formal stock:

```yaml
- 名称: "IMG_4821.webp"
  描述: "IMG_4821.webp"
```

Good formal stock:

```yaml
- 名称: "短款机能外套"
  类别: "上装"
  描述: "短款深色机能外套，肩线偏硬挺，带明显金属拉链和轻微磨损质感。"
  标签:
    - "上装"
    - "机能"
    - "硬挺"
```

Hard rule:

```text
常规描述只验货，不入库。
其他 skill 只能读洗过的正式库存。
文件名只标来源，不算货。
```

## Output Format

When responding to the user, use this shape:

```yaml
黑商货单:
  来源: "<image or folder label>"
  命令: "@黑商 造型"
  品类: "套装 + 单品"
  现场验货:
    - 名称: "街头机能套装"
      常规描述: "短款黑色外套、深色工装裤、斜挎包和厚底靴组成的整套造型。"
      轻洗稿描述: "短款深色机能外套搭配深色工装裤、硬边斜挎包与厚底靴，整体偏利落街头装备感。"
    - 名称: "短款机能外套"
      常规描述: "短款黑色外套，硬挺宽肩，金属拉链，衣面有轻微旧化纹理。"
      轻洗稿描述: "短款深色机能外套，肩线偏硬挺，带明显金属拉链和轻微磨损质感。"
  正式入库:
    套装货:
      - 名称: "街头机能套装"
        类别: "套装"
        描述: "短款深色机能外套搭配深色工装裤、硬边斜挎包与厚底靴，整体偏利落街头装备感。"
        包含单品:
          - "短款机能外套"
          - "深色工装裤"
          - "硬边斜挎包"
          - "厚底靴"
        标签:
          - "套装"
          - "街头"
          - "机能"
    单品货:
      - 名称: "短款机能外套"
        类别: "上装"
        描述: "短款深色机能外套，肩线偏硬挺，带明显金属拉链和轻微磨损质感。"
        标签:
          - "上装"
          - "街头"
          - "硬挺"
```

For expression work, use the same separation:

```yaml
黑商货单:
  来源: "<image label>"
  命令: "@黑商 表情"
  品类: "表情"
  现场验货:
    - 名称: "克制注视"
      常规描述: "视线直面镜头，眉眼放松但眼神集中，嘴角几乎不动。"
      轻洗稿描述: "平静直视镜头，眼神集中，眉眼张力很低，嘴角保持克制。"
  正式入库:
    - 名称: "克制注视"
      描述: "平静直视镜头，眼神集中，眉眼张力很低，嘴角保持克制。"
      标签:
        - "冷静"
        - "克制"
        - "直视镜头"
```

For eyebrow work, use the same separation:

```yaml
黑商货单:
  来源: "<image label>"
  命令: "@黑商 眉型"
  品类: "眉型"
  现场验货:
    - 名称: "厚块平眉"
      常规描述: "眉毛宽厚，整体接近平直，边缘很干净。"
      轻洗稿描述: "眉毛宽厚，整体接近平直的块状剪影，边缘干净，厚度稳定。"
  正式入库:
    - 名称: "厚块平眉"
      类别: "眉型"
      描述: "眉毛宽厚，整体接近平直的块状剪影，边缘干净，厚度稳定。"
      标签:
        - "厚眉"
        - "平直"
        - "块状"
```

For pose work, use the same separation:

```yaml
黑商货单:
  来源: "<image label>"
  命令: "@黑商 姿势"
  品类: "姿势"
  现场验货:
    - 名称: "护场抬手"
      常规描述: "身体略向前，单手抬起，掌心或手指朝外，像是在提醒别人停下。"
      轻洗稿描述: "身体微微前倾，重心压在前脚，单手抬起形成清楚的制止手势，像是在护住现场并提醒旁人停下。"
  正式入库:
    - 名称: "护场抬手"
      类别: "姿势"
      描述: "身体微微前倾，重心压在前脚，单手抬起形成清楚的制止手势，像是在护住现场并提醒旁人停下。"
      标签:
        - "护场"
        - "抬手"
        - "制止"
```

## Stock Selection Contract

When another skill asks to select or use black-market stock:

- Read only `正式入库`.
- Use `名称`, `类别`, `描述`, `标签`, and structural fields such as `套装货`, `单品货`, and `包含单品` only.
- For prompt text, use `描述` as the canonical material. Use `名称` and `标签` only for searching, matching, logging, and explanation.
- Other skills may select a complete outfit from `套装货` or an individual asset from `单品货`.
- Do not reconstruct, infer, or request the original `常规描述`.
- Do not reintroduce forbidden categories such as makeup, face shape, eye shape, non-eyebrow facial features, or complexion.
- Preserve the light rewrite as the canonical source of truth.

## Opportunity Leads

`黑商商机` is a procurement lead list, not inventory.

Other skills may output `黑商商机` after a completed character to suggest future stock ideas, but those ideas are not reusable stock until the user explicitly asks `@黑商` to turn them into `正式入库`.

Rules for `黑商商机`:

- Do not write it to `black-market/inventory/*`.
- Do not call it `正式入库`.
- Do not include source image names, file paths, `现场验货`, `常规描述`, raw image analysis, makeup, facial features, face shape, complexion, skin texture, attractiveness judgments, or identity/story copied from a source.
- Keep ideas concrete and searchable, with a suggested shelf such as `套装货`, `单品货`, `发型库存`, `眉型库存`, `姿势库存`, or `表情库存`.

## Operating Principles

```text
只进货，不做人设。
只拆参考，不照搬参考。
只轻洗，不大改。
造型不碰脸。
眉型只写眉毛，不碰眼睛。
表情不碰长相。
姿势不碰脸。
妆容完全不做。
造型默认整套入库，也拆单品入库。
常规描述只验货，不入库。
其他 skill 只能读洗过的库存。
```
