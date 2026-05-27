---
name: plan-strategic-and-financial
description: Produce the annual strategic and financial planning narrative for a team or function — what we're doing, why, the bets we're making, and the money/people that requires. Use during planning season or when handing off to a new finance partner.
---

# Plan Strategic and Financial

This skill produces the annual strategic + financial planning narrative — the document that connects the team's strategy to the resources (people, money, time) it needs. Use it during planning season; it's the bridge between the team charter and the year's OKRs.

Part of `org-foundations-and-planning` (Chapter 2 of *Scaling People*).

## Mode

Ask the user which mode to run in. Default to `draft` if they don't specify.

- **`teach`** — Socratic walk-through (10-20 min). Use when the user is new to this artifact or wants to internalize the framework. Walk through every heuristic in the Rubric as a question; build the artifact incrementally; explain the "why" alongside the "what."
- **`draft`** — Targeted intake → first draft → refinement (5-10 min). Use when the user knows roughly what they want. Ask the 3-5 questions listed under "Draft-mode intake" below; produce a complete first draft; offer one round of refinement against the Rubric.
- **`polish`** — Critique-and-polish (2-5 min). Use when the user pastes an existing draft. Critique against every Rubric heuristic; rewrite to address gaps; explain what changed.

## Rubric

1. **A strategy should hurt.** The trade-offs you make — where you put time and money and where you do not — should feel painful and disappointing to someone, either internally or to customers. A plan that prioritizes everything is not a strategy; it is the peanut-butter problem in writing.

2. **Pair a multi-year financial model with a short-term plan.** Produce two artifacts together: a financial model of the next three or more years that captures what must be true to hit those numbers, and a shorter plan answering "What are we getting done in the next 6-12 months, and what does the P&L look like by December?" Each document points to the other; neither is complete alone.

3. **Link the plan to long-term goals and the mission.** The financial outcomes are a means to create discipline and measurement, not the reason the team exists. Every plan narrative should name which long-term strategic themes it is advancing. If you can strip out the mission reference and the plan still reads the same, the connection isn't made.

4. **Distinguish maturity stages within the plan.** Not all parts of a business are at the same horizon. Mature efforts need clear metrics and short-term goals. Emerging efforts may have a goal as simple as "launch and test product-market fit." Treating all lines of work as the same stage produces the wrong targets and the wrong resource levels.

5. **Reserve space for foundational and existential work.** Leadership must explicitly protect investment in work that no team will naturally prioritize — security, technical debt, people development, internal tooling. These should appear as named line items in the plan, not as a hope that someone will get to them. If a top-down ask will consume meaningful team capacity, the plan should account for it.

6. **Build the planning-ahead muscle, not just the plan.** The real value of annual planning is not the document — it is forcing teams to step back, state long-term goals, and estimate the resources those goals require. Even if the forecast turns out to be wrong, the discipline of submitting a plan and measuring performance against it changes how leaders think about priorities.

## Draft-mode intake

1. "What's the planning period and the team scope?"
2. "What are the 2-4 strategic bets you're proposing for the period?"
3. "What's your headcount and budget today?"
4. "What changes are you asking for, and what would each unlock?"

## Artifact

**Format:** Markdown — narrative (1-2 pages) + headcount/budget tables.
**Default save path:** `./docs/management/strategic-financial-plan-YYYY-MM-DD.md` in the user's cwd. Ask before saving; ask before overwriting if file exists.
**Template:** (No shared template — produce inline.)

## Source

*Scaling People* — Claire Hughes Johnson, Stripe Press 2023 — Chapter 2, "The operating system > Strategic and financial planning."

Encoded heuristic: Strategic and financial planning connects a team's mission and long-term goals to the concrete resources — people, budget, time — needed to execute. The book teaches two inseparable artifacts: a multi-year financial model that forces strategic conversation, and a short-term operating plan that answers what gets done this year. The central test of any plan is whether it makes real trade-offs: if the plan prioritizes everything, it is the peanut-butter problem in writing. Plans should distinguish between horizon-1 (mature/core), horizon-2 (emerging), and horizon-3 (investment) efforts, and must explicitly protect foundational work — security, debt, development — that no team will self-fund.

(No shared template — produce inline.)
