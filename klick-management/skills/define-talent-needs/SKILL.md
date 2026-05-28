---
name: define-talent-needs
description: Build insight on what success in the role looks like before opening it — capabilities, experience, working style, growth runway. Use at the start of any new role or before backfilling.
---

# Define Talent Needs

This skill produces a candidate assessment rubric and role profile — the research-backed foundation you need before writing a JD or interviewing anyone. Use it when you are opening a new role, backfilling an existing one, or when your last search produced the wrong kind of candidates. The output is a concrete document, not a job description — it is the internal brief that the JD will later be written from.

Part of `hiring` (Chapter 3 of *Scaling People*).

## Mode

Use the `AskUserQuestion` tool to ask which mode to run in. Default to `draft` if the user skips or picks "Other" without specifying.

- **`teach`** — Socratic walk-through (10-20 min). Use when the user is new to this artifact or wants to internalize the framework. Walk through every heuristic in the Rubric as a question; build the artifact incrementally; explain the "why" alongside the "what."
- **`draft`** — Targeted intake → first draft → refinement (5-10 min). Use when the user knows roughly what they want. Ask the 3-5 questions listed under "Draft-mode intake" below; produce a complete first draft; offer one round of refinement against the Rubric.
- **`polish`** — Critique-and-polish (2-5 min). Use when the user pastes an existing draft. Critique against every Rubric heuristic; rewrite to address gaps; explain what changed.

**When asking the user any question during this skill** (mode selection, intake, refinement, clarification): prefer the `AskUserQuestion` tool for any question with 2-4 reasonably discrete options (the user can always pick "Other" to free-text). Use plain chat only for questions that genuinely need a sentence or paragraph of free-form response. Multi-select questions are fine when the user could legitimately choose more than one.

## Rubric

1. **Start by studying who's already winning.** Before writing anything, ask: Who on the current team is doing really well? Who is scaling at the same pace as the company, and why? What qualities and capabilities do they have in common? What perspectives and experiences are missing? This internal audit grounds the rubric in observed reality rather than abstract ideals.

2. **Use the three-circle Venn test.** The ideal employee is good at their work, makes a significant impact on the company's progress, and loves what they do. Map your internal exemplars against all three. Use that mapping to identify the questions you'll ask in the interview to surface whether a candidate shares those qualities.

3. **Distinguish must-haves from nice-to-haves — in writing.** For every capability or experience item, force yourself to label it. A must-have is something the candidate cannot succeed without. A nice-to-have would accelerate their impact but its absence should not be disqualifying. Mixing the two is how searches get stalled or misaligned.

4. **Investigate the role through outside conversations before opening it.** Talk to advisers, people in the role at other companies, and people who have hired for it successfully. Ask specifically: What are the most important capabilities for success? What was it in the successful person's background that mattered? What were the biggest challenges in the first year? Do not use the interview process itself to calibrate your expectations — that wastes candidates and damages your reputation.

5. **Watch for the experience trap.** The more experienced someone is, the better they tend to be at interviewing. Separately, beware of "playbook thinkers" — candidates who have done something once and become stuck on one way to do it. What you are seeking is trajectory and momentum: raw curiosity, learning aptitude, and a demonstrated ability to overcome challenges and deliver results. Design the rubric to surface these, not just credentialed experience.

6. **Factor in complementarity with the existing team.** Especially for leadership roles, the rubric should include a dimension for what the new person adds to the team's existing skills, perspectives, and working styles — not just whether they can do the job in isolation.

7. **State what the role will become, not just what it is today.** Roles at growing companies evolve. The people who will scale with the company are the ones who can anticipate what they need to learn now in order to excel at what the role will become in six months. Include a "trajectory requirement" in the rubric: what does the candidate need to demonstrate about their capacity to adapt?

## Draft-mode intake

1. "What is the role, and is it new or a backfill?"
2. "Who on your team right now is thriving — what qualities do they have in common?"
3. "What perspectives or capabilities are missing from your team today?"
4. "What does the person in this role need to achieve in their first six months to be considered successful?"
5. "Are there any adjacent companies or people in this role you admire? Who would be your 'dream hire' profile?"

## Artifact

**Format:** Markdown document with sections: Role summary, Ideal employee profile (the three-circle analysis), Capability dimensions (each labeled must-have or nice-to-have with a 1-2 sentence description), Trajectory requirement, Research notes (people consulted + key findings), and Risks/watch-outs.
**Default save path:** `./docs/management/talent-needs-[role]-YYYY-MM-DD.md` in the user's cwd. Ask before saving; ask before overwriting if file exists.
**Template:** Inline — no shared template.

## Source

*Scaling People* — Claire Hughes Johnson, Stripe Press 2023 — Chapter 3, "Recruiting > Build insights on talent needs and candidate success."

Encoded heuristic: Before opening a role, study success from the inside out. Map your current high performers against three criteria — they are good at their work, they have a strong impact, and they love what they do. Use that Venn diagram to build a rubric that tests for the same combination in candidates. Supplement with outside research: talk to people who have hired for or done the role successfully before you interview anyone. Resist the experience trap — experienced candidates are skilled at interviewing, and playbook thinkers look credentialed. What you actually want is trajectory, learning aptitude, and the demonstrated capacity to grow into what the role will become.

(No shared template — produce inline.)
