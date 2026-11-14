# Identity-first design system

Create your own design system starting from the identity **you** want: an interview about your values, personality and references, two or three directions, a name with meaning, a visual proposal page for approval, and then working tokens (light/dark CSS + contrast tests) from a starter kit.

[Leia em português](../pt/README.md)

## Install

```bash
git clone https://github.com/Akiiiiyama/skills-para-designers.git
cp -R skills-para-designers/skills/03-design/identity-design-system ~/.claude/skills/
```

Restart Claude Code.

## Use

Ask Claude: *"I want to create my own design system"* or *"help me turn my visual identity into tokens"*. Claude will:

1. Interview you in short rounds (purpose, values, sliders, references, constraints) and write an identity brief for your yes.
2. Propose 2–3 directions with palettes, type, shape, motion and a signature detail, with contrast ratios.
3. Suggest names and turn the metaphor into layer names (raw values → theme → components → pages).
4. Build a proposal page in your direction and iterate until you approve.
5. Fill [`templates/starter`](../templates/starter) with your tokens: `npm run build && npm test`.
6. Grow it into components, a docs page and Figma, one approved step at a time.

The identity is always yours: every choice cites something you said.

Real example: [IY Lotus](https://github.com/Akiiiiyama/iylotus) and the [`lotus-design-system`](../../../02-discover/lotus-design-system/en/skill.md) skill.
