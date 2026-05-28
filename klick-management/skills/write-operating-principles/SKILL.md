---
name: write-operating-principles
description: Draft a set of operating principles in Stripe-style three-category structure (how we work / who we are / and leaders). Use when the team is large enough that decisions need a shared sense of "how we do things here" without you in every conversation.
---

# Write Operating Principles

This skill produces a set of operating principles — short, memorable statements that describe how the team works, who its members are, and what's expected of its leaders. Principles complement (don't replace) mission and values: mission says why, principles say how.

Part of `org-foundations-and-planning` (Chapter 2 of *Scaling People*).

## Mode

Ask the user which mode to run in. Default to `draft` if they don't specify.

- **`teach`** — Socratic walk-through (10-20 min). Use when the user is new to this artifact or wants to internalize the framework. Walk through every heuristic in the Rubric as a question; build the artifact incrementally; explain the "why" alongside the "what."
- **`draft`** — Targeted intake → first draft → refinement (5-10 min). Use when the user knows roughly what they want. Ask the 3-5 questions listed under "Draft-mode intake" below; produce a complete first draft; offer one round of refinement against the Rubric.
- **`polish`** — Critique-and-polish (2-5 min). Use when the user pastes an existing draft. Critique against every Rubric heuristic; rewrite to address gaps; explain what changed.

## Rubric

1. **Authentic, not aspirational fiction.** Principles must feel true to how the company already operates at its best — not a description of a company you wish you were. The most common failure mode is principles so idealistic they have no connection to daily reality. If a principle requires employees to mentally translate it before applying it, it will not be used. The test: if a new hire read these on day one, would they recognize them as true six months later?

2. **Relevant, believable, enduring, and deliverable.** Apply these four brand-quality filters to each principle. Relevant: does it address something the team actually wrestles with? Believable: does the company already demonstrate it, at least some of the time? Enduring: will it still be true in five years? Deliverable: can a manager hire, develop, and reward against it?

3. **Organized into three categories: How we work / Who we are / And leaders.** The Stripe structure separates behavioral norms (how we work), character traits the org selects and develops (who we are), and explicit expectations for people with formal authority (and leaders). This split matters: it prevents leaders from hiding behind individual-contributor principles and makes leadership accountability visible and nameable.

4. **Rooted in notable moments from company history.** The strongest principles are distilled from moments that actually happened — major decisions, product choices, rallying crises — not from what the company hoped would happen. When drafting, ask: what was true in those moments? What belief system prevailed? Use those examples as the raw material. Principles drafted from the desk without evidence tend to be generic.

5. **Drafted with broad input, finalized by the leader.** At Stripe, early drafts were written by employees — a mix of espoused beliefs and embedded assumptions — then reviewed and rewritten by the founder before circulating for comment. The process matters: broad input surfaces the actual culture; leader revision ensures the principles are owned, not just aggregated.

6. **Revisited regularly to stay authentic and relevant.** Principles are not set-and-forget. Revisit every year or two and ask: do we still hire against these? Do we still reward against these? Are there new behaviors we have developed that these don't capture? A principle that no longer describes how the company actually operates should be updated or retired.

7. **Expressed in how the company hires, rewards, and leads — not just documented.** Principles that live only in a document are decorative. The measure of whether principles are real is whether they show up in hiring criteria, performance conversations, and promotion decisions. If they don't, the company has espoused values, not operating principles.

## Draft-mode intake

1. "What's the team or org?"
2. "What do you most want people to do more of?"
3. "What do you most want people to do less of?"
4. "What does a great leader on this team look like?"
5. "Any existing values or principles to extend or reconcile with?"

## Artifact

**Format:** Markdown — three sections (How we work / Who we are / And leaders), each with 4-6 principles. Each principle: a short headline + 2-4 sentence elaboration with example behaviors.
**Default save path:** `./docs/management/operating-principles-YYYY-MM-DD.md` in the user's cwd. Ask before saving; ask before overwriting if file exists.
**Template:** Where the book provides a template, see references/templates/operating-principles-example.md.

## Source

*Scaling People* — Claire Hughes Johnson, Stripe Press 2023 — Chapter 2, "Founding documents > Principles" (and Exercises and templates > Stripe's Operating Principles).

Encoded heuristic: Operating principles establish the culture that enables the team to work toward its goals — they are the "how" to the mission's "why." The critical requirement is authenticity: principles must reflect how the company actually operates at its best, not a fantasy version of it. The Stripe structure separates them into three categories — how we work, who we are, and what leaders specifically are expected to do — which keeps leadership accountability explicit. Draft from real company history (decisions that revealed what the company actually believes), seek input broadly, and then test each principle against whether you would hire, reward, and promote differently because of it.
