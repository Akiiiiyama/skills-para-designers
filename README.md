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
| [`identity-design-system`](skills/identity-design-system/SKILL.md) | Creates your own design system from the identity you want: interview, directions, a name with meaning, a visual proposal for approval, and a starter with DTCG tokens, light/dark CSS and contrast tests. | Draft |
| [`lotus-design-system`](skills/lotus-design-system/SKILL.md) | The real process behind IY Lotus, from a brand reel to tokens, React, a Figma plugin and a live site — to retell it or extend it. | Draft |

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

Bilingual skills follow the same pattern as [pilulas-ia](https://github.com/Akiiiiyama/pilulas-ia): `SKILL.md` is a short entry point and the full content lives in a `pt/` folder and an `en/` folder with the same structure (`README.md`, `skill.md`, references). Shared code, like starters, stays at the skill root. Claude follows the file in the language the person is using.

## Install

Copy a skill folder into `~/.claude/skills/` (all projects) or `<project>/.claude/skills/` (one project) and restart Claude Code. Skills with scripts have their own setup steps:

- `brand-motion-intro`: [how to install and use](skills/brand-motion-intro/README.md) · [como instalar e usar](skills/brand-motion-intro/README.pt.md)
- `identity-design-system`: [how to install and use](skills/identity-design-system/en/README.md) · [como instalar e usar](skills/identity-design-system/pt/README.md)
- `lotus-design-system`: [how to install and use](skills/lotus-design-system/en/README.md) · [como instalar e usar](skills/lotus-design-system/pt/README.md)

The skills will also be packaged as a Claude Code plugin with the first release.

## License

[MIT](LICENSE)
