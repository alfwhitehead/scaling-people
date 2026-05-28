---
name: design-interview-loop
description: Design the interview loop — rubric, question assignments, and optional written exercise — for a role. Use when building or updating the loop before interviews begin.
---

# Design Interview Loop

This skill produces a complete interview framework: the capability dimensions to assess, the structured stages (screens, onsite, written project), the per-interview focus areas and sample questions, and a scoring rubric. Use it before you start interviewing candidates for a role — whether the role is new, infrequently filled, or one for which you have had inconsistent hiring quality. The output is the document you share with every interviewer before they enter the process.

Part of `hiring` (Chapter 3 of *Scaling People*).

## Mode

Ask the user which mode to run in. Default to `draft` if they don't specify.

- **`teach`** — Socratic walk-through (10-20 min). Use when the user is new to this artifact or wants to internalize the framework. Walk through every heuristic in the Rubric as a question; build the artifact incrementally; explain the "why" alongside the "what."
- **`draft`** — Targeted intake → first draft → refinement (5-10 min). Use when the user knows roughly what they want. Ask the 3-5 questions listed under "Draft-mode intake" below; produce a complete first draft; offer one round of refinement against the Rubric.
- **`polish`** — Critique-and-polish (2-5 min). Use when the user pastes an existing draft. Critique against every Rubric heuristic; rewrite to address gaps; explain what changed.

## Rubric

1. **Assign one or two rubric dimensions to each interviewer — no overlap.** Every interviewer should be responsible for assessing a specific subset of the capabilities you have identified for the role. Overlap wastes interview time and reduces the breadth of your signal. When interviewers each own a dimension, they go deeper and the combined picture is wider.

2. **Keep the panel to a maximum of eight people; less for entry-level roles.** Studies show diminishing returns beyond eight interviewers. For well-understood, entry-level roles, four or five is often sufficient. More is not more rigorous — it is just more expensive and harder to schedule.

3. **Use a consistent set of questions across all candidates.** You cannot benchmark an excellent answer if you asked different questions of different candidates. Consistency is the prerequisite to calibration. You can probe and follow up differently, but the core questions must be the same.

4. **Mix question types: situational, behavioral, and strict competency.** Behavioral questions ("Tell me about a challenge you overcame") reveal actual past behavior. Situational questions ("How would you handle this scenario?") test judgment. Competency questions ("Describe the last model you built") assess specific skills. A well-designed loop includes all three types.

5. **Test for self-awareness and learning orientation in every loop.** The most revealing questions ask candidates how their colleagues would describe them, what constructive feedback they've received, and what they've done to improve. Monitor whether they use "I" or "we" — too much "I" often signals poor collaboration; too much "we" may obscure their individual contribution.

6. **Consider a written exercise for roles where writing, structured thinking, or work-product quality matter.** A written exercise puts the candidate in a realistic scenario and reveals how they structure thinking and solve problems independently of real-time pressure. Provide clear instructions, a reasonable deadline (typically 2-3 days), and a scored rubric with pass/fail guidance.

7. **Build the rubric to produce concrete, behavior-anchored evidence — not impressions.** Each dimension should specify what a "poor," "good," and "strong" answer looks like. FUD (fear, uncertainty, or doubt) must be tied directly to a rubric dimension, not expressed as general culture fit concern. "I have some culture FUD" is not feedback; "Candidate was dismissive about the contributions of their team" is.

8. **For less frequently filled or senior roles, hold a kickoff meeting with all interviewers.** Before the first candidate interviews, get everyone aligned on the role, the rubric, and their specific focus area. This prevents misaligned questions and ensures pattern-matching across candidates.

## Draft-mode intake

1. "What is the role, and how often does the company hire for it?"
2. "What are the 5-8 capability dimensions most critical to success in this role?"
3. "Who will be on the interview panel, and what are their relationships to the role?"
4. "Is there a stage of the process where a written exercise or roleplay would be a better signal than a live interview?"
5. "What does a 'strong yes' candidate look like on each dimension — what would make you excited?"

## Artifact

**Format:** See `references/templates/interview-rubric.md` for the fillable scaffold. The completed artifact includes: role overview and capability list, interview stage structure (screen → team screen/written project → onsite interviews), per-stage interviewer assignments and focus dimensions, sample questions per stage with STAR-style follow-ups, and a Poor/Good/Strong rubric table for each dimension.
**Default save path:** `./docs/management/interview-loop-[role]-YYYY-MM-DD.md` in the user's cwd. Ask before saving; ask before overwriting if file exists.
**Template:** `references/templates/interview-rubric.md`

## Source

*Scaling People* — Claire Hughes Johnson, Stripe Press 2023 — Chapter 3, "Hiring > Interviewing" and "Exercises and templates: Interview Framework and Rubric: Recruiting for Recruiters (L2+)" and "Sample Interview Questions" and "Written Exercise Example."

Encoded heuristic: An interview loop is a measurement instrument, and like any instrument it must be calibrated and consistent. Assign each interviewer one or two capability dimensions from the rubric so the panel produces breadth without overlap. Keep the panel small — eight people is the ceiling, fewer for common roles. Ask every candidate the same core questions so you can benchmark answers. Mix situational, behavioral, and competency questions. Build the rubric with behavior-anchored descriptors so that FUD is always tied to a specific dimension, not to vague "culture" concern. For roles where writing or structured thinking matters, add a scored written exercise. The best loops test not just functional expertise but learning orientation and self-awareness — the qualities most predictive of long-term success.

Where the book provides a template, see `references/templates/interview-rubric.md`.
