# Design system starter

Tokens in the W3C DTCG format, built to CSS custom properties and JavaScript, with WCAG contrast tests. No dependencies (Node 20+).

```bash
npm run build   # tokens/ → dist/tokens.json, dist/index.js, dist/tokens.css
npm test        # build + contrast checks in light and dark
```

1. Rename the package and set `dsPrefix` in `package.json` (it names the type classes: `.ds-type-h1`).
2. Replace the placeholder values in `tokens/primitives.json` and `tokens/typography.json` with your approved direction.
3. Point the theme aliases in `tokens/theme/light.json` and `dark.json` at your primitives. Keep the same names in both.
4. If a contrast test fails, change the alias, not the minimum.

Use it: `<link rel="stylesheet" href="dist/tokens.css">` and `<html data-theme="dark">` to force a theme (without it, the page follows the system).
