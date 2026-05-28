---
name: prep-qbr
description: Produce a quarterly business review (QBR) document per the book's outline — exec summary, narrative, metrics performance, cross-functional focus, goals progress, required appendices. Use ~2 weeks before the QBR meeting.
---

# Prep QBR

This skill produces a quarterly business review — the doc that gets read before the QBR meeting, with the goal of leaving the meeting with specific true statements (calibrated on progress, aligned on top risks and asks). The outline is opinionated; this skill respects it.

Part of `org-foundations-and-planning` (Chapter 2 of *Scaling People*).

## Mode

Use the `AskUserQuestion` tool to ask which mode to run in. Default to `draft` if the user skips or picks "Other" without specifying.

- **`teach`** — Socratic walk-through (10-20 min). Use when the user is new to this artifact or wants to internalize the framework. Walk through every heuristic in the Rubric as a question; build the artifact incrementally; explain the "why" alongside the "what."
- **`draft`** — Targeted intake → first draft → refinement (5-10 min). Use when the user knows roughly what they want. Ask the 3-5 questions listed under "Draft-mode intake" below; produce a complete first draft; offer one round of refinement against the Rubric.
- **`polish`** — Critique-and-polish (2-5 min). Use when the user pastes an existing draft. Critique against every Rubric heuristic; rewrite to address gaps; explain what changed.

**When asking the user any question during this skill** (mode selection, intake, refinement, clarification): prefer the `AskUserQuestion` tool for any question with 2-4 reasonably discrete options (the user can always pick "Other" to free-text). Use plain chat only for questions that genuinely need a sentence or paragraph of free-form response. Multi-select questions are fine when the user could legitimately choose more than one.

## Rubric

1. **Six true statements, not a progress report.** After a strong QBR, these six things should be demonstrably true: (a) leadership understands the team's charter and operating metrics with quarterly targets through year-end; (b) they understand which goals you executed on, which you missed, why, and what it will take to close the gap; (c) they can make an investment decision based on what the area is producing; (d) participants leave with clear mutual expectations for the coming periods; (e) potential obstacles through year-end are visible; and (f) leadership knows what the team needs to accelerate. If any of these are absent, the QBR is incomplete.

2. **Candor over polish.** The executive summary is a candid assessment, not a summary of successes. If you missed goals, the narrative should be skewed toward lowlights — why didn't you deliver? Even when goals were met, any areas that didn't go well must appear. Leadership wants honesty about what happened, not a polished story.

3. **Respect the six-page limit.** The QBR is a six-page narrative plus a required appendix. Brevity is structural, not optional. Executive summary: 250 words or fewer. Narrative: two pages maximum. Metrics performance: two pages maximum. Goals progress: one page maximum. When content exceeds the limit, cut — do not link out to supplementary material.

4. **Share the memo 24 hours in advance.** The meeting is a discussion informed by the document, not a presentation of it. Attendees read before or during a reading period at the start. Do not design the QBR to be "walked through" slide by slide — design it to be read.

5. **Show the two-year arc on metrics.** Metrics charts should cover roughly a two-year horizon, not just the current period. If targets were revised during planning, include both the original and revised targets. Embed relevant visualizations in the narrative where useful; move the rest to the metrics performance section.

6. **The narrative should be at least 50% forward-looking.** Balance discussion of current-quarter results with outlook for the rest of the year and longer-term strategic considerations. Most teams should spend at least half their discussion on strategy and trajectory, not just what happened.

7. **Appendix A is required, not optional.** Prior QBR action items (with status), operating expenses or product P&L, headcount by sub-team, and top user asks (with commitment status) are all required. Carry forward unresolved action items explicitly — don't let them disappear between QBRs.

8. **After the meeting: close the loop.** Share notes with all participants. Log action items in the tracker. Reflect on QBR quality. The value of a QBR compounds over time only if each one addresses what the prior one surfaced.

## Draft-mode intake

1. "What's the team/function and the quarter being reviewed?"
2. "Top 3 wins and top 3 misses this quarter?"
3. "What's the biggest open question you want stakeholders to engage on?"
4. "Top asks from users this quarter?"
5. "Any prior QBR action items still open?"

## Artifact

**Format:** Markdown — populated QBR per references/templates/qbr-outline.md.
**Default save path:** `./docs/management/qbr-YYYY-MM-DD.md` in the user's cwd. Ask before saving; ask before overwriting if file exists.
**Template:** Where the book provides a template, see `references/templates/qbr-outline.md`.

## Source

*Scaling People* — Claire Hughes Johnson, Stripe Press 2023 — Chapter 2, "Quarterly Business Reviews (QBRs)" (Exercises and templates, including QBR guidelines, Delivering a stellar QBR, Prepare/During/After, and QBR outline).

Encoded heuristic: The QBR is not a progress update — it is a structured accountability mechanism whose success is measured by whether six specific statements are true when the meeting ends: metrics are clear with quarterly targets, goal execution is explained honestly, investment ROI is legible, mutual expectations are set, obstacles are surfaced, and acceleration needs are visible. The format is strict: six pages maximum, 24 hours advance share, meeting as discussion not presentation. Candor is structural — if you missed goals, the document should be skewed toward explaining why, not toward highlighting what went well.

Where the book provides a template, see `references/templates/qbr-outline.md`.
