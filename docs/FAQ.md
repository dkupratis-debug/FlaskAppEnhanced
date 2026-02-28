# FAQ

## Access and Safety

### Can I break the repo by looking at it?
No. Viewing is read-only.

### Can I break it by forking?
No. A fork is your own copy.

### Can I push directly to this repo?
Only if you have write access. `main` is protected.

## Getting Started

### I am new. Where do I start?
1. `README.md`
2. `docs/FIRST_10_MINUTES.md`
3. Pinned issue `#9 Start Here`
4. `docs/PRACTICE_EXAMPLES.md` Exercise 1

### What should my first change be?
One sentence in `README.md` in your fork.

### Where do I see if I did it correctly?
Open `Actions` and confirm all checks are green.

## GitHub Workflow

### What is the difference between Issue and Pull Request?
- Issue: task/question/bug discussion
- Pull Request: proposed code/docs change

### Why do checks run on PRs?
To ensure quality before merge (lint, tests, docs/link checks).

### Why is my PR blocked?
Common reasons:
- checks still running
- failed check
- unresolved review comments

## Releases and Packages

### What is a Release?
Versioned project snapshot with notes and assets.

### What is a Package?
Registry-published artifact (for this repo, GHCR container image).

## Troubleshooting

### I see permission errors with pytest cache folders
Use:
- `python -m pytest -q tests`

### I see old commits on GitHub
Make sure changes were committed and pushed:
- `git add .`
- `git commit -m "..."`
- `git push`

### I still need help
Open an Issue and include:
- what step you are on
- what command you ran
- exact error text

### `python -m build` fails with temp-folder permission errors on Windows
Use a repo-local temp path, then build without isolation:

```powershell
New-Item -ItemType Directory -Force .tmp\build-temp | Out-Null
$env:TEMP = (Resolve-Path .tmp\build-temp).Path
$env:TMP = $env:TEMP
python -m build --no-isolation
```
