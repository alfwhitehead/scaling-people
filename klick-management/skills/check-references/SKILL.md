---
name: check-references
description: Run a structured reference-check process — questions, calibration techniques, and read-out. Use after a candidate clears the loop and before extending an offer.
---

# Check References

This skill structures the reference-check process: which calls to make, who should make them, the questions to ask, how to interpret the answers, and how to document and act on the findings. Use it after a candidate has passed the interview loop and before you extend a verbal offer. Reference calls are not a formality — they are an additional round of data collection that the interview process, by design, cannot replicate.

Part of `hiring` (Chapter 3 of *Scaling People*).

## Mode

Use the `AskUserQuestion` tool to ask which mode to run in. Default to `draft` if the user skips or picks "Other" without specifying.

- **`teach`** — Socratic walk-through (10-20 min). Use when the user is new to this artifact or wants to internalize the framework. Walk through every heuristic in the Rubric as a question; build the artifact incrementally; explain the "why" alongside the "what."
- **`draft`** — Targeted intake → first draft → refinement (5-10 min). Use when the user knows roughly what they want. Ask the 3-5 questions listed under "Draft-mode intake" below; produce a complete first draft; offer one round of refinement against the Rubric.
- **`polish`** — Critique-and-polish (2-5 min). use when the user has already completed some reference calls and wants to interpret or document the findings. Critique for gaps; suggest additional questions or calls; help write the read-out.

**When asking the user any question during this skill** (mode selection, intake, refinement, clarification): prefer the `AskUserQuestion` tool for any question with 2-4 reasonably discrete options (the user can always pick "Other" to free-text). Use plain chat only for questions that genuinely need a sentence or paragraph of free-form response. Multi-select questions are fine when the user could legitimately choose more than one.

## Rubric

1. **Not making reference calls is a mistake.** You just ran a set of 30-45 minute interviews; a reference call gives you data from someone who has worked closely with this person, often for years. The incremental information is high. The cost of skipping is a higher rate of hiring mistakes.

2. **The hiring manager should make at least one call, ideally to the candidate's most recent manager.** For entry-level roles, the recruiter may handle all reference calls. But the more experienced the candidate and the more high-impact the role, the more important it is for the hiring manager to be personally on the phone with at least one reference who knew the candidate's work directly.

3. **A lukewarm reference is a red flag. Do not hire that person.** The candidate selected these references. They should, at a minimum, be enthusiastic. If the best their reference can say is that they were "pretty good" or "competent," you have your answer.

4. **Use the percentile question to get honest data.** Ask: "Would you say this person is in the top 50 percent of people you've worked with?" If yes: "Top 20? Top 10? Top 5?" People who want to be positive will answer vaguely if asked open-ended questions. Quantitative framing produces honest, specific answers 99 percent of the time.

5. **Ask behavioral, not evaluative, questions.** Questions like "What are their strengths and weaknesses?" invite generic, high-level answers. Behavioral questions — "When was the last time you didn't see eye to eye?" or "Tell me about a time you coached them on something" — produce specific examples that reveal real patterns.

6. **Always end with the management advice question.** "What advice do you have for me as their manager to help them be successful in this role?" This question almost always surfaces a development area the reference is willing to share. It also begins the onboarding conversation: if you hire the person, this is context you will use in your first weeks together.

7. **For leadership hires, pursue back-channel references carefully.** For senior roles, the candidate's provided references from current employment will be limited by confidentiality. Go deep with references from past companies. For back-channels, be transparent: tell the candidate you know people who've worked with them, name them, and ask if it is okay to reach out confidentially. Most candidates will say yes, and they will respect the rigor.

## Draft-mode intake

1. "What is the role and level of the candidate?"
2. "Who are the references the candidate has provided — what is each person's relationship to the candidate?"
3. "Are there any areas of FUD or unresolved concerns from the interview loop that you want to probe in references?"
4. "Who on your side will make which reference calls — recruiter, hiring manager, both?"
5. "Is this a leadership hire requiring back-channel outreach?"

## Artifact

**Format:** Markdown document with sections per reference call: reference name and relationship, key questions asked, verbatim or near-verbatim answers for each behavioral question, percentile rating given, overall signal (strong positive / lukewarm / concerning), and a final summary section with the overall reference picture and any recommended actions.
**Default save path:** `./docs/management/references-[candidate name]-YYYY-MM-DD.md` in the user's cwd. Ask before saving; ask before overwriting if file exists.
**Template:** Inline — no shared template.

## Source

*Scaling People* — Claire Hughes Johnson, Stripe Press 2023 — Chapter 3, "Hiring > Checking references."

Encoded heuristic: Reference calls are a second data collection phase, not a box-checking ritual. The candidate chose their references — if those references are lukewarm, that is your signal. Avoid generic "strengths and weaknesses" questions, which invite vague praise. Use behavioral questions that surface specific examples: the last disagreement, the coaching conversation, the ways they helped others. Use the percentile ladder — "top 50? top 20? top 10?" — to get honest quantitative signal from people who want to be positive. And always ask for management advice. It almost always reveals a development area the reference is willing to share, and it begins your onboarding relationship with the candidate if you extend the offer.

(No shared template — produce inline.)
