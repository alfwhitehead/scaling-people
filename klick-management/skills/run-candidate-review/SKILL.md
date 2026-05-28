---
name: run-candidate-review
description: Facilitate the candidate-review decision-making forum — reviewing scorecards, verifying rubric use, and reaching a hire/no-hire and level decision. Use after a candidate's loop closes and before extending an offer.
---

# Run Candidate Review

This skill produces a facilitated candidate review (CR) session and a documented decision — with rationale — for a hire/no-hire outcome and a proposed job level. Use it when a candidate has completed their interview loop and the team needs a structured, bias-aware process to reach a final decision. It is especially valuable for high-volume roles (where a standing CR panel handles decisions independently of any single hiring manager) and for any role where the interview committee includes disagreement or newness.

Part of `hiring` (Chapter 3 of *Scaling People*).

## Mode

Use the `AskUserQuestion` tool to ask which mode to run in. Default to `draft` if the user skips or picks "Other" without specifying.

- **`teach`** — Socratic walk-through (10-20 min). Use when the user is new to this artifact or wants to internalize the framework. Walk through every heuristic in the Rubric as a question; build the artifact incrementally; explain the "why" alongside the "what."
- **`draft`** — Targeted intake → first draft → refinement (5-10 min). Use when the user knows roughly what they want. Ask the 3-5 questions listed under "Draft-mode intake" below; produce a complete first draft; offer one round of refinement against the Rubric.
- **`polish`** — Critique-and-polish (2-5 min). Use when the user pastes an existing draft. Critique against every Rubric heuristic; rewrite to address gaps; explain what changed.

**When asking the user any question during this skill** (mode selection, intake, refinement, clarification): prefer the `AskUserQuestion` tool for any question with 2-4 reasonably discrete options (the user can always pick "Other" to free-text). Use plain chat only for questions that genuinely need a sentence or paragraph of free-form response. Multi-select questions are fine when the user could legitimately choose more than one.

## Rubric

1. **The mission of candidate review is consistency, efficiency, and bias control.** A good CR process applies the same decision framework to every candidate so that hiring outcomes are driven by rubric performance — not by who advocates loudest, which team is most desperate to fill a seat, or which candidate interviewed on a particularly good day.

2. **Start with the objective layer: the hiring committee scorecard.** Review the standardized rubric scores for each interview first. These are the most objective measures. A completed hiring committee scorecard is a prerequisite for CR — do not review packets that lack one.

3. **Then read the subjective layer: the hiring manager rationale.** The rationale explains how the committee reached its conclusion, especially where the outcome differs from the raw rubric scores. Flag inconsistencies between scorecard outcomes and the stated rationale — not because inconsistencies are inherently wrong, but because they deserve conscious examination.

4. **Verify that scorecards actually reflect the rubric.** The CR reviewer's job is to check that each individual scorecard is tied to rubric dimensions — not to subjective impressions — and that scores are neither too lenient nor too strict. Feedback that strays from the rubric should be flagged, not incorporated silently.

5. **The discussion must focus on evidence, not advocacy.** Any FUD (fear, uncertainty, or doubt) raised in the CR meeting must be tied to a specific rubric dimension with a specific behavioral example. "I just have a bad feeling" is not a valid CR input. "The candidate was unable to give a concrete example of managing conflict after three follow-up probes" is.

6. **Decide based on what's best for the company, not for the team or the referrer.** Even if a team is desperately short-staffed, even if the candidate was referred by a respected colleague, the decision frame must be: "Do we expect this person to at least meet expectations in their first performance review at the level we're considering?" If the answer is no or uncertain, the right answer is no hire.

7. **The outcome must be one of six specific options.** Hire at suggested level; hire at higher level; hire at lower level; no hire (committee outcome overturned); no hire (committee outcome confirmed); TBD (sent back for additional information). A decision that cannot be stated as one of these six has not been made yet.

8. **Close the loop with interviewers via feedback.** When the CR outcome differs from what individual interviewers submitted — or when feedback was not rubric-anchored — the CR lead should send a brief note to the interviewer explaining what was observed. This is how calibration improves over time and how CR avoids becoming a black box.

## Draft-mode intake

1. "Is this a standard CR review (panel reviews independently) or a hiring manager-led committee with CR as a check?"
2. "What is the candidate's suggested outcome and level from the hiring committee?"
3. "Were there any significant disagreements or unresolved FUD in the interview panel?"
4. "Were all scorecards rubric-anchored, or were there any that included subjective or non-rubric feedback?"
5. "What is the timeline for reaching a decision — is there competitive pressure on this candidate?"

## Artifact

**Format:** See `references/templates/candidate-review.md` for the fillable framework. The completed artifact includes: candidate overview (role, level, suggested outcome), per-dimension evidence summary (strengths and concerns from scorecards), scorecard verification notes, areas of disagreement and how they were resolved, decision framework walkthrough (steps 1-5), final outcome (one of six options) with rationale, and any feedback to be returned to interviewers.
**Default save path:** `./docs/management/candidate-review-[name]-YYYY-MM-DD.md` in the user's cwd. Ask before saving; ask before overwriting if file exists.
**Template:** `references/templates/candidate-review.md`

## Source

*Scaling People* — Claire Hughes Johnson, Stripe Press 2023 — Chapter 3, "Hiring > Decision-making" and sidebar "Candidate review" and "Exercises and templates: Candidate Review: Decision-Making Framework."

Encoded heuristic: Candidate review exists to make the hiring bar consistent across every candidate, regardless of which team is hiring, how urgently they need to fill the role, or who referred the candidate. The process works in sequence: review the objective scorecard first, then the hiring manager's rationale, then verify that individual scorecards reflect the rubric, then discuss and decide. Every discussion input must be evidence-anchored; every outcome must be one of six specific options. The feedback loop — returning observations to interviewers when their feedback strayed from the rubric — is what makes CR improve over time rather than calcify. Without that loop, CR becomes a black box that interviewers distrust.

Where the book provides a template, see `references/templates/candidate-review.md`.
