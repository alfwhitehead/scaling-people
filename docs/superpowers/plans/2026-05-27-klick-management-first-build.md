# klick-management Skill Library — First Build Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the `klick-management` Claude Code plugin: 6 top-level router skills (one per chapter of *Scaling People*), 14 fully-built Chapter 2 sub-skills, 35 one-line stubs for the other chapters' sub-skills, 5 shared templates, a validation script, and a README.

**Architecture:** Markdown-based Claude Code plugin. Each skill is a `skills/<name>/SKILL.md` file with YAML frontmatter (`name`, `description`) plus a body following one of two patterns: **router** (chapter overview + sub-skill list) or **sub-skill** (mode selection → rubric → artifact → source attribution). Tiering is conceptual (routers + descriptions), not file-system (loader requires flat `skills/<name>/SKILL.md`).

**Tech Stack:** Markdown, YAML frontmatter, Python 3 stdlib (for validation), git, Claude Code plugin marketplace. No build step.

**Source material location:** *Scaling People* EPUB at `/Users/awhitehead/Library/Mobile Documents/iCloud~md~obsidian/Documents/AlfVault/40-49 Career/49 Reference/49.11 Business eBooks/Scaling People_ Tactics for Management and - Claire Hughes Johnson.epub`. Extracted to `/tmp/scaling-people-epub` for content lookup during sub-skill body construction.

---

## Scope Check

This plan covers a single coherent subsystem (one plugin). It is large in line count (mostly because the universal sub-skill template is rendered once per Chapter 2 sub-skill so each task is self-contained for subagent dispatch) but every task produces a small, independently testable file. Most tasks are mutually independent and can be dispatched in parallel.

---

## File Structure

After completion the repo looks like this. The repo root IS the plugin source.

```
scaling-people-skills/                     ← repo root, also installs as plugin root
  .claude-plugin/plugin.json
  README.md
  LICENSE
  scripts/validate-skills.py
  skills/
    # 6 router skills
    operating-principles/SKILL.md
    org-foundations-and-planning/SKILL.md
    hiring/SKILL.md
    team-development/SKILL.md
    feedback-and-performance/SKILL.md
    manager-self/SKILL.md
    # 14 Ch 2 sub-skills (built)
    write-mission/SKILL.md
    write-long-term-goals/SKILL.md
    write-operating-principles/SKILL.md
    write-team-charter/SKILL.md
    plan-strategic-and-financial/SKILL.md
    design-resource-allocation/SKILL.md
    write-okrs/SKILL.md
    score-okrs/SKILL.md
    define-metrics/SKILL.md
    prep-qbr/SKILL.md
    plan-internal-comms/SKILL.md
    define-ownership-and-accountability/SKILL.md
    design-operating-cadence/SKILL.md
    audit-operating-system/SKILL.md
    # 35 stubs across Ch 1, 3, 4, 5, Conclusion
    self-awareness-assessment/SKILL.md
    write-working-with-me/SKILL.md
    prep-to-say-the-hard-thing/SKILL.md
    clarify-management-vs-leadership/SKILL.md
    define-talent-needs/SKILL.md
    open-a-role/SKILL.md
    design-interview-loop/SKILL.md
    run-candidate-review/SKILL.md
    check-references/SKILL.md
    design-leader-hiring-process/SKILL.md
    plan-onboarding/SKILL.md
    hire-postmortem/SKILL.md
    design-team-structure/SKILL.md
    diagnose-team-state/SKILL.md
    plan-reorganization/SKILL.md
    run-career-conversation/SKILL.md
    plan-delegation/SKILL.md
    plan-offsite/SKILL.md
    design-meeting/SKILL.md
    manage-distributed-or-changing-team/SKILL.md
    apply-d-and-i-lens/SKILL.md
    run-hypothesis-coaching/SKILL.md
    give-hard-feedback/SKILL.md
    build-feedback-culture/SKILL.md
    run-performance-review/SKILL.md
    prep-comp-conversation/SKILL.md
    manage-high-performer/SKILL.md
    manage-steady-middle/SKILL.md
    manage-low-performer/SKILL.md
    manage-managers/SKILL.md
    plan-departure/SKILL.md
    support-through-hardship/SKILL.md
    audit-time-and-energy/SKILL.md
    develop-key-relationships/SKILL.md
    reflect-on-career/SKILL.md
  references/
    book-frameworks/scaling-people-overview.md
    templates/team-charter.md
    templates/qbr-outline.md
    templates/okr-template.md
    templates/metrics-writeup.md
    templates/operating-principles-example.md
  docs/
    superpowers/specs/2026-05-27-klick-management-skill-library-design.md  (exists)
    superpowers/plans/2026-05-27-klick-management-first-build.md           (this file)
```

---

## Conventions (referenced by tasks below)

### §C1 — Sub-skill SKILL.md template

Every built sub-skill follows this exact structure. Tasks below specify each slot.

```markdown
---
name: <skill-slug>
description: <one-line description with explicit trigger phrases; 60-200 chars; second-person>
---

# <Skill Title in Title Case>

<One short paragraph (2-3 sentences) stating what this skill produces and when to use it. Refer to it as "this skill," not "I.">

Part of `<top-level-router-slug>` (Chapter <N> of *Scaling People*).

## Mode

Ask the user which mode to run in. Default to `draft` if they don't specify.

- **`teach`** — Socratic walk-through (10-20 min). Use when the user is new to this artifact or wants to internalize the framework. Walk through every heuristic in the Rubric as a question; build the artifact incrementally; explain the "why" alongside the "what."
- **`draft`** — Targeted intake → first draft → refinement (5-10 min). Use when the user knows roughly what they want. Ask the 3-5 questions listed under "Draft-mode intake" below; produce a complete first draft; offer one round of refinement against the Rubric.
- **`polish`** — Critique-and-polish (2-5 min). Use when the user pastes an existing draft. Critique against every Rubric heuristic; rewrite to address gaps; explain what changed.

## Rubric

<Numbered list of heuristics extracted from the relevant book section. Each item is a bold label + 1-2 sentence elaboration. This is the source-of-truth checklist all three modes pull from. Aim for 4-8 items per skill — match what the book actually offers.>

## Draft-mode intake

<3-5 short questions that gather the minimum context to produce a first draft. Always include at least one "team/role" context question and at least one "what does success look like" question.>

## Artifact

**Format:** <markdown / table / numbered list / structured doc — match what the book templates>
**Default save path:** `./docs/management/<artifact-slug>-YYYY-MM-DD.md` in the user's cwd. Ask before saving; ask before overwriting if file exists.
**Template:** <path inside `references/templates/` if a shared template applies, otherwise "Inline — no shared template.">

## Source

*Scaling People* — Claire Hughes Johnson, Stripe Press 2023 — Chapter <N>, "<exact section path from the book TOC>."

Encoded heuristic: <one-paragraph paraphrase of the central guidance this skill encodes. Quote at most one short rubric line if the book uses memorable phrasing.>

Where the book provides a template, see `references/templates/<file>.md`.
```

### §C2 — Router skill SKILL.md template

```markdown
---
name: <chapter-slug>
description: <one-line description naming the chapter's domain and listing trigger words; routes to specific sub-skills>
---

# <Chapter Title>

> Top-level router for *Scaling People* Chapter <N> — "<chapter name>."

## What this chapter is for

<~100-word paraphrase of the chapter's central framework. Same voice as the book — direct, second-person, pragmatic.>

## Sub-skills

| Skill | Use when |
|---|---|
| `<sub-skill-slug>` | <one-line trigger from the design spec> |
| ... | ... |

## If you don't know which sub-skill you need

Ask the user: "What are you trying to do?" Match their answer to the sub-skill list above and route there. If nothing fits, point them at the closest match and ask whether to proceed or back out.

## Source

*Scaling People* — Claire Hughes Johnson, Stripe Press 2023 — Chapter <N>.
```

### §C3 — Stub sub-skill SKILL.md template

```markdown
---
name: <skill-slug>
description: <one-line description with trigger phrases; same shape as a built skill>
---

# <Skill Title>

Part of `<top-level-router-slug>` (Chapter <N> of *Scaling People*).

> **Stubbed.** This skill's body has not been built yet. See the parent router for context; for now, use the book itself (Chapter <N>, "<section>") and the design spec (`docs/superpowers/specs/2026-05-27-klick-management-skill-library-design.md`) as your guide.

## Source

*Scaling People* — Claire Hughes Johnson, Stripe Press 2023 — Chapter <N>, "<exact section>."
```

### §C4 — plugin.json template

```json
{
  "name": "klick-management",
  "version": "0.1.0",
  "description": "Management practices from *Scaling People* (Claire Hughes Johnson) as Claude Code skills. Founding documents, OKRs, QBRs, hiring, team development, feedback, performance — produce real artifacts at decision points.",
  "author": {
    "name": "Klick"
  }
}
```

### §C5 — Validation contract

The validator (`scripts/validate-skills.py`) checks every `skills/*/SKILL.md`:
1. File exists and is non-empty.
2. YAML frontmatter present, parses, contains keys `name` and `description`.
3. `name` matches the parent directory name.
4. `description` is 20-400 chars (covers both short router descriptions and longer trigger-rich sub-skill descriptions).
5. Body contains the required headings for its type:
   - **Router** (one of the 6 named in `ROUTER_SLUGS`): `## Sub-skills`, `## Source`.
   - **Stub** (body contains `> **Stubbed.**`): `## Source`.
   - **Built sub-skill** (everything else): `## Mode`, `## Rubric`, `## Draft-mode intake`, `## Artifact`, `## Source`.

Exit 0 if all skills pass; exit 1 with a per-file error list otherwise.

### §C6 — Book extraction helper

A subagent picking up any Chapter 2 sub-skill task starts by ensuring the book is extracted (idempotent):

```bash
if [ ! -f /tmp/scaling-people-epub/OEBPS/Text/Chapter2.xhtml ]; then
  rm -rf /tmp/scaling-people-epub && mkdir -p /tmp/scaling-people-epub
  cd /tmp/scaling-people-epub && unzip -q "/Users/awhitehead/Library/Mobile Documents/iCloud~md~obsidian/Documents/AlfVault/40-49 Career/49 Reference/49.11 Business eBooks/Scaling People_ Tactics for Management and - Claire Hughes Johnson.epub"
fi
```

Use the `Bash` tool to read sections from `/tmp/scaling-people-epub/OEBPS/Text/Chapter<N>.xhtml` after extraction. To get plain text for a section, the same Python parser used during design works:

```python
import re, html
with open('/tmp/scaling-people-epub/OEBPS/Text/Chapter2.xhtml') as f:
    text = f.read()
text = re.sub(r'<[^>]+>', ' ', text)
text = html.unescape(text)
text = re.sub(r'\s+', ' ', text)
# then search for the section heading text and extract surrounding paragraphs
```

---

## Phase 0 — Plugin scaffold

### Task 1: Create plugin manifest and skeleton directories

