---
name: write-mission
description: Produce or refine a team or org mission statement. Use when starting a new team, when the existing mission no longer guides decisions, or when leadership above you has set a mission and you need a team-level version that rolls up cleanly.
---

# Write Mission

This skill produces a mission statement — one sentence (occasionally two) stating what the team or org exists to do. Use it when the mission is missing, stale, or aspirational-without-being-useful. The output should be concrete enough to guide a real decision the same week you publish it.

Part of `org-foundations-and-planning` (Chapter 2 of *Scaling People*).

## Mode

Ask the user which mode to run in. Default to `draft` if they don't specify.

- **`teach`** — Socratic walk-through (10-20 min). Use when the user is new to this artifact or wants to internalize the framework. Walk through every heuristic in the Rubric as a question; build the artifact incrementally; explain the "why" alongside the "what."
- **`draft`** — Targeted intake → first draft → refinement (5-10 min). Use when the user knows roughly what they want. Ask the 3-5 questions listed under "Draft-mode intake" below; produce a complete first draft; offer one round of refinement against the Rubric.
- **`polish`** — Critique-and-polish (2-5 min). Use when the user pastes an existing draft. Critique against every Rubric heuristic; rewrite to address gaps; explain what changed.

## Rubric

1. **Let the mission make itself known.** Even when no one has formalized a mission, it often surfaces organically — in early marketing copy, in what candidates keep quoting back to you, in the phrases that stick after all-hands talks. Before drafting from scratch, ask whether the mission has already presented itself and just hasn't been accepted yet.

2. **Descriptive and aspirational in equal measure.** A good mission is descriptive — specific enough that no other organization could claim the same statement word-for-word. It is also aspirational — pointing at an outcome unlikely ever to be fully achieved, giving the team an infinite horizon to work toward. A mission that is only descriptive becomes a job description; one that is only aspirational becomes a poster.

3. **Uniquely specific, not category-generic.** Test your draft: could a direct competitor adopt the same words? If yes, the mission is not yet yours. The specificity should reflect what your team or company actually does and for whom, not a generic version of the category ("deliver value to customers").

4. **Ladders up and down the stack.** Every part of the organization — team, division, company — should have a mission, and each level should roll up to the next. If your team's mission doesn't connect to the division's, either your mission is off or you've found a gap in the org above you. Individuals can also have missions, though those shift more frequently as roles evolve.

5. **Does not need a completion date.** Unlike annual or quarterly goals, a mission is not meant to be achieved in any particular timeframe. Bill Gates' early goal of "a computer on every desk and in every home" was not expected to be checked off by a fiscal year. The mission provides the direction; the goals provide the milestones.

6. **Short enough to remember, specific enough to apply.** A mission that must be paraphrased to be explained is too long. Aim for one sentence. If the team cannot use it to reject an opportunity or resolve a priority dispute, it is not doing its job.

## Draft-mode intake

1. "Whose mission is this — a team, a function, a whole org?"
2. "Who are the people you serve, in one phrase?"
3. "What does the team do, in one verb phrase?"
4. "What changes for those people if you succeed?"
5. "What's a recent decision the new mission should have made obvious?"

## Artifact

**Format:** Markdown — a heading-level mission line plus a 1-paragraph rationale plus a "rejected alternatives" list of 2-3 considered-and-cut wordings.
**Default save path:** `./docs/management/mission-YYYY-MM-DD.md` in the user's cwd. Ask before saving; ask before overwriting if file exists.
**Template:** Inline — no shared template.

## Source

*Scaling People* — Claire Hughes Johnson, Stripe Press 2023 — Chapter 2, "Founding documents > Mission."

Encoded heuristic: A mission states why you exist — it is both descriptive (uniquely specific to your org, not transferable to a competitor) and aspirational (pointing beyond what any timeframe can fully achieve). The mission often surfaces organically before it is formalized: watch for the phrase that candidates keep quoting, the line that appeared in early copy, the words people reach for when explaining the company to a stranger. Every team, division, and company should have one, and each should ladder up to the next. The test is practical: can someone use the mission to decide, in the moment, what to work on or what to decline?

Where the book provides a template, see references/templates/operating-principles-example.md (only for contrast — mission vs principles).
