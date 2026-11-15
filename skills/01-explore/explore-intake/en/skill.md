# Explore intake

[Leia em português](../pt/skill.md)

Before drawing anything, a prototype needs a plan: **which question it answers, what would make the idea be dropped, which part of the PRD is in, and who approves**. This skill reads the PRD with a designer's eye, finds what is missing to prototype, asks the person only what the PRD does not answer, and writes `prototype-plan.md`.

The intake does not draw screens or propose solutions. It prepares the ground for the next stages (references, concepts, lo-fi prototype).

## When to use

- There is a PRD (or a draft) and the person wants to prototype an idea for approval.
- The person wants to know what is missing in the PRD before starting.
- The `explore` orchestrator called stage 1.
- Not for writing the PRD from scratch (that is product work; the BMAD Method `prd` template is good for it) or reviewing the PRD for engineering.

## Steps

### 1. Find the exploration and the PRD

- If the orchestrator passed an `explore/<slug>/` folder, use it. If not, create the folder and the `README.md` with the status board, as described in the `explore` skill's `gates.md` (or just the folder and the plan, if the orchestrator is not installed).
- Ask for the PRD path, or look for `*prd*.md` in the project and confirm with the person which one it is.
- If a `prototype-plan.md` already exists in the folder, read it and continue where it stopped instead of starting over.

### 2. Read the whole PRD and recognize its format

Read the PRD from start to finish before asking anything.

- **BMAD Method PRD**: the frontmatter has `template: prd` or `template: prd-light`. Use its IDs as they are: journeys `UJ-N`, requirements `FR-N`, rules `RULE-N`, metrics `SM-N`, open questions `OQ-N`.
- **Free-form PRD**: find the equivalent of each section (vision, users and journeys, requirements, non-goals, scope, metrics, open questions). If there are no IDs, number journeys and requirements **in the plan**, marked as provisional, and offer to add them to the PRD. The PRD belongs to whoever wrote it: do not edit it without asking.

Make a summary for your own use: the vision in one sentence, the journeys (protagonist + climax), requirements grouped by journey, non-goals and open questions. Do not copy the PRD into the plan; the plan points to the IDs.

### 3. Find the gaps

Walk through [`references/prd-gaps.md`](references/prd-gaps.md). Only what affects the **prototype** counts as a gap; engineering, data and operations details stay out.

Classify each gap:

- **blocking**: without the answer, there is no way to know what to prototype. It must be resolved before the gate.
- **becomes an assumption**: a reasonable hypothesis lets you go on. It goes into the plan tagged `[ASSUMPTION]`, and the prototype is there to test it.
- **for product**: it does not block the prototype, but the PM needs to know. It goes into the plan's "Questions for product" section.

### 4. Ask only what the PRD does not answer

Use short rounds, at most 4 questions at a time. When the PRD already suggests the answer, **propose it and ask for confirmation** instead of asking from scratch ("From the PRD, the main journey is UJ-1. Just that one?").

Round order:

1. **Question and kill criterion.** What must the prototype answer, in one sentence? What result would make you drop the idea? The criterion must be observable and written before building, because a bar set after the results always flatters them. Examples: "if 3 of 5 people cannot find where to vote without help", "if the main flow needs more than 4 screens".
2. **Scope.** Which journeys are in (1 to 3)? Which form factor (mobile, web, desktop)? If the person wants the whole PRD, say that a smaller prototype answers the question faster, suggest what can wait and leave the decision to them.
3. **Design system and approval.** Which design system? Look in the project before asking (`DESIGN.md`, `tokens/*.json`, `dist/tokens.css`, a Storybook, a package with `dsPrefix`) and confirm with the person; "none" is also an answer, and then the prototype uses a neutral wireframe. Who approves, and how (meeting, link with comments, user test)? Is there a timebox?
4. **Blocking gaps.** One at a time, with your suggested answer.

When the person says "go ahead", stop asking: tag what is left as `[ASSUMPTION]` and finish the plan.

### 5. Write the plan

Copy [`references/prototype-plan.md`](references/prototype-plan.md) to `explore/<slug>/prototype-plan.md` and fill it in. The plan fits on one page, two at most. The sections for later stages (References, Concepts, Outcome) keep the `(stage N)` marker; the other skills fill them in.

### 6. Check the gate and ask for approval

Show the Gate 1 checklist with ✓ or ✗ on each item, the assumptions and the questions for product. If everything passes, ask whether you can mark it `final`. Only with the person's yes:

- change the frontmatter to `status: final` and update `updated`;
- update the status board in the exploration's `README.md`;
- say the next step: stage 2 (visual references, optional) or stage 3 (concepts).

## Rules

- Do not invent requirements, journeys or metrics. Anything not in the PRD and not said by the person is an `[ASSUMPTION]` or a question.
- The intake describes what the prototype must show, never what the screens look like.
- One prototype, one question. If two big questions come up, suggest two explorations.
- The PRD is not edited without an explicit request.
- Use the PRD's glossary terms exactly as written.

## Checklist (Gate 1)

- [ ] The prototype's question is written in one sentence
- [ ] The kill criterion is written
- [ ] 1 to 3 journeys in scope, with IDs, and the requirements they use
- [ ] What is out of the prototype is listed
- [ ] Form factor defined and design system pointed to (or "none")
- [ ] No blocking gap left open
- [ ] Who approves, and how, is defined
- [ ] The person approved and the plan is `status: final`

## Example

[`../examples/prd-clube-do-livro.md`](../examples/prd-clube-do-livro.md) is a PRD in the BMAD prd-light format (in Portuguese), with gaps on purpose. To test: *"read the PRD at examples/prd-clube-do-livro.md and plan the prototype"*.
