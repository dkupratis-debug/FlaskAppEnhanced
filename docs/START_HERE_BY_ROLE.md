# Start Here by Role

Use this page to jump directly to the right learning path.

If you want one universal entry point first, read:
- `docs/START_HERE.md`

## Beginner Path (first 60 minutes)

1. Open `README.md`.
1. Open `docs/FIRST_10_MINUTES.md`.
1. Open `https://github.com/dkupratis-debug/FlaskAppEnhanced/discussions/29`.
1. Run locally:
   - `python -m venv venv`
   - `.\venv\Scripts\activate`
   - `pip install -r requirements.txt`
   - `python app.py`
1. Visit:
   - `http://127.0.0.1:5000/`
   - `http://127.0.0.1:5000/learn`
1. Complete one tiny task from `docs/PRACTICE_EXAMPLES.md`.
1. Ask one question in `Q&A` if blocked.

Expected outcome:
- You understand repository tabs, basic workflow, and how to run the app.

## Reviewer Path (PR review practice)

1. Open a PR in this repo.
1. Use `docs/PR_REVIEW_CHECKLIST.md`.
1. Validate:
   - behavior change
   - tests
   - lint/format
   - security impact
1. Review CI in Actions (`test`, `precommit`, `markdownlint`, `yamllint`, `links`).
1. Leave concrete comments with file references.

Expected outcome:
- You can perform a structured, security-aware PR review.

## Maintainer Path (operations and safety)

1. Read:
   - `docs/TRAINING_OPERATIONS.md`
   - `docs/DISCUSSIONS_GUIDE.md`
   - `docs/SECURITY_BEST_PRACTICES.md`
1. Verify branch protections and rulesets in Settings.
1. Triage:
   - open Issues
   - open Discussions
   - open Dependabot alerts
1. Run weekly checklist from `docs/SECURITY_BEST_PRACTICES.md`.
1. Publish one weekly announcement and one poll.

Expected outcome:
- You can run the repo as a safe, consistent training program.

## Cross-Role References

- Universal start path: `docs/START_HERE.md`
- Troubleshooting path: `docs/CI_TROUBLESHOOTING_FLOW.md`
- Security baseline: `docs/SECURITY_BEST_PRACTICES.md`
