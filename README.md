# Skills for designers

Claude Code skills that help designers ship better UI with AI: accessibility review, design token checks and motion for portfolio case studies.

> Work in progress. The first skills land in the coming weeks.

## Planned skills

| Skill | What it does | Status |
|---|---|---|
| `accessibility-review` | Reviews a page or component against a practical WCAG checklist (semantics, focus, contrast, labels) and suggests fixes. | Planned |
| `token-check` | Flags hard-coded colors, spacing and radii that should be design tokens. | Planned |
| `portfolio-device-motion` | Turns app screenshots or screen recordings into motion inside an iPhone frame for a portfolio section. | Planned |

## How a skill is organized

```
skills/
  <skill-name>/
    SKILL.md        # instructions Claude reads (name, description, steps)
    examples/       # before/after samples
```

Start from [`templates/SKILL.template.md`](templates/SKILL.template.md).

## Install (coming soon)

The skills will be packaged as a Claude Code plugin. Installation steps will be added with the first release.

## License

[MIT](LICENSE)
