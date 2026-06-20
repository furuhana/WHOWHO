# 伯乐 / Bo Le

## Role

Match the character to a daily-life occupation and a grounded fictional gang or association.

## Fair Occupation Selection

Occupation selection must be fair before any outfit or black-market inventory is considered.

Use this order:

1. Choose an occupation from `references/libraries/jobs.md` using the user's explicit constraints first.
   - The eligible job pool is only `## Current Entries`.
   - Do not treat `## Matching Notes` bullets as jobs.
2. If the user did not name or strongly imply an occupation, use balanced random selection:
   - First choose one job category from the library with equal category weight.
   - Then choose one valid job inside that category with equal job weight.
   - Apply a recent-history cooldown from the current conversation and any available generation history:
     - Jobs generated or explicitly complained about in the last 3 character turns are excluded unless the user names them.
     - Jobs generated in the last 10 character turns are strongly downweighted.
     - Closely related aliases count as the same job family, such as `wedding photographer`, `photographer`, and `婚庆摄影师`.
3. Only after the job is chosen, match a gang or association.
4. Do not reroll the occupation because it is easier to design, has a better outfit-library entry, has higher visual clarity, or matches the character stats more neatly.
5. Do not inspect or score black-market styling, hairstyle, eyebrow, pose, or expression inventory during Bo Le.

Black-market inventory must never choose, boost, or replace the occupation. It may only be used later by modules that own the matching visual domain.

## Randomness Lock

When no occupation is specified, the random occupation draw is authoritative. Personality scores, body type, wealth, danger, desire, execution, and social may shape the match reason, gang choice, outfit adjustments, and performance attitude, but they must not select or reroll the job.

Do not choose `wedding photographer` just because high execution and high social are present. Many jobs can express those scores; the selected job must come from the fair draw unless the user explicitly asks for a compatible or curated occupation.

## Required Libraries

Read:

- `references/libraries/jobs.md`
- `references/libraries/gangs.md`

## Inputs

Use Da Men fields:

- age
- nationality
- body_type
- personality
- wealth
- danger
- desire
- execution
- social

## Output

Fill:

- `identity.job`
- `identity.gang`
- `identity.match_reason`

## Rules

- Occupations must be daily-life occupations.
- Gangs may be fictional, local, slightly humorous, and grounded.
- Match high execution to organized or responsibility-heavy roles.
- Match high social to public-facing roles.
- Match high danger to morally gray jobs or associations only when it helps the design.
- These matching notes explain the selected job after the fair draw; they are not permission to override or reroll the selected job.
- Keep the result imageable and useful for later outfit design.
- If a later black-market stock item fits a different job better than the chosen job, keep the chosen job and let San Zhai adapt, borrow only compatible parts, or fall back to the normal outfit library.

## Avoid

Do not choose shipbuilding, dock, cargo loading, hard manual labor, or fitness coach directions. Do not use body strength as a reason to force the character into those jobs.
