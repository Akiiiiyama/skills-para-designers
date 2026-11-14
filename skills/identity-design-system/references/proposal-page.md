# Visual proposal page

One self-contained HTML file, built **in the chosen direction** (its colors, type and signature detail), so the person judges the look, not a table. Keep it to one page that scrolls.

## Sections, in order

1. **Hero** — the system's name with the signature detail, the tagline (the values), and a single line on what it is for. Whole words only: never cut a word across lines in the first fold.
2. **Values → decisions** — each value with the visual rule it became.
3. **Palette** — neutrals and accent as swatches with name, hex and the contrast of text on it; mark which pairs pass AA.
4. **Typography** — the scale (display → caption) with real phrases from the person's work, not lorem ipsum.
5. **Spacing, radius, elevation, motion** — small visual rulers; one easing demo on hover.
6. **Components** — Button (variants × sizes × default/hover/focus/disabled), TextField (default/focus/error/disabled), Card. Static is fine; states side by side.
7. **Light and dark** — the same block in both themes, side by side.
8. **Layers** — the metaphor (e.g. Root / Stem / Petal / Bloom) with one example per layer.

## Rules

- Colors as CSS variables on `:root`, redefined for dark under `[data-theme="dark"]` and `prefers-color-scheme`; `body` gets an explicit background.
- Works at phone width (16 px gutters, no horizontal scroll).
- No dates, version numbers or "draft" labels in the hero unless asked.
- After feedback, change only what was pointed at, and say what changed.
- The page later becomes the docs page (Primitives, Components, Layouts, Foundations, Theme, Typography).
