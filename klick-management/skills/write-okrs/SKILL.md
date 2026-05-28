---
name: write-okrs
description: Turn rough goals into well-formed OKRs / SMART objectives. Includes expected hit rate, 1-2 personal goals per individual, and the "how" alongside the "what." Use during quarterly or annual planning, or when an existing goal isn't actionable.
---

# Write OKRs

This skill turns a rough goal into a well-formed OKR set. The book treats OKRs as more than a format — they're a contract on ambition, hit-rate expectation, the work behind the outcome, and personal growth. This skill produces all of those, not just the format.

Part of `org-foundations-and-planning` (Chapter 2 of *Scaling People*).

## Mode

Use the `AskUserQuestion` tool to ask which mode to run in. Default to `draft` if the user skips or picks "Other" without specifying.

- **`teach`** — Socratic walk-through (10-20 min). Use when the user is new to this artifact or wants to internalize the framework. Walk through every heuristic in the Rubric as a question; build the artifact incrementally; explain the "why" alongside the "what."
- **`draft`** — Targeted intake → first draft → refinement (5-10 min). Use when the user knows roughly what they want. Ask the 3-5 questions listed under "Draft-mode intake" below; produce a complete first draft; offer one round of refinement against the Rubric.
- **`polish`** — Critique-and-polish (2-5 min). Use when the user pastes an existing draft. Critique against every Rubric heuristic; rewrite to address gaps; explain what changed.

**When asking the user any question during this skill** (mode selection, intake, refinement, clarification): prefer the `AskUserQuestion` tool for any question with 2-4 reasonably discrete options (the user can always pick "Other" to free-text). Use plain chat only for questions that genuinely need a sentence or paragraph of free-form response. Multi-select questions are fine when the user could legitimately choose more than one.

## Rubric

1. **Objectives describe an end state, not an activity.** An objective answers "Where do I want to go?" and should read as an outcome — the state of the world at the end of the period. If the objective starts with a verb like "launch," "build," or "refactor," you probably have an action. Reframe: translate "X so that Y" into "Y via X," then ask whether X belongs in the objective at all.

2. **Key results are concrete and binary, not open to interpretation.** A key result answers "How will I know I'm getting there?" Each one is measurable in a way that the whole team assesses the same way. If one person could call it done and another could reasonably disagree, the key result is not specific enough. Outcomes, not activities — 1-5 per objective, no more.

3. **Say what percentage of goals you expect people to hit up front.** Don't leave ambiguity about whether the goal is aspirational or committed. Aspirational goals (expect 70-80% attainment) challenge teams to think differently and generate fresh energy; committed goals (expect 95%+) are appropriate when another team is blocked, a customer was given a deadline, or there is an existential threat. Name which is which before the period starts.

4. **3-5 objectives maximum; if it doesn't fit on one page, cut.** People can hold about three to five things in working memory. More than one page of goals is not focused goal-setting — it is a project list. If your team can't memorize the goals, the goals are not guiding day-to-day decisions. When you wince looking at the list — "what about X?" — that's a sign you haven't focused enough.

5. **An individual's goals should include one or two personal goals.** Every individual's goal set should contain at least one development goal alongside the work output goals. The work of an individual is both company-focused (what they'll do to contribute) and individual-focused (how their work builds their career and capabilities). Omitting personal goals signals that development is an afterthought; including them is an act of commitment to the person, not just the quarter.

6. **The "how" is just as important as the "what."** Don't assess goals only on whether they were achieved. Pay attention to how the team approached the work. A Pyrrhic delivery — hitting the goal but breaking the team and the relationships — is not a success. The book's formulation: performance equals results multiplied by behaviors. A high result achieved by "fomenting unrest and backstabbing" should score near zero, not 95 percent.

7. **Avoid the four common pitfalls.** (1) Using an activity or action as an outcome. (2) Having a key result with no measurable definition of done. (3) Turning a roadmap directly into objectives and key results. (4) Writing more than 3-5 objectives or more than 1-5 key results per objective. Check each OKR against all four before publishing.

## Draft-mode intake

1. "What's the scope — team, function, or individual?"
2. "What's the period (quarter / year)?"
3. "What's the rough outcome you're aiming at?"
4. "What's the realistic hit-rate target (60% / 70% / 100%)?"
5. "For an individual: what's a personal-growth goal that's not tied to a team outcome?"

## Artifact

**Format:** Markdown — populated OKR template per references/templates/okr-template.md, with hit-rate expectation declared and any personal goals included.
**Default save path:** `./docs/management/okrs-YYYY-MM-DD.md` in the user's cwd. Ask before saving; ask before overwriting if file exists.
**Template:** Where the book provides a template, see `references/templates/okr-template.md`.

## Source

*Scaling People* — Claire Hughes Johnson, Stripe Press 2023 — Chapter 2, "The operating system > Annual and quarterly goals" (incl. "Good goals" sidebar; Exercises and templates > "Writing Good OKRs").

Encoded heuristic: OKRs separate two questions: "Where do I want to go?" (objective) and "How will I know I'm getting there?" (key results). Good objectives are outcome states, not actions; good key results are binary, measurable, and unambiguous. The book insists on declaring the expected hit rate up front — aspirational goals expect 70-80% and stretch thinking; committed goals expect 95%+ and must be sacrificed toward if they fall behind. No individual's goal set is complete without at least one personal development goal. And no OKR review is complete without assessing the "how" alongside the "what" — a result achieved at the cost of team trust or sustainable pace counts against you, not for you.

Where the book provides a template, see `references/templates/okr-template.md`.
