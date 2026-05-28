# Design — `klick-management` skill library

**Date:** 2026-05-27
**Owner:** awhitehead@klick.com
**Source material:** *Scaling People: Tactics for Management and Company Building* — Claire Hughes Johnson (Stripe Press, 2023)

## Purpose

Turn the management practices in *Scaling People* into a Claude Code skill library that the author uses in real management situations and shares with a small set of managers he coaches. Skills produce usable artifacts (mission statements, OKRs, charters, review docs, etc.); they do not replace the book or the conversations the manager still has to have.

## Audience

- **Primary:** the author, using skills at decision points in his own management work.
- **Secondary:** a small set of managers the author coaches, who install the plugin.
- **Out of scope:** general distribution outside this circle, "all of Klick," or non-Klick managers (not blocked — just not designed for).

## Library shape

Tiered: **6 top-level skills (one per book chapter, mirroring the book exactly) + ~49 sub-skills.**

| Top-level skill | Book chapter | Sub-skills | Build status |
|---|---|---|---|
| `operating-principles` | Ch 1 — Essential Operating Principles | 4 | Stubbed |
| `org-foundations-and-planning` | Ch 2 — Foundations and Planning | 14 | **Built first, end-to-end** |
| `hiring` | Ch 3 — A Comprehensive Hiring Approach | 8 | Stubbed |
| `team-development` | Ch 4 — Intentional Team Development | 9 | Stubbed |
| `feedback-and-performance` | Ch 5 — Feedback and Performance Mechanisms | 11 | Stubbed |
| `manager-self` | Conclusion — You | 3 | Stubbed |

"Stubbed" = the sub-skill exists as a one-line SKILL.md placeholder so the library has full shape, but the body is filled in later.

## Plugin layout

Claude Code's plugin loader requires a flat `skills/<name>/SKILL.md` layout — sub-skills are siblings of top-level skills in the file system. **Tiering is preserved at the behavioral layer** (router skills + skill descriptions) rather than the file system layer.

```
klick-management/                          ← this repo IS the plugin source
  .claude-plugin/
    plugin.json                            ← name, version, description, author
  README.md                                ← what this is, attribution, getting started
  LICENSE
  skills/
    # Top-level router skills (one per book chapter)
    operating-principles/SKILL.md          ← Ch 1 router
    org-foundations-and-planning/SKILL.md  ← Ch 2 router
    hiring/SKILL.md                        ← Ch 3 router
    team-development/SKILL.md              ← Ch 4 router
    feedback-and-performance/SKILL.md      ← Ch 5 router
    manager-self/SKILL.md                  ← Conclusion router

    # Ch 1 sub-skills (stubbed)
    self-awareness-assessment/SKILL.md
    write-working-with-me/SKILL.md
    prep-to-say-the-hard-thing/SKILL.md
    clarify-management-vs-leadership/SKILL.md

    # Ch 2 sub-skills (built first)
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

    # Ch 3 sub-skills (stubbed) — 8 directories
    define-talent-needs/SKILL.md
    open-a-role/SKILL.md
    design-interview-loop/SKILL.md
    run-candidate-review/SKILL.md
    check-references/SKILL.md
    design-leader-hiring-process/SKILL.md
    plan-onboarding/SKILL.md
    hire-postmortem/SKILL.md

    # Ch 4 sub-skills (stubbed) — 9 directories
    design-team-structure/SKILL.md
    diagnose-team-state/SKILL.md
    plan-reorganization/SKILL.md
    run-career-conversation/SKILL.md
    plan-delegation/SKILL.md
    plan-offsite/SKILL.md
    design-meeting/SKILL.md
    manage-distributed-or-changing-team/SKILL.md
    apply-d-and-i-lens/SKILL.md

    # Ch 5 sub-skills (stubbed) — 11 directories
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

    # Conclusion sub-skills (stubbed) — 3 directories
    audit-time-and-energy/SKILL.md
    develop-key-relationships/SKILL.md
    reflect-on-career/SKILL.md

  references/
    book-frameworks/                       ← short chapter-by-chapter summaries cited by skills
    templates/                             ← reusable artifact templates
      team-charter.md
      qbr-outline.md
      okr-template.md
      metrics-writeup.md
      operating-principles-example.md
      working-with-me.md                   ← used by Ch 1 sub-skill
  scripts/
    validate-skills.py                     ← lints frontmatter, checks required sections
  docs/
    superpowers/specs/                     ← design specs (this file lives here)
    superpowers/plans/                     ← implementation plans
```

