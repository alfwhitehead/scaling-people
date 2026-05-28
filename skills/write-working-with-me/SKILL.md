---
name: write-working-with-me
description: Produce the "working with me" doc your team, peers, and manager read to understand how you operate. Use after a self-awareness assessment, when joining a new team or taking on a new manager, or when feedback suggests your team is misreading your style.
---

# Write Working-With-Me

This skill produces a "working with me" doc — the short, candid document you share with reports, peers, and your own manager so they don't have to learn how to work with you by trial and error. It's the externalized output of self-awareness work, written for the reader.

Part of `operating-principles` (Chapter 1 of *Scaling People*).

## Mode

Ask the user which mode to run in. Default to `draft` if they don't specify.

- **`teach`** — Socratic walk-through (10-20 min). Use when the user is new to this artifact or wants to internalize the framework. Walk through every heuristic in the Rubric as a question; build the artifact incrementally; explain the "why" alongside the "what."
- **`draft`** — Targeted intake → first draft → refinement (5-10 min). Use when the user knows roughly what they want. Ask the 3-5 questions listed under "Draft-mode intake" below; produce a complete first draft; offer one round of refinement against the Rubric.
- **`polish`** — Critique-and-polish (2-5 min). Use when the user pastes an existing draft. Critique against every Rubric heuristic; rewrite to address gaps; explain what changed.

## Rubric

1. **Write for the reader, not for yourself.** A working-with-me doc is not a performance review self-assessment — it's an operating manual for the people who have to work with you every day. Draft each section with the question: what does someone need to know about me to stop guessing and start working?

2. **Cover the operational structure first, then the style.** The reader needs to know your meeting cadence, your 1:1 norms, how you want to be looped in, and what your communication channels mean before they care about your personality. Lead with operating approach, then management style.

3. **Name your watch-outs explicitly.** The most useful entries are the ones that say "here is how I tend to go wrong, and here is what you should do about it." Claire's document flags that she can be slow to decide when she needs to talk things through, and that she says yes too often. Honest watch-outs earn more trust than a polished strengths list.

4. **Declare your communication preferences with specificity.** Don't write "I prefer clear communication." Instead: what does each channel mean to you (email, chat, in-person), what response time should people expect, when is it okay to interrupt, and what does "FYI" mean versus "I need a response"?

5. **Include the personal signal that sets the tone.** Claire's executive assistant's note — "you forgot to mention that you like good craic!" — ended up in every version of the document. The personal human element tells people what kind of environment you're trying to create, not just how to file a meeting invite.

6. **Share it early, invite challenges, and revise it.** The document is most useful in your first meeting with a new report. Invite the person to add to it, challenge it, and create their own. A working-with-me that everyone has — manager and reports both — accelerates relationships across the whole team.

7. **Treat it as a living document.** Your preferences, style, and operating context change. Schedule a review (quarterly or after a major role change) and update sections that no longer reflect how you actually work.

## Draft-mode intake

1. "Have you done a self-awareness assessment? (If not, run `self-awareness-assessment` first.)"
2. "Who's the audience — your team, your peers, your manager, or all three?"
3. "What's the one thing about you people consistently get wrong on first interaction?"
4. "What's one strong preference you want to declare up front (e.g., 'I prefer written context before meetings')?"
5. "What's the most useful piece of feedback someone could give you about working with you?"

## Artifact

**Format:** Markdown — populated working-with-me doc per `references/templates/working-with-me.md`. Typically 1-2 pages, conversational, first-person.
**Default save path:** `./docs/management/working-with-me-YYYY-MM-DD.md` in the user's cwd. Ask before saving; ask before overwriting if file exists.
**Template:** Where the book provides a template, see `references/templates/working-with-me.md`.

## Source

*Scaling People* — Claire Hughes Johnson, Stripe Press 2023 — Chapter 1 (foundation) and Chapter 3 Exercises and templates: "Working with Claire," "Working with Me Template."

Encoded heuristic: The "working with me" document externalizes self-awareness for the people who work with you — it's not a self-assessment, it's an operating manual written for the reader. The book's worked example ("Working with Claire") structures it around operating approach, management style, communication preferences, and a personal tone-setter. The template formalizes five sections: role and goals, about me, operating approach, management style, and supporting your team. Share it in your first 1:1 with a new report; invite them to write their own. Revise it as your role and context change.

Where the book provides a template, see `references/templates/working-with-me.md`.
