---
name: plan-departure
description: Plan managing out, firing for misconduct, or a layoff — pre-work, the departure conversation (junior vs senior structure differs), legal considerations. Use as soon as departure is the path.
---

# Plan Departure

This skill covers the final stage of managing out a low performer, as well as firing for gross misconduct and layoffs. The departure conversation is different from a PIP or performance feedback conversation: by the time you're here, the decision is made. Your job is to have a clear, kind, brief conversation that moves quickly from the decision to the logistics — and to do it well enough that how you treat this departure reflects well on you, your team, and your company.

Part of `feedback-and-performance` (Chapter 5 of *Scaling People*).

## Mode

Use the `AskUserQuestion` tool to ask which mode to run in. Default to `draft` if the user skips or picks "Other" without specifying.

- **`teach`** — Socratic walk-through (10-20 min). Use when the user is new to this artifact or wants to internalize the framework. Walk through every heuristic in the Rubric as a question; build the artifact incrementally; explain the "why" alongside the "what."
- **`draft`** — Targeted intake → first draft → refinement (5-10 min). Use when the user knows roughly what they want. Ask the 3-5 questions listed under "Draft-mode intake" below; produce a complete first draft; offer one round of refinement against the Rubric.
- **`polish`** — Critique-and-polish (2-5 min). Use when the user pastes an existing draft. Critique against every Rubric heuristic; rewrite to address gaps; explain what changed.

**When asking the user any question during this skill** (mode selection, intake, refinement, clarification): prefer the `AskUserQuestion` tool for any question with 2-4 reasonably discrete options (the user can always pick "Other" to free-text). Use plain chat only for questions that genuinely need a sentence or paragraph of free-form response. Multi-select questions are fine when the user could legitimately choose more than one.

## Rubric

1. **Complete the pre-work before the conversation.** Before the departure conversation: assemble all written feedback and prior PIPs, familiarize yourself with local employment laws (protected classes, discrimination law, termination processes), and inform your manager and HR partner. Showing up to this conversation under-prepared is the most common mistake.

2. **Junior-level conversations are shorter and more direct (1-2 sittings).** Because requirements for junior roles are more standardized, the gap is easier to demonstrate. Start by summarizing the PIP and asking how they think they've done. If they don't volunteer to leave, state clearly that you haven't seen enough progress and you want to agree on a timeline for their departure. Move quickly from the decision to the logistics: how do they want to inform people, when is their last day, how can you help? This is not a negotiation.

3. **Senior-level conversations take longer and rarely involve a formal PIP (a few months, 2-3 conversations minimum).** Senior employees who aren't meeting expectations were usually high performers in prior roles; the gap is specific to this role and this company. Discuss the performance issues in terms of this specific context. Half the time, a senior leader will see the writing on the wall and volunteer that it may be time to leave — which is a great outcome for both of you. If they don't, be direct: "I don't see us closing the gap between what's needed and what you're delivering." Then move to transition: "Let's start talking about your timing and your transition plan."

4. **Move from the decision to logistics as quickly as possible.** Once you've communicated the departure, the most constructive thing you can do is let the person control what they can still control: how they want to inform people, when they'll leave, how you can help them. This moves the conversation from loss to planning, reduces conflict, and is more humane for everyone involved.

5. **Two responses to expect — re-litigation and next steps.** If they re-litigate (less than 5% of cases), be kind and firm. Reiterate the reasons, remind them of the process you undertook, and end with "I'm sorry, but I don't see another path." If they start talking about next steps, support that direction fully.

6. **Legal considerations require pause, not improvisation.** If the employee mentions "retaliation" or "discrimination," stop the conversation immediately. Tell them this is not the conversation you were expecting to have and that it makes sense to continue it with HR and legal present. Do not try to handle this alone.

7. **For gross misconduct, one conversation, same-day departure.** If someone has clearly violated your code of conduct, plan for them to leave that day. If there's been an investigation, communicate the conclusion and the departure terms in one meeting. Keep waiting time short.

8. **Fire fast, but fire well.** How you treat forced departures reflects on you, your team, and your company. The goal is mutual agreement, but when that's not possible, firm and humane is the right standard. Letting bad hires linger leaves organizational scars — on morale, on culture, and sometimes in the form of additional bad hires made by the underperforming senior employee.

## Draft-mode intake

1. "What type of departure is this — managing out a low performer, a gross misconduct situation, or a layoff?"
2. "Is the employee junior or senior? What's their role and level?"
3. "What's the pre-work status — have you informed HR and your manager, documented the performance history, and reviewed local employment law?"
4. "How mutual do you expect this departure to be — will they see it coming, or is this likely to be a surprise?"
5. "Is there a specific part of the conversation you're most uncertain about?"

## Artifact

**Format:** Markdown — a pre-work checklist (items complete / outstanding), the conversation structure with specific language for the departure decision, anticipated responses and how to handle them, and a transition/communications plan.
**Default save path:** `./docs/management/departure-plan-YYYY-MM-DD.md` in the user's cwd. Ask before saving; ask before overwriting if file exists.
**Template:** See `references/templates/managing-out-checklist.md`.

## Source

*Scaling People* — Claire Hughes Johnson, Stripe Press 2023 — Chapter 5, "Managing out, firing, and layoffs" (subsections: Pre-work; The departure conversation — junior-level / senior-level; Legal considerations; Gross misconduct and layoffs).

Encoded heuristic: Most of the time you can manage someone out — meaning you and your report come to the conclusion that they should leave, without a formal termination conversation. By the time you have the "you should leave" conversation, you should be confident in the decision, and ideally both of you have had conversations that led to this conclusion organically. The junior-level departure conversation is short and standard: summarize the PIP, ask how they think it went, state that it won't work out, and move to planning the departure. The senior-level departure conversation takes months and involves 2-3 conversations; half the time the senior leader volunteers to leave. Fire fast but fire well: how you treat forced departures reflects on you, your team, and your company.

Where the book provides a template, see `references/templates/managing-out-checklist.md`.
