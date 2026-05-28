# klick-management

A Claude Code plugin: management practices from *Scaling People* (Claire Hughes Johnson, Stripe Press 2023) as invokable skills. Use these at decision points — producing the founding documents, OKRs, charters, reviews, and conversation preps the book teaches — not as a substitute for reading the book.

## What's in here

Six top-level "router" skills, one per chapter, plus 49 sub-skills.

| Router | Chapter | Sub-skills |
|---|---|---|
| `operating-principles` | Ch 1 — Essential Operating Principles | 4 (built) |
| `org-foundations-and-planning` | Ch 2 — Foundations and Planning | 14 (built) |
| `hiring` | Ch 3 — A Comprehensive Hiring Approach | 8 (built) |
| `team-development` | Ch 4 — Intentional Team Development | 9 (built) |
| `feedback-and-performance` | Ch 5 — Feedback and Performance Mechanisms | 11 (built) |
| `manager-self` | Conclusion — You | 3 (built) |

All 49 sub-skills are built. Each is grounded in a specific section of the book and supports three modes (teach / draft / polish).

## Getting started

Five good first runs covering different moments:

1. **`/klick-management:self-awareness-assessment`** — the grounding work the rest of the library assumes. Run once when starting a new role or as a periodic check-in.
2. **`/klick-management:write-team-charter`** — produces a complete team charter in 5-10 minutes. Fastest way to feel the library.
3. **`/klick-management:prep-qbr`** — populates a full QBR doc from the book's outline.
4. **`/klick-management:prep-to-say-the-hard-thing`** — 5-min prep before a difficult conversation.
5. **`/klick-management:run-career-conversation`** — prep + structure for a development conversation with a direct report.

Each sub-skill supports three modes:
- **`teach`** — Socratic walk-through (10-20 min); good first time
- **`draft`** — 3-5 intake questions → first draft → refinement (5-10 min); default
- **`polish`** — paste a rough version → critique → polished (2-5 min); fastest

## Installation

This repo is both the plugin source and a one-plugin marketplace named `scaling-people`. Install in Claude Code in two steps.

**1. Add the marketplace** (one-time):

```
/plugin marketplace add alfwhitehead/scaling-people
```

Or edit `~/.claude/settings.json` and add under `extraKnownMarketplaces`:

```json
"scaling-people": {
  "source": {
    "source": "github",
    "repo": "alfwhitehead/scaling-people"
  }
}
```

**2. Install and enable the plugin**:

```
/plugin install klick-management@scaling-people
```

Or add to `~/.claude/settings.json` under `enabledPlugins`:

```json
"klick-management@scaling-people": true
```

Then restart Claude Code.

**Updating to a new version**: `/plugin marketplace update scaling-people` then restart. Tagged releases (`v1.0.0`, etc.) on GitHub mark stable points.

**Local development install** (for editing skills against a checked-out clone): see [`dev/README.md`](dev/README.md) — uses a separate `scaling-people-local` marketplace pointing at your local working tree.

## How this library was built

See [docs/superpowers/specs/2026-05-27-klick-management-skill-library-design.md](docs/superpowers/specs/2026-05-27-klick-management-skill-library-design.md). The "Methodology" section explains how the book was broken down into skills and how additional books can be blended in later.

## Validation

```
python3 klick-management/scripts/validate-skills.py
```

Runs on every skill: checks frontmatter, naming, and required body structure (router / stub / built sub-skill).

## Attribution

All skill content is derived from and credited to *Scaling People: Tactics for Management and Company Building* by Claire Hughes Johnson (Stripe Press, 2023). This plugin is a working aid, not a substitute for the book.

## License

MIT. See [LICENSE](LICENSE).
