# Screenshot Capture Checklist

Use this checklist when preparing screenshots/GIFs for beginners.

## Goal

Capture a clean visual walkthrough that is easy for non-technical users to follow.

## Before You Capture (Safety)

1. Confirm the repo is the correct one: `dkupratis-debug/FlaskAppEnhanced`
2. Close unrelated tabs/windows
3. Hide bookmarks bar if it shows private links
4. Make sure no secrets/tokens are visible anywhere
5. Sign out of any account you do not want shown
6. Crop or blur profile menus/notifications if needed

## Browser Setup (Consistency)

1. Set browser zoom to `100%`
2. Use one browser for all screenshots
3. Use a desktop-sized window (not tiny)
4. Keep the same window size for all captures

## Exact Screenshots to Capture (Recommended Order)

1. Repo homepage (`Code` tab)
   - Include repo name, visibility badge, top tabs, and README start
   - Save as `github-code-tab.png`
2. Pinned `Start Here` issue
   - Show issue title and first section
   - Save as `github-start-here-issue.png`
3. Workshop issues list
   - Show labels and pinned issue
   - Save as `github-issues-list.png`
4. Pull Request conversation page
   - Show checks summary and review area (use a sample PR)
   - Save as `github-pr-conversation.png`
5. Pull Request `Files changed` tab
   - Show line comments area if possible
   - Save as `github-pr-files-changed.png`
6. Actions run (successful)
   - Show workflow name and green checks
   - Save as `github-actions-run-success.png`
7. Releases page
   - Show latest release and assets
   - Save as `github-release-page.png`
8. Packages page (if visible/public)
   - Show package name and tags
   - Save as `github-package-page.png`
9. Branch protection / ruleset screen (optional advanced)
   - Save as `github-branch-protection.png`

## Optional GIFs (5-15 seconds)

1. Open a PR and watch checks start
   - `open-pr-and-watch-ci.gif`
2. Find a workflow run in `Actions`
   - `find-workflow-run-in-actions.gif`
3. Open a release and inspect assets
   - `create-release-and-view-assets.gif`

## Quality Checklist (Before Saving)

- Text is readable without zooming too much
- Important UI labels are visible
- No private or personal info is visible
- Filenames match the plan in `docs/images/README.md`

## After Capture

1. Save files into `docs/images/`
2. Update `README.md` and/or `docs/GITHUB_GUIDE.md` to embed the screenshots
3. Keep image sizes reasonable (prefer PNG, compress if needed)
