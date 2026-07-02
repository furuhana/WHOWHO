# Character Schema

Keep one shared record and update it module by module.

```yaml
basic:
  name:
  gender:
  age:
  nationality:
  body_type:
  personality:
  wealth: 1-10
  danger: 1-10
  desire: 1-10
  execution: 1-10
  social: 1-10

world_context:
  era_background:
  culture_system:
  culture_stage:
  street_texture:
  technology_level:
  order_level:
  material_ecology:
  visual_taboo:

identity:
  job:
  gang:
  match_reason:

outfit:
  outerwear:
  base_layer:
  pants:
  socks:
  shoes:
  accessories:
    - slot:
      item:
  styling_algorithm:
  base_garment_prototype:
  designer_method_references:
    -
  designer_prompt_references:
    -
  design_operators:
    - operator:
      body_part:
      purpose:
  panel_paths:
    - name:
      start:
      route:
      endpoint:
      rule:
  pattern_strategy:
    type:
    placement:
      -
    density:
    prohibitions:
      -
  craft_boundaries:
    -
  body_fit_strategy:
  footwear_accessory_structure:
  complexity_budget:
  design_failure_avoidance:
    -
  design_function_slots:
    -
  replacement_slots_used:
    -
  variation_matrix:
    scene:
    emotion:
    body_need:
    resource_source:
    recognition_strength:
    variation_scale:
  anti_default_decision:
  outfit_reason:

grooming:
  hairstyle:
  eyebrows:
  beard:
  face_shape:
  grooming_reason:

muse:
  verdict:
  outfit_read:
  strengths:
    - 
  issues:
    - module:
      reason:
      reroute_to:
  repair_advice:
    - 

blackwall:
  passed:
  issues:
    - module:
      reason:
      reroute_to:
  integrated_design:

azoth:
  dynamic_slots:
    role_visual:
    outfit_dynamic:
    accessory_dynamic:
    grooming_dynamic:
    pose_dynamic:
    expression_dynamic:
    platform_dynamic_decisions:
  prompt_en:
  prompt_cn:
  prompt_notes:
```

The YAML keys above are internal structure keys. In user-facing output, translate them into Chinese labels.

## User-Facing Chinese Labels

Use these labels in final answers:

```text
basic -> 基础信息
name -> 名字
gender -> 性别
age -> 年龄
nationality -> 国籍
body_type -> 体型
personality -> 性格
wealth -> 贫富值
danger -> 危险值
desire -> 欲望值
execution -> 执行力
social -> 社交力

world_context -> 世界底盘
era_background -> 时代背景
culture_system -> 文化体系
culture_stage -> 文化阶段
street_texture -> 市井特点
technology_level -> 技术层级
order_level -> 秩序状态
material_ecology -> 材料生态
visual_taboo -> 视觉禁忌

identity -> 社会身份
job -> 职业
gang -> 帮派
match_reason -> 匹配理由

outfit -> 工作服
outerwear -> 外套
base_layer -> 打底
pants -> 裤子
socks -> 袜子
shoes -> 鞋子
accessories -> 饰品/道具
slot -> 部位
item -> 物件
styling_algorithm -> 造型算法
base_garment_prototype -> 基础款原型
designer_method_references -> 匿名设计方法
designer_prompt_references -> 设计师提示引用
design_operators -> 设计操作符
operator -> 操作
body_part -> 部位
purpose -> 作用
panel_paths -> 裁片路径
name -> 名称
start -> 起点
route -> 经过
endpoint -> 终点
rule -> 规则
pattern_strategy -> 图案策略
type -> 类型
placement -> 位置
density -> 密度
prohibitions -> 禁忌
craft_boundaries -> 工艺边界
body_fit_strategy -> 身体适配
footwear_accessory_structure -> 鞋饰结构
complexity_budget -> 复杂度配额
design_failure_avoidance -> 失败规避
design_function_slots -> 设计功能位
replacement_slots_used -> 可替换位
variation_matrix -> 变化矩阵
scene -> 场景
emotion -> 情绪
body_need -> 身体需求
resource_source -> 资源来源
recognition_strength -> 识别强度
variation_scale -> 变化幅度
anti_default_decision -> 反默认判断
outfit_reason -> 服装理由

grooming -> 头脸造型
hairstyle -> 发型
eyebrows -> 眉型
beard -> 胡子
face_shape -> 脸型
grooming_reason -> 造型理由

muse -> 缪斯审核
verdict -> 结论
outfit_read -> 穿搭识别
strengths -> 值得保留
repair_advice -> 修改建议

blackwall -> 黑墙审核
passed -> 是否通过
issues -> 问题
module -> 问题模块
reason -> 原因
reroute_to -> 打回对象
integrated_design -> 整合设定

azoth -> 阿佐特提示词
dynamic_slots -> 动态提示词槽位
role_visual -> 职业视觉
outfit_dynamic -> 服装动态描述
accessory_dynamic -> 饰品/道具动态描述
grooming_dynamic -> 头脸动态描述
pose_dynamic -> 姿势动态描述
expression_dynamic -> 表情动态描述
platform_dynamic_decisions -> 底座动态决策
prompt_en -> 英文提示词
prompt_cn -> 中文提示词
prompt_notes -> 提示词说明
```

