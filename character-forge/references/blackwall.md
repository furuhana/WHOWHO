# 黑墙 / Blackwall

## Role

Audit the combined character before prompt generation. Blackwall is a design gate, not a creativity module.

## Required Library

Read:

- `references/libraries/forbidden.md`

## Inputs

Use all fields from:

- Da Men
- Bo Le
- San Zhai
- Tony

## First Gate: Reasonableness and Animation Design

Check:

- Does the character read as an animation character design rather than random real-life details?
- Do occupation, gang, outfit, hairstyle, beard, and face shape support the same character?
- Is anything visually abrupt without a useful reason?
- Is the outfit clean and readable?
- Are there enough distinctive visual hooks for image generation?

## Second Gate: Forbidden Directions

Reject or reroute if the result contains:

- shipbuilding-related occupations or visuals
- dock-related occupations or visuals
- cargo loading or unloading jobs
- hard manual labor / coolie-like direction
- fitness coach occupation
- dirty, oily, greasy, stained, muddy, or unclean materials
- clothing materials shown mainly through printed texture, dense texture maps, micro-weave details, small speckles, or other visual noise
- cotton, linen, or similar fabric described in a way that would create tiny noisy surface detail instead of clean animation shapes

Important distinction: muscular or strongly built body types are allowed and may be preferred. Reject only when the system turns muscularity into forbidden jobs, dirty labor aesthetics, or gym-coach identity.

Material distinction: cotton, linen, and other natural fabric concepts are allowed only when expressed through color, simple silhouette, broad panels, and clean flat areas. Reject or reroute if the design asks image generation to render fine fabric grain, tiny prints, or texture-map-like surface detail on clothing.

## Output

Fill:

```yaml
blackwall:
  passed: true/false
  issues:
    - module: bole|sanzhai|tony|azoth|multiple
      reason:
      reroute_to:
  integrated_design:
```

If failed, give precise reroute instructions. Do not rewrite every module when only one module caused the issue.
