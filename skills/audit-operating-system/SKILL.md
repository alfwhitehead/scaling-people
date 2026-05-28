---
name: audit-operating-system
description: Diagnose what's wrong with the current operating system or cadence — defensive process, stale process, missing forums, overgrown rituals. Recommends what to add, cut, or change. Use when team velocity is dropping, decisions aren't sticking, or meetings keep multiplying.
---

# Audit Operating System

This skill diagnoses an existing operating system — what's defensive, what's stale, what's missing, what's overgrown. Output is a punch list of additions, cuts, and changes, prioritized. Use it when something feels wrong with how the team runs: decisions are slow, goals are unclear, meetings are multiplying, or participation is dropping.

Part of `org-foundations-and-planning` (Chapter 2 of *Scaling People*).

## Mode

Ask the user which mode to run in. Default to `draft` if they don't specify.

- **`teach`** — Socratic walk-through (10-20 min). Use when the user is new to this artifact or wants to internalize the framework. Walk through every heuristic in the Rubric as a question; build the artifact incrementally; explain the "why" alongside the "what."
- **`draft`** — Targeted intake → first draft → refinement (5-10 min). Use when the user knows roughly what they want. Ask the 3-5 questions listed under "Draft-mode intake" below; produce a complete first draft; offer one round of refinement against the Rubric.
- **`polish`** — Critique-and-polish (2-5 min). Use when the user pastes an existing draft. Critique against every Rubric heuristic; rewrite to address gaps; explain what changed.

## Rubric

1. **Check for the seven warning signs first.** The book names specific symptoms: goals, timelines, or owners are unclear; everything feels too slow; people flag problems but offer no solutions; status is unfindable; no one can name the decision-maker or the priorities; participation is dropping; updates feel pointless and no one is updating trackers. A single symptom can be noise — multiple symptoms together signal structural failure.

2. **Distinguish defensive process from stale process.** Defensive process emerges when ownership is unclear — reviews multiply, approvers accumulate, sign-off lists grow. The fix is to clarify ownership and shrink the approval surface. Stale process is different: it was once useful, has outgrown its purpose, or the problem it solved is gone. The fix is to sunset or reshape it, not add more structure on top.

3. **Look for participation collapse as a leading indicator.** When people stop submitting updates, open their laptops in review meetings, or drift into the "What about the bigger picture?" role, the process has already gone stale. Treat disengagement as data, not personality.

4. **Don't change processes too quickly.** Revisiting every six months is the right tempo. More frequent changes destabilize the team; less frequent changes cause people to switch to autopilot. When you do change a process, run it as a time-boxed experiment with stated evaluation criteria.

5. **Audit whether process and meetings are being conflated.** A process that adds meetings is a red flag. Ask: could any of these forums' objectives be achieved through a written update or a project tracker? The audit should surface forums that exist to compensate for missing clarity rather than to accomplish real work.

6. **Match each forum to a named owner.** A cadence item without an owner drifts. If no one is "switched on" for a given review — prepared, engaged, ready to make decisions — the forum has outlived its justification.

7. **Produce a prioritized punch list, not a manifesto.** The output of an audit is concrete: add X, cut Y, change Z. Each item should state the symptom it addresses, the proposed action, and who is accountable for the change. Avoid vague recommendations like "improve communication."

## Draft-mode intake

1. "What team is being audited?"
2. "What symptoms triggered the audit (e.g., slow decisions, missed goals, meeting overload)?"
3. "What's the current cadence map (paste or describe)?"
4. "What's changed recently (org, scope, size, leadership)?"

## Artifact

**Format:** Markdown — diagnosis (symptoms → likely cause) + punch list (add / cut / change items with rationale per item).
**Default save path:** `./docs/management/os-audit-YYYY-MM-DD.md` in the user's cwd. Ask before saving; ask before overwriting if file exists.
**Template:** (No shared template — produce inline.)

## Source

*Scaling People* — Claire Hughes Johnson, Stripe Press 2023 — Chapter 2, "Operating cadence > How to tell if something is wrong with your operating system or cadence" (cross-reference: "A brief note on process").

Encoded heuristic: A broken operating system shows up in recognizable patterns — unclear ownership, sluggish decisions, missing status, falling participation, and a proliferation of meetings that feel like overhead rather than work. Two distinct failure modes drive most of these symptoms: defensive process (created to compensate for unclear ownership) and stale process (once useful, now rote or irrelevant). An audit should name the failure mode, not just the symptom, because the remedy differs: defensive process requires ownership clarification; stale process requires sunsetting or reshaping. The output is a concrete punch list — what to add, what to cut, what to change — each item tied to a named symptom and an accountable owner.

(No shared template — produce inline.)
