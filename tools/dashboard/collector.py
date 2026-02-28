"""Collect and store local engagement snapshots for FlaskAppEnhanced.

Usage:
  python tools/dashboard/collector.py
"""

from __future__ import annotations

import json
import os
import sqlite3
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

REPO = os.getenv("DASHBOARD_REPO", "dkupratis-debug/FlaskAppEnhanced")
API_BASE = "https://api.github.com"
GRAPHQL_URL = f"{API_BASE}/graphql"
DEFAULT_DB_PATH = Path(__file__).resolve().parent / "data" / "engagement.db"


@dataclass
class Snapshot:
    captured_at: str
    views_count: int
    views_uniques: int
    clones_count: int
    clones_uniques: int
    open_issues: int
    open_prs: int
    discussions_count: int
    discussion_comments_total: int
    workflow_runs_24h: int
    workflow_failures_24h: int
    raw_json: str


def _headers() -> dict[str, str]:
    token = os.getenv("GITHUB_TOKEN", "").strip()
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "FlaskAppEnhanced-LocalDashboard",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


def _request_json(url: str, method: str = "GET", payload: dict[str, Any] | None = None) -> Any:
    data = None
    headers = _headers()
    if payload is not None:
        data = json.dumps(payload).encode("utf-8")
        headers["Content-Type"] = "application/json"

    req = Request(url, data=data, method=method, headers=headers)
    try:
        with urlopen(req, timeout=25) as response:
            return json.loads(response.read().decode("utf-8"))
    except HTTPError as exc:
        body = exc.read().decode("utf-8", errors="ignore")
        raise RuntimeError(f"GitHub API error {exc.code} for {url}: {body}") from exc
    except URLError as exc:
        raise RuntimeError(f"Network error for {url}: {exc}") from exc


def _request_json_with_headers(
    url: str, method: str = "GET", payload: dict[str, Any] | None = None
) -> tuple[Any, dict[str, str]]:
    data = None
    headers = _headers()
    if payload is not None:
        data = json.dumps(payload).encode("utf-8")
        headers["Content-Type"] = "application/json"

    req = Request(url, data=data, method=method, headers=headers)
    try:
        with urlopen(req, timeout=25) as response:
            body = json.loads(response.read().decode("utf-8"))
            resp_headers = {k.lower(): v for k, v in response.headers.items()}
            return body, resp_headers
    except HTTPError as exc:
        body = exc.read().decode("utf-8", errors="ignore")
        raise RuntimeError(f"GitHub API error {exc.code} for {url}: {body}") from exc
    except URLError as exc:
        raise RuntimeError(f"Network error for {url}: {exc}") from exc


def _next_link(headers: dict[str, str]) -> str | None:
    link_header = headers.get("link", "")
    if not link_header:
        return None
    for part in link_header.split(","):
        section = part.strip()
        if 'rel="next"' not in section:
            continue
        start = section.find("<")
        end = section.find(">", start + 1)
        if start != -1 and end != -1:
            return section[start + 1 : end]
    return None


def _paginate_rest(url: str) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    next_url: str | None = url
    while next_url:
        body, headers = _request_json_with_headers(next_url)
        if not isinstance(body, list):
            break
        items.extend(body)
        next_url = _next_link(headers)
    return items


def _paginate_workflow_runs(url: str) -> list[dict[str, Any]]:
    runs: list[dict[str, Any]] = []
    next_url: str | None = url
    while next_url:
        body, headers = _request_json_with_headers(next_url)
        if not isinstance(body, dict):
            break
        for run in body.get("workflow_runs", []):
            runs.append(run)
        next_url = _next_link(headers)
    return runs


def _graphql(query: str) -> Any:
    return _request_json(GRAPHQL_URL, method="POST", payload={"query": query})


def _fetch_views_clones(repo: str) -> dict[str, int]:
    views = _request_json(f"{API_BASE}/repos/{repo}/traffic/views")
    clones = _request_json(f"{API_BASE}/repos/{repo}/traffic/clones")
    return {
        "views_count": int(views.get("count", 0)),
        "views_uniques": int(views.get("uniques", 0)),
        "clones_count": int(clones.get("count", 0)),
        "clones_uniques": int(clones.get("uniques", 0)),
    }


def _fetch_issue_pr_counts(repo: str) -> dict[str, int]:
    issues = _paginate_rest(f"{API_BASE}/repos/{repo}/issues?state=open&per_page=100")
    open_issues = 0
    open_prs = 0
    for item in issues:
        if "pull_request" in item:
            open_prs += 1
        else:
            open_issues += 1
    return {"open_issues": open_issues, "open_prs": open_prs}


def _fetch_discussions(repo_owner: str, repo_name: str) -> dict[str, int]:
    total_count = 0
    comment_total = 0
    has_next = True
    cursor = "null"

    while has_next:
        query = f"""
        query {{
          repository(owner: \"{repo_owner}\", name: \"{repo_name}\") {{
            discussions(
              first: 100,
              after: {cursor},
              orderBy: {{field: UPDATED_AT, direction: DESC}}
            ) {{
              totalCount
              pageInfo {{ hasNextPage endCursor }}
              nodes {{
                comments {{ totalCount }}
              }}
            }}
          }}
        }}
        """
        result = _graphql(query)
        if result.get("errors"):
            raise RuntimeError(f"GraphQL error: {result['errors']}")
        discussions = result["data"]["repository"]["discussions"]
        total_count = int(discussions["totalCount"])
        comment_total += sum(int(n["comments"]["totalCount"]) for n in discussions["nodes"])

        page_info = discussions["pageInfo"]
        has_next = bool(page_info["hasNextPage"])
        cursor_value = page_info["endCursor"]
        if has_next and cursor_value:
            cursor = f'"{cursor_value}"'
        else:
            cursor = "null"

    return {"discussions_count": total_count, "discussion_comments_total": comment_total}


