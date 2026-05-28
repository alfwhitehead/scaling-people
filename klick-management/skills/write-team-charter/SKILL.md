---
name: write-team-charter
description: Produce a team charter covering mission, vision, customers, metrics, strategic importance, major risks, and provided/dependent interfaces. Use when forming a new team, taking over an existing team, or when cross-team friction suggests responsibilities aren't clear.
---

# Write Team Charter

This skill produces a team charter — the one-document answer to 'what is this team, who does it serve, what does it own, and what does it depend on?' Use it to force the foundational questions in one pass and to give the rest of the org a single artifact to react to.

Part of `org-foundations-and-planning` (Chapter 2 of *Scaling People*).

## Mode

Use the `AskUserQuestion` tool to ask which mode to run in. Default to `draft` if the user skips or picks "Other" without specifying.

- **`teach`** — Socratic walk-through (10-20 min). Use when the user is new to this artifact or wants to internalize the framework. Walk through every heuristic in the Rubric as a question; build the artifact incrementally; explain the "why" alongside the "what."
- **`draft`** — Targeted intake → first draft → refinement (5-10 min). Use when the user knows roughly what they want. Ask the 3-5 questions listed under "Draft-mode intake" below; produce a complete first draft; offer one round of refinement against the Rubric.
- **`polish`** — Critique-and-polish (2-5 min). Use when the user pastes an existing draft. Critique against every Rubric heuristic; rewrite to address gaps; explain what changed.

**When asking the user any question during this skill** (mode selection, intake, refinement, clarification): prefer the `AskUserQuestion` tool for any question with 2-4 reasonably discrete options (the user can always pick "Other" to free-text). Use plain chat only for questions that genuinely need a sentence or paragraph of free-form response. Multi-select questions are fine when the user could legitimately choose more than one.

## Rubric

1. **Mission: one or two sentences, same rules as a team mission statement.** The charter's mission field is the team's mission — short, specific, unique to this team. It should roll up to the division's mission. If you can't write one sentence that would tell a new employee what this team exists to do, you don't yet have clarity on the team's purpose.

2. **Vision: what success looks like in the long run.** The vision goes beyond the mission to describe the future state the team is building toward — the condition the org is in when this team has done its job well. It is longer than the mission (a paragraph is fine) and more concrete: name the user experience, the internal trust level, or the business outcome that marks success.

3. **Customers: who the team serves, both internal and external.** Name the specific user groups and internal partners who depend on this team's work. Be precise: "all dashboard users" is less useful than "merchant accounts managing access controls." This field forces the team to think about whose experience they are accountable for.

4. **Metrics: two or three measurable outcomes with target values.** Metrics in the charter are the team's charter metrics — the long-term measures that show whether the team is doing its job, distinct from quarterly OKR targets. Each metric should name what it measures, why that measurement matters, and a target value or direction. Resist adding more than three; too many means none of them are truly primary.

5. **Strategic importance: why this team's work matters to the company.** The strategic importance field explains the downstream effect of the team's work on company goals, user trust, revenue, or risk. It is the answer to "why does this team exist at this level of investment?" — useful when new employees join, when leadership asks whether to grow or shrink the team, or when the team needs to communicate its value cross-functionally.

6. **Major risks: what could prevent the team from delivering.** List the realistic threats to the team's ability to do its work — not generic risks, but the specific ones. In the book's security team example: being pulled into compliance work, a major breach, death by a thousand one-off enterprise requests, tech debt. Naming risks in the charter makes them discussable and allows leadership to help mitigate them proactively.

7. **Provided and dependent interfaces define your contract with the rest of the org.** Provided interfaces are what the team owns and makes available to others. Dependent interfaces are what the team relies on from others. Together, they map the team's organizational surface area and make dependencies explicit. When a team publishes both, cross-team friction decreases because everyone can see where one team's work ends and another's begins.

8. **Make it discoverable and link to living metrics.** The charter should live on the team's intranet page, not in a document that gets emailed and forgotten. If possible, link out to a live dashboard of the charter's metrics. New employees should be able to find the charter, understand the team's role, and know how to work with the team — all from a single page.

## Draft-mode intake

1. "What's the team and how many people?"
2. "Who are your primary internal/external customers?"
3. "What top 2-3 metrics will you be measured on?"
4. "What does the rest of the org most often misunderstand about this team?"
5. "What teams do you most depend on, and which depend most on you?"

## Artifact

**Format:** Markdown — populated charter template per references/templates/team-charter.md.
**Default save path:** `./docs/management/team-charter-YYYY-MM-DD.md` in the user's cwd. Ask before saving; ask before overwriting if file exists.
**Template:** Where the book provides a template, see references/templates/team-charter.md.

## Source

*Scaling People* — Claire Hughes Johnson, Stripe Press 2023 — Chapter 2, "Founding documents > Team charters" (and Exercises and templates > Team Charter).

Encoded heuristic: A team charter is a one-page document that answers the org's most basic question about a team: why does it exist, who does it serve, what does it own, and what does it depend on? The book's eight-field structure — mission, vision, customers, metrics, strategic importance, major risks, provided interfaces, dependent interfaces — forces the foundational questions in a single pass. The provided and dependent interface fields are especially important as organizations scale: they turn implicit dependencies into explicit contracts, reducing the friction that comes from teams not knowing where their responsibilities end and another team's begin. The charter should live somewhere discoverable and link to live metrics, not sit in a drawer.
