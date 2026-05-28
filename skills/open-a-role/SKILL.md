---
name: open-a-role
description: Write the JD and self-selection guide that attracts the right candidates and filters out the wrong ones. Use when posting a role, especially when previous applicants have been off-target.
---

# Open a Role

This skill produces two outputs: a job description and a self-selection guide — the combination that ensures candidates who apply are genuinely suited for the role and the company, rather than projecting their aspirations onto a vague posting. Use it when a role is ready to be posted publicly, or when a prior search attracted candidates who looked good on paper but were wrong for the environment.

Part of `hiring` (Chapter 3 of *Scaling People*).

## Mode

Ask the user which mode to run in. Default to `draft` if they don't specify.

- **`teach`** — Socratic walk-through (10-20 min). Use when the user is new to this artifact or wants to internalize the framework. Walk through every heuristic in the Rubric as a question; build the artifact incrementally; explain the "why" alongside the "what."
- **`draft`** — Targeted intake → first draft → refinement (5-10 min). Use when the user knows roughly what they want. Ask the 3-5 questions listed under "Draft-mode intake" below; produce a complete first draft; offer one round of refinement against the Rubric.
- **`polish`** — Critique-and-polish (2-5 min). Use when the user pastes an existing draft. Critique against every Rubric heuristic; rewrite to address gaps; explain what changed.

## Rubric

1. **Design to entice the right candidate and discourage the wrong one.** Resist the urge to make the JD a rosy advertisement. Its job is to help people self-select accurately — both in and out. The person who starts a role that doesn't resemble the posting will be disappointed, and you will have wasted months of everyone's time.

2. **Be transparent about the work environment.** If the pace is fast and people are expected to act independently, say so plainly. Being self-aware as a company — knowing who you are and how you work — is the prerequisite to hiring well. This is not the place to soften edges.

3. **State clear role expectations, not inflated aspirations.** Open the aperture wide enough to attract candidates who have the potential to succeed, but not so wide that you attract everyone and screen no one. If the role is still being defined, say so — that ambiguity will itself be a filter. Candidates who are uncomfortable with it will opt out, which is often the right outcome.

4. **Build in your culture's self-selection questions.** Embed the questions that help candidates assess whether your company is a place they want to work. For each company principle or operating norm, surface a corresponding question that reveals whether the candidate has genuinely considered it. This is not a quiz — it is an honest invitation to reflect before applying.

5. **Watch for bias-transmitting language.** Job descriptions can contain subtle signals about who "should" or "should not" apply — language that encodes assumptions about education, background, or working style. Use tooling (like Textio) or a deliberate review pass to neutralize these signals and ensure the JD does not inadvertently narrow the candidate pool.

6. **Treat the first JD as the beginning of your talent brand.** What you say early on about your company and the roles you are hiring for is the foundation of both your talent and company brand. Take as much care with these foundations as you do with your first product releases.

7. **Include practical facts, not just marketing copy.** Company mission and culture are important — but so are benefits, work practices, and the realities of the role. Candidates calibrate fit on practical information as much as inspirational language.

## Draft-mode intake

1. "What is the role, and has it been open before or is it new?"
2. "What does the work environment actually look like — pace, autonomy, ambiguity level?"
3. "What kind of candidate would be a bad fit, even if their resume looks right?"
4. "What are the 3-5 most important things someone needs to be able to do to succeed in this role?"
5. "What are 1-2 questions a candidate should ask themselves to know whether your company is right for them?"

## Artifact

**Format:** Two sections: (1) Job Description — role summary, responsibilities, qualifications (labeled must-have vs. nice-to-have), and practical details; (2) Self-Selection Guide — 3-6 culture/environment questions tied to operating principles or working norms, with brief framing for each.
**Default save path:** `./docs/management/jd-[role]-YYYY-MM-DD.md` in the user's cwd. Ask before saving; ask before overwriting if file exists.
**Template:** Inline — no shared template.

## Source

*Scaling People* — Claire Hughes Johnson, Stripe Press 2023 — Chapter 3, "Recruiting > Open a role and help applicants self-select."

Encoded heuristic: A job description is not an advertisement — it is a filter. Its purpose is to attract candidates who are genuinely likely to succeed and help those who are not to opt out before applying. Be transparent about the work environment, the pace, and the level of ambiguity. Tie your culture principles to self-selection questions that let candidates honestly assess fit. And watch the language carefully: even well-intentioned JDs can carry bias signals that narrow the candidate pool in ways you did not intend. The JD is often the first impression a potential hire has of your company; treat it with the same care as a product launch.

(No shared template — produce inline.)
