# Explore (orchestrator)

[Leia em português](../pt/skill.md)

The Explore stage turns a PRD into a low-fidelity prototype that someone approves, adjusts or drops. It is done by several small skills, each with a single job. This skill does none of those jobs: it **sets up the folder, knows the order, checks the gates and calls the next skill**.

A gate is the condition to move on. Each stage writes an artifact with `status: draft` or `status: final` in its frontmatter and a definition-of-done checklist. The next stage only starts when the previous artifact is `final` and its checklist passes. The person always marks `final`, never Claude alone.

## When to use

- A feature has a PRD (or a PRD draft) and the person wants to get to a visible idea to approve, fast.
- The person opens an exploration folder and asks where things stand or what comes next.
- Not for building the real feature (that is the Prototype stage) or refining an approved design (Polish).

## The stages

| # | Skill | Produces | Required? |
|---|---|---|---|
| 1 | `explore-intake` | `prototype-plan.md` | Yes |
| 2 | `explore-refs` | `refs/` + `patterns.md` | No: can be skipped, with the reason recorded |
| 3 | `explore-concepts` | `concepts.md` | Yes |
| 4 | `explore-lofi` | `prototype/index.html` | Yes |
| 5 | `explore-review` | `review.html` + Outcome section in the plan | Yes |

The gate for each stage is in [`references/gates.md`](references/gates.md). Read that file every time you check a gate.

## Steps

### 1. Find or create the exploration

- If the person is in an `explore/<slug>/` folder, or names one, use it.
- If not, look for `explore/*/README.md` in the project. If an exploration has open stages, ask whether to continue it.
- If it is new: ask for the feature's short name (it becomes the kebab-case `<slug>`) and where the PRD is. Create `explore/<slug>/` at the project root, unless the person points elsewhere, and write the exploration's `README.md` with the status board (template in [`references/gates.md`](references/gates.md#status-board)).

The PRD stays where it is. The exploration only stores its path.

### 2. Read the state

For each stage, read the artifact's frontmatter (`status`, `updated`) and classify it:

- **not started**: the file does not exist;
- **in progress**: it exists with `status: draft`;
- **done**: `status: final` and the gate checklist passes;
- **skipped**: stage 2 only, with `skipped: true` and a reason in the README.

If an artifact says `final` but its checklist does not pass (someone edited it by hand, for example), treat it as **in progress** and say which item failed.

Update the status board in the exploration's `README.md` with what you found.

### 3. Say where it stands and what comes next

Answer in a few lines: the current stage, what is missing for its gate to pass, and which skill comes after. Example:

> Stage 1 (intake) in progress. The kill criterion and who approves are missing. After that comes stage 2 (visual references), which you can skip if you already have references.

### 4. Call the next skill

- If the current stage's gate passed, call the next stage's skill and pass it the exploration path.
- If that skill is not installed, say so and offer to do the stage by hand, following what the gate asks. The artifact must keep the same name and frontmatter so the gate keeps working.
- If the person asks to skip a required stage, explain what is lost (for example: without `concepts.md`, the prototype has no alternative to compare against) and only go on if they confirm. Record the decision in the exploration's README.

### 5. Going back a stage

If a later stage shows an earlier one was wrong (the prototype reveals the chosen journey does not answer the question, for example), set the earlier artifact back to `status: draft`, record the reason in the README and redo from there. Artifacts after it also go back to `draft`.

## Rules

- One stage at a time. Never run two stage skills in the same step.
- Only the person marks `final`. Claude shows the checklist and asks.
- The README status board is a summary; the truth is each artifact's frontmatter.
- Every decision to skip, go back or force a stage goes into the README's Decisions section, with date and reason.
- File names and frontmatter keys are the same in Portuguese and English, so explorations in either language work with the same skills.

## Checklist

- [ ] The exploration has a folder, a `README.md` and the PRD path
- [ ] The status board matches the artifacts' frontmatter
- [ ] The person knows the current stage, what is missing and what comes next
- [ ] No stage started with the previous gate open (or the exception is recorded)
