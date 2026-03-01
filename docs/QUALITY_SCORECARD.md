# Repository Quality Scorecard

This page explains current quality posture in plain English.

Last updated: 2026-03-01

## Governance

- Branch protection on `main`: enabled
- Required approvals: 1
- Last push approval: enabled
- CODEOWNERS review: enabled
- Conversation resolution: enabled
- Admin bypass disabled by policy enforcement: effectively enforced

## CI Quality Gates

Required checks on `main`:

- `test`
- `precommit`
- `markdownlint`
- `yamllint`
- `links`

## Release Integrity

- `v*` tags protected by ruleset
- Tag update blocked: yes
- Tag deletion blocked: yes
- Release flow tied to protected branch workflow

## Security Controls

- Secret scanning: enabled
- Push protection: enabled
- Dependabot security updates: enabled
- Security best-practice guide: `docs/SECURITY_BEST_PRACTICES.md`

## Learning Experience

- Role-based onboarding: `docs/START_HERE_BY_ROLE.md`
- First 10 minute guide: `docs/FIRST_10_MINUTES.md`
- CI troubleshooting flow: `docs/CI_TROUBLESHOOTING_FLOW.md`
- Discussions onboarding: `docs/DISCUSSIONS_GUIDE.md`

## Remaining Risks to Acknowledge

- Public code can still be copied manually.
- A single maintainer bottleneck can delay approvals.
- Social engineering remains a human risk.

## Monthly Review Checklist

1. Re-verify branch protection settings.
1. Review collaborator list and permissions.
1. Check open security alerts.
1. Confirm pinned onboarding discussion is still pinned.
1. Validate docs links and examples still work.
