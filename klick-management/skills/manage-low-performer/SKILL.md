---
name: manage-low-performer
description: Manage a low performer through the phased approach — Phase 0 (pattern) → Phase 1 (align) → Phase 2 (next steps) → Phase 3 (action plan / PIP / role move). Use as soon as the pattern is clear, not after the formal review cycle.
---

# Manage Low Performer

When one-off coaching feedback becomes a pattern, you are managing a low performer. This skill walks you through the four-phase approach: recognizing and naming the pattern, aligning with the employee on what's happening, agreeing on next steps, and executing an action plan — whether that's a PIP, a role move, or a departure. Acting early and moving deliberately is far less costly than waiting.

Part of `feedback-and-performance` (Chapter 5 of *Scaling People*).

## Mode

Use the `AskUserQuestion` tool to ask which mode to run in. Default to `draft` if the user skips or picks "Other" without specifying.

- **`teach`** — Socratic walk-through (10-20 min). Use when the user is new to this artifact or wants to internalize the framework. Walk through every heuristic in the Rubric as a question; build the artifact incrementally; explain the "why" alongside the "what."
- **`draft`** — Targeted intake → first draft → refinement (5-10 min). Use when the user knows roughly what they want. Ask the 3-5 questions listed under "Draft-mode intake" below; produce a complete first draft; offer one round of refinement against the Rubric.
- **`polish`** — Critique-and-polish (2-5 min). Use when the user pastes an existing draft. Critique against every Rubric heuristic; rewrite to address gaps; explain what changed.

**When asking the user any question during this skill** (mode selection, intake, refinement, clarification): prefer the `AskUserQuestion` tool for any question with 2-4 reasonably discrete options (the user can always pick "Other" to free-text). Use plain chat only for questions that genuinely need a sentence or paragraph of free-form response. Multi-select questions are fine when the user could legitimately choose more than one.

## Rubric

1. **Phase 0 — Recognize the pattern and form a hypothesis on the outcome (under 3 weeks).** When one-off feedback becomes persistent underperformance with no visible improvement, you're no longer in coaching mode — you're in a performance management process. Before you begin, develop a hypothesis about the most likely outcome: the employee improves in the role, moves to a different role, or leaves the company. You'll adjust the hypothesis as you gather data, but having one sharpens how you communicate expectations throughout.

2. **Phase 1 — Get aligned about the performance challenge (1-3 conversations, ~2 weeks).** Use a regular 1:1 to deliver the feedback. Two additions distinguish Phase 1 from informal coaching: state explicitly that you are now seeing a pattern, and state explicitly that the employee is not meeting the expectations of the role. Reference an objective source — a role charter or job ladder — when you do this. Don't assume the employee understands they are officially not meeting expectations until you say it out loud.

3. **Phase 2 — Agree on next steps (1-2 conversations, ~1 week).** After Phase 1, you and the employee should be moving toward one of three paths: a formal performance improvement plan, a move to another team or role, or a departure. Even if they don't fully agree, by the third conversation you need to name the path and start moving down it.

4. **Phase 3 — Execute the action plan (1-3 months).** If the path is a PIP, it should include: the specific skills or behaviors that need to change, an end date for evaluation, and how progress will be measured. Performance issues fall into three categories — operational/tactical, overall skills fit, and behavioral/attitudinal — and the appropriate duration and measurement approach differ for each.

5. **No surprises.** By the time you put someone on a formal PIP, they should have had at least two or three feedback conversations in which you've stated that their work is not meeting the expectations of the role. If they're surprised, you haven't managed the process — you've deferred it.

6. **Document every discussion.** Document feedback in writing after each significant conversation. Email is best: it pushes information to the employee and creates a record both parties have. Document the pattern, the specific examples, the agreed-upon next steps, and the timeline. Share documentation with HR once you've identified a low-performance situation.

7. **Show compassion without withholding clarity.** Compassionate management does not mean holding off on feedback because the employee seems overwhelmed. It means giving honest observations, being clear about options to course-correct, and sharing your honest assessment of likely outcomes. Compassion and clarity are not in tension. "Ruinous empathy" — being nice while withholding the truth — is worse for everyone, including the employee.

8. **Move deliberately — three months maximum.** Waiting too long introduces new variables: the employee becomes stressed, their performance worsens, and issues like mental health may emerge that complicate the process. In most cases, a resolution should come within three months. Many cases can be resolved within one month.

## Draft-mode intake

1. "What's the specific performance gap — what role expectations are not being met and what's the pattern?"
2. "What conversations have already happened — what has been said, and was it explicit that they are not meeting expectations?"
3. "What's your current hypothesis about the likely outcome — improvement, role move, or departure?"
4. "What phase are you in? Phase 0 (just recognized pattern), Phase 1 (aligning), Phase 2 (agreeing on next steps), or Phase 3 (executing)?"
5. "Does your company have HR involved? What do they know?"

## Artifact

**Format:** Markdown — a phase tracker (current phase + what's been done), the hypothesis on likely outcome, the next conversation plan with specific language, and (if Phase 3) the framework for the PIP or role-move conversation.
**Default save path:** `./docs/management/low-performer-plan-YYYY-MM-DD.md` in the user's cwd. Ask before saving; ask before overwriting if file exists.
**Template:** See `references/templates/pip-template.md` for PIP and documentation email templates.

## Source

*Scaling People* — Claire Hughes Johnson, Stripe Press 2023 — Chapter 5, "Managing low performers" (subsections: Edge cases; The role of HR teams; Phases of managing low performers — Phase 0/1/2/3; Delivering the feedback — Response 1 denial / Response 2 relief; Document your discussion; Phase 2: Agree on next steps; Phase 3: Create an action plan; Potential outcome 1: PIP; Potential outcome 2: Move roles or teams).

Encoded heuristic: When there's a persistent gap between a report's performance and the demands of their role, you're managing a low performer. The most important thing is to act quickly: provide feedback early and often; document every discussion; never let the employee be surprised at a formal PIP. The four phases — pattern recognition, alignment, next steps, action plan — take no more than three months in total for most situations. Most low-performer situations resolve through a mutual agreement to move on, not a formal firing. The manager's job is to support the person through the process while keeping an eye on the degree of difficulty and maintaining an honest hypothesis about the outcome.

Where the book provides templates, see `references/templates/pip-template.md`.
