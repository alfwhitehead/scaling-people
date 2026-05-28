---
name: manage-distributed-or-changing-team
description: Remote/distributed practices + managing through uncertainty or crisis. Use when going distributed, adding remote workers, or leading through a change/crisis.
---

# Manage Distributed or Changing Team

This skill produces a distributed-team operating plan or an uncertainty-response plan: a diagnosis of the primary challenge (coordination, cohesion, or participation), a set of norms and structural mitigations matched to the team's configuration, and — when the team is navigating uncertainty — a communication and action plan grounded in transparency and forward movement. Use it when adding remote workers, managing across time zones, or leading a team through an ambiguous or difficult period.

Part of `team-development` (Chapter 4 of *Scaling People*).

## Mode

Ask the user which mode to run in. Default to `draft` if they don't specify.

- **`teach`** — Socratic walk-through (10-20 min). Use when the user is new to this artifact or wants to internalize the framework. Walk through every heuristic in the Rubric as a question; build the artifact incrementally; explain the "why" alongside the "what."
- **`draft`** — Targeted intake → first draft → refinement (5-10 min). Use when the user knows roughly what they want. Ask the 3-5 questions listed under "Draft-mode intake" below; produce a complete first draft; offer one round of refinement against the Rubric.
- **`polish`** — Critique-and-polish (2-5 min). Use when the user pastes an existing draft. Critique against every Rubric heuristic; rewrite to address gaps; explain what changed.

## Rubric

1. **Diagnose the primary challenge: coordination, cohesion, or participation.** A few remote employees on a mostly centralized team: participation is the hardest problem. A fully remote team: cohesion — invest in early in-person time and relationship-building, not just tactical meetings. A team split across offices or two teams working across locations: coordination — focus on documentation, async-first norms, and shared decision visibility. When the whole company is remote, participation gaps shrink but coordination and cohesion challenges remain.

2. **Level the playing field structurally.** The minute an in-person conversation turns into a work discussion, it moves to a channel where everyone can see it. Every meeting needs a video link, not just a room number. Serious remote setups (Automattic-style) have each person join calls from their own device even when co-located, so no one experiences being "the one dialing in." Documentation is not optional — it is how trust is maintained across time zones.

3. **Make room for in-person time on a regular cadence.** There is no viable substitute for quality in-person time. When first forming a remote team, plan to meet at least quarterly. Once the team is established, biannual is often workable. When the team is in growth mode or adding new members, return to quarterly. In-person time is for spontaneous social connection and getting people out of operating rhythm — both of which are very hard to engineer remotely.

4. **Build a strong operating system before adding remote workers.** Remote work amplifies every gap in your documentation, ownership clarity, and operating cadence. If you do not have strong async information sources (video recordings, meeting notes, snippets docs) and explicit norms, add remote workers only when you are willing to invest in building those systems first.

5. **Managing through uncertainty: be transparent, to a point.** Acknowledge challenges head-on without over-indexing on your own worry. The more common mistake is pretending a plan is in place when it isn't — this erodes trust at the moment the team needs their manager most. It is acceptable and often necessary to say: "We don't have all the details yet, but here is what I know and here is what I am working on."

6. **Reiterate the vision during uncertain times.** Uncertainty does not mean the direction is wrong. Retell the story of why the team exists and where the work leads. Authentic hope requires clarity and imagination — both management (naming what is happening) and leadership (pointing at the better future).

7. **Bias toward action, even small actions.** During uncertainty, the temptation to wait for a perfect plan is strong and almost always wrong. Small, clearly communicated decisions create momentum and signal competence. Communicate openly about what you are doing and what you are learning. Movement beats analysis paralysis.

## Draft-mode intake

1. "What type of distributed situation are you managing — a few remote people on a central team, a fully remote team, or offices in multiple locations?"
2. "Which challenge is most acute right now: coordination (information flow and decisions), cohesion (team identity and belonging), or participation (equal access and inclusion)?"
3. "Are you in a period of uncertainty or change right now? If so, what do your team members know, and what are they likely worried about?"
4. "What does your current documentation and async-communication infrastructure look like? Strong, weak, or nonexistent?"
5. "When did your team last meet in person, and how did it go?"

## Artifact

**Format:** Markdown — a "team configuration and primary challenge" section, a "structural mitigations" checklist matched to the challenge type, and (if uncertainty applies) a "managing through uncertainty" section with a communication plan and a list of near-term actions.
**Default save path:** `./docs/management/distributed-team-plan-YYYY-MM-DD.md` in the user's cwd. Ask before saving; ask before overwriting if file exists.
**Template:** Inline — no shared template.

## Source

*Scaling People* — Claire Hughes Johnson, Stripe Press 2023 — Chapter 4, "Team-building complexities > Managing distributed and remote teams," "Adding remote workers," "Managing through uncertainty," and the sidebar "Reid Hoffman on managing through crisis."

Encoded heuristic: Distributed teams face three challenges: coordination (information and decision flow), cohesion (team identity and belonging), and participation (equal access). The right mitigation depends on which configuration the team is in: a few remote workers on a central team need participation-focused interventions; fully remote teams need cohesion investment (early in-person time, relationship rituals); multi-office or cross-location teams need coordination infrastructure. The three mitigations that apply across all types are: inclusive meeting norms and documentation, leveling the playing field (hallway chats in Slack, every person on their own video), and budgeted in-person time. For managing through uncertainty, the formula is: be transparent without amplifying your own anxiety; reiterate the vision; bias toward action even when the plan is incomplete. "Authentic hope requires clarity and imagination."

Where the book provides a template, see `references/templates/offsite-plan.md` (for the in-person gatherings that anchor distributed team cohesion).
