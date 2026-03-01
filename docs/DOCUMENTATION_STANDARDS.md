# Documentation Standards

Use these rules when adding or editing docs in this repository.

## Goals

- Keep beginner-first clarity
- Make every document actionable
- Keep structure consistent across files
- Avoid stale or conflicting instructions

## Required Structure (for major docs)

1. Purpose: what this doc is for
2. Audience: who should read it
3. Prerequisites: what user needs first
4. Steps: explicit steps in order
5. Expected outcome: what success looks like
6. Troubleshooting or next step links

## Writing Rules

- Use plain language and short sentences.
- Prefer exact file paths and commands.
- Use absolute GitHub links when a click target matters.
- Avoid ambiguous terms like "just", "simply", "obvious".
- Keep examples copy/paste safe.

## Formatting Rules

- Use `1.` numbering for ordered steps.
- Use fenced code blocks for commands.
- Keep headings descriptive and short.
- Keep line length readable (roughly <= 100 chars where practical).

## Link Hygiene

- Link to local files using repository paths (for maintainability).
- Link to exact GitHub pages for UI click walkthroughs.
- Re-check links when renaming docs.

## Change Hygiene

When a feature/workflow changes:

1. Update the relevant doc page.
2. Update `docs/INDEX.md` if discoverability changed.
3. Update `README.md` quick links if entry points changed.
4. Add changelog note if user-facing behavior changed.

## Monthly Doc Audit

1. Validate top onboarding path still works.
2. Validate all workflows/doc references still exist.
3. Check for outdated screenshots and stale dates.
4. Confirm security and contribution policies still match settings.
