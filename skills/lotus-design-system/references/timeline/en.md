# IY Lotus — timeline with artifacts

[Leia em português](pt.md)

Use this when retelling the story (case study, talk, post). Each step lists what was produced and what the owner decided.

| # | Step | Artifact | Decision |
|---|---|---|---|
| 1 | Brand reel | `brand-motion-intro` reel, 9:16 and 16:9 in 4K | Black + one red, light/bold whole words, red period as signature |
| 2 | Website idea | — | Build the portfolio in React; it also serves as study material |
| 3 | Naming | 10 name options | **IY Lotus 🌺 — Growth, beauty, discipline and wisdom** |
| 4 | Written proposal | tokens, inputs, buttons, cards, package names | Approved direction; npm scope `@iylotus/*` |
| 5 | Visual proposal | HTML page in the reel's style | Iterated: light/dark balance, whole words in the first fold, no dates |
| 6 | Docs page | `docs/index.html`, sections 1–6, floating header, no grid | "Design system aprovado" |
| 7 | Path choice | — | Path A, code-first (Figma Starter, View seat) |
| 8 | Tokens | `@iylotus/tokens`: DTCG JSON, build script, contrast tests | Root → Stem aliases; dark text accent = red/300 |
| 9 | Styles | `@iylotus/styles`: CSS variables, themes, type classes | `[data-theme]` + `prefers-color-scheme` |
| 10 | Components | `@iylotus/react`: 13 components, Storybook, SSR tests | Props = Figma variant names |
| 11 | Figma plugin | dev plugin, variables + styles + components | Starter fallback: dark in a second collection; verified in real Figma |
| 12 | Release prep | Changesets (fixed), CI, release workflow gated on `NPM_TOKEN` | 0.1.0 ready; publish waits for the npm org |
| 13 | Site | `apps/site` (Next.js) on Vercel, domain isabelayukari.com | Every change previewed locally and approved before merge |

## One-paragraph version

IY Lotus started from a motion reel that already had a look: black, one red, light and bold type. I named it after what I want my work to have — growth, beauty, discipline and wisdom — and turned the lotus into the architecture: Root (raw values), Stem (themes), Petal (components), Bloom (pages). I proposed it in writing and then as a page in the reel's own style, got it approved, and built it code-first because my Figma plan could not hold a shared library: DTCG tokens with a build script, CSS variables for light and dark, React components with Storybook, contrast as a failing test, and a Figma plugin that rebuilds the same variables and components from the code. Then I used it to build my site.
