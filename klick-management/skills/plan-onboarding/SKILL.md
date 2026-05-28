---
name: plan-onboarding
description: Build the onboarding plan for an IC or a new leader (NLE). Handles both; mode-switches based on hire type. Use as soon as an offer is accepted.
---

# Plan Onboarding

This skill produces an onboarding plan — the sequence of activities, connections, context transfers, and early-milestone commitments that set a new hire up to succeed. It covers both IC (individual contributor) onboarding and New Leader Experience (NLE) onboarding; ask which type before proceeding, as the depth, stakeholder involvement, and 90-day structure differ substantially. Use it as soon as an offer is accepted — the plan should begin taking shape before the first day.

Part of `hiring` (Chapter 3 of *Scaling People*).

## Mode

Use the `AskUserQuestion` tool to ask which mode to run in. Default to `draft` if the user skips or picks "Other" without specifying.

- **`teach`** — Socratic walk-through (10-20 min). Use when the user is new to this artifact or wants to internalize the framework. Walk through every heuristic in the Rubric as a question; build the artifact incrementally; explain the "why" alongside the "what."
- **`draft`** — Targeted intake → first draft → refinement (5-10 min). Use when the user knows roughly what they want. Ask the 3-5 questions listed under "Draft-mode intake" below (including the IC vs. new-leader question); produce a complete first draft; offer one round of refinement against the Rubric.
- **`polish`** — Critique-and-polish (2-5 min). Use when the user has an existing onboarding plan. Critique against every Rubric heuristic; rewrite to address gaps; explain what changed.

**When asking the user any question during this skill** (mode selection, intake, refinement, clarification): prefer the `AskUserQuestion` tool for any question with 2-4 reasonably discrete options (the user can always pick "Other" to free-text). Use plain chat only for questions that genuinely need a sentence or paragraph of free-form response. Multi-select questions are fine when the user could legitimately choose more than one.

## Rubric

### For all hires (IC and leader)

1. **Design onboarding to feel true to the company's character.** A great onboarding experience reflects the "why" (mission and story), the "what" (current priorities and goals), and the "how" (operating principles and how people work together). It is not just paperwork and laptop setup — it is the fastest possible ramp to the culture.

2. **Complete all administrative work before day one.** If the company has a sound onboarding program, all prep — paperwork, equipment, access — happens asynchronously before the program starts. The new hire's first day should be spent learning and connecting, not filing forms.

3. **Use the first 1:1 to establish mutual expectations, not just to orient.** Share your "Working with Me" guide (or equivalent), discuss operating approach and communication preferences, clarify initial priorities, and preview the career conversation you will have once you know each other better. Invite the new hire to write their own version if they are willing.

4. **For internal transfers, treat onboarding as a first-class process.** Internal new hires are often overlooked. Survey the person, their former manager, and their new manager whenever someone changes teams. Track whether the move is voluntary and growth-oriented or is a signal of something else. Run a manager-to-manager transition meeting to transfer context, strengths, and development areas explicitly.

### Additional heuristics for new-leader onboarding (NLE)

5. **Begin before the start date — with context, not judgment.** Share publicly available reading before the leader's first day, followed by an internal reading packet on day one. Help them understand what they need to know now versus in one month versus in three months. Give data points, not pre-processed conclusions. Let the new leader form their own judgments.

6. **Equip the leader with people — not just materials.** The NLE requires a spin-up buddy (answers day-to-day tactical questions), a company guide (a peer mentor who can be asked "why do we do things this way?" questions safely), a people partner, and a hiring manager willing to do daily or every-other-day standups in the first weeks. The plan only works if these people commit to their roles.

7. **Loan social capital actively.** New leaders start with significant responsibility and near-zero social capital. As an existing leader, broker introductions, advocate for the new leader in small and large forums, and set them up for early, quick wins. The fastest way to build their credibility is to visibly transfer some of yours.

8. **Calibrate listening vs. acting — and name it explicitly.** The highest art of leader onboarding is knowing when to switch from gathering information to taking action. Moving too fast causes lasting damage from premature decisions; moving too slowly paralyzes the division. The hiring manager and spin-up buddy should have an explicit conversation with the new leader about this balance in the first two weeks.

9. **Run a 90-day feedback process.** Survey or interview key stakeholders and direct reports at the 90-day mark, synthesize the findings, and share them with the new leader. This is also the point to start formal coaching engagement (e.g., via a Hogan assessment or equivalent). Early feedback enables early course correction before small patterns become organizational problems.

## Draft-mode intake

1. "Is this an IC onboarding plan or a new-leader (NLE) onboarding plan?" *(If new leader, proceed with NLE-specific questions; if IC, use the standard set below.)*

**For IC:**
2. "What team and role is this person joining, and when do they start?"
3. "What company-wide onboarding program already exists, and what gaps will you need to fill at the team level?"
4. "What does the new hire need to understand about the team's current work, priorities, and dynamics that they will not get from company onboarding?"
5. "Are there any internal mobility considerations — is this an internal transfer or a new external hire?"

**For new leader (NLE):**
2. "What role and level is this leader joining, and who are their key direct reports and cross-functional stakeholders?"
3. "Who will serve as their spin-up buddy, company guide, and people/HR partner?"
4. "What are the most critical areas of context they need in the first 30 days? What can wait until day 31-60 and 61-90?"
5. "Are there any known organizational sensitivities or resistance points that the onboarding plan needs to address?"

## Artifact

**For IC hires:** Markdown document covering pre-start logistics checklist, first-week schedule (company onboarding + team context), first 1:1 agenda template, 30-day priorities, and manager transition notes (if applicable).

**For new-leader hires:** See `references/templates/new-leader-experience.md` for the full NLE scaffold. The completed artifact covers pre-start week, first 30/60/90 days, onboarding support team roles, listening tour structure, decision-making first commitments, and what direct reports and the existing team should do.

**Default save path:** `./docs/management/onboarding-[name]-YYYY-MM-DD.md` in the user's cwd. Ask before saving; ask before overwriting if file exists.
**Template:** `references/templates/new-leader-experience.md` (for leader onboarding); inline for IC.

## Source

*Scaling People* — Claire Hughes Johnson, Stripe Press 2023 — Chapter 3, "Onboarding" (including subsections: Internal mobility, New hire onboarding, New leader onboarding, sidebars "New Leader Experience" and "New leader onboarding: a direct report's perspective") and "Exercises and templates: Manager Transitions Guide" and "New Leader Experience."

Encoded heuristic: Onboarding is not the period after hiring ends — it is the period when the investment in hiring pays off or is squandered. For IC hires, the first 1:1 is not orientation; it is the beginning of a working relationship that should be designed as deliberately as the hiring process itself. For new leaders, the stakes are higher: the success or failure of the hire becomes visible to the whole organization in weeks. Equip the leader with a spin-up buddy, a company guide, and a people partner who all commit to their roles. Give them data, not conclusions. Loan them social capital. Set up for early wins. And run a 90-day feedback process — the earlier the course correction, the smaller the correction required.

Where the book provides a template, see `references/templates/new-leader-experience.md`.
