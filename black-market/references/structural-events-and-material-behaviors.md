# Structural Events And Material Behaviors

编码: UTF-8

此文件把“解构”和“材质替换”转译为可生成、可审核的结构事件与材质行为。结构事件说明衣服发生了什么；材质行为说明材料如何改变衣服的功能、体积或身体读法。

## 核心原则

- 解构不是破烂、脏污、随机线条或满身拼接。
- 材质替换不是只写透明、皮革、金属或尼龙。
- 每套造型最多使用 1 个主结构事件，最多 1 个辅助材质行为，除非用户明确要求高复杂度。
- 结构事件必须落到部位、路径、闭合方式、身体作用和失败规避。
- 材质行为必须说明它改变了衣服的什么行为: 显露、封存、支撑、包覆、防水、压缩、反光、重量转移或动作释放。

## 结构事件库

```yaml
错入口:
  定义: "衣服的入口、袖口、门襟或侧开口偏离常规位置，但仍保持可穿逻辑。"
  可用原型: ["multi-opening jacket", "pullover anorak", "utility smock", "offset-placket jacket"]
  可见部位: ["侧腰入口", "后肩 inactive sleeve opening", "偏移门襟", "侧向半拉链"]
  身体作用: "制造不安定穿法，同时避免主身体变形。"
  失败规避: ["多肢误读", "画成身体畸形", "不可穿纯概念"]

反穿内外互换:
  定义: "内衬、挂面、反缝、标签片或背面结构成为外观。"
  可用原型: ["inside-out shell", "shop coat", "straight overcoat", "deconstructed blazer"]
  可见部位: ["外露挂面", "反缝", "背面衬衫结构", "内衬边"]
  身体作用: "让制作过程和隐藏层成为角色信息。"
  失败规避: ["破烂", "脏污", "品牌四角线复制", "随机毛边"]

错肢穿法:
  定义: "袖子、领口或包覆件出现在非传统位置，像衣服主动错开身体，但不改变人体。"
  可用原型: ["multi-opening jacket", "hooded smock", "short shoulder mantle"]
  可见部位: ["第二袖筒悬在背肩", "空袖沿侧腰垂下", "领口偏移到一侧"]
  身体作用: "把衣服作为可变结构，不把角色画成多手臂。"
  失败规避: ["多臂", "袖子像肉体", "遮脸", "动作不可读"]

制服切开:
  定义: "制服、正装或服务外层被切去、错开、削短或转移重心，但仍保留秩序感。"
  可用原型: ["guard tunic", "service coat", "cropped formal jacket", "straight overcoat"]
  可见部位: ["切开下摆", "削短前身", "肩线外移", "腰部急收", "胸侧弧片"]
  身体作用: "保留权力感，同时让角色从普通制服中脱出来。"
  失败规避: ["普通西装", "历史戏服堆砌", "廉价破洞"]

制作痕迹外露:
  定义: "缝份、反缝、拉链牙、包边、临时固定片或干净未完成边成为设计。"
  可用原型: ["inside-out shell", "offset-placket jacket", "panelled technical pants"]
  可见部位: ["门襟", "袖缝", "衣摆", "裤侧线", "鞋舌", "包盖"]
  身体作用: "把制作逻辑显影，增强裁片可信度。"
  失败规避: ["脏污", "破烂", "毛边噪点", "随机线"]

材质封存:
  定义: "饰品、线迹、口袋内容、标记片或小硬件像被透明/半硬材料封住。"
  可用原型: ["sealed pocket shell", "rescue shell", "box bag", "technical backpack"]
  可见部位: ["胸前封存袋", "袖袋硬窗", "包盖透明硬片", "腰侧封存标记"]
  身体作用: "把身份、工具或秘密变成一个可控焦点。"
  失败规避: ["只写透明", "满身塑料", "可读文字污染"]

单片包覆:
  定义: "一整片材料绕肩、背、胸或腰形成外壳，利用空隙和固定点成型。"
  可用原型: ["single-sheet wrap shell", "folded geometric outer shell", "weather poncho"]
  可见部位: ["肩固定点", "侧腰扣", "连续包边", "背部折面"]
  身体作用: "让衣服像外壳或生命体包住身体。"
  失败规避: ["裙化", "围裙化", "拖地", "吞掉四肢"]

普通原型故障:
  定义: "熟悉原型出现错觉拼接、假袖、假层或部件错位，普通衣服不再普通。"
  可用原型: ["varsity-like short shell", "denim trucker-like shell", "shop coat", "canvas low-top"]
  可见部位: ["半挂袖", "假双层前襟", "错位口袋", "鞋底侧墙变形"]
  身体作用: "用一点异常打破日常感，不牺牲职业可读性。"
  失败规避: ["拼贴过载", "来源款复制", "笑话化"]

身体硬件命名:
  定义: "一个硬件、扣具、徽章、钥孔、胸片或手部件明确标记身体部位。"
  可用原型: ["protective vest", "service coat", "wide support belt", "box bag"]
  可见部位: ["胸前单一硬件", "腰扣", "手套焦点", "背部中心板"]
  身体作用: "用单一焦点强调胸、腰、手或背，而不是满身装饰。"
  失败规避: ["超现实堆满身", "五官饰品污染", "品牌符号"]

热压折线成体积:
  定义: "布面通过热压折线、重复折面或放射褶形成体积和运动方向。"
  可用原型: ["folded geometric outer shell", "wide trousers", "short shoulder mantle", "bag body"]
  可见部位: ["宽裤", "披覆外层", "衣摆", "包体边"]
  身体作用: "用折线控制动作和空间，不依赖印花。"
  失败规避: ["随机皱纹", "微织纹", "胸腹被切碎"]
```

