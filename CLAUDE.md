# CLAUDE.md

This file is read automatically by Claude Code (in the terminal and in the
GitHub Action) at the start of every session. Treat it as the standing
instructions you'd give a new teammate. The more accurate this is, the more
the AI's output matches how *your* team actually works.

## Project
A tiny Python library (`textutils`) used to learn the modern PR + CI/CD flow.

## Commands
- Install dev deps: `pip install pytest ruff`
- Run tests: `pytest -q`
- Lint: `ruff check src tests`

## Conventions
- Source lives in `src/textutils/`, tests in `tests/`.
- Every behaviour change needs a matching test.
- Keep functions small and pure where possible; add a docstring with examples.
- Branch names: `<initials>/ENG-1234-short-description`.
- Commit messages: imperative mood, reference the ticket, e.g.
  `Add max_length support to slugify (ENG-1234)`.

## Before opening a PR (always do this)
1. Run `ruff check src tests` and fix anything it flags.
2. Run `pytest -q` and make sure everything passes.
3. Write a PR description that fills in the template.

## Guardrails
- Never commit secrets, API keys, or customer data.
- Don't change unrelated files in the same PR.
- If a ticket is ambiguous, ask a clarifying question instead of guessing.
