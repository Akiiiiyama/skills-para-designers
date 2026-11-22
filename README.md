# Skills for designers

Claude Code skills for designers, organized by the moments of the design process: **Explore → Discover → Design → Prototype → Polish**. Claude Code can work with your team's real codebase (GitHub/GitLab) and Figma files at every step.

[Leia em português](#português)

| Stage | What it is for | Skills |
|---|---|---|
| [**1 · Explore**](skills/01-explore) | Rapid prototyping. Make it real fast. | [`brand-motion-intro`](skills/01-explore/brand-motion-intro/README.md) |
| [**2 · Discover**](skills/02-discover) | Explore the codebase and history. Understand the current state. | [`lotus-design-system`](skills/02-discover/lotus-design-system/en/README.md) |
| [**3 · Design**](skills/03-design) | Plan projects. Identify edge cases and scope. | [`identity-design-system`](skills/03-design/identity-design-system/en/README.md) |
| [**4 · Prototype**](skills/04-prototype) | Implement code and test. Test new features in your product. | `portfolio-device-motion` *(planned)* |
| [**5 · Polish**](skills/05-polish) | The last 2%. Design polish and quality. | `accessibility-review`, `token-check` *(planned)* |

Each stage folder has a README (Portuguese and English) describing its skills.

## How a skill is organized

```
skills/
  0N-<stage>/
    README.md         # the stage and its skills (pt + en)
    <skill-name>/
      SKILL.md        # entry point Claude reads (name, description)
      README.md       # index: Português | English
      pt/             # README.md (install and use), skill.md (full content), referencias/
      en/             # README.md, skill.md, references/  (same structure as pt/)
      scripts/        # optional shared helper scripts
      templates/      # optional shared starting files
```

Bilingual skills follow the same pattern as [pilulas-ia](https://github.com/Akiiiiyama/pilulas-ia): Claude follows `pt/` or `en/` by the language of the conversation. Start a new skill from [`templates/SKILL.template.md`](templates/SKILL.template.md) and place it in the stage where a designer would reach for it.

## Install

Copy a skill folder (the one with `SKILL.md`) into `~/.claude/skills/` (all projects) or `<project>/.claude/skills/` (one project) and restart Claude Code. Example:

```bash
git clone https://github.com/Akiiiiyama/skills-para-designers.git
cp -R skills-para-designers/skills/03-design/identity-design-system ~/.claude/skills/
```

Skills with scripts have their own setup steps in their README. The skills will also be packaged as a Claude Code plugin with the first release.

---

## Português

Skills do Claude Code para designers, organizadas pelos momentos do processo de design: **Explorar → Descobrir → Projetar → Prototipar → Refinar**. Em cada etapa, o Claude Code pode trabalhar com o código real do time (GitHub/GitLab) e com os arquivos do Figma.

| Etapa | Para quê | Skills |
|---|---|---|
| [**1 · Explorar**](skills/01-explore) | Prototipagem rápida. Tornar real rápido. | [`brand-motion-intro`](skills/01-explore/brand-motion-intro/README.pt.md) |
| [**2 · Descobrir**](skills/02-discover) | Explorar o código e o histórico. Entender o estado atual. | [`lotus-design-system`](skills/02-discover/lotus-design-system/pt/README.md) |
| [**3 · Projetar**](skills/03-design) | Planejar projetos. Identificar casos de borda e escopo. | [`identity-design-system`](skills/03-design/identity-design-system/pt/README.md) |
| [**4 · Prototipar**](skills/04-prototype) | Implementar código e testar. Testar features novas no produto. | `portfolio-device-motion` *(planejada)* |
| [**5 · Refinar**](skills/05-polish) | Os últimos 2%. Acabamento e qualidade de design. | `accessibility-review`, `token-check` *(planejadas)* |

Para instalar, copie a pasta da skill (a que tem o `SKILL.md`) para `~/.claude/skills/` e reinicie o Claude Code.

## License

[MIT](LICENSE)
