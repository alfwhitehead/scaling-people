---
name: run-performance-review
description: Run the formal review process — peer reviews, self-assessment, manager review, calibration. Use during review season or when standing up a review process from scratch.
---

# Run Performance Review

This skill guides you through the formal performance review cycle: gathering peer feedback, reading the employee's self-assessment, writing your own manager review, navigating calibration, and delivering the review in a conversation that is forward-looking rather than a readout. Done well, the review documents coaching conversations you've already had and marks a formal moment of recognition or direction-setting.

Part of `feedback-and-performance` (Chapter 5 of *Scaling People*).

## Mode

Use the `AskUserQuestion` tool to ask which mode to run in. Default to `draft` if the user skips or picks "Other" without specifying.

- **`teach`** — Socratic walk-through (10-20 min). Use when the user is new to this artifact or wants to internalize the framework. Walk through every heuristic in the Rubric as a question; build the artifact incrementally; explain the "why" alongside the "what."
- **`draft`** — Targeted intake → first draft → refinement (5-10 min). Use when the user knows roughly what they want. Ask the 3-5 questions listed under "Draft-mode intake" below; produce a complete first draft; offer one round of refinement against the Rubric.
- **`polish`** — Critique-and-polish (2-5 min). Use when the user pastes an existing draft. Critique against every Rubric heuristic; rewrite to address gaps; explain what changed.

**When asking the user any question during this skill** (mode selection, intake, refinement, clarification): prefer the `AskUserQuestion` tool for any question with 2-4 reasonably discrete options (the user can always pick "Other" to free-text). Use plain chat only for questions that genuinely need a sentence or paragraph of free-form response. Multi-select questions are fine when the user could legitimately choose more than one.

## Rubric

1. **No surprises.** If you've managed well, the review documents conversations you've already had. The formal process should feel like a confirmation, not a revelation. If the employee is surprised by what's in the review, you have a feedback gap to close, not a review problem to fix.

2. **Peer reviews give you coverage and credibility.** Have the employee select three to five peers; you should agree the list is representative. Peer prompts should ask about observed strengths, one development area, and how they embody the team's operating principles. Read this input before writing your own review; let it inform — and sometimes correct — your initial assessment.

3. **Read the self-assessment carefully.** The employee's self-summary reveals their self-awareness and how closely their perception aligns with yours. A self-assessment that significantly over- or under-estimates their impact is itself a coaching signal worth addressing in the review conversation.

4. **Write the manager review after reading peer and self input.** Your review covers: a summary of top contributions, one or two demonstrated strengths with examples, at least one development area with ideas for improvement, your performance designation, and a promotion recommendation if applicable. For each impact area, name the project, the employee's role, key collaborators, and whether expectations were met.

5. **Write the designation-anchoring sentences.** Complete both: "In one sentence, why did I not choose a higher designation?" and "In one sentence, why did I not choose a lower designation?" These force you to articulate the boundary and will help you hold your position in calibration.

6. **Calibration is for alignment, not politics.** Your job in calibration is to advocate for your team members with evidence and to remain open to adjusting designations that aren't consistent with others at the same level. Come prepared: know your outliers, understand the rubric, and be ready to explain — or reconsider — any designations that seem inconsistent with the group. Guard against the lowest common denominator; the hardest conversations should be at the "meets → exceeds" and "exceeds → greatly exceeds" lines.

7. **Deliver the review forward-looking.** Send the review 24 hours in advance. Start the meeting by asking what the employee thought of the feedback. Spend about 10 minutes on the review itself; spend the remaining 40 minutes on "Do you feel set up for success?" and what they should work on or take on next. If they push back on a point, acknowledge their perspective and reframe toward next time rather than re-arguing the past.

## Draft-mode intake

1. "Who is the review for, and what review period does it cover?"
2. "Have you read the peer feedback and self-assessment? What stands out — alignments and gaps?"
3. "What are this person's 2-3 biggest impact areas this period?"
4. "What are their top 1-2 strengths and their most important development area?"
5. "What's your proposed designation, and are you recommending them for promotion? Why or why not?"

## Artifact

**Format:** Markdown — a complete manager review document following the book's template (name, level, designation, promotion, impact areas, strengths, development areas, promotion proposal).
**Default save path:** `./docs/management/performance-review-YYYY-MM-DD.md` in the user's cwd. Ask before saving; ask before overwriting if file exists.
**Template:** See `references/templates/performance-review.md`.

## Source

*Scaling People* — Claire Hughes Johnson, Stripe Press 2023 — Chapter 5, "The formal review process" (subsections: Minimum viable people processes, Performance feedback — Peer reviews / Self-assessment / Manager review, Calibration) and sidebar "A manager's advice for delivering performance reviews."

Encoded heuristic: The manager plays a critical role in making sure the process functions as it should. If you've managed well, there are no surprises — you're merely documenting the conversations you've already had with your direct report. The peer feedback and employee self-assessment can be submitted simultaneously. The manager review should be written after the manager has read both. Calibration is a check on managers who are too lenient or too tough; the goal is alignment across similar roles and levels, not a political exercise. When delivering the review, spend relatively little time talking through the document and more time focused on how the person should act on the feedback in the upcoming period.

Where the book provides a template, see `references/templates/performance-review.md`.
