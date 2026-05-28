---
name: prep-comp-conversation
description: Prepare for a compensation conversation — educate yourself, instill trust in the system, understand motivators, have the talk. Use before every comp delivery, including no-change conversations.
---

# Prep Comp Conversation

This skill helps you prepare for one of the most fraught manager conversations: compensation. The goal is not to deliver a number but to link pay to performance in a way the employee finds fair and trustworthy, and to leave the conversation with insight into how they think about their role and trajectory. It covers all outcomes — increases, promotions, no change, and disappointment.

Part of `feedback-and-performance` (Chapter 5 of *Scaling People*).

## Mode

Use the `AskUserQuestion` tool to ask which mode to run in. Default to `draft` if the user skips or picks "Other" without specifying.

- **`teach`** — Socratic walk-through (10-20 min). Use when the user is new to this artifact or wants to internalize the framework. Walk through every heuristic in the Rubric as a question; build the artifact incrementally; explain the "why" alongside the "what."
- **`draft`** — Targeted intake → first draft → refinement (5-10 min). Use when the user knows roughly what they want. Ask the 3-5 questions listed under "Draft-mode intake" below; produce a complete first draft; offer one round of refinement against the Rubric.
- **`polish`** — Critique-and-polish (2-5 min). Use when the user pastes an existing draft. Critique against every Rubric heuristic; rewrite to address gaps; explain what changed.

**When asking the user any question during this skill** (mode selection, intake, refinement, clarification): prefer the `AskUserQuestion` tool for any question with 2-4 reasonably discrete options (the user can always pick "Other" to free-text). Use plain chat only for questions that genuinely need a sentence or paragraph of free-form response. Multi-select questions are fine when the user could legitimately choose more than one.

## Rubric

1. **Educate yourself first.** Know the ins and outs of your compensation system before you walk in: what the company rewards, how often reviews happen, how your comp compares to market. Start every comp conversation with a review of the system and philosophy; if the employee has questions you can't answer, commit to a follow-up rather than guessing.

2. **Instill trust in the system.** Compensation and equity misunderstandings can permanently destroy trust. If the system or its educational materials are lacking, invest in improving them with HR. Even when the outcome is disappointing, the employee should leave understanding that there is a system of review in place and that you, as their manager, stand behind it.

3. **Understand the motivators before the meeting.** Think through this person's story: their career stage, last uplevel, last increase, and what they're likely expecting. Most people are primarily motivated by recognition of impact, not purely by financial gain. Frame rewards as indicators of how the company views their contributions, not as goals the company defines for them.

4. **Have the conversation even when there's no change.** Remind the employee that there was a compensation review process, acknowledge there's no change this cycle, and explain why. Silence signals ambiguity, not neutrality. Owning the no-change outcome builds more trust than avoiding it.

5. **Handle comparisons by keeping the focus on the individual.** If an employee says someone else is paid more for the same work, stay on the system and on this employee's performance. "I can't discuss anyone else's compensation, but if you think something is unfair, I'm happy to make sure HR looks into it" is a complete answer. Don't get drawn into specifics about another person's package.

6. **Manage disappointment by anchoring to development, not defense.** If a high performer is disappointed with a meaningful increase, help them understand the system and get perspective. Reframe: "How can we work together so that in six months, your compensation and perceived impact feel more aligned?" If they're pushing for promotion, focus on what that would require and what you'll do together to get them there.

7. **Tie the outcome to performance every time.** Whether the news is good or bad, explicitly connect the comp outcome to the employee's performance and impact. A raise celebrated without context is a missed coaching moment. A flat outcome explained without reference to performance is a missed accountability moment.

## Draft-mode intake

1. "Who is the employee and what's the comp outcome — raise, bonus, promotion, no change?"
2. "What's your company's compensation philosophy and how does this outcome fit within it?"
3. "What's your read on this employee's motivators — is it about impact recognition, financial gain, something else?"
4. "What reaction are you expecting, and what's the most difficult part of this conversation?"
5. "Are there development areas or a promotion timeline you want to connect to the outcome?"

## Artifact

**Format:** Markdown — a completed prep document covering the outcome summary, system context to share, employee motivators to address, anticipated reactions and how to handle them, and a conversation script outline.
**Default save path:** `./docs/management/comp-conversation-prep-YYYY-MM-DD.md` in the user's cwd. Ask before saving; ask before overwriting if file exists.
**Template:** See `references/templates/comp-conversation-prep.md`.

## Source

*Scaling People* — Claire Hughes Johnson, Stripe Press 2023 — Chapter 5, "Compensation" (subsections: Compensation conversations — Educate yourself / Instill trust in your systems / Understand the motivators / Have the conversation; Comparisons; Managing disappointment).

Encoded heuristic: Of all the conversations you will have as a manager, the compensation conversation can be the most fraught. People usually want to know two things: Am I being treated fairly? Am I being recognized for my performance? Start every conversation with a review of the system and philosophy. Don't ignore the opportunity to use compensation as part of your management tool kit — these conversations naturally follow from formal processes like performance reviews. In cases where the employee isn't receiving a compensation change, it's still important to have the conversation: acknowledge the review happened, explain why there's no change, and connect the outcome to the development areas you've been discussing.

Where the book provides a template, see `references/templates/comp-conversation-prep.md`.
