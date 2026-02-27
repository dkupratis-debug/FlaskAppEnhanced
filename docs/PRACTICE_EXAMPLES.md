# Practice Examples

Use these exercises to practice GitHub skills from beginner to intermediate.

## How to Use This File

1. Pick one exercise.
2. Do it in your own fork first.
3. Use the "Success check" section to confirm you did it right.

## Beginner (Start Here)

### Exercise 1: Tiny README Fix
- Goal: Learn branch -> commit -> PR flow.
- Steps:
1. Fork the repo.
2. Create a branch named `docs/readme-one-line-fix`.
3. Edit one sentence in `README.md`.
4. Commit and open a PR in your fork.
- Success check:
1. PR exists.
2. `Actions` checks are green.
3. The changed line appears in `Files changed`.

### Exercise 2: Find the Latest Release
- Goal: Learn where releases live and what they contain.
- Steps:
1. Open `Releases`.
2. Open the latest version.
3. Find the wheel and source assets.
- Success check:
1. You can name the latest tag.
2. You can explain what each asset file is.

### Exercise 3: Read an Actions Run
- Goal: Understand CI status.
- Steps:
1. Open `Actions`.
2. Open a successful `CI` run.
3. Open job `test`.
4. Read the first and last log steps.
- Success check:
1. You can explain what was checked.
2. You can say pass/fail status.

## Beginner-Intermediate

### Exercise 4: Improve a Doc Link
- Goal: Practice small docs improvements.
- Steps:
1. Pick one doc in `docs/`.
2. Add one useful link to another related doc.
3. Open PR.
- Success check:
1. Link works.
2. PR description explains why the link helps.

### Exercise 5: Review a PR with Checklist
- Goal: Practice reviewer workflow.
- Steps:
1. Open a PR (existing or in your fork).
2. Use `docs/PR_REVIEW_CHECKLIST.md`.
3. Leave at least one line comment and one summary comment.
- Success check:
1. Review comments are posted.
2. You can explain at least one risk or improvement.

### Exercise 6: Track One File History
- Goal: Learn file-level Git history.
- Steps:
1. Run:
   - `git log --follow --stat -- README.md`
2. Pick one commit from output.
3. Open that commit on GitHub and inspect changes.
- Success check:
1. You can identify who changed the file and when.
2. You can explain what changed in that commit.

## Intermediate

### Exercise 7: Compare Two Releases
- Goal: Learn version-based diffs.
- Steps:
1. Run:
   - `git diff --stat v0.2.2..v0.2.3`
2. Open both release pages in GitHub.
3. Match file changes to release notes.
- Success check:
1. You can explain what changed between the two tags.

### Exercise 8: Local Quality Check
- Goal: Practice pre-PR validation.
- Steps:
1. Run:
   - `python -m ruff check .`
   - `python -m pytest -q tests`
2. Fix any failures.
3. Open PR only after both pass.
- Success check:
1. Both commands pass.
2. PR checks pass on GitHub.

### Exercise 9: Release Workflow Reading
- Goal: Understand release automation.
- Steps:
1. Open `.github/workflows/release.yml`.
2. Find tag/version guard logic.
3. Explain why it exists.
- Success check:
1. You can explain how mismatched tags are prevented.

## Advanced (Optional)

### Exercise 10: Demo Deployment Walkthrough
- Goal: Understand production-style setup basics.
- Steps:
1. Read `docs/DEPLOY_DEMO.md`.
2. Review `render.yaml`.
3. Identify required environment variables.
- Success check:
1. You can list `SECRET_KEY` and `TRUST_PROXY_COUNT` and why they matter.

### Exercise 11: Security Review Drill
- Goal: Build secure maintainer habits.
- Steps:
1. Review `SECURITY.md` and `docs/SAFE_SHARING.md`.
2. Check branch protection settings on `main`.
3. Check collaborator access.
- Success check:
1. You can explain how unauthorized pushes are blocked.

### Exercise 12: Teach-Back
- Goal: Confirm understanding by explaining it to someone else.
- Steps:
1. Write a short summary:
   - what `Issues`, `PRs`, `Actions`, and `Releases` do.
2. Share your summary with a friend.
- Success check:
1. Someone non-technical can follow your explanation.

## Suggested Learning Order

1. Exercise 1
2. Exercise 2
3. Exercise 3
4. Exercise 5
5. Exercise 8
6. Exercise 7
7. Exercise 9
