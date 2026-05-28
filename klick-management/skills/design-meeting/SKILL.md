---
name: design-meeting
description: Purpose, roles, norms, decision-making for any recurring meeting (incl. leadership-team variant). Use when starting a new recurring meeting or fixing one that's broken.
---

# Design Meeting

This skill produces a meeting design document: a PAL (Purpose, Agenda, Limit) structure, defined roles, agreed norms, and a decision-making framework for a new or broken recurring meeting. Use it when launching a new recurring meeting, onboarding a new team into an existing one, or diagnosing why a meeting has stopped working.

Part of `team-development` (Chapter 4 of *Scaling People*).

## Mode

Use the `AskUserQuestion` tool to ask which mode to run in. Default to `draft` if the user skips or picks "Other" without specifying.

- **`teach`** — Socratic walk-through (10-20 min). Use when the user is new to this artifact or wants to internalize the framework. Walk through every heuristic in the Rubric as a question; build the artifact incrementally; explain the "why" alongside the "what."
- **`draft`** — Targeted intake → first draft → refinement (5-10 min). Use when the user knows roughly what they want. Ask the 3-5 questions listed under "Draft-mode intake" below; produce a complete first draft; offer one round of refinement against the Rubric.
- **`polish`** — Critique-and-polish (2-5 min). Use when the user pastes an existing draft. Critique against every Rubric heuristic; rewrite to address gaps; explain what changed.

**When asking the user any question during this skill** (mode selection, intake, refinement, clarification): prefer the `AskUserQuestion` tool for any question with 2-4 reasonably discrete options (the user can always pick "Other" to free-text). Use plain chat only for questions that genuinely need a sentence or paragraph of free-form response. Multi-select questions are fine when the user could legitimately choose more than one.

## Rubric

1. **Use PAL to anchor every meeting: Purpose, Agenda, Limit.** A meeting should have one or two purposes, not five. State the purpose explicitly so participants feel bought in. The agenda lists the specific topics that serve that purpose. The limit sets time for the meeting and each agenda item — covering too many topics in too little time is the most common way meetings become surface-level or end in frustration.

2. **Assign three roles explicitly: DRI, facilitator, notetaker.** The DRI owns the meeting's success. The facilitator keeps the meeting on time, gets through the objectives, and captures decisions and actions — this is often but not always the DRI. The notetaker records top-level discussion, decisions made, and action items with owners and timelines. Notes should not be a transcript; they should be sent out after the meeting.

3. **Set norms before the first meeting, not during a crisis.** Norms are the commitments the group makes about how to show up: meeting time and punctuality, laptop use, pre-reads (read in advance or with 10 minutes at the start?), action-item tracking, and delegate policy. Name the "stinky fish" norm explicitly — any issue lurking beneath the surface, no matter how uncomfortable, belongs on the table. Refer to norms when violations occur; it is much harder to course-correct without them.

4. **Operate both operator and creator modes.** Operator meetings have clear agendas and produce decisions, updates, and alignment. Creator meetings are for brainstorming — less structured, may not result in a decision, but generate ideas worth following. Both are necessary. Over-programming a creative session will kill it; under-programming an operational one will waste everyone's time. Be explicit about which mode each session or block is in.

5. **Disagree and commit; have a parking lot.** Participants can disagree during deliberation, but once a decision is made, everyone commits to supporting its success. Any topic not immediately relevant to the meeting's purpose goes to the parking lot — and the facilitator must close out parking lot items before the meeting ends or they become the town dump.

6. **Hold your opinion until the end if you are the most senior person.** If the leader opines first, it chills the room for those who disagree. Wait, integrate what others say, then share your view. Break this default only when you want to put forward a provocative idea to elicit a reaction.

7. **Audit and reconfigure every three to six months.** Meetings go stale. Poll participants or have a neutral person do so: Are they useful? Are the right people involved? Could more be accomplished asynchronously? Then either refresh (reset norms), evolve (change participants or topics), or start over (new business need). The most senior team in an organization sets the model for the entire company — the leadership team's meeting habits will propagate downward.

## Draft-mode intake

1. "What is the single most important purpose of this meeting — decisions, updates, alignment, problem-solving, or creative brainstorming?"
2. "Who needs to be in the room, and what role will each person play (DRI, facilitator, notetaker, participant)?"
3. "What norms does this group need to agree on explicitly — and are there any known meeting dysfunctions to address up front?"
4. "For decision-making meetings: is the decision autocratic, consultative, consensus, democratic, or delegated?"
5. "Is this an operator meeting, a creator meeting, or a mix — and does the agenda reflect that?"

## Artifact

**Format:** Markdown — a PAL block (Purpose, Agenda, Limit), a Roles section (DRI / facilitator / notetaker), a Norms section (logistics, stinky fish, electronics, parking lot, disagree-and-commit), a Decision-making section (who decides and how), and a Reconfigure date.
**Default save path:** `./docs/management/meeting-design-[meeting-name]-YYYY-MM-DD.md` in the user's cwd. Ask before saving; ask before overwriting if file exists.
**Template:** Inline — no shared template.

## Source

*Scaling People* — Claire Hughes Johnson, Stripe Press 2023 — Chapter 4, "Creating the team environment > Meetings."

Encoded heuristic: Good meetings are generative, decisive, and inclusive — they are expressions of the team at its best. They require two things: groundwork laid before the first meeting (common understanding of roles, work styles, and norms), and deliberate running mechanics. Use PAL (Purpose, Agenda, Limit) to structure every meeting. Assign three explicit roles: DRI, facilitator, notetaker. Set norms before they are needed: meeting time, electronics, pre-reads, action-item tracking, and the stinky fish agreement (no topic is undiscussable). Distinguish operator mode (decisions, updates, alignment) from creator mode (brainstorming, strategy, big-picture thinking) and design the session format accordingly. The most senior person should hold their opinion until the end. Audit meetings every three to six months and reconfigure when they stop serving their purpose.

Where the book provides a template, see `references/templates/offsite-plan.md` (for offsite sessions that use the same PAL structure).
