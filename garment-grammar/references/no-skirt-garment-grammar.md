# No-Skirt Garment Grammar

编码: UTF-8

This reference upgrades basic WHOWHO clothing into professional garment-construction language while obeying the global no-skirt and no-apron preference.

## Design Intent

Each outfit should stay wearable, readable, and animation-friendly, but it must show that someone designed the garment. Do not solve this by adding noise. Solve it through silhouette, cutting, construction, fabric zoning, closure, trouser architecture, footwear, and body-aware accessories.

Use these shared prototype and event libraries when they exist:

- `black-market/references/base-garment-prototypes.md`
- `black-market/references/outer-shell-prototypes.md`
- `black-market/references/structural-events-and-material-behaviors.md`

`shirt`, `jacket`, `pants`, `shoes`, and `bag` are category words only. They are not precise final prototypes. Final garment language must choose a specific prototype such as `hooded rain smock`, `field coat`, `long sleeveless coat`, `pullover anorak`, `protective vest`, `panelled technical pants`, or `segmented sole training shoe`.

## Outer Shell Requirement

When an outfit has any outer layer, Garment Grammar must name a precise `outer_shell_prototype`. Do not leave the outer layer as `jacket`, `coat`, `vest`, `shirt jacket`, `outerwear`, or `hoodie`.

Use one of these families or an equivalent precise prototype:

```yaml
short_outer_shells: ["cropped box jacket", "cropped utility jacket", "cropped riding jacket", "short track shell", "short field shell"]
mid_outer_shells: ["shop coat", "chore coat", "field coat", "safari jacket", "utility smock", "rain smock", "mechanic coat"]
long_outer_shells: ["straight overcoat", "long narrow coat", "trench coat", "hooded long shell", "greatcoat"]
sleeveless_outer_shells: ["utility vest", "protective vest", "long sleeveless coat", "equipment vest shell"]
drape_shells: ["short shoulder mantle", "weather poncho", "back-mounted cloak panel", "folded geometric outer shell"]
pullover_shells: ["pullover anorak", "hooded smock", "technical half-zip shell"]
occupational_shells: ["guard tunic", "service coat", "rescue shell", "maintenance coat"]
structural_shells: ["offset-placket jacket", "inside-out shell", "multi-opening jacket", "single-sheet wrap shell", "sealed pocket shell"]
```

If a shirt-like garment is present, it is a base or middle layer unless the user explicitly requested a plain shirt outfit. The main visual carrier must be the precise outer shell, vest/armor, waist system, leg system, shoes, head/neck frame, or mounted accessory system.

## Structural Event Grammar

Each advanced outfit should include one primary `structural_event` and zero or one supporting `material_behavior`.

Preferred structural events:

```yaml
structural_events:
  - "错入口: side entry, inactive sleeve opening, offset placket, or secondary opening that stays wearable"
  - "反穿内外互换: exposed facing, lining, reverse seam, or back-side construction used as the visible side"
  - "错肢穿法: extra garment limb or displaced sleeve/neck logic that never changes the human body"
  - "制服切开: uniform or tailoring cut away, shortened, shifted, or waist-suppressed while staying authoritative"
  - "制作痕迹外露: clean exposed seams, seam allowance, zipper teeth, binding, temporary tabs, or unfinished clean edges"
  - "材质封存: objects, marker plates, stitch lines, or small tools sealed inside translucent or semi-rigid panels"
  - "单片包覆: one continuous sheet wraps around shoulder, back, chest, or waist with clear fixed points"
  - "普通原型故障: familiar garment appears wrong through false sleeves, false layers, offset pockets, or trompe-l'oeil splicing"
  - "身体硬件命名: one hardware focal point names chest, waist, hand, or back"
  - "热压折线成体积: heat-pressed fold planes create volume and movement direction"
```

Preferred material behaviors:

```yaml
material_behaviors:
  - "透明显露"
  - "封存"
  - "防水外壳"
  - "第二皮肤"
  - "半硬支撑"
  - "人工皮革单片包覆"
  - "软硬冲突"
  - "重量转移"
  - "反光硬标"
  - "压缩收束"
```

Bad:

```text
stylish deconstructed jacket with transparent material
```

Good:

```text
hooded rain smock with an offset side entry, sealed translucent chest pocket blocks, broad back-yoke panel from rear collar base to outer shoulder seams, matte waterproof shell over a fitted compression base layer, and segmented sole training shoes grounding the body
```

## Banned Shapes

Never use these unless the user explicitly overrides the ban:

