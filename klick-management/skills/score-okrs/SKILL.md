---
name: score-okrs
description: Score OKRs mid-quarter or at quarter end; handle priority changes and information updates that hit mid-period. Use at the scoring checkpoint or when something material has changed since OKRs were set.
---

# Score OKRs

This skill produces a scored OKR review — including how to handle the case where the goal has changed since it was set, where information has invalidated an assumption, or where progress can't be cleanly summarized. Use it as a checkpoint, not a verdict.

Part of `org-foundations-and-planning` (Chapter 2 of *Scaling People*).

## Mode

Ask the user which mode to run in. Default to `draft` if they don't specify.

- **`teach`** — Socratic walk-through (10-20 min). Use when the user is new to this artifact or wants to internalize the framework. Walk through every heuristic in the Rubric as a question; build the artifact incrementally; explain the "why" alongside the "what."
- **`draft`** — Targeted intake → first draft → refinement (5-10 min). Use when the user knows roughly what they want. Ask the 3-5 questions listed under "Draft-mode intake" below; produce a complete first draft; offer one round of refinement against the Rubric.
- **`polish`** — Critique-and-polish (2-5 min). Use when the user pastes an existing draft. Critique against every Rubric heuristic; rewrite to address gaps; explain what changed.

## Rubric

1. **Use a lightweight green / yellow / red rubric — don't over-engineer the scoring.** The mid-quarter and end-quarter reviews should use simple color-coded scoring (green = success, yellow = mixed, red = failure) accompanied by on track / at risk / off track assessments. If the scoring requires enormous effort or feels like it needs to happen more often, the team hasn't internalized the goals and isn't using them to guide day-to-day work.

2. **The mid-quarter review is a refocus checkpoint, not a verdict.** Its purpose is to surface items that have gone off track or fallen out of mind so the team can redirect energy and build in recovery time. End-of-quarter reviews serve a different purpose: recalibrating how aggressive you were and identifying areas where the team regularly fails to make progress.

3. **If the goal changes, score the old one anyway — don't erase it.** When priorities shift or new information arrives mid-period, start working on the new goal immediately. But keep the original goal in the OKR set and score it: add a zero with an asterisk, or document that it was dropped and why. Erasing changed goals removes the organizational memory of what was deprioritized and why. If this happens constantly, you are setting goals that are too specific or mixing activity planning into the goal-setting process.

4. **Document changes and notify affected teams every time.** When you add or drop a key result, document the decision and notify impacted teams. When you add an objective due to an urgent shift, document whether it resulted in deprioritizing existing work, and name what was deprioritized. When you drop an objective entirely — which should be rare — keep it in the OKR set for scoring and discussion. Consistency and transparency in handling changes matters as much as the change itself.

5. **Use end-of-quarter scoring to improve the next period, not to assign blame.** The end-quarter review should produce three outputs: a retrospective on areas where the team regularly falls behind (to inform future goal-setting ambition), clarity on what to keep, what to drop, and what to adjust next period, and a recalibrated sense of what "ambitious but credible" means for this team. Scoring is input to the next planning cycle, not a performance judgment in isolation.

## Draft-mode intake

1. "What's the OKR set being scored?"
2. "Mid-quarter or end-of-quarter?"
3. "What's changed since these were set — priorities, information, scope?"
4. "What's the rough self-assessment per key result?"

## Artifact

**Format:** Markdown — scored table (objective / KR / score / commentary / change-since-set) + a short narrative on what to keep / drop / adjust next period.
**Default save path:** `./docs/management/okr-scoring-YYYY-MM-DD.md` in the user's cwd. Ask before saving; ask before overwriting if file exists.
**Template:** Where the book provides a template, see `references/templates/okr-template.md` (extended with scoring columns).

## Source

*Scaling People* — Claire Hughes Johnson, Stripe Press 2023 — "Iterating and Scoring" (Exercises and templates), with cross-reference to "Good goals" FAQs ("How do you score goals?" and "What do you do if the goal changes before the time period ends?") in Chapter 2.

Encoded heuristic: OKR scoring is a lightweight, recurring discipline — green / yellow / red at mid-quarter and end-of-quarter — whose value comes from consistency, not precision. The mid-quarter review is a refocus tool; the end-quarter review is a recalibration tool. When priorities or information change mid-period, the book's guidance is pragmatic: start working on the new goal immediately, but score the old one anyway rather than erasing it (use a zero with an asterisk). This preserves organizational memory and surfaces whether the team is setting goals at the wrong granularity. Documenting every change and notifying affected teams is non-optional — it is what turns a local decision into a shared understanding.

Where the book provides a template, see `references/templates/okr-template.md` (extended with scoring columns).
