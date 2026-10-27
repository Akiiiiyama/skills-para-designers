# Skills for designers

Claude Code skills that help designers ship better UI with AI: accessibility review, design token checks and motion for portfolio case studies.

> Work in progress. The first skills land in the coming weeks.

## Planned skills

| Skill | What it does | Status |
|---|---|---|
| `accessibility-review` | Reviews a page or component against a practical WCAG checklist (semantics, focus, contrast, labels) and suggests fixes. | Planned |
| `token-check` | Flags hard-coded colors, spacing and radii that should be design tokens. | Planned |
| `portfolio-device-motion` | Turns app screenshots or screen recordings into motion inside an iPhone frame for a portfolio section. | Planned |
| [`brand-motion-intro`](skills/brand-motion-intro/SKILL.md) | Plans and renders a 10–20 s personal-brand motion video from a one-line message, the design system and a licensed track, with every transition on the beat. Includes render, beat analysis, audio splice and flicker-scan scripts. | Draft |

## How a skill is organized

```
skills/
  <skill-name>/
    SKILL.md        # instructions Claude reads (name, description, steps)
    examples/       # before/after samples
    scripts/        # optional helper scripts the skill runs
    templates/      # optional starting files
```

Start from [`templates/SKILL.template.md`](templates/SKILL.template.md).

## Install (coming soon)

The skills will be packaged as a Claude Code plugin. Installation steps will be added with the first release.

## License

[MIT](LICENSE)