**Naming under flat layout.** Top-level router skills keep their chapter-slug names (`org-foundations-and-planning`, `feedback-and-performance`, etc.) — these are already verb-distinct from sub-skill names so collision is impossible. Sub-skills keep their verb-first action phrases (`write-mission`, `prep-qbr`, `give-hard-feedback`). No chapter prefix needed; if a future book introduces a sub-skill with the same artifact, methodology Step 3 says merge into the existing skill rather than create a duplicate.

**How tiering still works.** A user (or Claude's auto-trigger) can:
- Invoke a top-level router for a chapter overview and routing help (`/klick-management:org-foundations-and-planning` or natural-language trigger).
- Invoke a sub-skill directly when the moment is known (`/klick-management:write-mission`).
- Auto-trigger via description matching on either.

The top-level router SKILL.md lists its sub-skills by their flat names and includes "use when X" hooks — so a user reading the router gets the same tiered mental model the original spec proposed.

## Conventions

### Naming

- Top-level skills: noun phrases matching the chapter, lowercase-kebab (`org-foundations-and-planning`).
- Sub-skills: verb-first action phrases (`write-mission`, `score-okrs`, `audit-operating-system`).
- One exception: `operating-principles` is a noun (it names the chapter); its sub-skills are verb-first as usual.

### Top-level SKILL.md pattern (~150 words)

Each top-level SKILL.md contains:
1. **Description** (frontmatter) — triggers covering the chapter's range of moments.
2. **What this chapter is for** — ~100 words paraphrasing the book.
3. **Sub-skills** — slug + one-line "use when X" hook for each.
4. **Routing behavior** — if invoked directly without a specific sub-skill in mind, ask the user "what are you trying to do?" and route.

Top-level skills do NOT contain sub-skill bodies. They are routers + overviews.

### Sub-skill SKILL.md pattern (three modes)

Every sub-skill opens with mode selection:

```
Step 1: Use the AskUserQuestion tool to ask which mode. Default to `draft` if the user skips.
  - teach   → Socratic walk-through (10-20 min). Output: artifact + understanding.
  - draft   → 3-5 targeted questions → first draft → refinement loop (5-10 min).
  - polish  → user pastes rough version → critique against book heuristics → polished (2-5 min).
Step 2: Run the selected mode using the rubric below.
Step 3: Save artifact to ./docs/management/<artifact-slug>-YYYY-MM-DD.md (or user-specified path).
         If file exists, prompt before overwriting.

Throughout the skill (mode selection, intake, refinement, clarification): prefer the
AskUserQuestion tool for any question with 2-4 reasonably discrete options. Use plain
chat only when the answer genuinely needs a sentence or paragraph of free-form text.
```

The rubric/checklist (the book's actual guidance for that artifact) lives once in the SKILL.md so all three modes pull from the same source of truth.

### Source attribution

Every skill SKILL.md ends with:

```
## Source
*Scaling People* — Claire Hughes Johnson — Ch X, "<section name>".
[Short paraphrase of the key heuristic/checklist the skill encodes.]
Where the book provides a template, see references/templates/<file>.
```

Paraphrase guidance; quote only short rubrics/checklists. README states the library is a working aid based on the book, not a substitute for reading it.

### Examples and tone

- **Examples:** generic management examples; the book's Stripe examples are paraphrased generically. Each skill asks the user for their team/role context in `teach` and `draft` modes and tailors outputs from there. No Klick-specific lore baked into skills — keeps them shareable and avoids stale references.
- **Tone:** direct, second-person, no fluff, no emojis. Same voice as the book — pragmatic operator. Skills assume a capable adult.

### Triggering

- Auto-trigger via Claude's standard skill-description matching.
- Top-level descriptions include broad trigger phrases ("team mission", "operating cadence", "QBR") → routes to the right sub-skill.
- Sub-skill descriptions include narrow trigger phrases ("OKR review" → `score-okrs`) so they can fire directly too.
- Explicit invocation always works: `/klick-management:write-mission`.

### Sharing model

Plugin lives in a git repo named `klick-management`. Coachees install via the plugin marketplace mechanism. README has a one-page getting-started that points at `operating-principles` first (self-awareness foundation), then `org-foundations-and-planning`.

## Chapter 2 sub-skills — full specification (built first)

Each entry: **slug** — trigger / what it produces.

### A. Founding documents

1. **`write-mission`** — "I need a team or org mission statement." Output: one-sentence mission + rationale + rejected alternatives.
2. **`write-long-term-goals`** — "What are our 3–5-year aspirations?" Output: vision + long-term goals with success conditions.
3. **`write-operating-principles`** — Stripe-style three-section set ("how we work" / "who we are" / "and leaders"). Output: principles list with one-paragraph elaborations and example behaviors.
4. **`write-team-charter`** — Output: completed charter per template (mission, vision, customers, metrics, strategic importance, major risks, provided interfaces, dependent interfaces).

### B. The operating system

5. **`plan-strategic-and-financial`** — Annual strategic + financial planning narrative for a team or function.
6. **`design-resource-allocation`** — Allocate FTE and budget across initiatives; produces an allocation table + communicated expectations.
7. **`write-okrs`** — Turn rough goals into well-formed OKRs / SMART objectives. Includes expected hit-rate, 1–2 personal goals, and the "how" alongside the "what."
8. **`score-okrs`** — Mid-quarter or end-quarter scoring; handles changed priorities and disagreements.
9. **`define-metrics`** — Build the metrics framework: long-term (mission/vision) + short-term (operating/input) + "other." Produces a metrics write-up doc.
10. **`prep-qbr`** — Generate a QBR doc per the book's outline (exec summary, narrative, metrics performance, cross-functional focus, goals progress, required appendices).
11. **`plan-internal-comms`** — Assess current state and build or improve internal communications program (cadence, channels, all-hands design, crisis-comms readiness).
12. **`define-ownership-and-accountability`** — Clarify ownership for a scope and the accountability mechanisms (decision rights, escalation, review forums).

### C. Operating cadence

13. **`design-operating-cadence`** — Define recurring meetings/rituals/forums for the team. Output: a cadence map (weekly/monthly/quarterly) with purpose per item.
14. **`audit-operating-system`** — Diagnose what's wrong with the current op-system/cadence. Flags defensive/stale process; recommends what to add, cut, or change.

### Shared templates (Chapter 2)

In `references/templates/`:
- `team-charter.md`
- `qbr-outline.md`
- `okr-template.md`
- `metrics-writeup.md`
- `operating-principles-example.md`

## Sub-skill maps for stubbed chapters

Stubs are one-line SKILL.md placeholders (slug + trigger + "Body: TBD"). Full bodies filled in as those chapters get prioritized.

### Ch 1 — `operating-principles` (4 subs)
1. `self-awareness-assessment` — values, work-style, skills audit
2. `write-working-with-me` — the "working with me" doc your team/peers/manager read
3. `prep-to-say-the-hard-thing` — preparing a difficult conversation (share feelings, be measured, separate person from idea)
4. `clarify-management-vs-leadership` — situational lens: management moment or leadership moment, and what's appropriate

### Ch 3 — `hiring` (8 subs)
1. `define-talent-needs` — insights on what success looks like for the role
2. `open-a-role` — JD + scorecard that helps candidates self-select
3. `design-interview-loop` — rubric + questions + written exercise (where useful)
4. `run-candidate-review` — facilitate the decision-making forum per the framework
5. `check-references` — questions, analysis, weight
6. `design-leader-hiring-process` — stakeholder loop, feedback-collection-not-decision forum
7. `plan-onboarding` — new-hire OR new-leader (NLE) onboarding; mode handles both
8. `hire-postmortem` — close the loop on a hire (esp. a bad one)

### Ch 4 — `team-development` (9 subs)
1. `design-team-structure` — teams vs working groups, layering, # reports, business leads
2. `diagnose-team-state` — skill/will + underperforming-team probes
3. `plan-reorganization` — three-phase reorg (decide structure → buy-in → comms)
4. `run-career-conversation` — prep + script for a development conversation
5. `plan-delegation` — when / how / to whom
6. `plan-offsite` — pick type by team stage, agenda, check-ins, run-of-show
7. `design-meeting` — purpose, roles, norms, decision-making, leadership-team variant
8. `manage-distributed-or-changing-team` — remote/distributed + managing through uncertainty
9. `apply-d-and-i-lens` — cross-cutting D&I review for hiring, performance, team practices

### Ch 5 — `feedback-and-performance` (11 subs)
1. `run-hypothesis-coaching` — gather data → form hypothesis → test
2. `give-hard-feedback` — explorer-not-lecturer (open question OR empathetic observation)
3. `build-feedback-culture` — informal-feedback practices for the team
4. `run-performance-review` — peer/self/manager + calibration
5. `prep-comp-conversation` — educate, instill trust, motivators, the conversation
6. `manage-high-performer` — pushers/pullers, retention, anti-boredom, no-promo talk
7. `manage-steady-middle` — engaging and developing the dependable core
8. `manage-low-performer` — phased approach, PIP, role move
9. `manage-managers` — manager-of-managers dynamics, 1:1 variants
10. `plan-departure` — managing out, firing for misconduct, layoffs
11. `support-through-hardship` — one-time event vs ongoing hardship vs legal-ramifications

### Conclusion — `manager-self` (3 subs)
1. `audit-time-and-energy` — task/energy audit, boundaries, productivity windows
2. `develop-key-relationships` — your manager, peer managers, founders/execs
3. `reflect-on-career` — career check-in for the manager themselves

## Output artifacts

Default save location for any artifact a skill produces: `./docs/management/<artifact-slug>-YYYY-MM-DD.md` in the user's current working directory. Each skill asks where to save and the user can override. Skills detect existing files and prompt before overwriting.

## Out of scope (explicit non-goals)

- No automated 1:1 transcription/summarization.
- No integration with Klick HR systems (Workday, Lattice, etc.). Skills produce documents the user pastes/uploads themselves.
- No "AI does the conversation for you." Skills prep the human; the human has the conversation.
- No skill bodies for non-Ch-2 chapters in the first build. Their top-level SKILL.md routers exist, sub-skills are one-line stubs.

## Success criteria

The first build is complete when:
1. The `klick-management` plugin installs cleanly.
2. All 6 top-level SKILL.md routers exist, each with the right description for triggering and a usable sub-skill list.
3. All 14 Chapter 2 sub-skills have complete bodies, three modes each, save artifacts correctly, and cite the book.
4. All 35 stubbed sub-skills have one-line SKILL.md placeholders so the library shape is real.
5. `references/templates/` contains the 5 Chapter 2 templates.
6. README walks a new user through installing and running their first skill (`operating-principles` → self-awareness, then a Ch 2 sub-skill).
7. The author runs at least 3 of the Ch 2 sub-skills against real situations and the outputs are usable without major rewrites.

## Methodology — how this library was derived from the book

This section documents the process used to break *Scaling People* into skills, so future work can:
(a) extend this library with additional sub-skills from the same book,
(b) blend in practices from additional books while keeping a coherent shape, and
(c) re-derive the library from scratch if conventions change.

### Step 1 — Extract the book's structure

For an EPUB (which is a zip):

```
unzip -q "<book>.epub" -d /tmp/<slug>
# Headers live in OEBPS/Text/*.xhtml; TOC in OEBPS/Text/toc.xhtml and OEBPS/toc.ncx
```

Pull H2/H3/H4 headers from each chapter file. These map to the book's intentional information hierarchy:
- **H2** typically = top-level section within a chapter (e.g., "Founding documents," "The operating system," "Operating cadence").
- **H3** typically = a specific practice, artifact, or process within that section (e.g., "Team charters," "Quarterly Business Reviews").
- **H4** typically = a sub-step, heuristic, or template element.
- **Sidebars** = adjacent examples or templates; they often contain the strongest reusable artifact templates and should be checked individually.

For other formats: extract a clean outline by whatever means (PDF table of contents, manual reading, etc.). The mapping rules below assume an outline with at least chapter / section / practice granularity.

### Step 2 — Identify the book's organizing principle

Before mapping, name how the book is organized. *Scaling People* is organized as **frameworks** (one per chapter) composed of **artifacts, processes, and decision moments**. Other books may be organized as:
- Sequential phases (do A, then B, then C) → top-level skills become phase-keyed, sub-skills become phase-internal practices.
- Catalogs of patterns (Design Patterns–style) → each pattern is roughly one sub-skill; group by category.
- A single thesis with supporting practices → one top-level skill, many sub-skills.

The organizing principle determines whether top-level skills mirror chapters (as here) or get reorganized around moments / phases / themes.

### Step 3 — Map structure to skills

The mapping used here:

| Book element | Skill element |
|---|---|
| Chapter | Top-level skill (router + ~150-word overview) |
| H2 section within a chapter | Sub-skill grouping (used to organize the sub-skill list inside the top-level SKILL.md, not its own skill) |
| H3 practice / artifact / process | One sub-skill |
| H4 heuristic / template / sub-step | Rubric content inside the sub-skill (not its own skill) |
| Sidebar example | Either rubric content OR a file in `references/templates/` if substantial |
| Exercises and templates (end-of-chapter) | Files in `references/templates/` |

**Heuristics for whether to split, merge, or skip:**
- **Split** an H3 into two sub-skills only if it covers two clearly different artifacts or moments (e.g., the book treats new-IC and new-leader onboarding distinctly enough that a single skill with a mode parameter, not two skills, is the right call — but only after checking the content).
- **Merge** two H3s into one sub-skill when they share the same artifact/output and differ only in context (e.g., skill/will diagnosis + underperforming-team probes both produce a team-state diagnostic).
- **Skip** an H3 that is purely commentary, history, or example with no actionable artifact (e.g., personal anecdotes, sidebars about specific people).
- **Promote** an H4 to a full sub-skill only if it has its own actionable artifact (rare; usually it stays as rubric inside the parent skill).
- **Cross-cut** when a practice spans chapters (e.g., D&I). Decide whether it lives in its strongest chapter and is referenced from others, or becomes a cross-cutting skill. Default to the former; revisit after use.

### Step 4 — Apply naming conventions

- **Top-level skills:** noun phrases matching the chapter theme, lowercase-kebab. Disambiguate if the noun clashes with a likely peer skill from another book (e.g., `org-foundations-and-planning`, not just `foundations`).
- **Sub-skills:** verb-first action phrases. Preferred verbs:
  - `write-X` for static artifacts (mission, charter, OKRs)
  - `design-X` for system-level outputs (cadence, structure, interview loop)
  - `plan-X` for time-bounded events (offsite, onboarding, departure)
  - `run-X` for facilitated processes (career conversation, candidate review)
  - `score-X` / `audit-X` / `diagnose-X` for evaluation skills
  - `prep-X` for skills that prepare the user for a conversation/event
  - `manage-X` for ongoing-relationship skills (high performer, low performer, managers)

Consistency matters more than perfection — a coachee should be able to guess a sub-skill name from the moment they're in.

### Step 5 — Apply the universal sub-skill pattern

Every sub-skill, regardless of source book:
1. Asks which **mode** (teach / draft / polish) up front.
2. Runs the chosen mode against a shared **rubric/checklist** drawn from the source.
3. Produces an **artifact** saved to `./docs/management/<slug>-YYYY-MM-DD.md` (asking before overwriting).
4. Ends with a **`## Source`** block citing the book, chapter, and section, paraphrasing the encoded heuristic, and pointing to any shared template.

This pattern is the load-bearing convention: it's what makes skills from different books feel like one library.

### Step 6 — Build first, stub the rest

Pick one chapter (the most leveraged, or the one the user will hit first) and build all its sub-skills end-to-end. For every other chapter, ship a top-level SKILL.md router + one-line stubs for each sub-skill. This gives the library its full shape on day one while bounding the build.

### Workflow for adding a new book

1. **Read the book's TOC** and apply Step 2 (name the organizing principle).
2. **Check overlap with existing top-level skills.** For each chapter/theme of the new book, decide:
   - **Merge into an existing top-level skill** if it covers the same ground (e.g., a different author on hiring → sub-skills land in `hiring/subs/`).
   - **Add a new top-level skill** if it opens new ground (e.g., a book on board management → new `board-management/` top-level).
   - **Split an existing top-level** if the new material justifies it (rare; prefer to wait until friction appears in use).
3. **For each candidate sub-skill from the new book**, check if there's already a sub-skill for that artifact/moment:
   - **No existing sub-skill** → add it, naming per Step 4.
   - **Existing sub-skill, compatible guidance** → extend the rubric in the existing skill; add the new book to its `## Source` block as a second citation; paraphrase the new heuristic into the rubric.
   - **Existing sub-skill, conflicting guidance** → keep the existing skill, and add a "Differing views" subsection that presents both heuristics with attribution. Let the user choose; don't pick a winner.
4. **Add the new book's templates** to `references/templates/` with a filename prefix when collision risk exists (e.g., `chj-team-charter.md` vs `<other-author>-team-charter.md`).
5. **Update the README's source-material list** with the new book.
6. **Re-derive** the library overview table (top-level skills + sub-skill counts) and check it still hangs together as one coherent library, not a Frankenstein.

### Conventions that make blending work

- **Source attribution is non-negotiable** — every skill cites its source(s). Without this, blended skills become unattributable and conflicts become invisible.
- **One artifact = one skill**, regardless of how many books describe it. The skill becomes a multi-source distillation, not N parallel skills.
- **Conflicts are surfaced, not resolved.** When two books disagree, present both; the user is the operator and picks.
- **Templates are shared.** If two books offer competing templates for the same artifact (e.g., two QBR formats), keep both in `references/templates/` and let the skill ask which the user wants.
- **The three-mode pattern is universal.** Resist the urge to invent a fourth mode for one specific book; if a skill genuinely needs a different interaction pattern, that's a signal it shouldn't be a sub-skill of this library.

## Open questions for implementation phase

- Plugin marketplace publishing mechanism for coachees — confirm the install command and any auth needed.
- Whether `write-working-with-me` lives in Ch 1 (`operating-principles`) where the self-awareness work originates, or Ch 3 (`hiring`) where the book templates it. Current call: Ch 1.
- Whether `apply-d-and-i-lens` should also exist as a callable cross-cutting skill that other sub-skills explicitly reference, or stay solo in `team-development`. Current call: solo, revisit after use.
