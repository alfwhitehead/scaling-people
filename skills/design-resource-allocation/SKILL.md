---
name: design-resource-allocation
description: Allocate FTE and budget across initiatives and communicate the expectations that come with the allocation. Use during planning, after a reorg, or when teams keep asking "is this funded?"
---

# Design Resource Allocation

This skill produces a resource allocation — FTE and budget split across initiatives — plus the expectations that go with it. Use it when the strategic plan is set and you need to translate it into who works on what, how much, and with what success conditions.

Part of `org-foundations-and-planning` (Chapter 2 of *Scaling People*).

## Mode

Ask the user which mode to run in. Default to `draft` if they don't specify.

- **`teach`** — Socratic walk-through (10-20 min). Use when the user is new to this artifact or wants to internalize the framework. Walk through every heuristic in the Rubric as a question; build the artifact incrementally; explain the "why" alongside the "what."
- **`draft`** — Targeted intake → first draft → refinement (5-10 min). Use when the user knows roughly what they want. Ask the 3-5 questions listed under "Draft-mode intake" below; produce a complete first draft; offer one round of refinement against the Rubric.
- **`polish`** — Critique-and-polish (2-5 min). Use when the user pastes an existing draft. Critique against every Rubric heuristic; rewrite to address gaps; explain what changed.

## Rubric

1. **Don't starve the cash cow in pursuit of Horizons 2 and 3.** Emerging and exploratory investments are tempting to over-fund. Your current core business — Horizon 1 — invariably needs more people and money to maintain growth than you expect. Check that your allocation doesn't assume the mature business will hold without investment.

2. **Use ratios as a gut check, not a formula.** Function ratios (e.g., 10 engineers to 1 PM, 1 HRBP per 250 employees) are a useful sanity check, but they don't account for your business model, efficiency gains over time, or the fact that resources should flow toward impact, not org size. Apply ratios as a cross-check after making an impact-based case, not as the primary allocation method.

3. **Allocate on cycles shorter than a year, and hold a reserve.** Allocating headcount on six-month cycles or reserving some headcount at the company level gives you optionality to shift toward emerging priorities without triggering an annual reallocation fight. It also makes the process feel less like a winner-takes-all event, which reduces political behavior.

4. **Invest in developer productivity — and resist deferring it.** A recurring trap at growing companies is under-investing in engineering infrastructure, shared tooling, and developer experience because the ROI is indirect. The book cites a benchmark of 5-8 percent of engineers dedicated exclusively to productivity; Stripe chose to exceed that benchmark in the interest of velocity. Treating productivity investment as a luxury deferred until after product work is done is a mistake that compounds.

5. **Set expectations as a leadership team, not just as individuals.** Before the allocation conversation, remind leaders what you expect from them: keep the company interest foremost, not the team interest; collaborate to find efficiency opportunities across teams; show up as owners of the whole, not advocates for their slice. Restating this norm at every contentious resource decision is not redundant — it is effective.

6. **Reward operational efficiency publicly.** Getting more resources is perceived as recognition. Counteract that dynamic by celebrating managers who come in under budget, reduce the resources they need, or give back headcount allocation. If efficiency is only punished (by losing the headcount permanently), leaders will hoard.

## Draft-mode intake

1. "What's the total FTE and budget under your control for the period?"
2. "What's the proposed split across initiatives?"
3. "What's the expected outcome per initiative?"
4. "What's the under-invested area you're tempted to defer (e.g., productivity, infra) — and why?"

## Artifact

**Format:** Markdown — allocation table (initiative / FTE / budget / outcome / owner) + a short "expectations" section.
**Default save path:** `./docs/management/resource-allocation-YYYY-MM-DD.md` in the user's cwd. Ask before saving; ask before overwriting if file exists.
**Template:** (No shared template — produce inline.)

## Source

*Scaling People* — Claire Hughes Johnson, Stripe Press 2023 — Chapter 2, "The operating system > Resource allocation" (incl. "Setting expectations around resource allocation" and "Investing in developer productivity" sidebars).

Encoded heuristic: Resource allocation is the art of giving early-stage efforts enough investment to demonstrate success while simultaneously driving operational efficiency in mature businesses. The book warns against three recurring mistakes: using ratio-based headcount planning as a primary method (it rewards org size over impact), under-investing in productivity and infrastructure (it compounds over time into Phase II and III crises), and allowing the annual allocation cycle to become a political negotiation between individual advocates. The antidote to all three is the same: use objective measures, allocate on shorter cycles with a reserve, reset leadership expectations before every contentious conversation, and visibly reward efficiency over acquisition.

(No shared template — produce inline.)
