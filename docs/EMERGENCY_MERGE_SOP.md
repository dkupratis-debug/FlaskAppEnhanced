# Emergency Merge SOP

Use this SOP only when a pull request must be merged and normal review policy blocks merge due to reviewer availability.

## Preconditions

Complete all items before changing branch protection:

- [ ] PR diff has been reviewed by maintainer
- [ ] All required checks are green
- [ ] No unresolved review threads
- [ ] Business reason for emergency merge is documented in PR comment

## Step 1: Capture Current Protection Settings

Open repo settings:

1. `Settings` -> `Branches`
2. Edit the `main` branch protection/ruleset
3. Record current values:
   - Required approving reviews count
   - Require approval of most recent push
   - Required status checks
   - Require conversation resolution
   - Enforce admins

## Step 2: Temporarily Relax Only What Is Needed

Adjust the smallest possible setting for merge:

1. Keep `Require a pull request before merging` enabled
2. Temporarily disable one of:
   - `Require approval of the most recent reviewable push`, or
   - Required approvals count (set to `0`) if absolutely necessary
3. Save changes

Do not disable unrelated safeguards.

## Step 3: Merge the PR

On the PR page:

1. Confirm required checks are still green
2. Merge using `Squash and merge` (preferred)
3. Delete source branch after merge
4. Add a short PR comment: merged under emergency SOP with temporary policy relaxation

## Step 4: Immediately Restore Protections

Return to `Settings` -> `Branches` and restore exactly:

- [ ] Required approval count restored
- [ ] Last-push approval requirement restored
- [ ] Required checks unchanged
- [ ] Conversation resolution restored
- [ ] Admin enforcement restored

## Step 5: Verify via CLI (Optional but Recommended)

```powershell
gh api repos/<owner>/<repo>/branches/main/protection --jq ".required_pull_request_reviews"
```

Confirm:

- `required_approving_review_count` is expected value
- `require_last_push_approval` is expected value (`true` if used previously)

## Step 6: Post-Incident Note

Create a short internal note in PR description or issue:

- Why emergency merge was needed
- Who approved policy change
- Exact start/end time of temporary relaxation
- Confirmation that protections were restored

## Guardrails

- Never leave relaxed protection settings in place.
- Never bypass checks for convenience.
- Prefer waiting for normal review unless there is a real delivery/blocking reason.
- If emergency merges become frequent, add more maintainers with write access and enable auto-merge.
