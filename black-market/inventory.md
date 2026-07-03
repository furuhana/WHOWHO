# 黑商正式库存

This file is the shared shelf index for black-market stock. Other skills may read formal stock from the files listed below, and may read only each file's `正式入库` section.

Do not store `现场验货`, `常规描述`, raw image analysis, source filenames, paths, makeup, face shape, complexion, skin texture, or attractiveness judgments in formal stock. Eyebrow shape is allowed only in `black-market/inventory/eyebrow.md`; all other facial features remain forbidden.

## 正式入库索引

### 造型库存

- 迁移入口：`black-market/inventory/styling.md`
- 套装货：`black-market/inventory/styling/sets.md`
- 单品货目录：`black-market/inventory/styling/items/`
- 当前状态：第一轮套装重建完成；第二轮已把套装中的裤装/下装结构同步拆入 `items/bottoms.md`，供三宅创建角色时降低裤型重复。
- 当前新货架数量：
  - 套装货：157 件
  - 单品货：129 件
  - 其中下装单品：46 件
  - 其中饰品与小件：4 件
- 旧货状态：已删除，不参与检索，不保留正式库存残留。

### 发型库存

- 货架：`black-market/inventory/hairstyle.md`
- 发型货：9 件

### 眉型库存

- 货架：`black-market/inventory/eyebrow.md`
- 眉型货：12 件

### 表情库存

- 货架：`black-market/inventory/expression.md`
- 表情货：44 件

### 姿势库存

- 货架：`black-market/inventory/pose.md`
- 姿势货：59 件

## 读取规则

- 三宅先读取 `black-market/inventory/styling/sets.md` 的 `正式入库 / 造型库存 / 套装货`，再读取 `black-market/inventory/styling/items/*.md` 的 `正式入库 / 造型库存 / 单品货`。创建角色时，`items/bottoms.md` 是裤子/腿部系统的正式候选池；三宅必须用它补强、替换或明确拒绝裤装候选，避免继续只用普通裤子。
- 归档文件只用于人工追溯，不参与正式选货。
- 托尼读取 `black-market/inventory/hairstyle.md` 的 `正式入库 / 发型库存`，再读取 `black-market/inventory/eyebrow.md` 的 `正式入库 / 眉型库存`。
- 阿佐特读取 `black-market/inventory/pose.md` 的 `正式入库 / 姿势库存`，再读取 `black-market/inventory/expression.md` 的 `正式入库 / 表情库存`。
- 黑墙审核所有被选中的黑商货。