**Files:**
- Create: `.claude-plugin/plugin.json`
- Create: `LICENSE`
- Create: `skills/.gitkeep`
- Create: `references/book-frameworks/.gitkeep`
- Create: `references/templates/.gitkeep`
- Create: `scripts/.gitkeep`

- [ ] **Step 1: Write `.claude-plugin/plugin.json`**

Create the file with this exact content (from §C4):

```json
{
  "name": "klick-management",
  "version": "0.1.0",
  "description": "Management practices from *Scaling People* (Claire Hughes Johnson) as Claude Code skills. Founding documents, OKRs, QBRs, hiring, team development, feedback, performance — produce real artifacts at decision points.",
  "author": {
    "name": "Klick"
  }
}
```

- [ ] **Step 2: Verify the JSON parses**

Run: `python3 -c "import json; print(json.load(open('.claude-plugin/plugin.json'))['name'])"`
Expected: `klick-management`

- [ ] **Step 3: Write `LICENSE`** (MIT)

```
MIT License

Copyright (c) 2026 Klick

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

- [ ] **Step 4: Create skeleton directories with `.gitkeep` files**

Run:
```bash
mkdir -p skills references/book-frameworks references/templates scripts
touch skills/.gitkeep references/book-frameworks/.gitkeep references/templates/.gitkeep scripts/.gitkeep
```

- [ ] **Step 5: Commit**

```bash
git add .claude-plugin LICENSE skills references scripts
git commit -m "scaffold: plugin manifest, license, skeleton directories"
```

---

### Task 2: Write `scripts/validate-skills.py`

**Files:**
- Create: `scripts/validate-skills.py`
- Test: run against the empty `skills/` directory (should pass trivially)

- [ ] **Step 1: Write the validator**

Create `scripts/validate-skills.py` with this exact content:

```python
#!/usr/bin/env python3
"""Validate every skills/*/SKILL.md against the klick-management contract.

Contract (see docs/superpowers/specs/2026-05-27-klick-management-skill-library-design.md
and the plan's §C5):
  - File exists, non-empty.
  - YAML frontmatter present, parses, has `name` and `description`.
  - `name` matches parent directory name.
  - `description` is 20-400 chars.
  - Body has the required headings for its type (router / stub / built sub-skill).
"""
from __future__ import annotations

import os
import re
import sys
from pathlib import Path

ROUTER_SLUGS = {
    "operating-principles",
    "org-foundations-and-planning",
    "hiring",
    "team-development",
    "feedback-and-performance",
    "manager-self",
}

BUILT_SUBSKILL_HEADINGS = ("## Mode", "## Rubric", "## Draft-mode intake", "## Artifact", "## Source")
ROUTER_HEADINGS = ("## Sub-skills", "## Source")
STUB_MARKER = "> **Stubbed.**"
STUB_HEADINGS = ("## Source",)


def parse_frontmatter(content: str) -> dict[str, str] | None:
    if not content.startswith("---\n"):
        return None
    end = content.find("\n---\n", 4)
    if end < 0:
        return None
    block = content[4:end]
    result: dict[str, str] = {}
    for line in block.split("\n"):
        if ":" in line:
            k, _, v = line.partition(":")
            result[k.strip()] = v.strip()
    return result


def validate_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill_md = skill_dir / "SKILL.md"
    rel = skill_md.relative_to(skill_dir.parent.parent)

    if not skill_md.exists():
        return [f"{rel}: missing SKILL.md"]

    content = skill_md.read_text()
    if not content.strip():
        return [f"{rel}: empty file"]

    fm = parse_frontmatter(content)
    if fm is None:
        return [f"{rel}: missing or malformed YAML frontmatter"]

    if "name" not in fm:
        errors.append(f"{rel}: frontmatter missing `name`")
    elif fm["name"] != skill_dir.name:
        errors.append(f"{rel}: frontmatter name '{fm['name']}' != directory name '{skill_dir.name}'")

    if "description" not in fm:
        errors.append(f"{rel}: frontmatter missing `description`")
    else:
        desc = fm["description"]
        if len(desc) < 20:
            errors.append(f"{rel}: description too short ({len(desc)} chars, min 20)")
        if len(desc) > 400:
            errors.append(f"{rel}: description too long ({len(desc)} chars, max 400)")

    # Body heading checks
    if skill_dir.name in ROUTER_SLUGS:
        required = ROUTER_HEADINGS
        kind = "router"
    elif STUB_MARKER in content:
        required = STUB_HEADINGS
        kind = "stub"
    else:
        required = BUILT_SUBSKILL_HEADINGS
        kind = "built sub-skill"

    for h in required:
        if h not in content:
            errors.append(f"{rel} ({kind}): missing required heading '{h}'")

    return errors


