---
name: run-career-conversation
description: Prep + script for a development conversation with a direct report. Use at least quarterly per report; more often during a transition.
---

# Run Career Conversation

This skill produces a career conversation prep document: the manager's framing script, a walk-through of the five conversation sections (origins, schooling, career history, motivations, future vision), and a set of follow-up development goals to carry into future 1:1s and performance reviews. Use it when you are new to managing someone, onboarding a team, or sensing that you have lost sight of a report's longer-term aspirations.

Part of `team-development` (Chapter 4 of *Scaling People*).

## Mode

Ask the user which mode to run in. Default to `draft` if they don't specify.

- **`teach`** — Socratic walk-through (10-20 min). Use when the user is new to this artifact or wants to internalize the framework. Walk through every heuristic in the Rubric as a question; build the artifact incrementally; explain the "why" alongside the "what."
- **`draft`** — Targeted intake → first draft → refinement (5-10 min). Use when the user knows roughly what they want. Ask the 3-5 questions listed under "Draft-mode intake" below; produce a complete first draft; offer one round of refinement against the Rubric.
- **`polish`** — Critique-and-polish (2-5 min). Use when the user pastes an existing draft. Critique against every Rubric heuristic; rewrite to address gaps; explain what changed.

## Rubric

1. **This is not a performance review, and it is not "what's your five-year plan?"** The career conversation is a get-to-know-you session. Its purpose is to understand the person's narrative arc — the decisions they have made, why they made them, and what that reveals about their values and motivations — not to audit their future ambitions or set expectations.

2. **Time it right: after a few months of working together, before any formal review.** You need enough shared context to be comfortable with the conversation. You don't want the career conversation to feel like an evaluation, so hold it well clear of the performance cycle.

3. **Three purposes, not one.** The conversation establishes that you care about the person and their career; it builds your understanding of their narrative arc in a broader context than their current role; and it creates a reference point you will return to at reorgs, at moments of over- or under-challenge, and when thinking about new assignments or delegation choices.

4. **Ask "why" a lot and listen actively.** The walk-through-history approach only yields insight if you probe the decisions, not just the facts. Take notes you can refer to in future conversations. What do they think about past choices now? What have they not explored? What do they want to return to?

5. **Project forward on work type, not title.** The forward-looking section should surface what kind of work they want to be doing — management, research, execution, communication, advanced problem-solving — not what job title they want to hold. The goal is to identify the skills and experiences that, if developed, will move them toward their envisioned future.

6. **Close with two or three named development goals.** The conversation is not complete until you have recapped it together, shared your notes, and agreed on two or three development goals to track going forward. These goals become the reference point in future 1:1s: "Does this project choice fit with the path we outlined?"

## Draft-mode intake

1. "Who is this conversation for — new to you, long-tenured, transitioning to a new role?"
2. "What do you already know about this person's career and motivations? What is still opaque to you?"
3. "Is there a decision or assignment coming up where their career-arc context would be directly useful?"
4. "Have you had any version of this conversation with them before? If so, what did you learn?"

## Artifact

**Format:** Use the shared template at `references/templates/career-conversation.md`. Fill in the "who / last conversation / this conversation's goal" header, record notes from each conversation section, and add follow-up development goals at the end.
**Default save path:** `./docs/management/career-conversation-[name]-YYYY-MM-DD.md` in the user's cwd. Ask before saving; ask before overwriting if file exists.
**Template:** `references/templates/career-conversation.md`

## Source

*Scaling People* — Claire Hughes Johnson, Stripe Press 2023 — Chapter 4, "(Re)building the team > Career conversations" and the "Career Conversations" exercise in the chapter appendix.

Encoded heuristic: The career conversation is the manager's primary tool for understanding what motivates a report and what trajectory they are on. It takes a walk-through-history approach — origins, schooling, post-school decisions, career path, forward vision — with heavy emphasis on why at each step. It is not a performance conversation and must not be framed as one. Schedule it after a few months of working together, hold it well before any formal review cycle, and treat the notes as a living reference. The output is mutual understanding of the person's narrative arc, plus two or three named development goals that the manager and report track together. The career conversation feeds directly into delegation decisions, reorg conversations, and performance reviews.

Where the book provides a template, see `references/templates/career-conversation.md`.
