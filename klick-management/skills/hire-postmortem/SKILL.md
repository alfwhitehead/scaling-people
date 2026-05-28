---
name: hire-postmortem
description: Close the loop on a hire — especially one that did not work. Use when a hire has departed, been managed out, significantly underperformed, or any time the process felt broken.
---

# Hire Postmortem

This skill produces a structured retrospective on a completed hire — what went wrong (or right), where the process broke down, and what specific changes to the rubric, the interviewer selection, the reference process, or the onboarding would reduce the probability of a similar outcome in the future. Use it after any hiring mistake, and optionally after particularly strong hires to understand what the process did well. It is also the entry point for company-wide, data-driven analysis of hiring quality over time.

Part of `hiring` (Chapter 3 of *Scaling People*).

## Mode

Use the `AskUserQuestion` tool to ask which mode to run in. Default to `draft` if the user skips or picks "Other" without specifying.

- **`teach`** — Socratic walk-through (10-20 min). Use when the user is new to this artifact or wants to internalize the framework. Walk through every heuristic in the Rubric as a question; build the artifact incrementally; explain the "why" alongside the "what."
- **`draft`** — Targeted intake → first draft → refinement (5-10 min). Use when the user knows roughly what they want. Ask the 3-5 questions listed under "Draft-mode intake" below; produce a complete first draft; offer one round of refinement against the Rubric.
- **`polish`** — Critique-and-polish (2-5 min). Use when the user has an existing draft or notes. Critique against every Rubric heuristic; strengthen the root-cause analysis and the recommendations; explain what changed.

**When asking the user any question during this skill** (mode selection, intake, refinement, clarification): prefer the `AskUserQuestion` tool for any question with 2-4 reasonably discrete options (the user can always pick "Other" to free-text). Use plain chat only for questions that genuinely need a sentence or paragraph of free-form response. Multi-select questions are fine when the user could legitimately choose more than one.

## Rubric

1. **Do something — and do it quickly.** The main thing when you realize you've made a hiring mistake is to act. Depending on circumstances, that may mean rescinding an offer, moving toward a swift termination, or negotiating a departure. It is better to pay a severance and separate than to drag out a process that negatively impacts the team. A short note to the team is sufficient; no need to overexplain.

2. **Trace the error back through every stage of the process.** Were there issues you should have caught in the process? Did the capabilities list correctly describe what the role required? Were there flags in the interview feedback or the references that were overlooked or rationalized away? Who conducted the interviews and reference calls? Was the onboarding thorough? Be honest about the role you personally played.

3. **Distinguish process failure from judgment failure.** Some hiring mistakes happen because the rubric was wrong; others because the process was right but the interviewer's assessment was off; others because a red flag was visible but not acted on. The root cause determines the fix. A rubric problem requires updating the capabilities list. A judgment problem may require interviewer training or panel composition changes.

4. **Interview panel quality is the primary lever.** The stronger the process and the more experienced and close to the work your interviewers are, the more reliable your hiring signal. Jack Welch tracked data on who the best interviewers were and made sure they trained others. The quality of the hiring outcome correlates closely with the experience level and role proximity of the interviewers who assessed it.

5. **Close the loop with data, not just reflection.** Use your applicant tracking system (ATS) to examine time-in-process, funnel conversion, and interviewer decisiveness. Map new hire performance data — from manager surveys at 6 weeks, 12 weeks, and 6 months — back against the interview feedback and rubric scores. Over time, this mapping will reveal which rubric items and which interviewers predicted success.

6. **Survey candidates you rejected — not just those you hired.** False negatives are hard to track, but you can gather signal from rejected candidates who completed one or more interview stages. Use an adjusted NPS survey to assess whether they would recommend your company as a place to apply. The feedback reveals process and experience quality that internal observation alone misses.

7. **Make the learnings available to your recruiting partner.** The postmortem is not just a personal exercise — it is an input to the shared hiring system. Share your root-cause findings and your recommended process changes with the recruiter who managed the search. The recruiting function is better positioned to implement systematic improvements when they have specific, evidence-based feedback from hiring managers.

## Draft-mode intake

1. "What happened — when did you realize the hire was a mistake, and what were the observable signals?"
2. "Where in the process did the mistake most likely originate — sourcing, rubric design, interview assessment, reference calls, onboarding, or somewhere else?"
3. "Were there any flags during the process — in interviews, references, or early in the role — that were either missed or rationalized away?"
4. "Who were the interviewers, and what was their level of experience with this type of role?"
5. "What specific change to the process, rubric, or panel composition would most reduce the probability of a similar outcome?"

## Artifact

**Format:** Markdown document with sections: Hire summary (role, dates, what happened), Process timeline (stages completed and any anomalies), Root-cause analysis (primary and contributing factors), Missed signals (flags that were present but not acted on), Recommended process changes (specific, actionable), Metrics to track going forward, and Summary for recruiting partner.
**Default save path:** `./docs/management/hire-postmortem-[role]-YYYY-MM-DD.md` in the user's cwd. Ask before saving; ask before overwriting if file exists.
**Template:** Inline — no shared template.

## Source

*Scaling People* — Claire Hughes Johnson, Stripe Press 2023 — Chapter 3, "Hiring mistakes > Close your hiring loop."

Encoded heuristic: Almost every hiring mistake is traceable to something that was either missed or rationalized away in the process. The postmortem's job is to find that thing — whether it was a poorly designed rubric, an inexperienced interview panel, a lukewarm reference that was explained away, or onboarding that did not surface misalignment quickly enough. The learning compounds when it is shared with your recruiting partner and when you build a habit of mapping interview feedback to post-hire performance data. The goal is not to assign blame — it is to improve the system, because talent is everything, and the system is the only thing you can actually control.

(No shared template — produce inline.)
