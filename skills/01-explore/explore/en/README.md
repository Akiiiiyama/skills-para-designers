# Explore (orchestrator)

Runs a feature's Explore stage, from the PRD to an approved low-fidelity prototype. The stage is done by several small skills, and this is the one that knows the order: it sets up the exploration folder, checks each stage's gate and calls the next one.

[Leia em português](../pt/README.md)

## The stages

1. **`explore-intake`**: reads the PRD, flags the gaps and writes the prototype plan.
2. **`explore-refs`** *(planned)*: visual references and the patterns they show. Optional.
3. **`explore-concepts`** *(planned)*: 2 or 3 different concepts, tied to the PRD's journeys.
4. **`explore-lofi`** *(planned)*: low-fidelity HTML prototype with the design system in a wireframe theme.
5. **`explore-review`** *(planned)*: concept comparison and the recorded decision.

While a skill is planned, the orchestrator offers to do the stage by hand, with the same artifact and the same gate.

## Install

```bash
git clone https://github.com/Akiiiiyama/skills-para-designers.git
cp -R skills-para-designers/skills/01-explore/explore ~/.claude/skills/
cp -R skills-para-designers/skills/01-explore/explore-intake ~/.claude/skills/
```

Restart Claude Code.

## Use

Ask Claude: *"let's explore the voting feature, the PRD is at docs/prd-voting.md"*. Then, at any time: *"where are we in the exploration?"* or *"what's next?"*.

Everything lives in `explore/<feature>/`, with a `README.md` showing each stage's status and the decisions made along the way. The gates are in [`references/gates.md`](references/gates.md).
