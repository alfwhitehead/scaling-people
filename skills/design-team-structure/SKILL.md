---
name: design-team-structure
description: Shape a team — teams vs working groups vs projects, layering, # reports, business leads. Use when forming a team, adding headcount, or rethinking reporting lines.
---

# Design Team Structure

This skill produces a team structure design: a written rationale for how a group should be organized (team, project, or working group), the horizontal/vertical orientation, the right number of direct reports, and a layering plan if needed. Use it when you are forming a new team, inheriting an existing one, adding a layer of management, or rethinking reporting lines in response to a strategic shift.

Part of `team-development` (Chapter 4 of *Scaling People*).

## Mode

Ask the user which mode to run in. Default to `draft` if they don't specify.

- **`teach`** — Socratic walk-through (10-20 min). Use when the user is new to this artifact or wants to internalize the framework. Walk through every heuristic in the Rubric as a question; build the artifact incrementally; explain the "why" alongside the "what."
- **`draft`** — Targeted intake → first draft → refinement (5-10 min). Use when the user knows roughly what they want. Ask the 3-5 questions listed under "Draft-mode intake" below; produce a complete first draft; offer one round of refinement against the Rubric.
- **`polish`** — Critique-and-polish (2-5 min). Use when the user pastes an existing draft. Critique against every Rubric heuristic; rewrite to address gaps; explain what changed.

## Rubric

1. **Structure follows strategy.** Before drawing any boxes, articulate the strategy. Ask: does this arrangement give the leader responsible for the most critical goal maximum solid-line leverage? If a product or region is make-or-break, that leader's org should reflect the priority, with dotted-line coverage of support functions where solid-line isn't warranted.

2. **Choose the right construct: team, project, or working group.** A team has a persistent mission (at least one year, full investment in norms and culture). A project is a subgroup with a clear task and defined end point (weeks to a few months). A working group is cross-functional, mission-oriented, and should dissolve in under three months — it needs a DRI, a defined scope, and an explicit spin-down plan. Using the wrong construct means investing at the wrong level.

3. **Avoid "I" structures and bottleneck spans.** A leader with one or two direct reports creates a fragile hierarchy. A leader with too many reports becomes a bottleneck and cannot do strategic work. Land in the middle: adequately flat, with enough bandwidth for unanticipated work that only the team leader can handle.

4. **Know where the hinge is.** In hybrid structures (multiple products or business lines), identify the pivot point between product focus and customer focus — this is the hinge. A product marketing team is a common hinge. As the business evolves, the hinge may need to move; build for that optionality.

5. **Be in your boat, not just in the org chart.** Think about who needs to be in your boat to win — regardless of solid or dotted lines. Obsessing over formal reporting structures when the right collaborators are clear is a distraction. Assemble the team that will help you win, then design the formal structure to enable that team.

6. **Introduce a new layer carefully, with narrative first.** When adding a layer of management, sketch the desired structure on paper without names first. Write the narrative explaining why the new structure addresses a strategic need and anticipate objections. Then consider who is scaling to the call — who has demonstrated capacity to take on more ownership — before attaching names to roles.

7. **Preserve optionality and normalize change.** Remind your team explicitly that the structure will evolve as strategy and talent change. Reexamine divisional and team structures at least once a year. Too much change is destabilizing; too little locks you into a structure that no longer fits the business.

## Draft-mode intake

1. "What is the strategy or goal this team structure needs to serve — in one sentence?"
2. "Is this a persistent mission (team), a time-bounded task (project), or a cross-functional alignment need (working group)?"
3. "How many direct reports do you currently have, and does that feel right for your strategic bandwidth?"
4. "Is there a new layer you need to introduce? If so, who is scaling to the call on your current team?"
5. "Are there any dotted-line or partner functions that need to be 'in your boat' even if they don't report to you?"

## Artifact

**Format:** Markdown — a one-paragraph structural rationale, a table or nested list of the proposed reporting structure, a section on who is in the "boat" (solid vs dotted), and a "future state / optionality" note.
**Default save path:** `./docs/management/team-structure-YYYY-MM-DD.md` in the user's cwd. Ask before saving; ask before overwriting if file exists.
**Template:** Inline — no shared template.

## Source

*Scaling People* — Claire Hughes Johnson, Stripe Press 2023 — Chapter 4, "Team structures."

Encoded heuristic: Organizational structure is a tool for executing strategy, not an end in itself. Always start with the strategy and ask which arrangement gives the most critical leaders the most leverage. The key distinctions are: teams (persistent mission, at least one year, invest heavily in norms), projects (subgroup, clear end point, weeks to months), and working groups (cross-functional, under three months, needs a DRI and a spin-down plan). Horizontal teams cut across verticals; vertical teams own a region, product, or business area. In hybrid multi-product structures, find the hinge — the pivot point between product and customer — and design accountability frameworks accordingly. Avoid "I" structures (one leader, one or two reports) and overloaded spans. When introducing a new layer, write the narrative before attaching names, and remind your team that further evolution is normal and expected.

Where the book provides a template, see `references/templates/team-charter.md` (for companion charter once structure is set).
