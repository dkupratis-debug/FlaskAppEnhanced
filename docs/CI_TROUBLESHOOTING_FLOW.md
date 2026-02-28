# CI Troubleshooting Flow

Use this when a PR check fails.

## Step 1: Identify the failing check

1. Open the PR.
1. Open `Checks`.
1. Click the failed job.
1. Scroll to first error line.

## Step 2: Apply the right fix path

### `test` failed

1. Run `pytest -q tests` locally.
1. Fix failing logic or test expectations.
1. Re-run `pytest -q tests`.
1. Commit + push.

### `precommit` failed

1. Run `pre-commit run --all-files`.
1. Accept auto-fixes if safe.
1. Re-run until clean.
1. Commit + push.

### `markdownlint` failed

1. Open reported markdown file/line.
1. Fix heading/list/line-length formatting.
1. Re-run local markdown lint (or pre-commit).
1. Commit + push.

### `yamllint` failed

1. Open reported YAML file/line.
1. Fix indentation, spacing, or syntax.
1. Re-run lint.
1. Commit + push.

### `links` failed

1. Open failing URL list in job log.
1. Remove dead links or replace with valid URLs.
1. Re-run checks.
1. Commit + push.

### Build step fails locally with Windows temp permission error

1. Create local temp folder: `New-Item -ItemType Directory -Force .tmp\build-temp | Out-Null`
1. Set temp vars:
   - `$env:TEMP = (Resolve-Path .tmp\build-temp).Path`
   - `$env:TMP = $env:TEMP`
1. Run build: `python -m build --no-isolation`

## Step 3: Confirm merge gates

Even after checks pass, merge may still be blocked by policy:

- review required
- code owner review required
- last push approval required

Open PR summary to see the exact blocker message.

## Fast command set

```powershell
pytest -q tests
pre-commit run --all-files
ruff check .
```
