---
name: define-metrics
description: Build the metrics framework — long-term (mission/vision), short-term (operating/input), and "other" metrics for a team or function. Produces a metrics write-up doc. Use when launching a team, setting up new measurement, or when current metrics don't drive decisions.
---

# Define Metrics

This skill produces a metrics write-up — the three-layer structure of long-term outcome metrics (mission/vision), short-term operating or input metrics, and "other" metrics that don't fit either category. The doc explains what each metric is for and how decisions will use it.

Part of `org-foundations-and-planning` (Chapter 2 of *Scaling People*).

## Mode

Use the `AskUserQuestion` tool to ask which mode to run in. Default to `draft` if the user skips or picks "Other" without specifying.

- **`teach`** — Socratic walk-through (10-20 min). Use when the user is new to this artifact or wants to internalize the framework. Walk through every heuristic in the Rubric as a question; build the artifact incrementally; explain the "why" alongside the "what."
- **`draft`** — Targeted intake → first draft → refinement (5-10 min). Use when the user knows roughly what they want. Ask the 3-5 questions listed under "Draft-mode intake" below; produce a complete first draft; offer one round of refinement against the Rubric.
- **`polish`** — Critique-and-polish (2-5 min). Use when the user pastes an existing draft. Critique against every Rubric heuristic; rewrite to address gaps; explain what changed.

**When asking the user any question during this skill** (mode selection, intake, refinement, clarification): prefer the `AskUserQuestion` tool for any question with 2-4 reasonably discrete options (the user can always pick "Other" to free-text). Use plain chat only for questions that genuinely need a sentence or paragraph of free-form response. Multi-select questions are fine when the user could legitimately choose more than one.

## Rubric

1. **Objectives before metrics.** Objectives are broad statements of prioritization, strategy, and intent — they answer "Where do I want to go?" Metrics answer "How will I know I'm getting there?" Never define a metric before you've stated the objective it serves. One objective can have one or many metrics, but every metric should trace back to an objective.

2. **Long-term metrics move slowly and that's the point.** Long-term metrics define success against the team's mission and multi-year vision. They are lagging indicators — they won't tell you whether you're on track week-to-week. Aim for three to five charter metrics; these should stay stable for two to five years. Set milestones for them in annual plans even though the metrics themselves move slowly.

3. **Short-term metrics are leading or real-time signals.** Operating or input metrics measure activities or intermediate outcomes. They tell you whether you're on track before the long-term numbers move. Link them directly to team goals. Like long-term metrics, aim for three to five — enough to signal trajectory, not so many that every week is a data debate.

4. **Convert binary metrics to continuous ones.** "Ship product X" is a binary metric. "Ship product X to 50 new users" is a continuous metric. Continuous metrics are more useful because they give you a directional signal before the finish line. When you catch yourself with a ship-it/miss-it metric, ask what ongoing quantity it could become.

5. **Shared definitions precede shared accountability.** Before any metric goes live, agree on what it actually measures. What is a customer — one-time buyer or active user? When does a user churn? Getting these definitions agreed across teams is harder than it sounds, but a metric that means different things in different rooms is useless as an accountability tool.

6. **Dashboards without review cadence are decoration.** Once you've set metrics, build a dashboard and then commit to using it. Review metrics weekly or biweekly — as a team, not just as a manager. Reviewing metrics together signals that everyone has a stake in them. Only through regular review do you learn when a metric is no longer measuring what you intended.

7. **Metrics ladder up and down.** Just as team missions should connect to division missions, team metrics should connect to division metrics. If your team's operating metric doesn't relate to any higher-level charter metric, either your metric is off or you've found a gap in how the org measures success.

## Draft-mode intake

1. "What team/function?"
2. "What's the long-term outcome you're trying to move (tied to mission)?"
3. "What 2-4 operating or input metrics would move that outcome?"
4. "What's measurable today vs needs instrumentation?"

## Artifact

**Format:** Markdown — metrics write-up per references/templates/metrics-writeup.md.
**Default save path:** `./docs/management/metrics-YYYY-MM-DD.md` in the user's cwd. Ask before saving; ask before overwriting if file exists.
**Template:** Where the book provides a template, see `references/templates/metrics-writeup.md`.

## Source

*Scaling People* — Claire Hughes Johnson, Stripe Press 2023 — Chapter 2, "The operating system > Metrics that matter" (incl. "Metrics write-up" sidebar).

Encoded heuristic: The book's metrics framework is three-layered: objectives (where to go), long-term metrics (mission and vision — lagging, stable for years, set milestones annually), and short-term operating or input metrics (leading indicators, linked to near-term goals). A fourth category, "other metrics," captures continuous measures of results that don't yet fit the first two layers. A metric is useless unless it's reviewed regularly; only through that review loop do you learn whether a metric actually measures what you meant it to. Shared definitions of core terms — what is a customer, what counts as churn — are a prerequisite for shared accountability across teams.

Where the book provides a template, see `references/templates/metrics-writeup.md`.
