# IY Lotus — how the design system was built

[Leia em português](pt.md)

*Growth, beauty, discipline and wisdom.*

IY Lotus is the design system behind isabelayukari.com. It was not drawn first and coded later: it started from a motion video, became a written and visual proposal, was approved, and was then built **code-first** — tokens in a repo are the source of truth, and Figma receives them through a plugin. This skill tells that story in order, with the decisions and the mistakes, so it can be retold or continued.

Repository: `github.com/Akiiiiyama/iylotus` (public, MIT). Site: `apps/site` in the same repo, deployed on Vercel.

Two modes:

- **Retell** (case study, talk, LinkedIn post, interview answer): follow [The process](#the-process) and the lessons; [`references/timeline/en.md`](references/timeline/en.md) has the step-by-step with artifacts.
- **Extend** (new token, color, component, page): follow [Extending IY Lotus](#extending-iy-lotus). Never edit `dist/`.

## The process

### 1. Start from something that already has identity

The system came from the `brand-motion-intro` reel (Design Engineer → Product Designer, black + one red, light and bold type on whole words). Its look was already approved by the owner, so the system **extracted** rules from it instead of inventing a style: near-black ink, paper and surface one step apart, one red accent on ~10% of the screen, DM Sans in light (300) and bold (700) on whole words, a red period as signature (`IY.`).

### 2. Name with meaning

Ten name options were proposed; the owner chose **IY Lotus 🌺 — Growth, beauty, discipline and wisdom**. The metaphor became the architecture, so the name is not decoration:

| Layer | Meaning | Contents |
|---|---|---|
| **Root** | primitives, raw values | `color/red/600 = #C8102E`, 4 px spacing |
| **Stem** | theme, meaning in light and dark | `color/action/accent` |
| **Petal** | components | `<Button variant="accent" />` |
| **Bloom** | layouts and pages | the site |

The four values became rules: **discipline** (4 px scale, every state of every component, same name in Figma, CSS and React), **wisdom** (WCAG AA as a failing test), **beauty** (light + bold, one accent), **growth** (versioned packages, changesets).

### 3. Propose before building — in writing, then visually

1. A written proposal: tokens, inputs, buttons, cards, naming, how it would ship (`@iylotus/tokens`, `@iylotus/styles`, `@iylotus/react`).
2. A **visual HTML proposal** in the style of the reel, so the owner judges the look, not a list. Iterated until approved: light/dark balance, first fold with whole words, no dates or version labels in the hero.
3. A separate **docs page** (`docs/index.html`) with sections Primitives, Components, Layouts, Foundations, Theme, Typography, and a floating header like the site.

Approval was explicit ("Design system aprovado") before any package existed.

### 4. Choose the path by the real constraints

Figma was on the **Starter plan with a View seat**: no shared libraries, one variable mode per collection. So **path A, code-first**: the repo is the source of truth; Figma gets variables, styles and components from a development plugin built from the same tokens. The alternative (draw in Figma, export) would have depended on paid features.

### 5. Tokens (Root + Stem)

- W3C **DTCG** JSON in `packages/tokens/src`: `primitives.json`, `typography.json`, `theme/light.json`, `theme/dark.json`.
- Theme tokens are **aliases** (`{color.neutral.0}`); components never use primitives.
- A zero-dependency `scripts/build.mjs` flattens, resolves references (with circular/missing checks), checks that light and dark have the **same token names**, and writes `dist/tokens.json`, `index.js`, `index.d.ts`.
- `test/contrast.test.mjs` (node:test) fails the build if any text pair drops below 4.5:1 or icon/focus below 3:1, in both themes.

Key decision: in dark mode the **text** accent is `red/300` (#E4637A) because `red/600` on near-black fails 4.5:1 for text. The brand mark (the period in `IY.` and in titles) is decorative, so the site keeps it `red/600` everywhere — a deliberate site rule, not a token change.

### 6. CSS (`@iylotus/styles`)

A second script turns tokens into CSS custom properties: primitives on `:root`, the light theme by default, dark via `prefers-color-scheme` **and** `[data-theme="dark"]` (so a block can force a theme), one class per type style (`.iy-type-h2`), plus base classes `.iy-lt`, `.iy-bd`, `.iy-dot`. Theme variables point to primitives (`var(--color-neutral-950)`) so the Stem layer stays readable in devtools.

### 7. Components (Petal)

`@iylotus/react`, React + TypeScript built with `tsc`, CSS per component bundled into `dist/styles.css`. v1: Button, TextField, TextArea, Select, Checkbox, Radio, Switch, Card, Tag, Badge, Avatar, Link, Divider. Storybook 8 with the a11y addon and a theme toolbar; SSR markup tests with `renderToStaticMarkup`. Props are the same words as Figma variants (`variant=accent, size=md`).

### 8. Figma, from the code

`packages/figma-plugin`: tokens are bundled at build time, no network. Commands create collections `IY Lotus · Root` and `IY Lotus · Stem` (Light/Dark), text and effect styles, a Root page with bound swatches and component sets for every v1 component. On Starter (one mode), dark goes to a second collection and the plugin says so. Tested in node with a simulated Figma API before the owner ran it in real Figma.

### 9. Ship and apply (Bloom)

npm workspaces monorepo, **Changesets** with fixed versions, GitHub Actions CI on PRs and a release workflow that publishes only when `NPM_TOKEN` exists. Then the site (`apps/site`, Next.js) used the system for real: hero, cards, an IY Lotus notebook mockup showing the dark docs, opening motion — and every visual change went through a local preview approved by the owner before merge.

## Lessons (keep these)

- **Change only what was asked.** Reworking approved parts "while you are there" cost a revert.
- **Show, then build.** A visual proposal in the brand's own style got approval faster than any token table.
- **Constraints choose the architecture.** The Figma plan decided code-first; say why in the README.
- **Make the values executable.** "Wisdom = accessibility" only became real when contrast was a failing test.
- **Separate text accent from brand mark.** Accessible text color and brand color can differ per theme; decide where each applies.
- **Same name everywhere.** `color/action/accent` ↔ `--color-action-accent` ↔ `themes.light.color.action.accent` ↔ Figma variable.
- **Preview, approve, then publish.** Production deploys only after the owner says so.

## Extending IY Lotus

1. Edit only `packages/tokens/src/*.json` (or the component in `packages/react/src/<Name>`).
2. New color: add the primitive in Root; if components need it, add a **Stem** alias in **both** `light.json` and `dark.json` (the build fails if they differ).
3. If it is a text/icon/focus color, add the pair to `PAIRS` in `test/contrast.test.mjs`.
4. `npm run build && npm test` at the repo root.
5. New component: CSS uses only theme variables; add a story with every state; add an SSR test; add it to the Figma plugin with the same variant names.
6. `npm run changeset` (patch / minor / major), open a PR, preview, wait for approval.

## Checklist

- [ ] No primitive used directly in a component
- [ ] Light and dark have the same tokens
- [ ] Contrast tests pass in both themes
- [ ] Same name in JSON, CSS, React props and Figma
- [ ] Every interactive state exists (default, hover, focus, disabled, error where relevant)
- [ ] Changeset added; nothing in `dist/` edited by hand
