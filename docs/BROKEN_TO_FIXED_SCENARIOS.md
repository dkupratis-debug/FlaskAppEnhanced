# Broken to Fixed Scenarios

Use these guided scenarios to practice debugging PR failures safely.

## Scenario 1: `markdownlint` fails

Broken state:
- ordered list numbering/style mismatch
- improper indentation

Practice flow:
1. Open failed `markdownlint` job in Actions.
1. Copy file + line from first error.
1. Fix formatting locally.
1. Run `pre-commit run --all-files`.
1. Push and verify green checks.

## Scenario 2: `test` fails

Broken state:
- route response text changed without test update

Practice flow:
1. Run `pytest -q tests`.
1. Inspect failing assertion.
1. Decide whether code or test is correct behavior.
1. Patch and rerun tests.
1. Push and re-check PR.

## Scenario 3: `yamllint` fails

Broken state:
- invalid indentation or malformed key/value in workflow/template YAML

Practice flow:
1. Open `yamllint` job log.
1. Fix YAML syntax.
1. Re-run local lint via pre-commit.
1. Push and validate CI.

## Scenario 4: `links` fails

Broken state:
- dead documentation URL or typo in link

Practice flow:
1. Open failed link report.
1. Replace dead link or add safe fallback.
1. Re-run checks.
1. Push and verify status.

## Suggested Training Cadence

1. Give each learner one broken scenario.
1. Ask for a short root-cause explanation in PR comments.
1. Require they link the exact failing CI log.
1. Have reviewer confirm both fix and explanation quality.
