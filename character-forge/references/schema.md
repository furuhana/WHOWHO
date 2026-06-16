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
  beard:
  face_shape:
  grooming_reason:

blackwall:
  passed:
  issues:
    - module:
      reason:
      reroute_to:
  integrated_design:

azoth:
  prompt_en:
  prompt_cn:
  prompt_notes:
```

## Score Meanings

- `wealth`: visible economic impression, 1 is poor or modest, 10 is rich.
- `danger`: moral ambiguity and threat aura, not physical strength. High values can be villainous, gray, or intimidating.
- `desire`: appetite, ambition, greed, obsession, vanity, or restless wanting.
- `execution`: ability to act, finish, organize, and enforce.
- `social`: ability to read people, persuade, network, and blend in.

## Visual Translation

When later writing prompts, translate scores into visible traits. Do not write abstract scores directly.

- Low wealth: modest but clean clothing, cheap details, practical accessories.
- High wealth: better fabrics, polished accessories, deliberate styling.
- High danger: sharp gaze, guarded posture, harder silhouette.
- High desire: restless expression, showy detail, ambitious energy.
- High execution: disciplined posture, practical tools, controlled styling.
- High social: open expression, confident presentation, approachable details.