def main() -> int:
    repo_root = Path(__file__).resolve().parent.parent
    skills_dir = repo_root / "skills"
    if not skills_dir.is_dir():
        print(f"ERROR: skills directory not found at {skills_dir}", file=sys.stderr)
        return 1

    all_errors: list[str] = []
    skill_dirs = sorted(p for p in skills_dir.iterdir() if p.is_dir() and not p.name.startswith("."))
    for skill_dir in skill_dirs:
        all_errors.extend(validate_skill(skill_dir))

    if all_errors:
        print(f"FAIL: {len(all_errors)} validation error(s) across {len(skill_dirs)} skill(s):")
        for e in all_errors:
            print(f"  - {e}")
        return 1

    print(f"OK: {len(skill_dirs)} skill(s) validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 2: Make it executable**

Run: `chmod +x scripts/validate-skills.py`

- [ ] **Step 3: Run against empty skills/ — should pass trivially**

Run: `python3 scripts/validate-skills.py`
Expected: `OK: 0 skill(s) validated`

- [ ] **Step 4: Commit**

```bash
git add scripts/validate-skills.py
git commit -m "scaffold: add skill validator (frontmatter, naming, required headings)"
```

---

## Phase 1 — Top-level router skills (6 tasks, parallelizable)

Each task below creates one router SKILL.md following §C2. After each, run the validator and commit. All six tasks are independent — dispatch in parallel.

### Task 3: Router — `operating-principles` (Ch 1)

**Files:**
- Create: `skills/operating-principles/SKILL.md`

- [ ] **Step 1: Create the file**

```markdown
---
name: operating-principles
description: Foundational management principles — self-awareness, saying hard things, management vs leadership, returning to your operating system. Use when reflecting on your own management style, before a difficult conversation, or when situating a moment as management vs leadership.
---

# Operating Principles

> Top-level router for *Scaling People* Chapter 1 — "Essential Operating Principles."

## What this chapter is for

These four principles sit underneath every other framework in the book. Build self-awareness so you can build mutual awareness with your team. Say the thing you think you cannot say — measured, separated from the person, surfaced not stewed on. Distinguish management (running the system) from leadership (setting direction); know which moment you're in. And when you lose the plot, come back to your operating system rather than improvising your way out.

## Sub-skills

| Skill | Use when |
|---|---|
| `self-awareness-assessment` | Auditing your own values, work-style preferences, strengths, and gaps |
| `write-working-with-me` | Producing the "working with me" doc for your team, peers, or manager |
| `prep-to-say-the-hard-thing` | Preparing for a difficult conversation (share feelings, be measured, separate person from idea) |
| `clarify-management-vs-leadership` | Situating a moment: is this a management call or a leadership call, and what's appropriate? |

## If you don't know which sub-skill you need

Ask the user: "What are you trying to do?" Match their answer to the sub-skill list above and route there. If they're unsure where to start, recommend `self-awareness-assessment` — it grounds everything else.

## Source

*Scaling People* — Claire Hughes Johnson, Stripe Press 2023 — Chapter 1.
```

- [ ] **Step 2: Validate**

Run: `python3 scripts/validate-skills.py`
Expected: `OK: 1 skill(s) validated` (or more, if other Phase 1 tasks ran in parallel)

- [ ] **Step 3: Commit**

```bash
git add skills/operating-principles/SKILL.md
git commit -m "router: operating-principles (Ch 1)"
```

---

### Task 4: Router — `org-foundations-and-planning` (Ch 2)

**Files:**
- Create: `skills/org-foundations-and-planning/SKILL.md`

- [ ] **Step 1: Create the file**

```markdown
---
name: org-foundations-and-planning
description: Founding documents (mission, principles, charter), the operating system (OKRs, metrics, QBRs, resource allocation, internal comms), and operating cadence. Use when setting team mission or principles, defining goals or metrics, designing recurring forums, or diagnosing what's broken in how the team runs.
---

# Org Foundations and Planning

> Top-level router for *Scaling People* Chapter 2 — "Foundations and Planning for Goals and Resources."

## What this chapter is for

Foundations — mission, long-term goals, operating principles, team charter — are the documents that change rarely and anchor everything else. The operating system — strategic and financial planning, resource allocation, OKRs, metrics, ownership, internal comms, QBRs — is the recurring machinery that turns the foundations into work. Operating cadence is the rhythm of meetings and rituals that runs the machinery. Get these right and most other management problems get easier; get them wrong and no amount of feedback skill makes up for it.

## Sub-skills

**Founding documents**

| Skill | Use when |
|---|---|
| `write-mission` | Producing or refining a team or org mission statement |
| `write-long-term-goals` | Articulating 3–5-year aspirations or vision |
| `write-operating-principles` | Drafting a Stripe-style principles set (how we work / who we are / and leaders) |
| `write-team-charter` | Producing the charter (mission, vision, customers, metrics, strategic importance, risks, interfaces) |

**The operating system**

| Skill | Use when |
|---|---|
| `plan-strategic-and-financial` | Writing the annual strategic + financial narrative for a team or function |
| `design-resource-allocation` | Allocating FTE and budget across initiatives and communicating expectations |
| `write-okrs` | Turning rough goals into well-formed OKRs / SMART objectives |
| `score-okrs` | Mid-quarter or end-quarter scoring; handling changed priorities |
| `define-metrics` | Building the metrics framework (long-term + operating + other) |
| `prep-qbr` | Producing a quarterly business review per the book's outline |
| `plan-internal-comms` | Assessing or building an internal communications program |
| `define-ownership-and-accountability` | Clarifying ownership for a scope and the accountability mechanisms |

**Operating cadence**

| Skill | Use when |
|---|---|
| `design-operating-cadence` | Defining recurring meetings, rituals, and forums for the team |
| `audit-operating-system` | Diagnosing what's wrong with the current operating system or cadence |

## If you don't know which sub-skill you need

Ask the user: "What are you trying to do?" Match their answer to the sub-skill list above. If they're early in setting up a team or function, recommend `write-team-charter` first — it forces the foundational questions in one pass.

## Source

*Scaling People* — Claire Hughes Johnson, Stripe Press 2023 — Chapter 2.
```

- [ ] **Step 2: Validate**

Run: `python3 scripts/validate-skills.py`
Expected: validator passes; this skill listed as a router.

- [ ] **Step 3: Commit**

```bash
git add skills/org-foundations-and-planning/SKILL.md
git commit -m "router: org-foundations-and-planning (Ch 2)"
```

---

### Task 5: Router — `hiring` (Ch 3)

**Files:**
- Create: `skills/hiring/SKILL.md`

- [ ] **Step 1: Create the file**

```markdown
---
name: hiring
description: Recruiting, hiring (IC and leader), onboarding, and closing the loop on hiring mistakes. Use when opening a role, writing a scorecard, designing an interview loop, debriefing candidates, planning onboarding for a new hire or new leader, or running a post-mortem on a hire that didn't work.
---

# Hiring

> Top-level router for *Scaling People* Chapter 3 — "A Comprehensive Hiring Approach."

## What this chapter is for

Hiring is the most leveraged thing a manager does — better-than-average hires compound; below-average hires create work for everyone for years. The book breaks hiring into recruiting (insights on talent, opening roles well, referrals, screening, leader recruiting), hiring (interview design, decision-making, candidate review, references, offers), onboarding (the New Leader Experience for leaders; structured ramps for ICs), and the discipline of closing the loop when a hire doesn't work.

## Sub-skills

| Skill | Use when |
|---|---|
| `define-talent-needs` | Building insight on what success in the role actually looks like before opening it |
| `open-a-role` | Writing the job description + scorecard that lets candidates self-select |
| `design-interview-loop` | Building the rubric, questions, and (where useful) a written exercise |
| `run-candidate-review` | Facilitating the decision-making forum per the book's framework |
| `check-references` | Reference-check questions, analysis, weighting |
| `design-leader-hiring-process` | Leader hire specifics: stakeholder loop, feedback-collection-not-decision forum |
| `plan-onboarding` | Building the onboarding plan (IC or new leader / NLE) |
| `hire-postmortem` | Closing the loop on a hire — especially one that didn't work |

## If you don't know which sub-skill you need

Ask the user: "Where in the hiring loop are you?" Map to the table above. If they're opening a role from scratch, run `define-talent-needs` first; then `open-a-role`.

## Source

*Scaling People* — Claire Hughes Johnson, Stripe Press 2023 — Chapter 3.
```

- [ ] **Step 2: Validate**

Run: `python3 scripts/validate-skills.py`

- [ ] **Step 3: Commit**

```bash
git add skills/hiring/SKILL.md
git commit -m "router: hiring (Ch 3)"
```

---

### Task 6: Router — `team-development` (Ch 4)

**Files:**
- Create: `skills/team-development/SKILL.md`

- [ ] **Step 1: Create the file**

```markdown
---
name: team-development
description: Team structures, diagnosing team state, reorganizations, career conversations, delegation, offsites, meeting design, distributed teams, and a D&I lens. Use when shaping or reshaping a team, diagnosing dysfunction, planning a reorg, running a career conversation, designing meetings or offsites, or applying a D&I review.
---

# Team Development

> Top-level router for *Scaling People* Chapter 4 — "Intentional Team Development."

## What this chapter is for

Teams don't develop themselves. The book covers how to shape teams (structures, layering, business leads, span of control), how to diagnose what's actually going on (skill/will, underperforming teams), how to change structures when needed (the three-phase reorg), and how to build the team environment (career conversations, delegation, offsites, meetings, distributed work, managing through uncertainty, D&I). The throughline: be deliberate. Don't let team shape and norms happen to you.

## Sub-skills

| Skill | Use when |
|---|---|
| `design-team-structure` | Shaping a team: teams vs working groups, layering, # reports, business leads |
| `diagnose-team-state` | Skill/will diagnosis + underperforming-team probes |
| `plan-reorganization` | Running the three-phase reorg (decide → buy-in → comms) |
| `run-career-conversation` | Prep + script for a development conversation with a direct report |
| `plan-delegation` | Deciding when to delegate, how, and to whom |
| `plan-offsite` | Picking offsite type by team stage; agenda, check-ins, run-of-show |
| `design-meeting` | Purpose, roles, norms, decision-making for any recurring meeting (incl. leadership team variant) |
| `manage-distributed-or-changing-team` | Remote/distributed practices + managing through uncertainty or crisis |
| `apply-d-and-i-lens` | Cross-cutting D&I review for hiring, performance, and team practices |

## If you don't know which sub-skill you need

Ask the user: "Is this about team shape, team state, or team rituals?" Shape → `design-team-structure` or `plan-reorganization`. State → `diagnose-team-state`. Rituals → `design-meeting`, `plan-offsite`, `run-career-conversation`.

## Source

*Scaling People* — Claire Hughes Johnson, Stripe Press 2023 — Chapter 4.
```

- [ ] **Step 2: Validate**

Run: `python3 scripts/validate-skills.py`

- [ ] **Step 3: Commit**

```bash
git add skills/team-development/SKILL.md
git commit -m "router: team-development (Ch 4)"
```

---

### Task 7: Router — `feedback-and-performance` (Ch 5)

**Files:**
- Create: `skills/feedback-and-performance/SKILL.md`

- [ ] **Step 1: Create the file**

```markdown
---
name: feedback-and-performance
description: Hypothesis-based coaching, hard feedback, informal feedback culture, formal reviews, calibration, compensation, managing high/middle/low performers, managing managers, managing out, firing, layoffs, and supporting through hardship. Use before delivering feedback, during review season, before a comp conversation, or when a performance situation needs careful handling.
---

# Feedback and Performance

> Top-level router for *Scaling People* Chapter 5 — "Feedback and Performance Mechanisms."

## What this chapter is for

Most management work eventually shows up here. The book frames coaching as hypothesis-driven (gather data → form hypothesis → test), feedback as exploratory (be an explorer, not a lecturer), and performance management as a system of mechanisms (informal feedback culture, formal reviews, calibration, comp) that need to operate together. It also covers the people-specific work: keeping high performers engaged, developing the steady middle, managing low performers through phased steps, managing managers, managing out / firing / layoffs, and supporting employees through hardship.

## Sub-skills

| Skill | Use when |
|---|---|
| `run-hypothesis-coaching` | Coaching someone: gather data → form hypothesis → test |
| `give-hard-feedback` | Preparing to deliver difficult feedback (explorer, not lecturer) |
| `build-feedback-culture` | Designing the team's informal feedback practices |
| `run-performance-review` | Running peer / self / manager review + calibration |
| `prep-comp-conversation` | Preparing for a compensation conversation |
| `manage-high-performer` | Pushers/pullers, retention, anti-boredom, no-promo conversations |
| `manage-steady-middle` | Engaging and developing the dependable core |
| `manage-low-performer` | Phased approach, PIP, role move |
| `manage-managers` | Manager-of-managers dynamics; 1:1 variants for managers |
| `plan-departure` | Managing out, firing for misconduct, layoffs |
| `support-through-hardship` | Supporting an employee through a one-time event, ongoing hardship, or legal situation |

## If you don't know which sub-skill you need

Ask the user: "Whose performance, and what stage?" If high performer at risk of disengaging → `manage-high-performer`. If pattern of underperformance → `manage-low-performer`. If a specific upcoming conversation → `give-hard-feedback` or `prep-comp-conversation`.

## Source

*Scaling People* — Claire Hughes Johnson, Stripe Press 2023 — Chapter 5.
```

- [ ] **Step 2: Validate**

Run: `python3 scripts/validate-skills.py`

- [ ] **Step 3: Commit**

```bash
git add skills/feedback-and-performance/SKILL.md
git commit -m "router: feedback-and-performance (Ch 5)"
```

---

### Task 8: Router — `manager-self` (Conclusion)

**Files:**
- Create: `skills/manager-self/SKILL.md`

- [ ] **Step 1: Create the file**

```markdown
---
name: manager-self
description: Managing yourself — time and energy, key relationships (your manager, peers, execs), career reflection. Use when energy is low or scattered, when relationships with your manager or peers feel off, or when you're due for a career check-in.
---

# Manager Self

> Top-level router for *Scaling People* Conclusion — "You."

## What this chapter is for

The work doesn't sustain unless you do. This short chapter covers the three things managers neglect about themselves: their time and energy (what's hard vs easy for you, where you're most productive, when to disappoint people), their key relationships (working well with your own manager, peer managers, founders/execs), and their own career trajectory.

## Sub-skills

| Skill | Use when |
|---|---|
| `audit-time-and-energy` | Auditing where your time goes; setting boundaries; finding your productive windows |
| `develop-key-relationships` | Working better with your manager, peer managers, or founders/execs |
| `reflect-on-career` | Career check-in for the manager themselves |

## If you don't know which sub-skill you need

Ask: "Is this about your time, your relationships, or your career?" Route accordingly.

## Source

*Scaling People* — Claire Hughes Johnson, Stripe Press 2023 — Conclusion ("You").
```

- [ ] **Step 2: Validate**

Run: `python3 scripts/validate-skills.py`

- [ ] **Step 3: Commit**

```bash
git add skills/manager-self/SKILL.md
git commit -m "router: manager-self (Conclusion)"
```

---

## Phase 2 — Stub sub-skills (5 batch tasks, parallelizable)

Each task creates the stub SKILL.md files for one chapter's sub-skills in a single commit. Use the §C3 template for every file. Run the validator at the end of each task.

### Task 9: Stubs — Ch 1 sub-skills (4 files)

**Files:**
- Create: `skills/self-awareness-assessment/SKILL.md`
- Create: `skills/write-working-with-me/SKILL.md`
- Create: `skills/prep-to-say-the-hard-thing/SKILL.md`
- Create: `skills/clarify-management-vs-leadership/SKILL.md`

- [ ] **Step 1: Create `skills/self-awareness-assessment/SKILL.md`**

```markdown
---
name: self-awareness-assessment
description: Self-awareness audit — values, work-style preferences (analyzer/director/promoter/collaborator), strengths and gaps. Use when starting a new role, before producing your working-with-me doc, or when stuck on a recurring management problem you might be the source of.
---

# Self-Awareness Assessment

Part of `operating-principles` (Chapter 1 of *Scaling People*).

> **Stubbed.** This skill's body has not been built yet. See the parent router for context; for now, use the book itself (Chapter 1, "Build self-awareness to build mutual awareness") and the design spec (`docs/superpowers/specs/2026-05-27-klick-management-skill-library-design.md`) as your guide.

## Source

*Scaling People* — Claire Hughes Johnson, Stripe Press 2023 — Chapter 1, "Build self-awareness to build mutual awareness."
```

- [ ] **Step 2: Create `skills/write-working-with-me/SKILL.md`**

```markdown
---
name: write-working-with-me
description: Produce the "working with me" doc your team, peers, and manager read to understand how you operate. Use after a self-awareness assessment, when joining a new team or taking on a new manager, or when feedback suggests your team is misreading your style.
---

# Write Working-With-Me

Part of `operating-principles` (Chapter 1 of *Scaling People*).

> **Stubbed.** This skill's body has not been built yet. See the parent router for context; for now, use the book itself (Chapter 3 templates section, "Working with Me Template" — referenced as a Ch 1 artifact in this library because it's the output of self-awareness work) and the design spec as your guide.

## Source

*Scaling People* — Claire Hughes Johnson, Stripe Press 2023 — Chapter 3 templates, "Working with Me Template" (rooted in Chapter 1 self-awareness work).
```

- [ ] **Step 3: Create `skills/prep-to-say-the-hard-thing/SKILL.md`**

```markdown
---
name: prep-to-say-the-hard-thing
description: Prepare to say the thing you think you cannot say — share feelings, be measured, separate the person from the idea or task. Use before any difficult conversation: feedback, escalation, pushback to your manager, disagreement with a peer.
---

# Prep to Say the Hard Thing

Part of `operating-principles` (Chapter 1 of *Scaling People*).

> **Stubbed.** This skill's body has not been built yet. See the parent router for context; for now, use the book itself (Chapter 1, "Say the thing you think you cannot say") and the design spec as your guide.

## Source

*Scaling People* — Claire Hughes Johnson, Stripe Press 2023 — Chapter 1, "Say the thing you think you cannot say."
```

- [ ] **Step 4: Create `skills/clarify-management-vs-leadership/SKILL.md`**

```markdown
---
name: clarify-management-vs-leadership
description: Situate a moment as a management call (running the system) vs a leadership call (setting direction), and choose the appropriate response. Use when you're unsure whether to enforce a process or change the process, or whether a problem needs operating-system attention vs vision attention.
---

# Clarify Management vs Leadership

Part of `operating-principles` (Chapter 1 of *Scaling People*).

> **Stubbed.** This skill's body has not been built yet. See the parent router for context; for now, use the book itself (Chapter 1, "Distinguish between management and leadership" and "Come back to your operating system") and the design spec as your guide.

## Source

*Scaling People* — Claire Hughes Johnson, Stripe Press 2023 — Chapter 1, "Distinguish between management and leadership."
```

- [ ] **Step 5: Validate**

Run: `python3 scripts/validate-skills.py`
Expected: all skills pass.

- [ ] **Step 6: Commit**

```bash
git add skills/self-awareness-assessment skills/write-working-with-me skills/prep-to-say-the-hard-thing skills/clarify-management-vs-leadership
git commit -m "stubs: Ch 1 sub-skills (4 placeholders)"
```

---

### Task 10: Stubs — Ch 3 sub-skills (8 files)

**Files:**
- Create: `skills/define-talent-needs/SKILL.md`
- Create: `skills/open-a-role/SKILL.md`
- Create: `skills/design-interview-loop/SKILL.md`
- Create: `skills/run-candidate-review/SKILL.md`
- Create: `skills/check-references/SKILL.md`
- Create: `skills/design-leader-hiring-process/SKILL.md`
- Create: `skills/plan-onboarding/SKILL.md`
- Create: `skills/hire-postmortem/SKILL.md`

- [ ] **Step 1-8: For each file above, create using the §C3 stub template with the slots below.**

Use this stub template (§C3) for all 8 files, substituting the per-file values:

```markdown
---
name: <slug>
description: <description>
---

# <Title>

Part of `hiring` (Chapter 3 of *Scaling People*).

> **Stubbed.** This skill's body has not been built yet. See the parent router for context; for now, use the book itself (Chapter 3, "<section>") and the design spec (`docs/superpowers/specs/2026-05-27-klick-management-skill-library-design.md`) as your guide.

## Source

*Scaling People* — Claire Hughes Johnson, Stripe Press 2023 — Chapter 3, "<section>."
```

Per-file values:

| slug | description | section | title |
|---|---|---|---|
| `define-talent-needs` | Build insight on what success in the role looks like before opening it — capabilities, experience, working style, growth runway. Use at the start of any new role or before backfilling. | Recruiting > Build insights on talent needs and candidate success | Define Talent Needs |
| `open-a-role` | Write the JD + scorecard that helps candidates self-select. Use when posting a role; especially when previous applicants have been off-target. | Recruiting > Open a role and help applicants self-select | Open a Role |
| `design-interview-loop` | Design the interview rubric, questions, and (where useful) a written exercise for a role. Use when building or updating the loop for a specific role. | Hiring > Interviewing | Design Interview Loop |
| `run-candidate-review` | Facilitate the candidate-review decision-making forum per the book's framework. Use after a candidate's loop closes and before extending an offer. | Hiring > Candidate review | Run Candidate Review |
| `check-references` | Reference-check questions, analysis, and weighting. Use after a candidate has cleared the loop and before an offer. | Hiring > Checking references | Check References |
| `design-leader-hiring-process` | Design a leader hiring process — stakeholder loop, feedback-collection-not-decision forum, transparency. Use when hiring a director or above. | Hiring > The hiring process for leadership | Design Leader Hiring Process |
| `plan-onboarding` | Build the onboarding plan — for an IC or for a new leader (NLE). Mode handles both. Use as soon as an offer is accepted. | Onboarding > New hire onboarding and New leader onboarding | Plan Onboarding |
| `hire-postmortem` | Close the loop on a hire — especially one that didn't work. Use when a hire has departed, been managed out, or significantly underperformed. | Hiring mistakes > Close your hiring loop | Hire Postmortem |

- [ ] **Step 9: Validate**

Run: `python3 scripts/validate-skills.py`
Expected: all skills pass.

- [ ] **Step 10: Commit**

```bash
git add skills/define-talent-needs skills/open-a-role skills/design-interview-loop skills/run-candidate-review skills/check-references skills/design-leader-hiring-process skills/plan-onboarding skills/hire-postmortem
git commit -m "stubs: Ch 3 sub-skills (8 placeholders)"
```

---

### Task 11: Stubs — Ch 4 sub-skills (9 files)

**Files:** 9 directories under `skills/`, one SKILL.md each.

- [ ] **Step 1-9: Create each file using the §C3 stub template with `hiring` replaced by `team-development` and Chapter 3 replaced by Chapter 4. Per-file values:**

| slug | description | section | title |
|---|---|---|---|
| `design-team-structure` | Shape a team — teams vs working groups vs projects, layering, # reports, business leads. Use when forming a team, adding headcount, or rethinking reporting lines. | Team structures | Design Team Structure |
| `diagnose-team-state` | Diagnose team state — skill/will quadrants + probes for an underperforming team. Use when a team is missing goals or feels off. | Diagnosing team state and Team-building complexities > Underperforming teams | Diagnose Team State |
| `plan-reorganization` | Run the three-phase reorg — decide structure (one month) → get buy-in (one to two weeks) → communicate (one to two days). Use when restructuring is on the table. | Team changes and restructuring | Plan Reorganization |
| `run-career-conversation` | Prep + script for a development conversation with a direct report. Use at least quarterly per report; more often during a transition. | (Re)building the team > Career conversations | Run Career Conversation |
| `plan-delegation` | Decide when, how, and to whom to delegate a piece of work. Use when your plate is full or when developing a report through stretch work. | (Re)building the team > Delegating | Plan Delegation |
| `plan-offsite` | Pick offsite type by team development stage; design agenda, check-ins, run-of-show. Use when planning a team or leadership-team offsite. | Creating the team environment > Offsites | Plan Offsite |
| `design-meeting` | Purpose, roles, norms, decision-making for any recurring meeting (incl. leadership-team variant). Use when starting a new recurring meeting or fixing one that's broken. | Creating the team environment > Meetings | Design Meeting |
| `manage-distributed-or-changing-team` | Remote/distributed practices + managing through uncertainty or crisis. Use when going distributed, adding remote workers, or leading through a change/crisis. | Team-building complexities > Managing distributed and remote teams and Managing through uncertainty | Manage Distributed or Changing Team |
| `apply-d-and-i-lens` | Apply a D&I review across hiring, performance, and team practices. Use during hiring loop design, calibration, or when designing team rituals. | Diversity and inclusion | Apply D&I Lens |

- [ ] **Step 10: Validate**

Run: `python3 scripts/validate-skills.py`

- [ ] **Step 11: Commit**

```bash
git add skills/design-team-structure skills/diagnose-team-state skills/plan-reorganization skills/run-career-conversation skills/plan-delegation skills/plan-offsite skills/design-meeting skills/manage-distributed-or-changing-team skills/apply-d-and-i-lens
git commit -m "stubs: Ch 4 sub-skills (9 placeholders)"
```

---

### Task 12: Stubs — Ch 5 sub-skills (11 files)

**Files:** 11 directories under `skills/`, one SKILL.md each.

- [ ] **Step 1-11: Create each file using the §C3 stub template with `team-development` replaced by `feedback-and-performance` and Chapter 4 replaced by Chapter 5. Per-file values:**

| slug | description | section | title |
|---|---|---|---|
| `run-hypothesis-coaching` | Coach a report by gathering data → forming a hypothesis → testing it. Use when behavior is off and you don't yet know why. | Hypothesis-based coaching | Run Hypothesis Coaching |
| `give-hard-feedback` | Prepare to deliver difficult feedback as an explorer, not a lecturer (open question OR empathetic observation). Use before any hard 1:1. | Giving hard feedback | Give Hard Feedback |
| `build-feedback-culture` | Design the team's informal feedback practices — asking for it, giving it, normalizing it. Use when starting a team or when feedback feels stuck. | Creating a culture of informal feedback | Build Feedback Culture |
| `run-performance-review` | Run the formal review process — peer reviews, self-assessment, manager review, calibration. Use during review season. | The formal review process | Run Performance Review |
| `prep-comp-conversation` | Prepare for a compensation conversation — educate yourself, instill trust in the system, understand motivators, have the talk. Use before every comp delivery. | Compensation | Prep Comp Conversation |
| `manage-high-performer` | Manage high performers — pushers/pullers, retention, anti-boredom, telling them they won't be promoted. Use when a top performer is at risk of disengaging or flight. | Managing high performers | Manage High Performer |
| `manage-steady-middle` | Engage and develop the dependable core. Use when a steady performer needs visible investment or a fresh challenge. | The steady middle | Manage Steady Middle |
| `manage-low-performer` | Manage a low performer through the phased approach — hypothesis → align → next steps → action plan → PIP or role move. Use as soon as the pattern is clear. | Managing low performers | Manage Low Performer |
| `manage-managers` | Manager-of-managers dynamics: individual 1:1s vs manager 1:1s; managing when you're not the expert. Use when stepping up to manage managers. | Managing managers | Manage Managers |
| `plan-departure` | Plan managing out, firing for misconduct, or a layoff — pre-work, the conversation (junior vs senior), legal considerations. Use as soon as departure is the path. | Managing out, firing, and layoffs | Plan Departure |
| `support-through-hardship` | Support an employee through a one-time event, ongoing hardship, or a situation with legal ramifications. Use as soon as you become aware. | Managing out, firing, and layoffs > When something bad happens to an employee | Support Through Hardship |

- [ ] **Step 12: Validate**

Run: `python3 scripts/validate-skills.py`

- [ ] **Step 13: Commit**

```bash
git add skills/run-hypothesis-coaching skills/give-hard-feedback skills/build-feedback-culture skills/run-performance-review skills/prep-comp-conversation skills/manage-high-performer skills/manage-steady-middle skills/manage-low-performer skills/manage-managers skills/plan-departure skills/support-through-hardship
git commit -m "stubs: Ch 5 sub-skills (11 placeholders)"
```

---

### Task 13: Stubs — Conclusion sub-skills (3 files)

**Files:** 3 directories under `skills/`, one SKILL.md each.

- [ ] **Step 1-3: Create each file using the §C3 stub template with parent `manager-self` and "Chapter X" replaced by "Conclusion ('You')". Per-file values:**

| slug | description | section | title |
|---|---|---|---|
| `audit-time-and-energy` | Audit where your time goes; figure out which tasks are easy vs hard for you; set boundaries; identify productive windows. Use quarterly, or when energy is scattered. | Manage your time and energy | Audit Time and Energy |
| `develop-key-relationships` | Work better with your own manager, peer managers, or founders/execs. Use when a key relationship feels off or before a high-stakes interaction. | Foster relationships | Develop Key Relationships |
| `reflect-on-career` | Career check-in for the manager themselves — what are you optimizing for, what would change your decision tree, what feedback would you need. Use annually, or after a major role transition. | Consider your career | Reflect on Career |

- [ ] **Step 4: Validate**

Run: `python3 scripts/validate-skills.py`

- [ ] **Step 5: Commit**

```bash
git add skills/audit-time-and-energy skills/develop-key-relationships skills/reflect-on-career
git commit -m "stubs: Conclusion sub-skills (3 placeholders)"
```

---

## Phase 3 — Chapter 2 sub-skill bodies (14 tasks, parallelizable)

Each task below builds one Ch 2 sub-skill's full body following §C1. Per-task workflow:

1. Ensure the book is extracted (use the §C6 helper).
2. Read the named section of `/tmp/scaling-people-epub/OEBPS/Text/Chapter2.xhtml` to extract the rubric heuristics.
3. Write the SKILL.md using the §C1 template with the slots specified below.
4. Run the validator.
5. Commit.

The tasks specify everything except the **Rubric body**, which is extracted from the book section. The Rubric must:
- Be 4-8 numbered items.
- Each item: bold label + 1-2 sentence elaboration in the skill's voice (direct, second-person, no fluff).
- Cover only what the book's named section actually teaches — don't pad from general management knowledge.

### Task 14: `write-mission`

**Files:**
- Create: `skills/write-mission/SKILL.md`

- [ ] **Step 1: Ensure book extracted**

Run §C6 extraction block.

- [ ] **Step 2: Read book section**

Open `/tmp/scaling-people-epub/OEBPS/Text/Chapter2.xhtml` and locate the section starting at the H3 "Mission" (under H2 "Founding documents"). Read through to the next H3 ("Long-term goals"). Extract the heuristics the book gives for what a good mission statement does and doesn't do.

- [ ] **Step 3: Write `skills/write-mission/SKILL.md`**

Use the §C1 template with these slots:

- `<skill-slug>` → `write-mission`
- `<description>` → `Produce or refine a team or org mission statement. Use when starting a new team, when the existing mission no longer guides decisions, or when leadership above you has set a mission and you need a team-level version that rolls up cleanly.`
- `<Skill Title>` → `Write Mission`
- Opening paragraph → "This skill produces a mission statement — one sentence (occasionally two) stating what the team or org exists to do. Use it when the mission is missing, stale, or aspirational-without-being-useful. The output should be concrete enough to guide a real decision the same week you publish it."
- `<top-level-router-slug>` → `org-foundations-and-planning`
- `<N>` → `2`
- **Rubric** → extracted from Step 2; 4-8 items
- **Draft-mode intake** →
  1. "Whose mission is this — a team, a function, a whole org?"
  2. "Who are the people you serve, in one phrase?"
  3. "What does the team do, in one verb phrase?"
  4. "What changes for those people if you succeed?"
  5. "What's a recent decision the new mission should have made obvious?"
- **Artifact**:
  - Format: `Markdown — a heading-level mission line plus a 1-paragraph rationale plus a "rejected alternatives" list of 2-3 considered-and-cut wordings.`
  - Default save path: as in template
  - Template: `Inline — no shared template.`
- **Source**:
  - Section: `Founding documents > Mission`
  - Encoded heuristic: extracted from Step 2; one paragraph
  - Template reference: `references/templates/operating-principles-example.md` (only for contrast — mission vs principles)

- [ ] **Step 4: Validate**

Run: `python3 scripts/validate-skills.py`

- [ ] **Step 5: Commit**

```bash
git add skills/write-mission/SKILL.md
git commit -m "skill: write-mission (Ch 2)"
```

---

### Task 15: `write-long-term-goals`

**Files:**
- Create: `skills/write-long-term-goals/SKILL.md`

- [ ] **Step 1: Ensure book extracted** (per §C6)

- [ ] **Step 2: Read book section**

In Chapter2.xhtml, locate H3 "Long-term goals" (under H2 "Founding documents"). Read through to the next H3 ("Principles"). Extract heuristics for long-term/aspirational goals.

- [ ] **Step 3: Write `skills/write-long-term-goals/SKILL.md`**

§C1 template with slots:

- slug: `write-long-term-goals`
- description: `Articulate 3-5 year long-term goals or vision for a team or org. Use when the mission exists but the team can't see the medium-term picture, or when annual planning keeps surfacing "but where are we headed?" questions.`
- Title: `Write Long-Term Goals`
- Opening: "This skill produces a small set of 3-5 year goals or a vision statement that sits between the mission (timeless) and annual OKRs (12 months). Use it when the team is shipping work but can't articulate what they're building toward."
- router: `org-foundations-and-planning`, N=2
- Rubric: extract from Step 2
- Draft-mode intake:
  1. "What's the team's mission today?"
  2. "Three years out, what does success look like in plain language?"
  3. "What would be true that isn't true today?"
  4. "What's a current bet that has to pay off for this to happen?"
- Artifact format: `Markdown — a vision/long-term statement plus 3-5 supporting long-term goals, each with one-sentence success condition.`
- Source section: `Founding documents > Long-term goals`
- Template reference: `Inline — no shared template.`

- [ ] **Step 4: Validate** (`python3 scripts/validate-skills.py`)

- [ ] **Step 5: Commit** (`git commit -m "skill: write-long-term-goals (Ch 2)"`)

---

### Task 16: `write-operating-principles`

**Files:**
- Create: `skills/write-operating-principles/SKILL.md`

- [ ] **Step 1: Ensure book extracted**

- [ ] **Step 2: Read book section**

In Chapter2.xhtml, locate H3 "Principles" and the sidebar H3 "A quick guide to Stripe's culture" (with subsections "We haven't won yet," "Move with urgency and focus," "Think rigorously"). Also locate the H3 "Stripe's Operating Principles" in the Exercises and templates section (with How we work / Who we are / And leaders structure). Extract: (a) what makes a good principle, (b) the three-category structure, (c) how principles differ from mission/values.

- [ ] **Step 3: Write `skills/write-operating-principles/SKILL.md`**

§C1 template with slots:

- slug: `write-operating-principles`
- description: `Draft a set of operating principles in Stripe-style three-category structure (how we work / who we are / and leaders). Use when the team is large enough that decisions need a shared sense of "how we do things here" without you in every conversation.`
- Title: `Write Operating Principles`
- Opening: "This skill produces a set of operating principles — short, memorable statements that describe how the team works, who its members are, and what's expected of its leaders. Principles complement (don't replace) mission and values: mission says why, principles say how."
- router: `org-foundations-and-planning`, N=2
- Rubric: extract from Step 2 — including the three-category split as one of the items
- Draft-mode intake:
  1. "What's the team or org?"
  2. "What do you most want people to do more of?"
  3. "What do you most want people to do less of?"
  4. "What does a great leader on this team look like?"
  5. "Any existing values or principles to extend or reconcile with?"
- Artifact format: `Markdown — three sections (How we work / Who we are / And leaders), each with 4-6 principles. Each principle: a short headline + 2-4 sentence elaboration with example behaviors.`
- Source section: `Founding documents > Principles` + `Stripe's Operating Principles` (templates section)
- Template reference: `references/templates/operating-principles-example.md`

- [ ] **Step 4: Validate**

- [ ] **Step 5: Commit** (`git commit -m "skill: write-operating-principles (Ch 2)"`)

---

### Task 17: `write-team-charter`

**Files:**
- Create: `skills/write-team-charter/SKILL.md`

- [ ] **Step 1: Ensure book extracted**

- [ ] **Step 2: Read book section**

In Chapter2.xhtml, locate H3 "Team charters" (under H2 "Founding documents" sidebar) and the H3 "Team Charter" in the Exercises and templates section. Extract: the charter template fields (Mission, Vision, Customers, Metrics, Strategic importance, Major risks, Provided interfaces, Dependent interfaces) and the book's guidance on each.

- [ ] **Step 3: Write `skills/write-team-charter/SKILL.md`**

§C1 template with slots:

- slug: `write-team-charter`
- description: `Produce a team charter covering mission, vision, customers, metrics, strategic importance, major risks, and provided/dependent interfaces. Use when forming a new team, taking over an existing team, or when cross-team friction suggests responsibilities aren't clear.`
- Title: `Write Team Charter`
- Opening: "This skill produces a team charter — the one-document answer to 'what is this team, who does it serve, what does it own, and what does it depend on?' Use it to force the foundational questions in one pass and to give the rest of the org a single artifact to react to."
- router: `org-foundations-and-planning`, N=2
- Rubric: extract from Step 2 — the eight fields + guidance per field
- Draft-mode intake:
  1. "What's the team and how many people?"
  2. "Who are your primary internal/external customers?"
  3. "What top 2-3 metrics will you be measured on?"
  4. "What does the rest of the org most often misunderstand about this team?"
  5. "What teams do you most depend on, and which depend most on you?"
- Artifact format: `Markdown — populated charter template per references/templates/team-charter.md.`
- Source section: `Founding documents > Team charters` + `Team Charter` template
- Template reference: `references/templates/team-charter.md`

- [ ] **Step 4: Validate**

- [ ] **Step 5: Commit** (`git commit -m "skill: write-team-charter (Ch 2)"`)

---

### Task 18: `plan-strategic-and-financial`

**Files:**
- Create: `skills/plan-strategic-and-financial/SKILL.md`

- [ ] **Step 1: Ensure book extracted**

- [ ] **Step 2: Read book section**

In Chapter2.xhtml, locate H3 "Strategic and financial planning" (under H2 "The operating system"). Read through to the next H3 ("Resource allocation"). Extract: the book's guidance on what the strategic plan covers, who participates, and how it ties to the financial plan.

- [ ] **Step 3: Write `skills/plan-strategic-and-financial/SKILL.md`**

§C1 template with slots:

- slug: `plan-strategic-and-financial`
- description: `Produce the annual strategic and financial planning narrative for a team or function — what we're doing, why, the bets we're making, and the money/people that requires. Use during planning season or when handing off to a new finance partner.`
- Title: `Plan Strategic and Financial`
- Opening: "This skill produces the annual strategic + financial planning narrative — the document that connects the team's strategy to the resources (people, money, time) it needs. Use it during planning season; it's the bridge between the team charter and the year's OKRs."
- router: `org-foundations-and-planning`, N=2
- Rubric: extract from Step 2
- Draft-mode intake:
  1. "What's the planning period and the team scope?"
  2. "What are the 2-4 strategic bets you're proposing for the period?"
  3. "What's your headcount and budget today?"
  4. "What changes are you asking for, and what would each unlock?"
- Artifact format: `Markdown — narrative (1-2 pages) + headcount/budget tables.`
- Source section: `The operating system > Strategic and financial planning`
- Template reference: `Inline — no shared template.`

- [ ] **Step 4: Validate**

- [ ] **Step 5: Commit** (`git commit -m "skill: plan-strategic-and-financial (Ch 2)"`)

---

### Task 19: `design-resource-allocation`

**Files:**
- Create: `skills/design-resource-allocation/SKILL.md`

- [ ] **Step 1: Ensure book extracted**

- [ ] **Step 2: Read book section**

In Chapter2.xhtml, locate H3 "Resource allocation" (under H2 "The operating system") AND the sidebar H3 "Setting expectations around resource allocation" AND H3 "Investing in developer productivity" (which is a worked example). Read through to the next H3 ("Annual and quarterly goals"). Extract: the book's guidance on how to allocate FTE/budget, communicate the allocation, and the productivity-investment principle.

- [ ] **Step 3: Write `skills/design-resource-allocation/SKILL.md`**

§C1 template with slots:

- slug: `design-resource-allocation`
- description: `Allocate FTE and budget across initiatives and communicate the expectations that come with the allocation. Use during planning, after a reorg, or when teams keep asking "is this funded?"`
- Title: `Design Resource Allocation`
- Opening: "This skill produces a resource allocation — FTE and budget split across initiatives — plus the expectations that go with it. Use it when the strategic plan is set and you need to translate it into who works on what, how much, and with what success conditions."
- router: `org-foundations-and-planning`, N=2
- Rubric: extract from Step 2 — including productivity investment as a heuristic
- Draft-mode intake:
  1. "What's the total FTE and budget under your control for the period?"
  2. "What's the proposed split across initiatives?"
  3. "What's the expected outcome per initiative?"
  4. "What's the under-invested area you're tempted to defer (e.g., productivity, infra) — and why?"
- Artifact format: `Markdown — allocation table (initiative / FTE / budget / outcome / owner) + a short "expectations" section.`
- Source section: `The operating system > Resource allocation` (incl. Setting expectations sidebar and Investing in developer productivity sidebar)
- Template reference: `Inline — no shared template.`

- [ ] **Step 4: Validate**

- [ ] **Step 5: Commit** (`git commit -m "skill: design-resource-allocation (Ch 2)"`)

---

### Task 20: `write-okrs`

**Files:**
- Create: `skills/write-okrs/SKILL.md`

- [ ] **Step 1: Ensure book extracted**

- [ ] **Step 2: Read book section**

In Chapter2.xhtml, locate H3 "Annual and quarterly goals" AND the sidebar H3 "Good goals" (subsections: Why we set goals, What good goals look like, Heuristics for testing your goals, FAQs, Say what percentage of goals you expect people to hit up front, An individual's goals should include one or two personal goals, The "how" is just as important as the "what"). Also locate H3 "Writing Good OKRs" in the Exercises and templates section (subsections: The basics, Guidance on ambition, Good OKRs start with good objectives, Define key results, Common pitfalls). Extract: what makes a good objective, what makes a good key result, the expected-hit-rate norm, the personal-goal norm, the "how" as part of the goal, common pitfalls.

- [ ] **Step 3: Write `skills/write-okrs/SKILL.md`**

§C1 template with slots:

- slug: `write-okrs`
- description: `Turn rough goals into well-formed OKRs / SMART objectives. Includes expected hit rate, 1-2 personal goals per individual, and the "how" alongside the "what." Use during quarterly or annual planning, or when an existing goal isn't actionable.`
- Title: `Write OKRs`
- Opening: "This skill turns a rough goal into a well-formed OKR set. The book treats OKRs as more than a format — they're a contract on ambition, hit-rate expectation, the work behind the outcome, and personal growth. This skill produces all of those, not just the format."
- router: `org-foundations-and-planning`, N=2
- Rubric: extract from Step 2 — pull from both "Good goals" sidebar AND "Writing Good OKRs" template
- Draft-mode intake:
  1. "What's the scope — team, function, or individual?"
  2. "What's the period (quarter / year)?"
  3. "What's the rough outcome you're aiming at?"
  4. "What's the realistic hit-rate target (60% / 70% / 100%)?"
  5. "For an individual: what's a personal-growth goal that's not tied to a team outcome?"
- Artifact format: `Markdown — populated OKR template per references/templates/okr-template.md, with hit-rate expectation declared and any personal goals included.`
- Source section: `The operating system > Annual and quarterly goals` (incl. Good goals sidebar) + `Writing Good OKRs` template
- Template reference: `references/templates/okr-template.md`

- [ ] **Step 4: Validate**

- [ ] **Step 5: Commit** (`git commit -m "skill: write-okrs (Ch 2)"`)

---

### Task 21: `score-okrs`

**Files:**
- Create: `skills/score-okrs/SKILL.md`

- [ ] **Step 1: Ensure book extracted**

- [ ] **Step 2: Read book section**

In Chapter2.xhtml, locate H3 "Iterating and Scoring" in the Exercises and templates section (subsections: Mid-quarter scoring, How to handle changes in information and priorities). Also re-read the FAQ items "How do you score goals?" and "What do you do if the goal changes before the time period ends?" in the "Good goals" sidebar. Extract: the scoring approach, mid-quarter scoring discipline, and how to handle priority changes mid-period.

- [ ] **Step 3: Write `skills/score-okrs/SKILL.md`**

§C1 template with slots:

- slug: `score-okrs`
- description: `Score OKRs mid-quarter or at quarter end; handle priority changes and information updates that hit mid-period. Use at the scoring checkpoint or when something material has changed since OKRs were set.`
- Title: `Score OKRs`
- Opening: "This skill produces a scored OKR review — including how to handle the case where the goal has changed since it was set, where information has invalidated an assumption, or where progress can't be cleanly summarized. Use it as a checkpoint, not a verdict."
- router: `org-foundations-and-planning`, N=2
- Rubric: extract from Step 2
- Draft-mode intake:
  1. "What's the OKR set being scored?"
  2. "Mid-quarter or end-of-quarter?"
  3. "What's changed since these were set — priorities, information, scope?"
  4. "What's the rough self-assessment per key result?"
- Artifact format: `Markdown — scored table (objective / KR / score / commentary / change-since-set) + a short narrative on what to keep / drop / adjust next period.`
- Source section: `Iterating and Scoring`
- Template reference: `references/templates/okr-template.md` (extended with scoring columns)

- [ ] **Step 4: Validate**

- [ ] **Step 5: Commit** (`git commit -m "skill: score-okrs (Ch 2)"`)

---

### Task 22: `define-metrics`

**Files:**
- Create: `skills/define-metrics/SKILL.md`

- [ ] **Step 1: Ensure book extracted**

- [ ] **Step 2: Read book section**

In Chapter2.xhtml, locate H3 "Metrics that matter" AND the sidebar H3 "Metrics write-up" (subsections: Introduction, Metrics framework — Objectives, Creating metrics, Long-term metrics: mission and vision, Short-term metrics: operating or input metrics, Other metrics, Using metrics). Extract: the three-layer metrics structure (long-term / short-term / other), what makes a metric usable, how to handle less-measurable outcomes.

- [ ] **Step 3: Write `skills/define-metrics/SKILL.md`**

§C1 template with slots:

- slug: `define-metrics`
- description: `Build the metrics framework — long-term (mission/vision), short-term (operating/input), and "other" metrics for a team or function. Produces a metrics write-up doc. Use when launching a team, setting up new measurement, or when current metrics don't drive decisions.`
- Title: `Define Metrics`
- Opening: "This skill produces a metrics write-up — the three-layer structure of long-term outcome metrics (mission/vision), short-term operating or input metrics, and 'other' metrics that don't fit either category. The doc explains what each metric is for and how decisions will use it."
- router: `org-foundations-and-planning`, N=2
- Rubric: extract from Step 2
- Draft-mode intake:
  1. "What team/function?"
  2. "What's the long-term outcome you're trying to move (tied to mission)?"
  3. "What 2-4 operating or input metrics would move that outcome?"
  4. "What's measurable today vs needs instrumentation?"
- Artifact format: `Markdown — metrics write-up per references/templates/metrics-writeup.md.`
- Source section: `The operating system > Metrics that matter` (incl. Metrics write-up sidebar)
- Template reference: `references/templates/metrics-writeup.md`

- [ ] **Step 4: Validate**

- [ ] **Step 5: Commit** (`git commit -m "skill: define-metrics (Ch 2)"`)

---

### Task 23: `prep-qbr`

**Files:**
- Create: `skills/prep-qbr/SKILL.md`

- [ ] **Step 1: Ensure book extracted**

- [ ] **Step 2: Read book section**

In Chapter2.xhtml, locate H3 "Quarterly Business Reviews (QBRs)" in the Exercises and templates section (subsections: QBR guidelines, QBR outline — Executive summary, Narrative, Example outline, Metrics performance, Product P&L, Cross-functional focus areas, Progress on goals, Appendix A: Required tables — Prior QBR action items, Operating expenses, Headcount, Top asks from users, Appendix B). Extract: the QBR outline in full, the "what statements should be true after your QBR meeting" criteria, prep/during/after guidance.

- [ ] **Step 3: Write `skills/prep-qbr/SKILL.md`**

§C1 template with slots:

- slug: `prep-qbr`
- description: `Produce a quarterly business review (QBR) document per the book's outline — exec summary, narrative, metrics performance, cross-functional focus, goals progress, required appendices. Use ~2 weeks before the QBR meeting.`
- Title: `Prep QBR`
- Opening: "This skill produces a quarterly business review — the doc that gets read before the QBR meeting, with the goal of leaving the meeting with specific true statements (calibrated on progress, aligned on top risks and asks). The outline is opinionated; this skill respects it."
- router: `org-foundations-and-planning`, N=2
- Rubric: extract from Step 2 — both the "what statements should be true" list and the outline-fidelity heuristics
- Draft-mode intake:
  1. "What's the team/function and the quarter being reviewed?"
  2. "Top 3 wins and top 3 misses this quarter?"
  3. "What's the biggest open question you want stakeholders to engage on?"
  4. "Top asks from users this quarter?"
  5. "Any prior QBR action items still open?"
- Artifact format: `Markdown — populated QBR per references/templates/qbr-outline.md.`
- Source section: `Quarterly Business Reviews (QBRs)`
- Template reference: `references/templates/qbr-outline.md`

- [ ] **Step 4: Validate**

- [ ] **Step 5: Commit** (`git commit -m "skill: prep-qbr (Ch 2)"`)

---

### Task 24: `plan-internal-comms`

**Files:**
- Create: `skills/plan-internal-comms/SKILL.md`

- [ ] **Step 1: Ensure book extracted**

- [ ] **Step 2: Read book section**

In Chapter2.xhtml, locate H3 "Internal communications" AND H4 "When should you start investing in internal communications?" AND the sidebar H3 "Stripe's writing culture" (subsections: Building and assessing an internal communications program, Communicate more in crisis and times of change, Make company-wide meetings count) AND the sidebar H3 "Stripe Home." Extract: when to start investing, what an internal comms program covers, crisis-comms posture, all-hands design.

- [ ] **Step 3: Write `skills/plan-internal-comms/SKILL.md`**

§C1 template with slots:

- slug: `plan-internal-comms`
- description: `Assess current internal comms or build/improve the program — cadence, channels, all-hands design, crisis-comms readiness, writing culture. Use when the org is growing past ~50 people, after a change/incident, or when "no one knew" keeps coming up.`
- Title: `Plan Internal Comms`
- Opening: "This skill produces an internal communications plan — what gets communicated, by whom, on what cadence, through which channels, and how that posture shifts in change or crisis. Use it when ad-hoc comms are no longer enough."
- router: `org-foundations-and-planning`, N=2
- Rubric: extract from Step 2 — include the "when to start investing" trigger as one item
- Draft-mode intake:
  1. "Org size and rough structure?"
  2. "What's the current state — what comms exist today?"
  3. "What's the biggest comms gap you keep hitting?"
  4. "Are you in a change or crisis state, or steady state?"
- Artifact format: `Markdown — comms program plan: audiences, channels, cadence, owners, special-case posture (crisis/change), all-hands format.`
- Source section: `The operating system > Internal communications` (incl. Stripe's writing culture sidebar and Stripe Home sidebar)
- Template reference: `Inline — no shared template.`

- [ ] **Step 4: Validate**

- [ ] **Step 5: Commit** (`git commit -m "skill: plan-internal-comms (Ch 2)"`)

---

### Task 25: `define-ownership-and-accountability`

**Files:**
- Create: `skills/define-ownership-and-accountability/SKILL.md`

- [ ] **Step 1: Ensure book extracted**

- [ ] **Step 2: Read book section**

In Chapter2.xhtml, locate H3 "Ownership" AND H3 "Accountability mechanisms" (both under H2 "The operating system"). Read through to the next H3 ("Internal communications"). Extract: how to assign ownership cleanly, what counts as an accountability mechanism, decision rights, escalation paths.

- [ ] **Step 3: Write `skills/define-ownership-and-accountability/SKILL.md`**

§C1 template with slots:

- slug: `define-ownership-and-accountability`
- description: `Clarify ownership for a scope and the accountability mechanisms that go with it — decision rights, escalation paths, review forums. Use when "who owns X?" keeps being asked, after a reorg, or when accountability has eroded.`
- Title: `Define Ownership and Accountability`
- Opening: "This skill produces an ownership-and-accountability doc for a defined scope: who owns it, what decisions they can make alone vs with input vs by consensus, who escalates to whom, and what review forums hold the owner accountable. The book treats ownership without accountability mechanisms as ownership in name only."
- router: `org-foundations-and-planning`, N=2
- Rubric: extract from Step 2
- Draft-mode intake:
  1. "What's the scope — a system, a metric, an initiative, a function?"
  2. "Who is the proposed owner today (if anyone)?"
  3. "What decisions does the owner currently make alone, with input, or by consensus?"
  4. "What forum reviews this scope, and how often?"
- Artifact format: `Markdown — ownership doc: scope, owner, decision rights matrix, escalation path, review forum and cadence.`
- Source section: `The operating system > Ownership` and `Accountability mechanisms`
- Template reference: `Inline — no shared template.`

- [ ] **Step 4: Validate**

- [ ] **Step 5: Commit** (`git commit -m "skill: define-ownership-and-accountability (Ch 2)"`)

---

### Task 26: `design-operating-cadence`

**Files:**
- Create: `skills/design-operating-cadence/SKILL.md`

- [ ] **Step 1: Ensure book extracted**

- [ ] **Step 2: Read book section**

In Chapter2.xhtml, locate H2 "Operating cadence" AND H3 "A brief note on process" (subsections: Watch out for defensive processes, Beware of stale processes, Allow for experimentation, Process is not synonymous with meetings). Read through but stop before H3 "How to tell if something is wrong with your operating system or cadence" (that's the next skill). Extract: what makes a healthy cadence, the defensive/stale/experimentation warnings, the process-not-meetings principle.

- [ ] **Step 3: Write `skills/design-operating-cadence/SKILL.md`**

§C1 template with slots:

- slug: `design-operating-cadence`
- description: `Define the recurring meetings, rituals, and forums for a team — the cadence map (weekly / monthly / quarterly) with purpose per item. Use when starting a team, after a reorg, or when current rhythm feels random or overgrown.`
- Title: `Design Operating Cadence`
- Opening: "This skill produces an operating cadence map — the recurring meetings, rituals, and forums that turn the operating system into rhythm. Each item has a clear purpose; the map is short enough to fit on one screen."
- router: `org-foundations-and-planning`, N=2
- Rubric: extract from Step 2 — including "process is not meetings" and the defensive/stale process warnings as heuristics
- Draft-mode intake:
  1. "Team scope and size?"
  2. "What recurring meetings or rituals exist today?"
  3. "What rhythm has been working and what hasn't?"
  4. "Any new forums you've been meaning to add?"
- Artifact format: `Markdown — cadence table (item / cadence / participants / purpose / decision output) grouped by weekly/monthly/quarterly.`
- Source section: `Operating cadence`
- Template reference: `Inline — no shared template.`

- [ ] **Step 4: Validate**

- [ ] **Step 5: Commit** (`git commit -m "skill: design-operating-cadence (Ch 2)"`)

---

### Task 27: `audit-operating-system`

**Files:**
- Create: `skills/audit-operating-system/SKILL.md`

- [ ] **Step 1: Ensure book extracted**

- [ ] **Step 2: Read book section**

In Chapter2.xhtml, locate H3 "How to tell if something is wrong with your operating system or cadence" (under H2 "Operating cadence"). Read through to H2 "Exercises and templates." Also re-read the "A brief note on process" warnings (defensive, stale, experimentation). Extract: the symptoms-of-broken-OS checklist and the response patterns.

- [ ] **Step 3: Write `skills/audit-operating-system/SKILL.md`**

§C1 template with slots:

- slug: `audit-operating-system`
- description: `Diagnose what's wrong with the current operating system or cadence — defensive process, stale process, missing forums, overgrown rituals. Recommends what to add, cut, or change. Use when team velocity is dropping, decisions aren't sticking, or meetings keep multiplying.`
- Title: `Audit Operating System`
- Opening: "This skill diagnoses an existing operating system — what's defensive, what's stale, what's missing, what's overgrown. Output is a punch list of additions, cuts, and changes, prioritized."
- router: `org-foundations-and-planning`, N=2
- Rubric: extract from Step 2 — the symptoms checklist plus the response patterns
- Draft-mode intake:
  1. "What team is being audited?"
  2. "What symptoms triggered the audit (e.g., slow decisions, missed goals, meeting overload)?"
  3. "What's the current cadence map (paste or describe)?"
  4. "What's changed recently (org, scope, size, leadership)?"
- Artifact format: `Markdown — diagnosis (symptoms → likely cause) + punch list (add / cut / change items with rationale per item).`
- Source section: `Operating cadence > How to tell if something is wrong with your operating system or cadence` (and `A brief note on process`)
- Template reference: `Inline — no shared template.`

- [ ] **Step 4: Validate**

- [ ] **Step 5: Commit** (`git commit -m "skill: audit-operating-system (Ch 2)"`)

---

## Phase 4 — Shared templates

### Task 28: Create the 5 Ch 2 templates and book-frameworks overview

**Files:**
- Create: `references/templates/team-charter.md`
- Create: `references/templates/qbr-outline.md`
- Create: `references/templates/okr-template.md`
- Create: `references/templates/metrics-writeup.md`
- Create: `references/templates/operating-principles-example.md`
- Create: `references/book-frameworks/scaling-people-overview.md`

For each template: extract the structure (NOT verbatim text) from the named section of `/tmp/scaling-people-epub/OEBPS/Text/Chapter2.xhtml` and produce a fillable markdown skeleton.

- [ ] **Step 1: `references/templates/team-charter.md`**

Source: "Team Charter" template in Ch 2 Exercises and templates. Structure (preserve the order and labels from the book; paraphrase any guidance text):

```markdown
# Team Charter — <team name>

**Last updated:** <YYYY-MM-DD>
**Owner:** <name>

## Mission
<one-sentence statement of what the team exists to do>

## Vision
<2-3 year picture of what success looks like>

## Customers
<who the team serves — internal teams, external users, both>

## Metrics
<top 2-4 metrics the team is measured on>

## Strategic importance
<why this team matters to the org's strategy; what doesn't happen without it>

## Major risks
<top 2-3 risks to the team achieving its mission>

## Provided interfaces
<what other teams/systems can rely on this team to deliver — APIs, services, decisions, reviews>

## Dependent interfaces
<what this team depends on from other teams/systems>
```

- [ ] **Step 2: `references/templates/qbr-outline.md`**

Source: "QBR outline" in Ch 2 Exercises and templates. Structure:

```markdown
# QBR — <team/function> — Q<N> <year>

**Owner:** <name>
**Date:** <YYYY-MM-DD>

## Executive summary
<250 words max — what happened, what it means, top asks>

## Narrative
<two pages max — the quarter's story in prose: bets made, results, surprises, what changed>

## Metrics performance
<two pages max — top metrics with target / actual / commentary; additional metrics in appendix>

### Examples of key metrics
- <metric 1>
- <metric 2>
- ...

### Product P&L (if applicable)
<revenue / cost / margin>

## Cross-functional focus areas
<top 2-4 areas with cross-team dependencies; status per area>

## Progress on goals
<one page max — OKRs scored, brief commentary; additional goals in appendix>

## Appendix A — Required tables

### Prior QBR action items
| Item | Owner | Status | Notes |
|---|---|---|---|

### Operating expenses (non-product teams)
<table>

### Headcount
<table: current / open / planned>

### Top asks from users
<list>

## Appendix B — Additional supporting materials
<charts, deeper metrics, related docs>
```

- [ ] **Step 3: `references/templates/okr-template.md`**

Source: "Writing Good OKRs" template + "Iterating and Scoring" in Ch 2 Exercises and templates. Structure:

```markdown
# OKRs — <team/individual> — <period>

**Owner:** <name>
**Period:** <Q<N> YYYY or YYYY>
**Expected hit rate:** <e.g., 70% — declared up front>

## Objective 1: <one-sentence outcome>

**Why:** <1-2 sentence rationale tying to mission/strategy>
**How (high-level approach):** <2-4 bullets — the "how" alongside the "what">

| Key Result | Target | Score (end-of-period) | Commentary |
|---|---|---|---|
| KR1.1: <measurable result> | <number/date> | <0.0-1.0> | <what happened> |
| KR1.2: ... | ... | ... | ... |

## Objective 2: ...
[same structure]

## Personal goals (for individual OKRs)
- <1-2 personal growth goals not tied to a team outcome>

## Changes mid-period
<log of priority/info changes that affected these OKRs, with date>
```

- [ ] **Step 4: `references/templates/metrics-writeup.md`**

Source: "Metrics write-up" sidebar in Ch 2. Structure:

```markdown
# Metrics — <team/function>

**Owner:** <name>
**Last updated:** <YYYY-MM-DD>

## Introduction
<2-4 sentences: what this team does, what we're measuring and why>

## Metrics framework

### Objectives
<the 1-3 outcomes these metrics serve>

### Creating metrics
<how we picked these — what we considered and rejected>

## Long-term metrics (mission and vision)
| Metric | Definition | Current | Target | Source |
|---|---|---|---|---|

## Short-term metrics (operating or input)
| Metric | Definition | Current | Target | Cadence | Source |
|---|---|---|---|---|---|

## Other metrics
<diagnostic metrics, leading indicators we watch but don't formally target>

## Using metrics
<how decisions are made from these — what we'd change if a metric moved, how we review them>
```

- [ ] **Step 5: `references/templates/operating-principles-example.md`**

Source: "Stripe's Operating Principles" in Ch 2 Exercises and templates. Structure — provide a labeled scaffolding (NOT Stripe's actual content; the book reproduces those but here we provide the shape so users fill with their own):

```markdown
# Operating Principles — <org/team name>

> Structure adapted from *Scaling People* (Claire Hughes Johnson), modeled on Stripe's operating principles. Three categories: how we work, who we are, and what we expect of leaders.

## How we work
<4-6 principles describing the team's operating behaviors. Each:>

### <Principle name (3-6 words)>
<2-4 sentences. What it means, what it looks like in practice, a sample behavior.>

## Who we are
<4-6 principles describing the team's character or values.>

### <Principle name>
<2-4 sentences.>

## And leaders
<4-6 principles describing what's specifically expected of people who lead others on this team.>

### <Principle name>
<2-4 sentences.>
```

- [ ] **Step 6: `references/book-frameworks/scaling-people-overview.md`**

Brief reference doc skill bodies can link to instead of restating the framework. Structure:

```markdown
# Scaling People — Framework Overview

A quick-reference summary of the book's frameworks, indexed by chapter. Skills in this plugin link here when they need to gesture at the broader framework without restating it.

## Chapter 1 — Essential Operating Principles
Four principles: build self-awareness; say the hard thing; distinguish management vs leadership; come back to your operating system.

## Chapter 2 — Foundations and Planning
Three layers: founding documents (mission, long-term goals, principles, charter), the operating system (strategic + financial planning, resource allocation, OKRs, metrics, ownership, internal comms, QBRs), and operating cadence.

## Chapter 3 — A Comprehensive Hiring Approach
Four phases: recruiting (build talent insights, open roles well, referrals, screening, leader recruiting), hiring (interview design, decision-making, candidate review, references, offers), onboarding (IC and New Leader Experience), and closing the loop on hiring mistakes.

## Chapter 4 — Intentional Team Development
Five lenses: team structures (teams vs working groups, layering, business leads), diagnosing team state (skill/will, underperforming teams), team changes (three-phase reorgs), (re)building the team (career conversations, delegation), creating the team environment (offsites, meetings, distributed work, uncertainty), and a D&I cross-cut.

## Chapter 5 — Feedback and Performance Mechanisms
Coaching is hypothesis-driven (gather data → form hypothesis → test). Feedback is exploratory, not lecturing. Performance management is a system: informal feedback culture, formal reviews, calibration, comp. Plus tier-specific guidance for high / steady-middle / low performers, managing managers, managing out / firing / layoffs, and supporting through hardship.

## Conclusion — You
Three areas managers neglect about themselves: time and energy, key relationships (your manager, peers, founders), career.

## Source
*Scaling People: Tactics for Management and Company Building* — Claire Hughes Johnson, Stripe Press, 2023.
```

- [ ] **Step 7: Commit**

```bash
git add references/
git commit -m "templates: 5 Ch 2 artifact templates + framework overview reference"
```

---

## Phase 5 — README and final verification

### Task 29: Write `README.md`

**Files:**
- Create: `README.md`

- [ ] **Step 1: Write the README**

```markdown
# klick-management

A Claude Code plugin: management practices from *Scaling People* (Claire Hughes Johnson, Stripe Press 2023) as invokable skills. Use these at decision points — producing the founding documents, OKRs, charters, reviews, and conversation preps the book teaches — not as a substitute for reading the book.

## What's in here

Six top-level "router" skills, one per chapter, plus 49 sub-skills.

| Router | Chapter | Sub-skills |
|---|---|---|
| `operating-principles` | Ch 1 — Essential Operating Principles | 4 (stubbed) |
| `org-foundations-and-planning` | Ch 2 — Foundations and Planning | **14 (built)** |
| `hiring` | Ch 3 — A Comprehensive Hiring Approach | 8 (stubbed) |
| `team-development` | Ch 4 — Intentional Team Development | 9 (stubbed) |
| `feedback-and-performance` | Ch 5 — Feedback and Performance Mechanisms | 11 (stubbed) |
| `manager-self` | Conclusion — You | 3 (stubbed) |

"Stubbed" = the skill exists for triggering and routing but its body is a one-line placeholder. Bodies are filled in over time as we use them.

## Getting started

Three good first runs:

1. **`/klick-management:operating-principles`** — read the chapter overview and the four sub-skills. Even as stubs, the router helps you situate where in the management toolkit you are.
2. **`/klick-management:write-team-charter`** — produces a complete team charter in 5-10 minutes (draft mode). The fastest way to feel the library.
3. **`/klick-management:prep-qbr`** — populates a full QBR doc from the book's outline.

Each sub-skill supports three modes:
- **`teach`** — Socratic walk-through (10-20 min); good first time
- **`draft`** — 3-5 intake questions → first draft → refinement (5-10 min); default
- **`polish`** — paste a rough version → critique → polished (2-5 min); fastest

## Installation

This plugin installs from the Klick plugins marketplace. Add the marketplace once, then install:

```
# In Claude Code
/plugin install klick-management
```

(If the marketplace command differs in your environment, install from source by symlinking this repo into `~/.claude/plugins/klick-management` and reloading.)

## How this library was built

See [docs/superpowers/specs/2026-05-27-klick-management-skill-library-design.md](docs/superpowers/specs/2026-05-27-klick-management-skill-library-design.md). The "Methodology" section explains how the book was broken down into skills and how additional books can be blended in later.

## Validation

```
python3 scripts/validate-skills.py
```

Runs on every skill: checks frontmatter, naming, and required body structure (router / stub / built sub-skill).

## Attribution

All skill content is derived from and credited to *Scaling People: Tactics for Management and Company Building* by Claire Hughes Johnson (Stripe Press, 2023). This plugin is a working aid, not a substitute for the book.

## License

MIT. See [LICENSE](LICENSE).
```

- [ ] **Step 2: Commit**

```bash
git add README.md
git commit -m "docs: README with getting-started, install, and attribution"
```

---

### Task 30: Final validation + local install + spot-check

- [ ] **Step 1: Run full validation**

Run: `python3 scripts/validate-skills.py`
Expected: `OK: 55 skill(s) validated` (6 routers + 14 built + 35 stubs).

If any errors: fix the offending files and re-run until clean.

- [ ] **Step 2: Verify file/directory counts**

Run:
```bash
ls skills/ | wc -l
find skills -name "SKILL.md" | wc -l
ls references/templates/ | grep -v '^\.gitkeep$' | wc -l
```
Expected:
- `55` (55 skill directories)
- `55` (one SKILL.md per directory)
- `5` (templates)

- [ ] **Step 3: Install plugin locally and spot-check triggering**

Symlink this repo into the local plugin path:
```bash
ln -sf "$(pwd)" ~/.claude/plugins/klick-management-local
```

Then in a fresh Claude Code session: trigger natural-language phrases that should match top-level routers and a few built sub-skills:
- "I need to write a team charter" → should surface `klick-management:write-team-charter`
- "Help me prep our quarterly business review" → should surface `klick-management:prep-qbr`
- "I want to set operating principles for my team" → should surface `klick-management:write-operating-principles`
- "How should I think about feedback?" → should surface `klick-management:feedback-and-performance` (router)

If any expected triggers fail, edit the relevant skill's `description` to add the trigger phrasing, re-validate, commit, and re-test.

- [ ] **Step 4: Run one built sub-skill end-to-end**

In Claude Code, run `/klick-management:write-mission` in `draft` mode against a real or fictional team. Confirm the produced artifact:
- Saves to `./docs/management/<artifact-slug>-YYYY-MM-DD.md` by default.
- Includes the rubric-driven sections specified in the SKILL.md.
- Cites the book in a `## Source` section in the artifact OR in its output.

If the output is materially worse than expected, file an issue (or update the skill's Rubric / intake / template path) before declaring done.

- [ ] **Step 5: Final commit (if any fixes from Steps 3-4)**

```bash
git add -A
git commit -m "fix: trigger phrasing and rubric tweaks from spot-check"
```

If no fixes needed, skip the commit.

- [ ] **Step 6: Tag the first build**

```bash
git tag -a v0.1.0 -m "First build: 6 routers + 14 Ch 2 sub-skills + 35 stubs"
```

---

## Self-Review (post-plan)

Done as part of writing this plan, fixed inline. Notes:

- **Spec coverage:** Every Ch 2 sub-skill in the spec has a task (Tasks 14-27 = 14 sub-skills). Every router has a task (Tasks 3-8 = 6 routers). Every stub category has a task (Tasks 9-13 = 5 chapter stub batches covering 35 sub-skills). Templates have a task (Task 28). README has a task (Task 29). Validation script has a task (Task 2). Install/spot-check has a task (Task 30). Plugin scaffold has a task (Task 1).
- **Placeholder scan:** Tasks for Ch 2 sub-skill bodies (14-27) specify "extract the rubric from book section X." This is a deterministic action with a fully-specified input and a fully-specified output shape — not a "fill in details later" placeholder. The agent has the file path, the section heading, the rubric format (numbered list, 4-8 items, bold label + 1-2 sentences), and the output template. Everything else (description, intake questions, artifact format, source citation) is rendered verbatim in the task.
- **Type consistency:** Skill slugs match across the plan, the spec, and the README. Router slug `org-foundations-and-planning` matches what was renamed in the spec.

## Open items deferred to execution

- The plugin's install command in the README (`/plugin install klick-management`) may need adjustment depending on the marketplace setup. The spot-check task (30, Step 3) catches this.
- Whether the rubric extractions feel high-quality enough across all 14 Ch 2 sub-skills. If not, the fix is to refine individual SKILL.md files post-execution rather than block the build.
