---
name: write-long-term-goals
description: Articulate 3-5 year long-term goals or vision for a team or org. Use when the mission exists but the team can't see the medium-term picture, or when annual planning keeps surfacing "but where are we headed?" questions.
---

# Write Long-Term Goals

This skill produces a small set of 3-5 year goals or a vision statement that sits between the mission (timeless) and annual OKRs (12 months). Use it when the team is shipping work but can't articulate what they're building toward.

Part of `org-foundations-and-planning` (Chapter 2 of *Scaling People*).

## Mode

Use the `AskUserQuestion` tool to ask which mode to run in. Default to `draft` if the user skips or picks "Other" without specifying.

- **`teach`** — Socratic walk-through (10-20 min). Use when the user is new to this artifact or wants to internalize the framework. Walk through every heuristic in the Rubric as a question; build the artifact incrementally; explain the "why" alongside the "what."
- **`draft`** — Targeted intake → first draft → refinement (5-10 min). Use when the user knows roughly what they want. Ask the 3-5 questions listed under "Draft-mode intake" below; produce a complete first draft; offer one round of refinement against the Rubric.
- **`polish`** — Critique-and-polish (2-5 min). Use when the user pastes an existing draft. Critique against every Rubric heuristic; rewrite to address gaps; explain what changed.

**When asking the user any question during this skill** (mode selection, intake, refinement, clarification): prefer the `AskUserQuestion` tool for any question with 2-4 reasonably discrete options (the user can always pick "Other" to free-text). Use plain chat only for questions that genuinely need a sentence or paragraph of free-form response. Multi-select questions are fine when the user could legitimately choose more than one.

## Rubric

1. **Small set, not a laundry list.** Long-term goals should be few enough to remember without notes — the book's example is a simple two-page document with a handful of items. More than five or six starts to dilute the signal. Force prioritization; resist the urge to name everything the team cares about.

2. **Durable across years, not tied to a single year's plan.** The test of a long-term goal is whether it survives the next annual planning cycle mostly unchanged. Stripe's goals written in 2014 were still recognizably the same eight years later. If a goal would look obviously wrong 18 months from now, it is not a long-term goal — it is an annual objective in disguise.

3. **Provides context for shorter-term goals, not a substitute for them.** Long-term goals exist to give annual and quarterly goals a direction to ladder up to. Without them, teams can hit every quarterly target and still drift. With them, goal-setters can ask "does this OKR move us toward one of our long-term aims?" and get a real answer.

4. **Ambitious without metric specificity.** Long-term goals state an aspiration ("accelerate globalization," "advance the state of the art in developer infrastructure") rather than a measurable target. Numeric precision belongs in annual goals; long-term goals are directional. Adding a hard number here creates false precision and premature accountability for something inherently uncertain.

5. **Bolsters and reinforces the mission.** When done well, the set of long-term goals reads as a decomposition of what the mission would look like if it were making progress. Employees should be able to look at the long-term goals and understand more concretely why the company exists and what "winning" roughly looks like.

## Draft-mode intake

1. "What's the team's mission today?"
2. "Three years out, what does success look like in plain language?"
3. "What would be true that isn't true today?"
4. "What's a current bet that has to pay off for this to happen?"

## Artifact

**Format:** Markdown — a vision/long-term statement plus 3-5 supporting long-term goals, each with one-sentence success condition.
**Default save path:** `./docs/management/long-term-goals-YYYY-MM-DD.md` in the user's cwd. Ask before saving; ask before overwriting if file exists.
**Template:** Inline — no shared template.

## Source

*Scaling People* — Claire Hughes Johnson, Stripe Press 2023 — Chapter 2, "Founding documents > Long-term goals."

Encoded heuristic: Long-term goals are the medium layer between the timeless mission and the annual plan — a small set of multi-year ambitions that give employees context for why the shorter-term work matters. They should be few, durable (Stripe's held stable for eight years), and directional rather than numeric. Their job is to ensure that every annual goal can answer the question "which long-term aspiration does this serve?" — and to provide a stable reference point when external forces push the company off course.
