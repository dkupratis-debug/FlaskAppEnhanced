# Safe Sharing Guide (Friends, Social Media, and Public Learning)

This guide is for sharing the repo with friends (for example on Facebook) while minimizing risk.

## Key Point: Viewing a Repo Is Not the Same as Having Write Access
People cannot push changes to your repository unless you grant them write/admin access.

What viewers can do (public repo):
- read code
- fork the repo
- open issues / pull requests (if enabled)

What they cannot do without permission:
- push to `main`
- edit your repo settings
- access secrets

## If the Repo Stays Private
Only invited collaborators can view it.

If you want friends to learn from it without granting access:
- share screenshots/GIFs
- share a screen recording walkthrough
- share a cloned copy in a separate public learning repo

## If You Make It Public (Recommended for Learning)
This repo is already set up with protections that reduce risk:
- branch protection on `main`
- required CI checks
- admin enforcement
- release and package automation
- no secrets stored in the repo

Before making public, verify:
1. No `.env` files or secrets are committed
2. No private URLs/tokens in docs/screenshots
3. GitHub Actions permissions stay minimal
4. Only trusted collaborators have write/admin access

## Safe Sharing Checklist for Facebook
1. Share the repo URL (read-only for most people)
2. Tell people to **fork** it for practice
3. Tell them not to ask for direct write access unless needed
4. Link to:
   - `README.md`
   - `docs/GITHUB_GUIDE.md`
   - `docs/PR_REVIEW_CHECKLIST.md`
5. Mention that they can learn by watching Actions/Releases/Packages tabs

## Optional “Public Demo” Strategy (Safer Than Granting Repo Access)
- Keep your main learning repo protected
- Deploy a demo app separately (Render/Fly.io/etc.)
- Share:
  - repo URL (code learning)
  - demo URL (app interaction)
  - short video walkthrough (GitHub navigation)

## Threat Model (Simple)
- Biggest risk is not “friends hacking by viewing”
- Biggest risks are:
  - leaked credentials/tokens
  - too much collaborator access
  - weak account security (no 2FA/passkeys)
  - unsafe Actions permissions or secrets

## Recommended Account Security
- Enable 2FA or passkeys
- Use fine-grained PATs only
- Rotate unused tokens
- Review active sessions/devices in GitHub account settings
