---
name: diagnose-team-state
description: Diagnose team state — skill/will quadrants + probes for an underperforming team. Use when a team is missing goals or feels off.
---

# Diagnose Team State

This skill produces a team-state diagnosis: a written assessment of where the team sits on the skill-will matrix (individually and collectively), which of Lencioni's five dysfunctions may be present, and a prioritized set of actions to move the team from its current state toward high-functioning. Use it when you inherit a new team, when goals are being consistently missed, or when something feels off but you can't name it yet.

Part of `team-development` (Chapter 4 of *Scaling People*).

## Mode

Ask the user which mode to run in. Default to `draft` if they don't specify.

- **`teach`** — Socratic walk-through (10-20 min). Use when the user is new to this artifact or wants to internalize the framework. Walk through every heuristic in the Rubric as a question; build the artifact incrementally; explain the "why" alongside the "what."
- **`draft`** — Targeted intake → first draft → refinement (5-10 min). Use when the user knows roughly what they want. Ask the 3-5 questions listed under "Draft-mode intake" below; produce a complete first draft; offer one round of refinement against the Rubric.
- **`polish`** — Critique-and-polish (2-5 min). Use when the user pastes an existing draft. Critique against every Rubric heuristic; rewrite to address gaps; explain what changed.

## Rubric

1. **Check the operating system first.** Before diagnosing people and dynamics, confirm that the team's mission, goals, and operating cadence are sound (Chapter 2). A poorly written mission or unclear goals will produce symptoms that look like skill or will problems but are actually structural.

2. **Place each team member in a skill-will quadrant.** "Skill" is ability to do the work; "will" is motivation to do it. The four interpretations: high skill / high will — delegate and empower; low skill / high will — invest in training, build in checkpoints; high skill / low will — dig into the root cause (personal issue, wrong role, or need for a new challenge?); low skill / low will — act quickly, this is usually a team-composition problem.

3. **Diagnose against Lencioni's five dysfunctions.** Absence of trust, fear of conflict, lack of commitment, avoidance of accountability, and inattention to results. If one or more is present, name it explicitly in the diagnosis. Make the discussion mutual: share survey results or observations with the team to build self-awareness, then co-create a commitment to change.

4. **Investigate underperformance with curiosity, not accusation.** Start with probing questions in 1:1s to test your hypothesis about the root cause. Then surface the issue in the team meeting: Why are we behind? Are the reasons in or out of our control? What can we do now to get back on track? Document answers and assign owners. If the goal is wrong, reset it transparently, with notes on why.

5. **Check for collaboration fractures before assuming individual failure.** When friction is widespread, conduct a 360-style interview process (or ask HR to do it) and write up a summary. Facilitate a session on dynamics and extract explicit commitments on what will change. Most points of friction come from a lack of mutual self-awareness — return to work-style assessments and shared vocabulary.

6. **Treat missing goals as symptoms, not verdicts.** Goals are frequently missed due to dependencies on other teams. Anticipate those dependencies during planning, check in regularly, embed a representative when needed, and escalate constructively rather than absorbing the miss silently. "Clearing the path my team needs to travel" is the manager's job.

## Draft-mode intake

1. "Which team member, or the team overall, feels most off to you right now — and in what way?"
2. "Walk me through the last missed goal or missed deadline. What explanation was given? Did it feel like the full story?"
3. "If you had to place each person on a 2×2 of skill (can they do the work?) vs will (do they want to do the work?), where would they land?"
4. "Are there signs of any of Lencioni's five dysfunctions — lack of trust, conflict avoidance, low commitment, accountability avoidance, or ignoring results?"
5. "Is the operating system (mission, goals, meeting cadence) clear and sound, or could confusion there be masking a people issue?"

## Artifact

**Format:** Markdown — a "team state summary" section with skill-will placement per person, a "dysfunction check" section, and a "next actions" table with owner and timeline.
**Default save path:** `./docs/management/team-state-YYYY-MM-DD.md` in the user's cwd. Ask before saving; ask before overwriting if file exists.
**Template:** Inline — no shared template.

## Source

*Scaling People* — Claire Hughes Johnson, Stripe Press 2023 — Chapter 4, "Diagnosing team state" and "Team-building complexities > Underperforming teams."

Encoded heuristic: Diagnosing a team starts with the operating system (mission, goals, cadence) and then moves to people. Use Max Landsberg's skill-will matrix to place each team member: high skill / high will = delegate; low skill / high will = invest and checkpoint; high skill / low will = dig into motivation; low skill / low will = act on team composition. Survey the team against Lencioni's five dysfunctions — absence of trust, fear of conflict, lack of commitment, avoidance of accountability, inattention to results — and make the results a shared, named conversation. For underperforming teams, probe root cause via 1:1s before the team meeting, then ask as a group: why are we behind, what is and isn't in our control, and what do we do now? Most chronic underperformance traces to dependencies, collaboration fractures, or a misdiagnosed skill/will problem — rarely to the wrong goal alone.

Where the book provides a template, see `references/templates/team-charter.md` (for the operating-system layer that underpins team state).
