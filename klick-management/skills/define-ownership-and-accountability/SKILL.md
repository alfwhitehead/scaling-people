---
name: define-ownership-and-accountability
description: Clarify ownership for a scope and the accountability mechanisms that go with it — decision rights, escalation paths, review forums. Use when "who owns X?" keeps being asked, after a reorg, or when accountability has eroded.
---

# Define Ownership and Accountability

This skill produces an ownership-and-accountability doc for a defined scope: who owns it, what decisions they can make alone vs with input vs by consensus, who escalates to whom, and what review forums hold the owner accountable. The book treats ownership without accountability mechanisms as ownership in name only.

Part of `org-foundations-and-planning` (Chapter 2 of *Scaling People*).

## Mode

Ask the user which mode to run in. Default to `draft` if they don't specify.

- **`teach`** — Socratic walk-through (10-20 min). Use when the user is new to this artifact or wants to internalize the framework. Walk through every heuristic in the Rubric as a question; build the artifact incrementally; explain the "why" alongside the "what."
- **`draft`** — Targeted intake → first draft → refinement (5-10 min). Use when the user knows roughly what they want. Ask the 3-5 questions listed under "Draft-mode intake" below; produce a complete first draft; offer one round of refinement against the Rubric.
- **`polish`** — Critique-and-polish (2-5 min). Use when the user pastes an existing draft. Critique against every Rubric heuristic; rewrite to address gaps; explain what changed.

## Rubric

1. **Every target needs an owner.** Each company or team target should have an owner who is ultimately responsible for tracking progress and escalating or unblocking if progress stalls. Even when a target has dependencies on other teams, someone must be accountable for it — shared responsibility without a named owner is the same as no owner.

2. **Tease apart ownership when dependencies are entangled.** When revenue or a shared target depends on multiple teams, assign ownership at the component level rather than letting it float. The book's example: separate "what's on the truck" revenue (owned by sales) from new-product revenue (owned by product). Forcing the separation surfaces hidden dependencies and removes the alibi of "I thought they were doing it."

3. **Unclear ownership is visible from outside.** Teams without clear ownership finger-point ("I thought sales was doing that"), fall behind on shared deliverables, and become political — people jockey to claim credit for the most important work and deflect blame when work isn't done. If you're hearing those patterns, ownership hasn't been assigned; assign it.

4. **Don't rely on the "wing and a prayer" method.** Putting work out to the team and hoping someone steps up is one of the worst management mistakes. Ownership must be explicit: named person, named scope, named deadline. The work that falls through is almost always the work that was "put out there" without an assigned owner.

5. **Accountability mechanisms are distinct from ownership.** Owning a target means being responsible for it; an accountability mechanism is the structure that makes that responsibility visible and reviewable. Mechanisms include: metrics dashboards, weekly metrics reviews, written snippets, QBRs, and meeting-based review forums. Without mechanisms, ownership exists only on paper.

6. **Match review cadence to how quickly the owner can affect the metric.** The frequency of accountability reviews should reflect how fast actions can move the number. Reviewing support response times weekly makes sense — a staffing change can show up in seven days. Reviewing a charter metric (e.g., total payment volume) weekly is demoralizing — the decisions that affect it take months. Set the cadence to make accountability actionable, not theatrical.

7. **Accountability mechanisms apply at every level.** Company-level targets need company-level owners and review forums (QBRs, all-hands metrics showcases). Team-level targets need team-level mechanisms (weekly metrics review, snippets, standing meetings). Individual-level goals need individual-level feedback loops (1:1s, performance reviews). The same structure should repeat at each layer — consistent mechanisms across the org reduce cognitive load and improve execution.

## Draft-mode intake

1. "What's the scope — a system, a metric, an initiative, a function?"
2. "Who is the proposed owner today (if anyone)?"
3. "What decisions does the owner currently make alone, with input, or by consensus?"
4. "What forum reviews this scope, and how often?"

## Artifact

**Format:** Markdown — ownership doc: scope, owner, decision rights matrix, escalation path, review forum and cadence.
**Default save path:** `./docs/management/ownership-YYYY-MM-DD.md` in the user's cwd. Ask before saving; ask before overwriting if file exists.
**Template:** (No shared template — produce inline.)

## Source

*Scaling People* — Claire Hughes Johnson, Stripe Press 2023 — Chapter 2, "The operating system > Ownership" and "Accountability mechanisms."

Encoded heuristic: Ownership is the act of assigning a named person to a named scope — from small action items to division-level outcomes. Without explicit ownership, teams finger-point, work falls through, and culture becomes political. The accountability mechanism is the structure that makes the owner's responsibility visible: dashboards, snippets, review meetings, QBRs. These are not the same thing as monitoring (dashboards with alerts). A mechanism is the cadenced human review loop — the regular moment where someone looks the owner in the eye and asks, "Are we on track? Why or why not?" Ownership without that loop is ownership in name only.

(No shared template — produce inline.)
