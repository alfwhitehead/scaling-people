---
name: apply-d-and-i-lens
description: Apply a D&I review across hiring, performance, and team practices. Use during hiring loop design, calibration, or when designing team rituals.
---

# Apply D&I Lens

This skill produces a D&I review of a specific management area — hiring, performance assessment and recognition, or team-running practices — with a list of concrete checks the manager can apply immediately and a set of improvements to implement. Use it during hiring loop design, before calibration cycles, when you notice participation imbalances in meetings, or any time you want to audit whether your management practices give every team member a fair chance to contribute and advance.

Part of `team-development` (Chapter 4 of *Scaling People*).

## Mode

Use the `AskUserQuestion` tool to ask which mode to run in. Default to `draft` if the user skips or picks "Other" without specifying.

- **`teach`** — Socratic walk-through (10-20 min). Use when the user is new to this artifact or wants to internalize the framework. Walk through every heuristic in the Rubric as a question; build the artifact incrementally; explain the "why" alongside the "what."
- **`draft`** — Targeted intake → first draft → refinement (5-10 min). Use when the user knows roughly what they want. Ask the 3-5 questions listed under "Draft-mode intake" below; produce a complete first draft; offer one round of refinement against the Rubric.
- **`polish`** — Critique-and-polish (2-5 min). Use when the user pastes an existing draft. Critique against every Rubric heuristic; rewrite to address gaps; explain what changed.

**When asking the user any question during this skill** (mode selection, intake, refinement, clarification): prefer the `AskUserQuestion` tool for any question with 2-4 reasonably discrete options (the user can always pick "Other" to free-text). Use plain chat only for questions that genuinely need a sentence or paragraph of free-form response. Multi-select questions are fine when the user could legitimately choose more than one.

## Rubric

The rubric is organized by the three areas where managers have the most direct influence. Apply the checks that correspond to the area you are reviewing.

**Hiring: check your pipeline before you start interviewing.**
Build a diverse pipeline before the first interview is scheduled — do not start the process with a thin or homogeneous pool. Add an interviewer with a significantly different background from yours; they may recognize strengths in candidates that your experience makes harder to see. Watch for cloning: fast-growth companies default to referral hiring, which creates self-similar teams. Break the cycle intentionally.

**Hiring: assess the portfolio, not just the candidate.**
Before each hiring cycle, audit what backgrounds and viewpoints your team is currently lacking. If you don't know what you're missing, visit other team's meetings to observe different dynamics. A candidate's strengths are best evaluated against what the team does not already have, not only against an ideal archetype.

**Performance: make opportunities visible and criteria explicit.**
Shoulder taps are efficient but exclusionary — they leave out everyone who didn't happen to be in the conversation. When assigning high-visibility projects, promotions, or leadership development opportunities, make the opportunity clear to the relevant group, specify the selection criteria, and let people raise their hand. Check why people you thought should volunteer didn't, and help them do so in the future.

**Performance: build equity checks into your processes.**
Establish a common, agreed-upon way of evaluating candidates for promotion or project assignment. Run lightweight calibration sessions that cross-check decisions against objective performance data and pay-parity analysis. The goal is not an exhaustive audit but a medical-checklist discipline — a short list of things you verify every time to prevent known error patterns.

**Running teams: pay attention to airtime.**
In every team meeting and team interaction, notice who has not spoken. Give them an opportunity. "Assume that how you manage can probably be more inclusive than it is." The test is simple: ask a trusted colleague to observe you and point out where your day-to-day management practices could create more equitable airtime.

**Running teams: inclusion is a process design problem, not just a cultural attitude.**
Almost any team interaction is an opportunity: how you collect agenda items, plan an offsite, run a meeting, make a decision on a controversial subject. Audit your team's onboarding process and solicit feedback from all new members, regardless of background, on whether they feel prepared to contribute after the first month. Build inclusion into the process so it does not depend on your awareness in the moment.

**Across all three areas: retain and develop, not just hire.**
Hiring is not a panacea. Diverse early-career employees may fail to advance at similar rates due to a weak sense of belonging and difficulty navigating unwritten professional norms. The manager's role after a more diverse team is assembled is to run it equitably and inclusively — otherwise attrition will undo the hiring investment and future diverse candidates will not be attracted to the team.

## Draft-mode intake

1. "Which area are you reviewing: hiring practices, performance or promotion processes, or how the team runs day to day?"
2. "What prompted this review — a specific decision, a pattern you've noticed, a scheduled calibration, or something else?"
3. "Do you know what backgrounds or viewpoints your team is currently missing? If not, how might you find out?"
4. "Is there a specific practice or ritual — a meeting, a project-assignment process, an onboarding step — that you want to examine first?"

## Artifact

**Format:** Markdown — a "scope" section identifying the area being reviewed, a "checks applied" section listing each heuristic with a pass / flag / improve verdict, and an "improvements" section with specific, time-bound actions.
**Default save path:** `./docs/management/di-review-[area]-YYYY-MM-DD.md` in the user's cwd. Ask before saving; ask before overwriting if file exists.
**Template:** Inline — no shared template.

## Source

*Scaling People* — Claire Hughes Johnson, Stripe Press 2023 — Chapter 4, "Diversity and inclusion."

Encoded heuristic: Managers influence diversity and inclusion in three areas — hiring, performance assessment and recognition, and running teams. In hiring, the critical checks are: build a diverse pipeline before interviewing begins, add an interviewer with a different background, and audit the team portfolio for missing perspectives. In performance, the critical checks are: make opportunities visible (not shoulder-tap-only), establish explicit selection criteria, and build equity into calibration and compensation review. In team-running, the critical checks are: track airtime in meetings and give voice to those who haven't spoken; audit every team process (onboarding, agenda-building, meeting facilitation, offsite design) for structural exclusions. Across all three areas, retention and development of diverse team members matters as much as hiring — diverse employees who lack belonging or access to unwritten norms will not advance at equal rates, which undoes the hiring investment.

Where the book provides a template, see `references/templates/career-conversation.md` (for understanding the backgrounds and motivations of each team member, a key input to inclusive management).
