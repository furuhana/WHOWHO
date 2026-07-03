# Base Garment Prototype Library

编码: UTF-8

此文件定义 WHOWHO 服装系统的基础款原型。基础款原型是服装被结构事件、材质行为或设计师方法加工之前，普通观众仍能识别的衣服类型。

## 使用原则

- `shirt`, `jacket`, `pants`, `shoes`, `bag` 只能作为大类，不得作为最终基础款原型。
- 最终记录必须细化到可生成原型，例如 `cropped utility jacket`, `hooded rain smock`, `panelled technical pants`, `segmented sole training shoe`, `crossbody tool bag`。
- 每套造型至少应选择一个非衬衫主视觉载体: 精确外层、马甲/护甲、腰部系统、腿部系统、鞋履系统、头颈系统、包具挂载或手臂系统。
- 如果职业确实需要衬衫或制服上衣，衬衫只能作为基础层或中层，必须由外层、腰部、腿部、鞋履或挂载系统接管主视觉。
- 禁止用裙、连衣裙、围裙、背带裙、sarong、kilt、wrap skirt 或 apron-like front panel 作为替代原型，除非用户明确覆盖全局偏好。

## 身体层级

```yaml
贴身底层:
  - fitted crewneck T-shirt
  - fitted ribbed tank top
  - sleeveless compression top
  - fitted high-neck base layer
  - mock-neck base layer
  - zip-neck compression base layer
  - rashguard base layer
  - thermal fitted base layer
  - bodysuit base layer
  - skinsuit base layer

中层:
  - Oxford shirt
  - dress shirt
  - stand-collar shirt
  - work shirt
  - camp-collar shirt
  - western shirt
  - crewneck sweater
  - cardigan
  - zip hoodie
  - half-zip pullover
  - rugby shirt
  - team jersey top
  - service tunic top
  - medical tunic top
  - utility overshirt

外层:
  - use `outer-shell-prototypes.md` for final selection

连体:
  - work coverall
  - boiler suit
  - mechanic jumpsuit
  - flight suit
  - utility jumpsuit
  - bib overalls
  - driver suit
  - racing suit
  - cycling suit
  - dive suit
  - sealed weather suit
  - clean-room protective suit

下装:
  - tailored trousers
  - pleated trousers
  - high-waisted wide trousers
  - cropped tailored trousers
  - cargo pants
  - utility pants
  - double-knee work pants
  - painter pants
  - mechanic pants
  - straight jeans
  - wide jeans
  - panelled denim pants
  - track pants
  - training pants
  - basketball warm-up pants
  - panelled technical pants
  - articulated knee pants
  - reinforced trousers
  - hakama-like wide trousers clearly split as pants
  - martial arts pants
  - tailored shorts
  - utility shorts
  - boxing shorts
  - basketball shorts
  - cycling shorts
  - swim shorts

鞋履:
  - derby shoe
  - loafer
  - monk-strap shoe
  - thick-sole formal shoe
  - runner sneaker
  - basketball sneaker
  - training shoe
  - court shoe
  - skate shoe
  - canvas low-top
  - high-top sneaker
  - combat boot
  - work boot
  - riding boot
  - Chelsea boot
  - hiking boot
  - engineer boot
  - short utility boot
  - sport sandal
  - strap sandal
  - geta-like sandal
  - cloth shoe
  - martial arts shoe
  - platform shoe
  - segmented sole shoe
  - sculptural sidewall sneaker
  - architectural sole shoe
  - sock shoe
  - gaiter-boot hybrid

防护装备:
  - hard torso vest
  - soft armor vest
  - protective chest plate
  - shoulder guard
  - forearm guard
  - elbow guard
  - sleeve armor
  - knee guard
  - shin guard
  - thigh panel
  - leg brace
  - wide support belt
  - load-bearing waist belt
  - back equipment frame
  - breathing pack
  - sealed hood shell

包具挂载:
  - daypack
  - technical backpack
  - roll-top backpack
  - rescue pack
  - crossbody bag
  - messenger bag
  - body bag
  - camera bag
  - waist pouch
  - hip pouch
  - leg pouch
  - tool pouch
  - duffel bag
  - doctor bag
  - tool case
  - box bag
  - key loop
  - tool ring
  - bottle holder
  - tag plate
  - badge tab
  - chest harness
  - shoulder harness
  - cross-back strap
  - suspender system

头颈手足:
  - cap
  - beanie
  - bucket hat
  - helmet
  - hood
  - wide-brim hat
  - work cap
  - stand collar
  - hood collar
  - scarf
  - neck gaiter
  - detachable collar
  - work gloves
  - fingerless gloves
  - protective gloves
  - arm warmers
  - forearm sleeves
  - crew socks
  - knee socks
  - compression socks
  - split-toe socks
  - gaiters
```

## 原型精度检查

通过:

```text
base_garment_prototype: "hooded rain smock + panelled technical pants + segmented sole training shoe"
```

打回:

```text
base_garment_prototype: "shirt, jacket, pants, shoes"
```

## 反默认规则

- 当输出含有 `shirt + jacket + pants` 的泛用组合时，三宅必须从 `outer-shell-prototypes.md` 重新选择一个精确外层原型，或说明哪个非衬衫系统承担主视觉。
- 当外层只写 `jacket`、`coat`、`vest`、`hoodie`、`outerwear` 时，缪斯和黑墙应打回。
- 当材质只写 `transparent material`、`leather`、`metal`、`nylon`，但没有说明材质行为时，缪斯和黑墙应打回。
