# modern-dev-starter

A deliberately tiny project for learning the modern development workflow end to end:
**branch → commit → pull request → review → CI → merge**, then layering on
**AI-assisted and AI-automated** versions of the same loop.

The actual "product" is one small function (`slugify`) plus its tests. The point
isn't the code — it's everything that happens *around* the code.

## What's in here

```
src/textutils/slug.py            the feature (a real function with real edge cases)
tests/test_slug.py               the tests CI runs to gate every PR
.github/workflows/ci.yml         Continuous Integration: lint + test on every PR
.github/workflows/claude.yml     Claude as a reviewer / @claude teammate
.github/pull_request_template.md auto-fills the PR description for good reviews
CLAUDE.md                        standing instructions Claude reads every session
.mcp.json.example                connect Claude Code to Jira (read tickets)
docs/jira-daily-loop.yml         the scheduled "read tickets, open PRs" loop
```

## Try it locally

```bash
pip install pytest ruff
pytest -q              # run the tests (this is what CI does)
ruff check src tests   # lint (also what CI does)
```

Start with **GUIDE.md** — it walks you through the whole thing in order.

_My first PR — opened 2026-06-29._