## 材质行为库

```yaml
透明显露:
  行为: "让内层、裁片路径或工具层被看见。"
  可用材料: ["透明防水膜", "半透明硬片", "透明鞋跟", "网眼罩层"]
  必须说明: "透明层覆盖哪里，露出什么，边界如何收住。"
  禁忌: ["只写 transparent", "大面积色情化暴露", "塑料噪点"]

封存:
  行为: "把小物、标记、线迹或饰品封进硬质/胶质/透明层。"
  可用材料: ["Perspex-like hard panel", "clear resin-like pocket block", "sealed vinyl window"]
  必须说明: "被封存物、封存位置、硬边边界。"
  禁忌: ["满身封存", "可读品牌文字", "垃圾袋质感"]

防水外壳:
  行为: "让衣服变成天气装备，形成兜帽、挡风片、抽绳和防水袋。"
  可用材料: ["matte rainproof cloth", "sealed nylon shell", "transparent rain film"]
  必须说明: "雨防边界、闭合方式、内层关系。"
  禁忌: ["普通雨衣", "裙状雨披", "湿脏质感"]

第二皮肤:
  行为: "贴身弹性层承载胸腹、肩背和手臂肌肉读法。"
  可用材料: ["compression knit", "smooth stretch base", "rashguard-like fabric"]
  必须说明: "如何包住胸腹主块和手臂。"
  禁忌: ["普通光滑T恤", "隐藏肌肉", "过度性感化"]

半硬支撑:
  行为: "材料让衣服架离身体，形成肩、胸、背、鞋底或包体结构。"
  可用材料: ["semi-rigid nylon", "molded soft shell", "hard-edge panel"]
  必须说明: "支撑点和连接点。"
  禁忌: ["不可穿雕塑", "全身硬壳", "关节僵死"]

人工皮革单片包覆:
  行为: "软硬之间的一片材料绕身成壳，像外皮而非普通布料。"
  可用材料: ["smooth artificial leather", "soft coated shell"]
  必须说明: "固定点、包边、空隙。"
  禁忌: ["紧身皮衣模板", "裙化", "油亮噪点"]

软硬冲突:
  行为: "软布与硬片、胶质、金属硬件或厚鞋底互相改变轮廓。"
  可用材料: ["matte cloth + hard shell", "soft knit + molded panels", "wool-blend + plasticized pocket"]
  必须说明: "软硬分区和哪个部位被改变。"
  禁忌: ["材质清单无关系", "赛博发光线"]

重量转移:
  行为: "通过厚鞋底、重裤脚、背板、腰带或包体改变重心。"
  可用材料: ["segmented outsole", "heavy boot sidewall", "dense trouser hem", "back equipment frame"]
  必须说明: "重量落点和身体读法。"
  禁忌: ["只写厚底", "上轻下空", "站姿不稳"]

反光硬标:
  行为: "小面积反光、硬标或警示块承担身份识别。"
  可用材料: ["low-density reflective tab", "hard marker plate", "sealed color chip"]
  必须说明: "位置、面积、功能。"
  禁忌: ["满身高亮条", "真实品牌logo", "文字污染"]

压缩收束:
  行为: "弹性、束带、腰带、袖口或裤脚把体积收住。"
  可用材料: ["ribbed cuff", "wide elastic belt", "flat buckle tab", "compression sleeve"]
  必须说明: "收束点和外溢体积。"
  禁忌: ["jogger cuff", "裤子塞袜子", "紧腿削弱宽体"]
```

## San Zhai 输出要求

```yaml
outer_shell_prototype: "<来自 outer-shell-prototypes.md 的精确外层，或同等精度新原型>"
structural_event:
  名称: "<一个主结构事件>"
  部位: "<发生位置>"
  可见机制: "<观众能看见的结构变化>"
  身体作用: "<服务宽体、职业、动作或身份>"
material_behavior:
  名称: "<0-1 个辅助材质行为>"
  部位: "<作用位置>"
  行为: "<材质如何改变服装>"
anti_shirt_jacket_default:
  判断: "<为什么这不是衬衫夹克印花>"
```

## 打回例子

打回:

```text
stylish deconstructed jacket with transparent details
```

通过:

```text
hooded rain smock with an offset side entry, sealed translucent chest pocket blocks, a broad back-yoke panel from rear collar base to outer shoulder seams, matte waterproof shell over a fitted compression base layer, and segmented sole training shoes grounding the body
```
