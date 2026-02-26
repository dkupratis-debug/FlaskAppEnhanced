# PR Review Checklist

Use this checklist to review pull requests consistently and teach good GitHub review habits.

## 1. Scope and Intent
- Is the PR title clear and specific?
- Does the PR description explain what changed and why?
- Is the PR focused on one goal (not many unrelated changes)?

## 2. Code Correctness
- Does the code do what the PR claims?
- Any obvious bugs, edge cases, or regressions?
- Are error cases handled safely?

## 3. Security / Safety
- Any secret, token, or credential exposure?
- Any auth/CSRF/rate-limit/security header changes?
- Any new GitHub Actions workflow permissions that are too broad?

## 4. Tests and Validation
- Are tests added or updated for behavior changes?
- Does CI pass?
- Are linting and formatting checks green?

## 5. Configuration and Deployment Impact
- Does this change `pyproject.toml`, workflow files, or runtime config?
- Could it affect releases, packaging, or production behavior?
- Are release/version changes consistent?

## 6. Documentation
- Is `README.md` updated if user behavior changed?
- Are examples/commands still accurate?
- Are new files/workflows explained?

## 7. GitHub Review Workflow
- Review `Files changed` tab carefully
- Leave comments on specific lines when needed
- Ask for changes or approve with a short rationale
- Merge only after checks are green and concerns are addressed

## Common Reviewer Questions
- "What problem does this solve?"
- "How was this tested?"
- "What could break?"
- "Does the documentation match the code?"