## Score Meanings

- `wealth` / 贫富值：可见的经济印象，1 是贫穷或朴素，10 是富裕。
- `danger` / 危险值：道德灰度和威胁感，不等于身体力量。高值可以是反派、灰色人物或压迫感。
- `desire` / 欲望值：野心、贪念、执念、虚荣或躁动。
- `execution` / 执行力：行动、完成、组织、落实的能力。
- `social` / 社交力：读人、说服、经营关系和融入场面的能力。

## Visual Translation

When later writing prompts, translate scores into visible traits. Do not write abstract scores directly.

Expression and pose words here are selection hints only. Azoth must prefer approved `表情库存` and `姿势库存` when shaping face performance or full-body acting, and must not treat these examples as a private expression library.

- 低贫富值：朴素但干净的衣服、便宜细节、实用配件。
- 高贫富值：更好的面料、更精致的饰品、更有意图的造型。
- 高危险值：锐利眼神、防备姿态、更硬的轮廓。
- 高欲望值：躁动表情、显眼细节、野心感。
- 高执行力：克制姿态、实用工具、有条理的造型。
- 高社交力：开放表情、自信呈现、容易接近的细节。

## User-Facing Table Display

In `角色档案`, prefer Markdown tables over long field lists.

Use two-group side-by-side tables when fields are compact:

```markdown
| 基础信息 | 内容 | 能力数值 | 内容 |
|---|---|---|---|
| 名字 |  | 贫富值 |  |
| 性别 |  | 危险值 |  |
| 年龄 |  | 欲望值 |  |
| 国籍 |  | 执行力 |  |
| 体型 |  | 社交力 |  |
| 性格 |  |  |  |

| 世界底盘 | 内容 | 世界底盘 | 内容 |
|---|---|---|---|
| 时代背景 |  | 技术层级 |  |
| 文化体系 |  | 秩序状态 |  |
| 文化阶段 |  | 材料生态 |  |
| 市井特点 |  | 视觉禁忌 |  |

| 社会身份 | 内容 | 头脸造型 | 内容 |
|---|---|---|---|
| 职业 |  | 发型 |  |
| 帮派 |  | 眉型 |  |
| 匹配理由 |  | 胡子 |  |
|  |  | 脸型 |  |
```

Use a single two-column table or short grouped list when values are long, especially for `工作服`, `服装理由`, audits, and prompt notes. Keep final prompts in fenced code blocks, not tables.

World context fields are selection and translation hints, not prompt text. Later modules should translate them into visible character-bound design:

- 时代背景：轮廓、闭合方式、层次节奏、硬件密度。
- 文化体系：包覆方式、腰部结构、身份标记、纹样位置、服务/市集/工会小件。
- 文化阶段：新配发、旧制度残留、干净自改、严格管制、繁荣定制、转型混搭。
- 市井特点：票卡、腰包、摊位牌、修理工具、雨具、巡查标、路线卡等随身物。
- 技术层级：模拟标签、机械扣具、民用设备、透明防护件、小型扫描器。
- 秩序状态：遮蔽、证件、徽章、巡查标记、防御层或街区自治标识。
- 材料生态：防水布、透明塑料、哑光合成面、金属扣具、旧制服布料、传统织物片。
- 视觉禁忌：直接约束服装、职业、材质和提示词，不写入最终 prompt 字面。
