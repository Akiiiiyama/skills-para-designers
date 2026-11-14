# Design system starter (English)

[Português abaixo](#starter-de-design-system-português)

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

---

# Starter de design system (português)

Tokens no formato DTCG do W3C, transformados em variáveis CSS e JavaScript, com testes de contraste WCAG. Sem dependências (Node 20+).

```bash
npm run build   # tokens/ → dist/tokens.json, dist/index.js, dist/tokens.css
npm test        # build + contraste no light e no dark
```

1. Renomeie o pacote e defina `dsPrefix` no `package.json` (ele dá nome às classes de tipografia: `.ds-type-h1`).
2. Troque os valores de exemplo em `tokens/primitives.json` e `tokens/typography.json` pela sua direção aprovada.
3. Aponte os apelidos de tema em `tokens/theme/light.json` e `dark.json` para os seus primitives, com os mesmos nomes nos dois.
4. Se um teste de contraste falhar, mude o apelido, não o mínimo.

Para usar: `<link rel="stylesheet" href="dist/tokens.css">` e `<html data-theme="dark">` para forçar um tema (sem isso, a página segue o sistema).
