---
name: plan-reorganization
description: Run the three-phase reorg — decide structure (one month) → get buy-in (one to two weeks) → communicate (one to two days). Use when restructuring is on the table.
---

# Plan Reorganization

This skill produces a reorganization plan: a written rationale for why the reorg is necessary, the proposed new structure, a phase-by-phase execution timeline, a stakeholder communications plan, and the key messages for each affected individual. Use it when a strategic shift or talent change is making the current structure a drag on execution.

Part of `team-development` (Chapter 4 of *Scaling People*).

## Mode

Ask the user which mode to run in. Default to `draft` if they don't specify.

- **`teach`** — Socratic walk-through (10-20 min). Use when the user is new to this artifact or wants to internalize the framework. Walk through every heuristic in the Rubric as a question; build the artifact incrementally; explain the "why" alongside the "what."
- **`draft`** — Targeted intake → first draft → refinement (5-10 min). Use when the user knows roughly what they want. Ask the 3-5 questions listed under "Draft-mode intake" below; produce a complete first draft; offer one round of refinement against the Rubric.
- **`polish`** — Critique-and-polish (2-5 min). Use when the user pastes an existing draft. Critique against every Rubric heuristic; rewrite to address gaps; explain what changed.

## Rubric

1. **Name the trigger honestly.** There are two valid reorg triggers: your structure no longer matches your strategy, or you have a talent issue. A third — an underperforming team — is frequently misused. Ask yourself: is it a structural misalignment, or is it a talent problem wearing a structural costume? Don't use a reorg to mask a coaching or performance issue you haven't addressed directly.

2. **Don't leave the ice cream on the counter for too long.** Once you begin including people beyond your HR partner and your own manager, the ice cream is out of the freezer. Misinformation spreads quickly and creates instability that is hard to undo. Move at deliberate speed in Phase 0; move quickly once Phase 1 begins.

3. **Never restructure around a single person.** Restructuring your team to retain or reward one individual — even a high performer — signals to the rest of the team that you optimize for individuals, not strategy. If a grouping doesn't make organizational sense, it will set that person up to fail. Exceptions exist (bridging toward a future state with incomplete headcount), but they must be explicitly named as interim.

4. **Phase 0 (one month): design with a tight circle.** Keep this phase to you, your manager, HR, and the peers who may be affected. Account for every person in the new structure. Do not include direct reports yet. The output is an agreed-upon design, not just a sketch.

5. **Phase 1 (one to two weeks): earn buy-in from those who will carry the change.** Share the plan with each affected manager or leader individually. Give them the why first — they need to believe it enough to explain it to others. Plan for two to three conversations per person; the first is rarely the last. Stay focused on the why; be firm on the decision while remaining open on undecided details. Don't rethink the plan because someone overreacts in the first conversation.

6. **Phase 2 (one to two days): communicate fast and completely.** Tell the most-affected people (those getting a new manager) first, then announce to the wider group within a day. Once the announcement is made, move immediately into new operating rhythms. Get the ice cream back in the freezer.

7. **Reorgs are signs of dynamism, not distress.** Set the expectation that structural change is normal in a high-growth environment — and reinforce that expectation in how you communicate the change. Your mindset permeates those around you. Treat the reorg as an opportunity for leaders to take on new responsibility and step up; the ones who do will define the new team.

## Draft-mode intake

1. "What is triggering this reorg — a strategy change, a talent change, or both?"
2. "Who are the affected individuals, and what is each person's likely first reaction to the change?"
3. "Is anyone moving into a reduced-scope role? What is the argument for why this is right for them and for the business?"
4. "What is the absolute minimum circle of people who need to be involved before Phase 1 begins?"
5. "What is the planned announcement timeline, and who tells whom, in what order?"

## Artifact

**Format:** Markdown — a trigger summary, a proposed org chart (described in prose or a list), a phase timeline table (Phase 0 / 1 / 2 with dates and owners), a stakeholder map with per-person talking points, and a draft announcement message.
**Default save path:** `./docs/management/reorg-plan-YYYY-MM-DD.md` in the user's cwd. Ask before saving; ask before overwriting if file exists.
**Template:** Inline — no shared template.

## Source

*Scaling People* — Claire Hughes Johnson, Stripe Press 2023 — Chapter 4, "Team changes and restructuring."

Encoded heuristic: Reorgs have two valid triggers — structure no longer matches strategy, or there is a talent issue — and one common misuse: masking a talent problem you haven't addressed. Once you start involving people beyond HR and your manager, the clock starts. Phase 0 (one month) is a small-circle design process with every person accounted for. Phase 1 (one to two weeks) is individual conversations with the managers who must carry the change — expect two to three conversations per person, stay firm on the why, don't rethink the plan on first pushback. Phase 2 (one to two days) is the announcement, starting with the most affected and reaching the full group within a day, followed immediately by new operating rhythms. Never structure around a single individual. Treat the reorg as a signal of dynamism and growth, not organizational distress.

Where the book provides a template, see `references/templates/team-charter.md` (for documenting the new team's mandate once the structure is finalized).
