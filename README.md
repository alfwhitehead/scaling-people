# klick-management

A Claude Code plugin: management practices from *Scaling People* (Claire Hughes Johnson, Stripe Press 2023) as invokable skills. Use these at decision points — producing the founding documents, OKRs, charters, reviews, and conversation preps the book teaches — not as a substitute for reading the book.

## What's in here

Six top-level "router" skills, one per chapter, plus 49 sub-skills.

| Router | Chapter | Sub-skills |
|---|---|---|
| `operating-principles` | Ch 1 — Essential Operating Principles | **4 (built)** |
| `org-foundations-and-planning` | Ch 2 — Foundations and Planning | **14 (built)** |
| `hiring` | Ch 3 — A Comprehensive Hiring Approach | 8 (stubbed) |
| `team-development` | Ch 4 — Intentional Team Development | 9 (stubbed) |
| `feedback-and-performance` | Ch 5 — Feedback and Performance Mechanisms | 11 (stubbed) |
| `manager-self` | Conclusion — You | 3 (stubbed) |

"Stubbed" = the skill exists for triggering and routing but its body is a one-line placeholder. Bodies are filled in over time as we use them.

## Getting started

Three good first runs:

1. **`/klick-management:self-awareness-assessment`** — the grounding work the rest of the library assumes. Run this once when starting a new role or as a periodic check-in.
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
