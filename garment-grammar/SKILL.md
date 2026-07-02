---
name: garment-grammar
description: WHOWHO garment-construction translator for upgrading plain outfits into precise no-skirt, no-apron fashion design language. Use when Character Forge, San Zhai, Muse, Blackwall, or Azoth needs professional garment keywords, cutting logic, silhouette rules, pants/outerwear design variants, or anti-basic-clothing constraints for character creation.
---

# Garment Grammar

## Role

Use this skill as the WHOWHO服装语法转换器. It does not create the whole character and does not replace San Zhai, Muse, Blackwall, or Azoth.

Its job is narrow:

```text
plain outfit intent / occupation clothing need
-> garment construction grammar
-> San Zhai outfit fields
-> Muse and Blackwall audit
-> Azoth image prompt wording
```

## Required Reference

Read `references/no-skirt-garment-grammar.md` whenever San Zhai is designing, revising, or auditing clothing. Use it together with the existing black-market design references when available:

- `../black-market/references/designer-methods.md`
- `../black-market/references/design-operators.md`
- `../black-market/references/pattern-and-cutting.md`
- `../black-market/references/footwear-accessory-grammar.md`

## Hard Clothing Ban

The user preference is global for WHOWHO character creation unless explicitly overridden in a later user request:

- no skirts
- no dresses
- no aprons
- no pinafores
- no maid aprons
- no kitchen, vendor, waist, or work aprons
- no skirt-like lower garments described with `skirt`, `dress`, `apron`, `pinafore`, or `sarong`

If a job would normally use an apron, replace the apron function with a non-apron structure: utility vest, waist belt, chest harness, tool belt, short overshirt, protective front placket, side pouch, crossbody tool bag, or modular pocket panel attached to trousers.

If a silhouette would normally use a skirt, replace it with pants or shorts: wide-leg trousers, pleated trousers, straight cropped trousers, panelled technical pants, tailored shorts, jumpsuit, coverall, or layered trouser panels that remain clearly pants.

## Division Of Labor

- San Zhai uses this skill before filling `outerwear`, `base_layer`, `pants`, `shoes`, accessories, and advanced design grammar fields.
- Muse checks whether San Zhai actually used garment construction instead of generic clothing names.
- Blackwall rejects banned lower garments, apron substitutes that still read as aprons, random decorative lines, and missing panel/craft logic.
- Azoth translates approved garment grammar into imageable English prompt prose. Azoth must not expose internal field names or module names in the prompt.

## Output Contract For San Zhai

Every designed outfit should provide:

```yaml
garment_grammar:
  garment_line: quiet_tailoring | soft_deconstruction | utility_atelier | street_atelier | protective_tailoring
  banned_shape_check: "no skirt, no dress, no apron; apron functions replaced by <structure>"
  base_garment_prototype:
  primary_design_point:
  secondary_design_point:
  silhouette:
  cut:
  construction:
  fabric_zones:
  closure_or_fastening:
  panel_paths:
    - start:
      route:
      endpoint:
      body_rule:
  craft_boundaries:
  trouser_design:
  footwear_structure:
  accessory_structure:
  professional_keywords:
  negative_clothing:
```

Then map those fields into the existing Character Forge record:

- `base_garment_prototype`
- `designer_method_references`
- `design_operators`
- `panel_paths`
- `pattern_strategy`
- `craft_boundaries`
- `body_fit_strategy`
- `complexity_budget`
- `design_failure_avoidance`
- `design_function_slots`
- `replacement_slots_used`
- `anti_default_decision`

## Prompt Handoff

Garment Grammar should hand Azoth concrete English construction language, not designer-name shortcuts.

Good:

```text
cropped structured jacket with exaggerated square shoulders, offset concealed placket, clean exposed inner facing, curved chest-side panels from shoulder peak to side waist, high-waisted 9-length wide-leg trousers with pressed front crease and reinforced side panels
```

Bad:

```text
designer outfit, high fashion, Margiela style, Rick Owens style, stylish black clothes
```

Always pass a compact negative clothing clause:

```text
no skirt, no dress, no apron, no pinafore, no maid outfit, no school uniform skirt, no generic T-shirt and jeans, no plain casualwear
```