```text
skirt, dress, apron, pinafore, sarong, kilt, maid apron, school uniform skirt, pleated skirt, wrap skirt, half apron, waist apron, kitchen apron, vendor apron, work apron
裙子, 半裙, 连衣裙, 围裙, 背带裙, 女仆围裙, 校服裙, 厨师围裙, 工作围裙, 腰围裙
```

Do not hide banned shapes behind softer language such as `skirt-like`, `apron-like`, `front apron panel`, `wrap skirt`, or `skirt over pants`.

Allowed replacements:

- `front utility placket attached to a jacket`
- `wide belt with flat tool tabs`
- `short structured overshirt`
- `crossbody tool harness`
- `waist tool belt`
- `side-mounted pouch system`
- `panelled trousers`
- `wide-leg trousers`
- `pleated trousers`
- `cropped tailored trousers`
- `tailored shorts`
- `jumpsuit`
- `coverall`

## Garment Lines

Use one line per outfit. Do not blend all lines at once.

```yaml
quiet_tailoring:
  use_for: "calm, formal, city, intelligent, high-social, controlled jobs"
  silhouette: ["cropped structured jacket", "long narrow coat", "sharp vest", "high-waisted trousers"]
  methods: ["square shoulder", "cinched waist", "concealed closure", "pressed trouser crease"]
  keywords: ["structured tailoring", "architectural shoulder", "clean waist suppression", "matte wool-blend", "sparse hardware"]

soft_deconstruction:
  use_for: "artist, repair, informal specialist, emotionally complex or off-duty roles"
  silhouette: ["offset overshirt", "deconstructed blazer", "layered high-neck top", "relaxed pleated trousers"]
  methods: ["offset placket", "exposed inner facing", "clean unfinished edge", "asymmetric panel route"]
  keywords: ["exposed construction", "offset closure", "visible facing", "controlled asymmetry", "clean raw edge"]

utility_atelier:
  use_for: "active jobs, street work, service roles, technical civilian roles"
  silhouette: ["short utility jacket", "modular vest", "panelled technical pants", "protective boots"]
  methods: ["modular pockets", "flat buckle tabs", "leg-side pouch", "articulated knee panels"]
  keywords: ["modular utility", "load-bearing waist", "articulated trouser panels", "matte nylon zones", "compact tool mounting"]

street_atelier:
  use_for: "young, subculture, entertainment, casual city roles"
  silhouette: ["cropped jacket", "oversized trousers", "layered hoodie", "distorted denim-like pants"]
  methods: ["short-wide proportion", "dropped shoulder", "mixed fabric blocks", "oversized trouser volume"]
  keywords: ["short-wide silhouette", "oversized leg volume", "mixed material blocking", "low-density graphic marker"]

protective_tailoring:
  use_for: "regulated, defensive, civic, security-adjacent or high-danger roles without military drift"
  silhouette: ["structured overshirt", "protective vest", "reinforced trousers", "stable boots"]
  methods: ["hard edge panels", "chest badge tab", "forearm guard", "reinforced side seam"]
  keywords: ["civilian protective tailoring", "clean hard-edge panels", "reinforced cuff", "stable boot sidewall"]
```

## Upgrade Patterns

Use these as phrase banks. Select one primary design point and one secondary design point.

### Outerwear

```yaml
jacket:
  - "cropped boxy jacket with exaggerated square shoulders, offset concealed placket, compact waist tabs"
  - "short utility jacket with modular chest pockets, flat buckle tabs, and a raised stand collar"
  - "structured overshirt with a diagonal front seam, exposed inner facing, and crisp bound edges"
  - "compact protective jacket with curved chest-side panels and reinforced forearm sections"

coat:
  - "long narrow coat with high stand collar, hidden placket, and clean vertical side panels"
  - "straight knee-length coat with shoulder-to-side-waist panel path and sparse metal hardware"
  - "rainproof matte coat with broad yoke panel, sealed pocket flaps, and controlled side opening"

blazer:
  - "deconstructed blazer with offset lapel, exposed facing, and one clean unfinished hem edge"
  - "cropped tailored blazer with square shoulder, short body, and sharp waist suppression"
  - "collarless blazer with curved front seam, concealed closure, and clean topstitch boundaries"

vest:
  - "structured utility vest with broad shoulder straps, compact chest tabs, and waist-level tool loops"
  - "tailored waistcoat with high armholes, clean front darts, and a wide back adjustment tab"
```

### Base Layers

Base layers support body readability. They should not become the main idea unless the job requires it.

