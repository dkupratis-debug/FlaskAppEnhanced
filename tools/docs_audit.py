"""Lightweight documentation quality audit for this repository.

Checks:
1) Required docs exist.
2) Required docs are discoverable from docs/INDEX.md.
3) Markdown fences are balanced.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
INDEX = DOCS / "INDEX.md"

REQUIRED_DOCS = [
    "docs/START_HERE.md",
    "docs/FIRST_10_MINUTES.md",
    "docs/START_HERE_BY_ROLE.md",
    "docs/PRACTICE_EXAMPLES.md",
    "docs/CI_TROUBLESHOOTING_FLOW.md",
    "docs/TRAINING_OPERATIONS.md",
    "docs/SAFE_SHARING.md",
]


def fail(message: str) -> None:
    raise SystemExit(message)


def check_required_files() -> None:
    missing = []
    for rel in REQUIRED_DOCS:
        if not (ROOT / rel).exists():
            missing.append(rel)
    if missing:
        fail("Missing required docs:\n- " + "\n- ".join(missing))


def check_index_links() -> None:
    index_text = INDEX.read_text(encoding="utf-8")
    missing_links = []
    for rel in REQUIRED_DOCS:
        if f"`{rel}`" not in index_text:
            missing_links.append(rel)
    if missing_links:
        fail("docs/INDEX.md missing required links:\n- " + "\n- ".join(missing_links))


def check_markdown_fences() -> None:
    fence_re = re.compile(r"^[ \t]{0,3}([`~]{3,})(.*)$")
    problems = []
    for path in ROOT.rglob("*.md"):
        lines = path.read_text(encoding="utf-8").splitlines()
        open_fence_char = None
        open_fence_len = 0
        for line in lines:
            match = fence_re.match(line)
            if not match:
                continue

            marker = match.group(1)
            marker_char = marker[0]
            marker_len = len(marker)
            trailer = match.group(2).strip()

            if open_fence_char is None:
                open_fence_char = marker_char
                open_fence_len = marker_len
                continue

            if (
                marker_char == open_fence_char
                and marker_len >= open_fence_len
                and trailer == ""
            ):
                open_fence_char = None
                open_fence_len = 0

        if open_fence_char is not None:
            problems.append(str(path.relative_to(ROOT)))
    if problems:
        fail("Unbalanced markdown fences:\n- " + "\n- ".join(problems))


def main() -> int:
    check_required_files()
    check_index_links()
    check_markdown_fences()
    print("Documentation audit passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
