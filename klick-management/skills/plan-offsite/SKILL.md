---
name: plan-offsite
description: Pick offsite type by team development stage; design agenda, check-ins, run-of-show. Use when planning a team or leadership-team offsite.
---

# Plan Offsite

This skill produces an offsite plan: a determination of the right offsite type based on the team's development stage, a structured agenda with check-ins, working sessions, and a check-out, DRI assignments for each session, and a pre-offsite planning checklist. Use it when planning any team or leadership-team offsite, from a half-day working session to a multi-day retreat.

Part of `team-development` (Chapter 4 of *Scaling People*).

## Mode

Ask the user which mode to run in. Default to `draft` if they don't specify.

- **`teach`** — Socratic walk-through (10-20 min). Use when the user is new to this artifact or wants to internalize the framework. Walk through every heuristic in the Rubric as a question; build the artifact incrementally; explain the "why" alongside the "what."
- **`draft`** — Targeted intake → first draft → refinement (5-10 min). Use when the user knows roughly what they want. Ask the 3-5 questions listed under "Draft-mode intake" below; produce a complete first draft; offer one round of refinement against the Rubric.
- **`polish`** — Critique-and-polish (2-5 min). Use when the user pastes an existing draft. Critique against every Rubric heuristic; rewrite to address gaps; explain what changed.

## Rubric

1. **Assess whether the team is ready for an offsite.** Offsites are for forming stronger bonds within a team designed to work well together — not for solving talent issues. Before planning one, confirm that the structural and talent decisions are already made. An offsite won't fix a composition problem.

2. **Match the agenda to the team's development stage (Tuckman's model).** Forming: more team-focused activities (work-style exercises, norms-setting), more direction from the leader, expect silence. Storming: work on goals, roles, and processes; frame conflict as healthy, don't squelch it. Norming: celebrate progress, maintain urgency. Performing: push the rate of challenge, know this phase is temporary. The more mature the stage, the more you can weight task over team.

3. **Balance task-focused and team-focused sessions.** Task-focused: reviewing metrics, setting goals, assigning DRIs, strategy discussions. Team-focused: work-style exercises, shared meals, defining norms, discussing roles and accountability. Neither alone is sustainable; both must appear in the agenda.

4. **Use a shared planning document.** A shared doc before and during the offsite creates inclusivity (ideas from people who prefer writing over debate), an anchoring effect (collective goals visible to all), and a shared mental space. Assign a DRI and a notetaker to each session; use PAL (Purpose, Agenda, Limit) to structure each block.

5. **Model the check-in — always.** The check-in sets the emotional rhythm for the day. Brief, personal, and a little vulnerable is the target. Model it yourself or have someone who understands the tone you're after go first. If you forget to model it, the first participant will set the tone for you.

6. **Close every offsite with a check-out.** Check-outs help participants commit the day's insights to memory and generate a sense of completion. Options: one-word, a question about the most important decision made, or a 30-second reflection on what they're still thinking about. The offsite is a shared memory; the check-out cements it.

7. **For senior teams, two to three times a year; for junior teams, at least annually.** Frequency should reflect the team's strategic importance and the pace of change. Distributed teams need more frequent in-person time, not less, especially in the first year.

## Draft-mode intake

1. "What is the team's development stage — forming, storming, norming, or performing?"
2. "What are the one to three goals for this offsite — team-building, strategy, both?"
3. "How long is the offsite (half-day, full day, multi-day) and how many people are attending?"
4. "Is the team co-located, distributed, or a mix — and does anyone need special accommodation to participate equally?"
5. "Who will own each session? Do you have DRIs identified, or do you need to assign them?"

## Artifact

**Format:** Use the shared template at `references/templates/offsite-plan.md`. Fill in the offsite type, team development stage, goals, agenda block (check-in / sessions / check-out with PAL for each), logistics checklist, and post-offsite follow-up actions.
**Default save path:** `./docs/management/offsite-plan-YYYY-MM-DD.md` in the user's cwd. Ask before saving; ask before overwriting if file exists.
**Template:** `references/templates/offsite-plan.md`

## Source

*Scaling People* — Claire Hughes Johnson, Stripe Press 2023 — Chapter 4, "Creating the team environment > Offsites" and the "Planning and Running Your Offsite" exercise in the chapter appendix.

Encoded heuristic: Offsites have three purposes: evolving a group into a team, evaluating progress and setting near-term priorities, and engendering long-term strategic thinking. Most offsites are a mix of all three. The agenda design starts with the team's development stage — Tuckman's forming, storming, norming, performing model — and balances task-focused sessions (metrics, goals, DRIs) with team-focused ones (work-style exercises, norms, meals). Every offsite should open with a modeled check-in and close with a check-out. A shared planning document is not optional; it creates inclusivity and an anchoring effect that in-room discussion alone cannot replicate. Use PAL (Purpose, Agenda, Limit) for each session block. Senior teams should gather two to three times a year; junior teams at least annually; distributed teams more frequently early on.

Where the book provides a template, see `references/templates/offsite-plan.md`.
