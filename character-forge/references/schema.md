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
