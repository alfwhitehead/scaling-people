---
name: give-hard-feedback
description: Prepare to deliver difficult feedback as an explorer, not a lecturer — open question OR empathetic observation. Use before any hard 1:1 where you need to raise a pattern or performance concern.
---

# Give Hard Feedback

This skill helps you prepare and open a constructive feedback conversation in a way that invites self-reflection rather than triggering defensiveness. The core technique is a choice between two openers: an open-ended question or an empathetic observation. Both are designed to start from a place of shared exploration, not a lecture with a predetermined answer.

Part of `feedback-and-performance` (Chapter 5 of *Scaling People*).

## Mode

Use the `AskUserQuestion` tool to ask which mode to run in. Default to `draft` if the user skips or picks "Other" without specifying.

- **`teach`** — Socratic walk-through (10-20 min). Use when the user is new to this artifact or wants to internalize the framework. Walk through every heuristic in the Rubric as a question; build the artifact incrementally; explain the "why" alongside the "what."
- **`draft`** — Targeted intake → first draft → refinement (5-10 min). Use when the user knows roughly what they want. Ask the 3-5 questions listed under "Draft-mode intake" below; produce a complete first draft; offer one round of refinement against the Rubric.
- **`polish`** — Critique-and-polish (2-5 min). Use when the user pastes an existing draft. Critique against every Rubric heuristic; rewrite to address gaps; explain what changed.

**When asking the user any question during this skill** (mode selection, intake, refinement, clarification): prefer the `AskUserQuestion` tool for any question with 2-4 reasonably discrete options (the user can always pick "Other" to free-text). Use plain chat only for questions that genuinely need a sentence or paragraph of free-form response. Multi-select questions are fine when the user could legitimately choose more than one.

## Rubric

1. **Be an explorer, not a lecturer.** Set the conversation up as a partnership: you're exploring a situation together. If you offer solutions before you both agree on the problem, you risk alienating your report. Start from shared understanding, then lay the groundwork for improvement together. A person is far more likely to change if the recognition that change is needed comes from themselves.

2. **Option 1 — Ask an open-ended question.** "How do you think that presentation went?" or "How do you think this quarter is going?" are good openers. They invite self-reflection without signaling that you've already decided the answer. Contrast with bad versions: "Do you think the meeting could have been better?" or "Would you agree this quarter hasn't gone well?" — both signal a predetermined conclusion. Never ask a closed yes/no question as your opener.

3. **Option 2 — Share an empathetic observation.** When the open question produces denial, shift to a specific, supportive, fact-based observation you own: "I was thinking about that presentation — it was so strong at the start, but I thought it could have been even more impactful at the end. What did you think?" Own it as your perception, not objective reality: "I noticed the last two projects each missed their deadlines by two weeks. Is there something I can help with?" Specific and empathetic opens a dialogue; generic and emotional ("Things have been slipping lately") puts people on their heels.

4. **Cycle between the two options if needed.** If the observation isn't landing, revert to an open question. If the question keeps producing denial, give your own answer: "Huh. My impression was that it was not that great. For example…" It may take a few rounds to arrive at common understanding. Most people are more self-aware than you expect.

5. **Own your observation; don't state it as fact.** Feedback is holding up a mirror and describing what you see. You're sharing your perception of them, not confirming a universal truth. "I have a theory that…" or "My impression was…" reduces defensiveness and keeps the door open for dialogue.

6. **Get to solutions only after you agree on the problem.** Rushing to solutions before aligning on the issue is how feedback conversations go off the rails. Once the report acknowledges the same concern you have — even partially — pivot immediately to "What might you do differently? How can I help?" The goal is mutual problem-solving, not persuasion.

7. **A persistent self-awareness gap may require a different approach.** If the person's self-assessment is consistently misaligned with what you and others observe, more data is needed before the feedback can land. Consider joining their team meetings, reviewing work product, or gathering peer perspectives before the next attempt.

## Draft-mode intake

1. "What's the feedback you need to give — what behavior or output, and what pattern have you observed?"
2. "What's your best guess about how your report currently sees the situation — do they know there's a problem?"
3. "Which opener feels right: an open-ended question, or an empathetic observation? Why?"
4. "What specific examples do you have that are concrete and recent enough to reference?"
5. "What outcome are you hoping for from this conversation?"

## Artifact

**Format:** Markdown — the feedback in one sentence, the chosen opener (Option 1 or Option 2) with exact wording, 2-3 specific examples to reference if needed, an anticipated response and how to handle it, and the follow-up question to pivot to solutions.
**Default save path:** `./docs/management/hard-feedback-prep-YYYY-MM-DD.md` in the user's cwd. Ask before saving; ask before overwriting if file exists.
**Template:** (No shared template — produce inline.)

## Source

*Scaling People* — Claire Hughes Johnson, Stripe Press 2023 — Chapter 5, "Giving hard feedback" (subsections: Be an explorer, not a lecturer; Option 1: Ask an open-ended question; Option 2: Share an empathetic observation).

Encoded heuristic: Instead of thinking of the meeting as a hard conversation where you deliver bad news, set it up as a partnership — you're exploring a situation together. There are two methods: ask an open-ended question ("How do you think that went?") or share an empathetic observation ("I noticed the last two projects missed their deadlines…"). Both start from curiosity and shared understanding rather than suspicion and differing perspectives. The worst openers are closed questions that signal you've already made up your mind. If the open question produces denial, shift to an empathetic observation; if the observation isn't working, give your own answer. The goal is to get your report thinking with you about the problem and starting to generate solutions — that's how change actually happens.

(No shared template — produce inline.)