```yaml
top:
  - "fitted high-neck base layer wrapping the chest and abdomen with clean anime anatomy contour"
  - "crisp shirt used as an underlayer, with extended cuffs and an offset collar edge"
  - "sleeveless fitted top under structured outerwear, exposing shoulder and arm mass clearly"
  - "compact zip-neck top with a clean vertical closure and broad flat color block"
```

### Pants And Shorts

Prefer pants, trousers, shorts, jumpsuits, and coveralls. Keep WHOWHO leg mass stable.

```yaml
trousers:
  - "high-waisted 9-length wide-leg trousers with pressed front crease and reinforced side panels"
  - "relaxed pleated trousers with deep front pleats, broad thigh volume, and a clean cropped break"
  - "straight tailored trousers with extended waistband tab, flat front, and controlled side stripe"
  - "panelled technical pants with articulated knee seams, side-mounted pocket block, and matte fabric zones"
  - "tapered protective trousers with large thigh volume, clean knee break, and stable shoe-collar opening"

shorts:
  - "structured above-knee tailored shorts with broad hem, clear belt line, and plain white socks visible below"
  - "utility shorts with flat cargo tabs, reinforced side seam, and compact tool loop near the hip"

jumpsuit:
  - "clean work jumpsuit with a defined waist belt, short upper opening, and panelled legs"
  - "sleeveless coverall with broad shoulder frame, front zipper track, and reinforced trouser panels"
```

## Panel Path Templates

Every advanced outfit needs at least one path.

```yaml
chest_side_panel:
  start: "below the shoulder peak"
  route: "around the outer pectoral mass"
  endpoint: "side waist tab"
  body_rule: "frames the huge chest without cutting the abdomen into small pieces"

sleeve_outer_panel:
  start: "outer shoulder cap"
  route: "breaks at the elbow and resumes along the forearm ridge"
  endpoint: "reinforced cuff"
  body_rule: "supports giant arms and avoids random lines across the joint"

trouser_side_panel:
  start: "high side waist"
  route: "down the outer thigh, breaking around the knee"
  endpoint: "shoe collar or lower calf edge"
  body_rule: "emphasizes thick thighs and stable lower body"

back_yoke_panel:
  start: "rear collar base"
  route: "across the upper back and shoulder blades"
  endpoint: "outer shoulder seam"
  body_rule: "widens the shoulder-back silhouette"

shoe_sidewall_path:
  start: "toe cap edge"
  route: "along the outer sole sidewall"
  endpoint: "raised heel block"
  body_rule: "grounds the heavy body through a readable sole structure"
```

## Professional Keyword Builder

Build final clothing language from these slots:

```text
[prototype] + [silhouette] + [cut / panel path] + [closure] + [fabric zones] + [craft boundary] + [body purpose]
```

Example:

```text
cropped structured jacket, exaggerated square shoulders, offset concealed placket, curved chest-side panels starting below the shoulder peak and ending at side waist tabs, matte wool-blend body with smooth nylon side panels, crisp bound edges, designed to widen the shoulder line and keep the chest mass readable
```

## Negative Clothing Clause

Use this in Azoth's compact negative constraints when garment grammar is active:

```text
no skirt, no dress, no apron, no pinafore, no maid outfit, no school uniform skirt, no wrap skirt, no apron-like front panel, no generic T-shirt and jeans, no plain casualwear, no random decorative garment lines
```

## Audit Checklist

Before passing to Muse or Blackwall, verify:

- The outfit contains no skirt, dress, apron, pinafore, or apron-like substitute.
- At least one outerwear, waist, leg, footwear, or accessory system carries the main design idea.
- A shirt or T-shirt is not the primary visual unless the occupation truly requires it and two other systems compensate.
- The primary design point is clear in one sentence.
- The outfit names one readable base prototype before modifications.
- Any outer layer has a precise outer-shell prototype, not generic jacket/coat/vest/hoodie wording.
- Any deconstruction has a named structural event with a visible mechanism.
- Any material replacement has a material behavior, not only a material name or transparency.
- If a shirt-like garment exists, another visible system carries the primary design idea.
- At least one panel path has start, route, endpoint, and body rule.
- Shoes include prototype, sole structure, upper cutting, cuff/sock/trouser connection, and grounding role.
- Accessories attach to a body location and change body reading or role readability.
- Complexity stays near large silhouette 60%, medium panels 25%, small craft 10%, pattern/symbol 5%.
- Designer names are absent unless the user explicitly allowed prompt-level designer references.
