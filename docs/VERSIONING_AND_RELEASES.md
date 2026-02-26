# Versioning and Release Process

This repo uses semantic versioning:
- `MAJOR.MINOR.PATCH` (example: `0.2.3`)

## How Versions Are Used Here
- Git tags: `v0.2.3`
- Python package version: `pyproject.toml` -> `project.version = "0.2.3"`
- GitHub Release title/tag: created from the pushed tag

## Important Guard (Implemented)
The release workflow validates that:
- pushed tag == `v{project.version}`

If they do not match, the release job fails before publishing artifacts.

This prevents a mismatch like:
- tag `v0.2.2`
- artifacts named `0.2.1`

## Release Checklist (Maintainer)
1. Update code/docs
2. Update `CHANGELOG.md`
3. Bump `pyproject.toml` version
4. Open PR and merge to `main`
5. Create and push tag `vX.Y.Z`
6. Verify Actions runs:
   - `CI`
   - `Release`
   - `Package (GHCR)`
7. Verify GitHub Release assets match the tag version

## Patch vs Minor vs Major
- `PATCH` (`0.2.4`): bug fixes/docs/maintenance
- `MINOR` (`0.3.0`): new features, backward-compatible changes
- `MAJOR` (`1.0.0`): breaking changes or stable milestone

## Teaching Tip
Show learners both:
- the tag (`v0.2.3`) in the GitHub Releases tab
- the version in `pyproject.toml`

Then explain why automation checks consistency between them.
