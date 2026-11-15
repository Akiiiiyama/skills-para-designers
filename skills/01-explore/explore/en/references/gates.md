# Gates and exploration folder

## Exploration folder

```
explore/<slug>/
  README.md              # status board + decisions (orchestrator)
  prototype-plan.md      # 1 · explore-intake
  refs/                  # 2 · explore-refs (images, with source link)
  patterns.md            # 2 · explore-refs
  concepts.md            # 3 · explore-concepts
  prototype/index.html   # 4 · explore-lofi
  review.html            # 5 · explore-review
```

The PRD is not copied here. `prototype-plan.md` stores its path in the `prd` field.

## Shared frontmatter

Every Markdown artifact starts like this (keys stay in English in both languages):

```yaml
---
title: "Feature name"
stage: 1-intake        # 1-intake | 2-refs | 3-concepts | 4-lofi | 5-review
status: draft          # draft | final
skipped: false         # only stage 2 may be true
created: 2026-11-14
updated: 2026-11-14
---
```

The prototype and the review page are HTML: their status goes in a comment at the top of the file, in the same format:

```html
<!-- stage: 4-lofi · status: draft · updated: 2026-11-14 -->
```

## Gates

Each gate is a checklist. Every item must pass, and the person must say they approve, for the artifact to become `final`.

### Gate 1 · intake → `prototype-plan.md`

- [ ] The question the prototype must answer is written in one sentence.
- [ ] The kill criterion is written (the result that would make the person drop the idea).
- [ ] 1 to 3 journeys in scope, with IDs (`UJ-N`), and the requirements (`FR-N`) they use.
- [ ] What is out of the prototype's scope is listed.
- [ ] Form factor defined (mobile, web, desktop) and the design system pointed to (token path or `DESIGN.md`, or "none").
- [ ] No open question marked as blocking.
- [ ] Who approves the prototype, and how, is defined.

### Gate 2 · refs → `patterns.md` (optional)

- [ ] The references in `refs/` were chosen by the person, not just collected.
- [ ] Each reference has its source link.
- [ ] `patterns.md` describes patterns (what repeats and why), not screens.
- [ ] Each pattern points to the journey or requirement it helps solve.
- To skip: `skipped: true` and the reason in the README's Decisions section.

### Gate 3 · concepts → `concepts.md`

- [ ] 2 to 3 truly different concepts (approach, not color).
- [ ] Each concept says which `UJ`/`FR` it serves best, pros, cons and risks.
- [ ] The person chose which concept(s) to prototype.

### Gate 4 · lo-fi → `prototype/index.html`

- [ ] Every beat of the in-scope journeys has a screen or a state.
- [ ] Each screen is tagged with the IDs it serves (`UJ-2 · FR-5`).
- [ ] Uses only design system components in the wireframe theme; a new component is marked as a proposal.
- [ ] Realistic content, no lorem ipsum.
- [ ] Opens in the browser with no console errors.

### Gate 5 · review → `review.html` + Outcome section

- [ ] The prototyped concepts appear side by side, with the plan's question at the top.
- [ ] The decision is recorded: go, adjust or drop, with the reason.
- [ ] The decision was checked against the kill criterion from Gate 1.
- [ ] Questions still open are listed for the Discover stage.

## Status board

Template for the exploration's `README.md`:

```markdown
# Explore · <Feature name>

PRD: [`<path>`](<path>)

| # | Stage | Artifact | Status | Updated |
|---|---|---|---|---|
| 1 | Intake | [prototype-plan.md](prototype-plan.md) | in progress | 2026-11-14 |
| 2 | References | [patterns.md](patterns.md) | not started | |
| 3 | Concepts | [concepts.md](concepts.md) | not started | |
| 4 | Lo-fi prototype | [prototype/index.html](prototype/index.html) | not started | |
| 5 | Review | [review.html](review.html) | not started | |

**Next step:** <one sentence>

## Decisions

- 2026-11-14 · <decision> · <reason>
```
