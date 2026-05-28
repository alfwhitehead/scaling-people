---
name: prep-to-say-the-hard-thing
description: Prepare to say the thing you think you cannot say — share feelings, be measured, separate the person from the idea or task. Use before any difficult conversation: feedback, escalation, pushback to your manager, disagreement with a peer.
---

# Prep to Say the Hard Thing

This skill produces a short prep doc for a hard conversation — what you're going to say, what feelings you'll name, how you'll keep the person separate from the idea, and where you might over- or under-react. It's prep for you, not a script for them.

Part of `operating-principles` (Chapter 1 of *Scaling People*).

## Mode

Use the `AskUserQuestion` tool to ask which mode to run in. Default to `draft` if the user skips or picks "Other" without specifying.

- **`teach`** — Socratic walk-through (10-20 min). Use when the user is new to this artifact or wants to internalize the framework. Walk through every heuristic in the Rubric as a question; build the artifact incrementally; explain the "why" alongside the "what."
- **`draft`** — Targeted intake → first draft → refinement (5-10 min). Use when the user knows roughly what they want. Ask the 3-5 questions listed under "Draft-mode intake" below; produce a complete first draft; offer one round of refinement against the Rubric.
- **`polish`** — Critique-and-polish (2-5 min). Use when the user pastes an existing draft. Critique against every Rubric heuristic; rewrite to address gaps; explain what changed.

**When asking the user any question during this skill** (mode selection, intake, refinement, clarification): prefer the `AskUserQuestion` tool for any question with 2-4 reasonably discrete options (the user can always pick "Other" to free-text). Use plain chat only for questions that genuinely need a sentence or paragraph of free-form response. Multi-select questions are fine when the user could legitimately choose more than one.

## Rubric

1. **Name the three layers before you walk in.** Every hard conversation has three components — the "it" (the task or issue at hand), the "we" (the relationship and its unspoken dynamics), and the "I" (your self-doubt and internal critics). Identify all three before you open your mouth; unsaid things in each layer are what derail conversations.

2. **Fine-tune your filters, don't max them out.** Over-filtering is as dangerous as under-filtering. The goal is not to say everything on your mind — it's to name your observation constructively, so you can have an honest conversation and start working on a solution. If you're in a meeting where something isn't being talked about, the move is to name that meta-observation ("It feels like there's something we're not discussing").

3. **Share the feeling, not just the fact.** "We didn't hit our targets" conveys no gravity. "We didn't hit our targets, and I'm worried about the impact on our team and the business" tells people there is a problem that needs fixing. Feelings are a management tool because everyone understands them — they contextualize the stakes of what you're saying.

4. **Be measured, not just honest.** There is a difference between sharing a feeling and destabilizing a room. "I'm worried" is measured. "I'm freaking out" triggers panic and impedes action. The test: will saying this help the team move toward a solution, or freeze them in place?

5. **Stand next to the person, not across from them.** Criticism delivered face-to-face feels oppositional. The more powerful move is to stand beside the person and look at the same problem together. Replace "That presentation was terrible" with "What did you think of the presentation? I was disappointed in aspects of it and would love to hear what you thought." You're not softening the feedback — you're directing it at the work, not the person.

6. **Separate the person from the idea or task.** The conversation should be about the "it" but will feel like a judgment of the "we" or "I" unless you make the separation explicit. Ask yourself: am I commenting on what they did, or am I commenting on who they are? Rewrite accordingly before the conversation.

## Draft-mode intake

1. "What's the conversation, in one sentence?"
2. "What's the thing you've been not saying — and what feeling sits underneath it?"
3. "Who's the person, and what's at stake for them and for you?"
4. "What's the smallest, most specific version of the thing you actually need to say?"

## Artifact

**Format:** Markdown — short prep doc: the conversation in one line, the feeling to name, the specific statement, person-vs-idea separation, anticipated reactions, your follow-up.
**Default save path:** `./docs/management/hard-thing-prep-YYYY-MM-DD.md` in the user's cwd. Ask before saving; ask before overwriting if file exists.
**Template:** (No shared template — produce inline.)

## Source

*Scaling People* — Claire Hughes Johnson, Stripe Press 2023 — Chapter 1, "2. Say the thing you think you cannot say" (subsections: Share your feelings; Be measured; Separate the person from the idea or task).

Encoded heuristic: Every hard conversation has three unsaid layers — the "it" (the issue), the "we" (the relationship), and the "I" (your self-doubt). Good management means fine-tuning your filters, not maxing them out: name your observation constructively, share the feeling that gives it gravity, and keep the criticism oriented at the work rather than the person. The practical test is posture — are you facing the person across a divide, or standing next to them looking at the same thing together? Practice gives you the repetitions; each time you fall flat you learn how to reframe for next time.

(No shared template — produce inline.)