def _fetch_workflow_health(repo: str) -> dict[str, int]:
    since = datetime.now(timezone.utc) - timedelta(days=1)
    runs = _paginate_workflow_runs(f"{API_BASE}/repos/{repo}/actions/runs?per_page=100")
    runs_24h = 0
    failures_24h = 0
    for run in runs:
        created_at = datetime.fromisoformat(run["created_at"].replace("Z", "+00:00"))
        if created_at < since:
            continue
        runs_24h += 1
        if run.get("conclusion") not in {"success", None}:
            failures_24h += 1
    return {
        "workflow_runs_24h": runs_24h,
        "workflow_failures_24h": failures_24h,
    }


def ensure_db(db_path: Path) -> None:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(db_path) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS snapshots (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                captured_at TEXT NOT NULL,
                views_count INTEGER NOT NULL,
                views_uniques INTEGER NOT NULL,
                clones_count INTEGER NOT NULL,
                clones_uniques INTEGER NOT NULL,
                open_issues INTEGER NOT NULL,
                open_prs INTEGER NOT NULL,
                discussions_count INTEGER NOT NULL,
                discussion_comments_total INTEGER NOT NULL,
                workflow_runs_24h INTEGER NOT NULL,
                workflow_failures_24h INTEGER NOT NULL,
                raw_json TEXT NOT NULL
            )
            """
        )
        conn.commit()


def collect_snapshot(repo: str = REPO) -> Snapshot:
    owner, name = repo.split("/", maxsplit=1)
    metrics: dict[str, int] = {}
    metrics.update(_fetch_views_clones(repo))
    metrics.update(_fetch_issue_pr_counts(repo))
    metrics.update(_fetch_discussions(owner, name))
    metrics.update(_fetch_workflow_health(repo))

    captured_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    return Snapshot(
        captured_at=captured_at,
        views_count=metrics["views_count"],
        views_uniques=metrics["views_uniques"],
        clones_count=metrics["clones_count"],
        clones_uniques=metrics["clones_uniques"],
        open_issues=metrics["open_issues"],
        open_prs=metrics["open_prs"],
        discussions_count=metrics["discussions_count"],
        discussion_comments_total=metrics["discussion_comments_total"],
        workflow_runs_24h=metrics["workflow_runs_24h"],
        workflow_failures_24h=metrics["workflow_failures_24h"],
        raw_json=json.dumps(metrics, sort_keys=True),
    )


def save_snapshot(snapshot: Snapshot, db_path: Path = DEFAULT_DB_PATH) -> None:
    ensure_db(db_path)
    with sqlite3.connect(db_path) as conn:
        conn.execute(
            """
            INSERT INTO snapshots (
                captured_at,
                views_count,
                views_uniques,
                clones_count,
                clones_uniques,
                open_issues,
                open_prs,
                discussions_count,
                discussion_comments_total,
                workflow_runs_24h,
                workflow_failures_24h,
                raw_json
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                snapshot.captured_at,
                snapshot.views_count,
                snapshot.views_uniques,
                snapshot.clones_count,
                snapshot.clones_uniques,
                snapshot.open_issues,
                snapshot.open_prs,
                snapshot.discussions_count,
                snapshot.discussion_comments_total,
                snapshot.workflow_runs_24h,
                snapshot.workflow_failures_24h,
                snapshot.raw_json,
            ),
        )
        conn.commit()


def load_recent(db_path: Path = DEFAULT_DB_PATH, limit: int = 30) -> list[dict[str, Any]]:
    ensure_db(db_path)
    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        rows = conn.execute(
            """
            SELECT captured_at, views_count, views_uniques, clones_count, clones_uniques,
                   open_issues, open_prs, discussions_count, discussion_comments_total,
                   workflow_runs_24h, workflow_failures_24h
            FROM snapshots
            ORDER BY id DESC
            LIMIT ?
            """,
            (limit,),
        ).fetchall()
    return [dict(row) for row in rows]


def collect_and_store(repo: str = REPO, db_path: Path = DEFAULT_DB_PATH) -> Snapshot:
    snapshot = collect_snapshot(repo)
    save_snapshot(snapshot, db_path)
    return snapshot


def main() -> int:
    snapshot = collect_and_store()
    print("Stored snapshot:")
    print(f"- captured_at: {snapshot.captured_at}")
    print(f"- views(14d): {snapshot.views_count} total / {snapshot.views_uniques} unique")
    print(f"- clones(14d): {snapshot.clones_count} total / {snapshot.clones_uniques} unique")
    print(f"- open issues/prs: {snapshot.open_issues}/{snapshot.open_prs}")
    print(
        "- discussions/comments: "
        f"{snapshot.discussions_count}/{snapshot.discussion_comments_total}"
    )
    print(
        "- workflow 24h (runs/failures): "
        f"{snapshot.workflow_runs_24h}/{snapshot.workflow_failures_24h}"
    )
    print(f"- db: {DEFAULT_DB_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
