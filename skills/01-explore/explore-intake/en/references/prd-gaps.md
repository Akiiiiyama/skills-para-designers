# PRD gaps that affect the prototype

Walk the list with the PRD open. For each item that fails, note the ID involved and classify it: **blocking**, **becomes an assumption** or **for product**. The "Usually" column suggests the most common classification; context can change it.

## Journeys

| Check | What to look for | Usually |
|---|---|---|
| Journey without a protagonist | "The user" instead of a person with a name and context ("Ana, who runs the club and only has her phone on the bus"). Without context, there is no way to decide form factor or density. | becomes an assumption |
| Journey without a climax | It is not clear at which moment the value lands for the person. That moment is exactly what the prototype must show. | blocking |
| Beat without a requirement | A journey beat needs the product, but no `FR` covers it. | becomes an assumption |
| Requirement without a journey | An `FR` no journey uses. It stays out of the prototype, unless the person says otherwise. | for product |
| Undefined entry state | Unknown whether the person is logged in, it is their first time, or they already have data. It changes the first screen. | becomes an assumption |

## States and content

| Check | What to look for | Usually |
|---|---|---|
| Empty state | What shows when there is nothing yet (first time, empty list)? | becomes an assumption |
| Error and failure | Does the PRD describe at least one failure of the main journey? | becomes an assumption |
| Content shape | How many items, text length, which data shows? Without it, the prototype falls back to lorem ipsum. | becomes an assumption |
| Ambiguous terms | A word used with two meanings, or missing from the glossary ("round", "session", "group"). | blocking if it is at the center of the journey |

## Scope and decision

| Check | What to look for | Usually |
|---|---|---|
| Non-goals | Is there a list of what the feature is not? Without it, the prototype tends to grow. | for product |
| Form factor | Mobile, web, desktop or several? | blocking |
| Success metric | Is there an `SM` or another way to know it worked? It helps write the kill criterion. | for product |
| Open questions | Does any `OQ` change what the prototype shows? That one becomes blocking. | depends |
| Decisions already made | Something the PRD already decided that the prototype should not reopen. Note it so no concept is spent on it. | (not a gap) |

## Only the person can answer

These are never in the PRD. Always ask:

- the question the prototype must answer;
- the kill criterion;
- who approves, and how;
- the timebox.
