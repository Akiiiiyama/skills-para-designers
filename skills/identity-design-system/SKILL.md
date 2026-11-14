---
name: identity-design-system
description: Guides a person to create their own design system starting from the visual identity THEY want — an interview about values, personality and references, two or three identity directions, a name with meaning, a visual proposal page for approval, and then a working code-first starter (W3C DTCG tokens, light/dark CSS, contrast tests) they can grow into components and Figma. Use when someone says "I want my own design system", "help me define my visual identity and turn it into tokens", "create a design system for my portfolio/brand/product", or wants to do what IY Lotus did for themselves.
---

# Identity-first design system

A design system that feels like someone starts with **who they are**, not with a component list. This skill runs the same path IY Lotus took (see the `lotus-design-system` skill) but for any person or brand: discover the identity, make it visible, get approval, and only then turn it into tokens that are tested and shippable.

The person decides the identity. Claude asks, proposes options, shows them, and builds — it never imposes a style. Every visual choice must trace back to something the person said.

## When to use

- Someone wants their own design system for a portfolio, personal brand, side project or small product.
- They have a vague identity ("minimal but warm", "bold like my reel") and want it turned into rules.
- Not for auditing an existing large system (use a design-system audit instead) or for picking a UI kit off the shelf.

## Steps

### 1. Identity interview (ask, don't assume)

Ask in short rounds — never more than 4 questions at a time. Use [`references/identity-interview.md`](references/identity-interview.md). Cover:

- **Purpose and audience**: what will it build first (site, app, deck)? who sees it?
- **Values**: 3–4 words they want their work to carry (IY Lotus: growth, beauty, discipline, wisdom).
- **Personality sliders**: calm ↔ energetic, minimal ↔ expressive, warm ↔ cool, classic ↔ experimental, rounded ↔ sharp, light ↔ dark first.
- **References**: 3 things they love (sites, posters, a video, a place) and 1 they don't want to look like. Ask why for each.
- **Existing assets**: logo, colors, fonts, a reel, a photo — anything already approved by them wins over new ideas.
- **Constraints**: tools and plans (Figma Starter has one variable mode per collection, no shared libraries), stack (React, plain HTML), accessibility needs, languages.

Write back a one-paragraph **identity brief** and get a yes before going on.

### 2. Two or three directions

From the brief, propose 2–3 distinct directions. For each: a name for the direction, the 4 values mapped to visual decisions, a palette (neutrals + 1 accent, max 2), a type pairing (one family is fine; weights carry the voice), shape (radius), density (spacing base), motion feel (easing, duration), and **one signature detail** (IY Lotus: the red period after a word). Show contrast ratios for text on background for every palette. Recommend one and say why, in the person's own words.

### 3. Name with meaning

Offer 6–10 names tied to the values or the person (initials + a symbol works well). When chosen, turn the metaphor into the **layer names** of the system, e.g. Root / Stem / Petal / Bloom, Ground / Wall / Room / House, Seed / Branch / Leaf / Tree. Layers are always: raw values → themed meaning → components → pages.

### 4. Visual proposal page (approval gate)

Build one HTML page in the chosen direction itself — not a neutral spec sheet. Follow [`references/proposal-page.md`](references/proposal-page.md): hero with the name and tagline, values, palette with contrast, type scale, spacing, radius, buttons/inputs/cards in all states, light and dark side by side. Iterate on their feedback, **changing only what they point at**. Get an explicit approval ("aprovado", "approved") before any code.

### 5. Choose the path

- **Code-first** (recommended when Figma is on Starter/View, or they code): tokens in a repo are the source of truth; Figma receives them later through a plugin or by import.
- **Figma-first** (paid plan with libraries and modes, team of designers): variables in Figma, exported to DTCG JSON.

Say which and why in one paragraph of their README.

### 6. Tokens from the starter

Copy [`templates/starter`](templates/starter) into their project and replace the placeholder values with the approved direction:

- `tokens/primitives.json` — raw palette, spacing (4 px base), radius, durations, easing, font families.
- `tokens/typography.json` — the type scale.
- `tokens/theme/light.json` and `tokens/theme/dark.json` — **aliases only** (`{color.neutral.0}`), same names in both.
- Set `"dsPrefix"` in `package.json` (e.g. `lotus`, `mx`) — it names the CSS classes.

Then `npm run build` (tokens → `dist/tokens.json`, `dist/tokens.css`) and `npm test` (contrast in both themes). Fix a failing pair by changing the **theme alias**, not by lowering the bar. If the brand color fails as text in one theme, use a lighter/darker step for text and keep the brand color for marks and fills — and write that rule down.

### 7. Grow it

In this order, each step previewed and approved before the next:

1. Base styles: body, type classes, the signature detail.
2. Components that the first page needs (usually Button, Link, TextField, Card), every state, using only theme variables. Props named like Figma variants.
3. Docs page: Primitives, Components, Layouts, Foundations, Theme, Typography.
4. Figma: variables (Root collection + Theme collection with Light/Dark modes, or two collections on Starter), text styles, components with the same names.
5. Versioning (Changesets) and publishing, only when they want packages.

## Rules

- The identity is theirs: every choice cites the brief. If they disagree, their call wins.
- Components never use primitives; themes are aliases; light and dark share names.
- WCAG AA is a failing test, not a guideline.
- Same name everywhere: `color/action/accent` ↔ `--color-action-accent` ↔ Figma variable.
- Change only what was asked in each iteration.

## Checklist

- [ ] Identity brief approved
- [ ] Direction chosen, name with meaning, layer names defined
- [ ] Visual proposal approved explicitly
- [ ] Starter tokens filled, `npm test` green in light and dark
- [ ] Signature detail defined and documented
- [ ] Path (code-first or Figma-first) explained in the README

## Example

IY Lotus — see the `lotus-design-system` skill and `github.com/Akiiiiyama/iylotus`.
