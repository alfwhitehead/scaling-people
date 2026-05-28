---
name: self-awareness-assessment
description: Self-awareness audit — values, work-style preferences (analyzer/director/promoter/collaborator), strengths and gaps. Use when starting a new role, before producing your working-with-me doc, or when stuck on a recurring management problem you might be the source of.
---

# Self-Awareness Assessment

This skill produces a structured self-awareness audit covering values, work-style preferences, strengths, and gaps. Use it as the grounding work that everything else in this plugin assumes — and as the input to write-working-with-me. The audit is for you, not your team; share excerpts deliberately.

Part of `operating-principles` (Chapter 1 of *Scaling People*).

## Mode

Use the `AskUserQuestion` tool to ask which mode to run in. Default to `draft` if the user skips or picks "Other" without specifying.

- **`teach`** — Socratic walk-through (10-20 min). Use when the user is new to this artifact or wants to internalize the framework. Walk through every heuristic in the Rubric as a question; build the artifact incrementally; explain the "why" alongside the "what."
- **`draft`** — Targeted intake → first draft → refinement (5-10 min). Use when the user knows roughly what they want. Ask the 3-5 questions listed under "Draft-mode intake" below; produce a complete first draft; offer one round of refinement against the Rubric.
- **`polish`** — Critique-and-polish (2-5 min). Use when the user pastes an existing draft. Critique against every Rubric heuristic; rewrite to address gaps; explain what changed.

**When asking the user any question during this skill** (mode selection, intake, refinement, clarification): prefer the `AskUserQuestion` tool for any question with 2-4 reasonably discrete options (the user can always pick "Other" to free-text). Use plain chat only for questions that genuinely need a sentence or paragraph of free-form response. Multi-select questions are fine when the user could legitimately choose more than one.

## Rubric

1. **Know your values before you try to change your behavior.** Values drive behavior at a level below conscious control — Eli kept reverting to oversharing not out of stubbornness but because withholding information felt like a betrayal of his core value of transparency. Until you name the value, you can't negotiate with it. Map each value to the work activity it drives, the positive outcome it produces, and the trade-off it creates.

2. **Plot your work-style quadrant — Analyzer, Director, Promoter, or Collaborator.** The book's four-quadrant model plots work style on two axes: introverted-to-extroverted and task-oriented-to-people-oriented. Analyzers (introverted, task-oriented) seek data before acting. Directors (extroverted, task-oriented) drive toward fast, strong-opinion outcomes. Promoters (extroverted, people-oriented) inspire and start but don't always finish. Collaborators (introverted, people-oriented) build inclusive systems that can overcomplicate. Know which quadrant describes your default, and note where your at-work and at-home placements diverge.

3. **Ask whether you talk to think or think to talk.** This single question surfaces your introversion-extroversion preference faster than any formal assessment. It also predicts where you'll do your best work: alone in a document or live in a room.

4. **Inventory skills separately from capabilities.** Skills are binary and tactical — you either can build a financial model or you can't. Capabilities are innate or acquired higher-order abilities — pattern-matching, synthesizing complex information, managing stakeholders under pressure. Your strengths are the sum of both. Identify them separately so you know which gaps need training and which need a complementary hire.

5. **Your biggest strength is also your biggest weakness.** A forceful communicator who jumps to action will build a team that never slows down to listen. A strong strategic thinker will hire too many strategists. The audit is incomplete until you've stated, for each strength, the failure mode it produces under pressure.

6. **Build the complementary team, not the mirror team.** Self-awareness is not just about knowing yourself — it's about knowing what you're not, so you can hire and arrange a team that covers those gaps. A portfolio of complementary preferences, experiences, skills, and capabilities outperforms a team of people who share your profile.

7. **Watch for telltale signs of low self-awareness.** You're consistently getting feedback you disagree with. You feel frustrated because colleagues don't understand what you're trying to convey. You feel drained at the end of the day and can't explain why. You can't describe what kinds of work you enjoy. You have friction with your manager you can't resolve. Any of these signals is a prompt to dig deeper.

## Draft-mode intake

1. "What's prompting the audit now — new role, recurring problem, time-based check-in?"
2. "What 3-5 values would you say you hold? (Examples are fine; the book has a list including accomplishment, balance, commitment, compassion, transparency.)"
3. "When you're at your best, are you more task-oriented or people-oriented? More introverted or extroverted?"
4. "What two strengths show up in feedback over and over?"
5. "What two gaps show up in feedback over and over?"

## Artifact

**Format:** Markdown — sections for values, work-style quadrant, strengths, gaps, and "what this means for how I work." 1-2 pages.
**Default save path:** `./docs/management/self-awareness-YYYY-MM-DD.md` in the user's cwd. Ask before saving; ask before overwriting if file exists.
**Template:** (No shared template — produce inline.)

## Source

*Scaling People* — Claire Hughes Johnson, Stripe Press 2023 — Chapter 1, "1. Build self-awareness to build mutual awareness" (incl. Exercises and templates: Understand Your Values, Self-Awareness Exercises).

Encoded heuristic: Self-awareness has three components — values, work-style preferences, and skills/capabilities. Values drive behavior below the level of conscious intention (Eli's story); you can't negotiate with a value you haven't named. Work-style preferences map onto a two-axis quadrant (introverted/extroverted × task/people-oriented), producing four types: Analyzer, Director, Promoter, Collaborator. Strengths are the sum of skills and capabilities, and the not-so-secret secret is that every strength carries a matching weakness. The goal of self-awareness is mutual awareness: once you know yourself, you can describe yourself, hire complementarily, and have a "conversation about the conversation" when your values collide with someone else's.

(No shared template — produce inline.)
