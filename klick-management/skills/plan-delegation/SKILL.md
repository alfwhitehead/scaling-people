---
name: plan-delegation
description: Decide when, how, and to whom to delegate a piece of work. Use when your plate is full or when developing a report through stretch work.
---

# Plan Delegation

This skill produces a delegation decision document: a classification of the work on the impact/trapdoor matrix, a choice of who should receive the work, and a delegation conversation guide covering assignment context, deliverables, timeline, and check-in cadence. Use it when you are overextended, when a report needs a stretch assignment for development, or when you realize you are a bottleneck for your team.

Part of `team-development` (Chapter 4 of *Scaling People*).

## Mode

Use the `AskUserQuestion` tool to ask which mode to run in. Default to `draft` if the user skips or picks "Other" without specifying.

- **`teach`** — Socratic walk-through (10-20 min). Use when the user is new to this artifact or wants to internalize the framework. Walk through every heuristic in the Rubric as a question; build the artifact incrementally; explain the "why" alongside the "what."
- **`draft`** — Targeted intake → first draft → refinement (5-10 min). Use when the user knows roughly what they want. Ask the 3-5 questions listed under "Draft-mode intake" below; produce a complete first draft; offer one round of refinement against the Rubric.
- **`polish`** — Critique-and-polish (2-5 min). Use when the user pastes an existing draft. Critique against every Rubric heuristic; rewrite to address gaps; explain what changed.

**When asking the user any question during this skill** (mode selection, intake, refinement, clarification): prefer the `AskUserQuestion` tool for any question with 2-4 reasonably discrete options (the user can always pick "Other" to free-text). Use plain chat only for questions that genuinely need a sentence or paragraph of free-form response. Multi-select questions are fine when the user could legitimately choose more than one.

## Rubric

1. **Classify the work before choosing the person.** Use the two-axis framework: Is the impact high or low? Is the outcome a trapdoor (hard to reverse) or adjustable (can be iterated)? High-impact trapdoor work is the only quadrant where you should personally retain ownership as a default. Everything else should almost always be delegated.

2. **Check yourself for under-delegation.** You are under-delegating if: reports bring you problems but rarely solutions; most decisions cannot be made without you and you are a bottleneck; things fall apart when you are away; you feel overwhelmed by day-to-day demands and cannot do strategic work. If any of these are true, the problem is systemic, not project-specific.

3. **Check yourself for over-delegation.** You are over-delegating if: your team consistently produces low-quality work; you learn of projects going off the rails too late; reports frequently feel overwhelmed; you cannot say off the top of your head what critical work your team has recently completed and what comes next. People-oriented managers who care a lot about trust are particularly at risk here.

4. **Match the work to the person using skill-will.** Delegate more to high skill / high will reports (delegate and empower). Delegate selectively to high will / low skill reports so they can build the needed skills, with checkpoints. If there is someone you are not comfortable delegating to, ask yourself why they are on the team.

5. **Use the delegation conversation to set the person up for success.** The conversation should cover: the broader context and why this work matters (bottom-line the assignment); why this person is the right choice (tie to their skills or development goals from the career conversation); what the finished work should look like (clear deliverables); when it is due and whether that timeline is feasible; explicit buy-in from the person; the first concrete next step; and how you will stay informed on progress.

6. **See one, do one, teach one.** When the work requires modeling before delegating, use this progression: you do the work and the report observes; the report does the work themselves; then the report delegates and oversees someone else doing it. Modeling without the practice and teach steps is incomplete and will not produce lasting capability.

7. **Delegating is expensive up front and cheap at scale.** It requires more initial investment than doing the work yourself, which is especially frustrating for task-oriented personalities. Remind yourself of the long-term payoff: leverage for you, development for the report, retained talent, and mutual reliance across the team.

## Draft-mode intake

1. "What is the piece of work you are considering delegating? Describe it in a sentence."
2. "Is this high or low impact? Is the outcome adjustable or a trapdoor?"
3. "Who on your team comes to mind as a candidate, and what is their current skill-will state for this type of work?"
4. "Is the goal here primarily to get the work done, or primarily to develop the person — or both?"
5. "How will you stay informed on progress without becoming a bottleneck again?"

## Artifact

**Format:** Markdown — a one-paragraph classification of the work (impact/trapdoor analysis), a one-paragraph rationale for the chosen person, and a delegation conversation guide (context, deliverables, timeline, buy-in question, next steps, check-in plan).
**Default save path:** `./docs/management/delegation-[project-name]-YYYY-MM-DD.md` in the user's cwd. Ask before saving; ask before overwriting if file exists.
**Template:** Inline — no shared template.

## Source

*Scaling People* — Claire Hughes Johnson, Stripe Press 2023 — Chapter 4, "(Re)building the team > Delegating."

Encoded heuristic: Delegation is the mechanism through which managers get leverage, develop their people, and build team resilience. The classification framework has two axes — impact (high vs low) and outcome reversibility (trapdoor vs adjustable). High-impact trapdoor work stays with you by default; everything else should almost always be delegated. Use the skill-will matrix to choose who receives the work: high skill / high will gets more; high will / low skill gets selective development assignments with checkpoints; persistent reluctance to delegate to someone is a signal about that person's fit. The delegation conversation must cover context, deliverables, timeline, buy-in, next steps, and a check-in plan. Delegation is front-loaded effort that pays off at scale; under-delegation turns managers into bottlenecks and stunts team development.

Where the book provides a template, see `references/templates/career-conversation.md` (for connecting delegation choices to the person's development goals).
