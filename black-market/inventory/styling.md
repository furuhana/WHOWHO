# 黑商造型库存迁移入口

编码: UTF-8
状态: 已迁移到结构化货架

这个文件不再存放正式造型货。旧货已经删除，不保留正式库存残留。

正式造型库存请读取:

- 套装货: `black-market/inventory/styling/sets.md`
- 单品货: `black-market/inventory/styling/items/*.md`

## 读取规则

- 其他技能不得从归档文件读取正式货。
- 其他技能不得把本文件当成造型货源。
- 三宅必须先读取 `styling/sets.md` 的完整套装，再按需读取 `styling/items/*.md` 补强。
- `styling/items/bottoms.md` 已同步套装里的裤装/下装拆件，是创建角色时的正式裤子候选池；三宅填写 `裤子 / pants` 时必须优先检查它。
- 旧货和乱码恢复档不参与角色生成；当前正式货架只认上面的新结构。
