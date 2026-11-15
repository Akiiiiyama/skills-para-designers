# Explore intake

First step of the Explore stage. Reads the feature's PRD with a designer's eye, flags what is missing to prototype, asks only what the PRD does not answer and writes `prototype-plan.md`: the question the prototype answers, the kill criterion, the journeys in scope, the design system and who approves.

[Leia em português](../pt/README.md)

It works with PRDs in the [BMAD Method](https://github.com/bmad-code-org/BMAD-METHOD) `prd` or `prd-light` format, using their IDs (`UJ-N`, `FR-N`, `OQ-N`), and with free-form Markdown PRDs.

## Install

```bash
git clone https://github.com/Akiiiiyama/skills-para-designers.git
cp -R skills-para-designers/skills/01-explore/explore-intake ~/.claude/skills/
```

Restart Claude Code. For the full flow, with status and gates between stages, also install [`explore`](../../explore/en/README.md).

## Use

Ask Claude: *"read the PRD at docs/prd-voting.md and plan the prototype"* or *"what's missing in this PRD before I prototype?"*. Claude will:

1. Read the whole PRD and recognize its format.
2. Find the gaps that affect the prototype ([list](references/prd-gaps.md)) and separate what blocks, what becomes an assumption and what goes to the PM.
3. Ask in short rounds: the question and kill criterion, the scope, the design system and approval.
4. Write the plan from the [template](references/prototype-plan.md).
5. Show the gate checklist and mark the plan `final` only with your yes.

To test: [`examples/prd-clube-do-livro.md`](../examples/prd-clube-do-livro.md) (in Portuguese).

The plan template is adapted from the BMAD Method `prototype-plan` and `prd` templates (MIT License, © 2025 BMad Code, LLC).
