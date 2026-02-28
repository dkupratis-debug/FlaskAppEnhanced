"""Local-only engagement dashboard for FlaskAppEnhanced."""

from __future__ import annotations

import os
import secrets
from pathlib import Path

from collector import DEFAULT_DB_PATH, collect_and_store, load_recent
from flask import Flask, flash, redirect, render_template, request, session, url_for

APP = Flask(__name__)
APP.config["SECRET_KEY"] = os.getenv("DASHBOARD_SECRET_KEY", secrets.token_hex(24))
APP.config["DB_PATH"] = Path(os.getenv("DASHBOARD_DB_PATH", str(DEFAULT_DB_PATH)))
APP.config["REPO"] = os.getenv("DASHBOARD_REPO", "dkupratis-debug/FlaskAppEnhanced")
APP.config["PASSWORD"] = os.getenv("DASHBOARD_PASSWORD", "").strip()


def _auth_enabled() -> bool:
    return bool(APP.config["PASSWORD"])


def _is_authenticated() -> bool:
    if not _auth_enabled():
        return True
    return bool(session.get("dashboard_auth"))


@APP.before_request
def _guard() -> None:
    if request.endpoint in {"login", "static"}:
        return
    if not _is_authenticated():
        return redirect(url_for("login"))
    return None


@APP.route("/login", methods=["GET", "POST"])
def login():
    if not _auth_enabled():
        flash("Login disabled because DASHBOARD_PASSWORD is not set.", "warning")
        return redirect(url_for("home"))

    if request.method == "POST":
        submitted = request.form.get("password", "")
        if secrets.compare_digest(submitted, APP.config["PASSWORD"]):
            session["dashboard_auth"] = True
            flash("Logged in.", "success")
            return redirect(url_for("home"))
        flash("Invalid password.", "error")
    return render_template("login.html")


@APP.route("/logout", methods=["POST"])
def logout():
    session.pop("dashboard_auth", None)
    flash("Logged out.", "success")
    return redirect(url_for("login"))


@APP.route("/", methods=["GET"])
def home():
    snapshots = load_recent(APP.config["DB_PATH"], limit=30)
    latest = snapshots[0] if snapshots else None
    previous = snapshots[1] if len(snapshots) > 1 else None

    delta = {}
    if latest and previous:
        for key in (
            "views_count",
            "clones_count",
            "open_issues",
            "open_prs",
            "discussions_count",
            "discussion_comments_total",
            "workflow_runs_24h",
            "workflow_failures_24h",
        ):
            delta[key] = int(latest[key]) - int(previous[key])

    return render_template(
        "index.html",
        repo=APP.config["REPO"],
        latest=latest,
        previous=previous,
        delta=delta,
        snapshots=snapshots,
        auth_enabled=_auth_enabled(),
    )


@APP.route("/collect", methods=["POST"])
def collect():
    try:
        collect_and_store(repo=APP.config["REPO"], db_path=APP.config["DB_PATH"])
        flash("Snapshot collected.", "success")
    except Exception as exc:  # noqa: BLE001
        flash(f"Collection failed: {exc}", "error")
    return redirect(url_for("home"))


if __name__ == "__main__":
    APP.run(host="127.0.0.1", port=int(os.getenv("DASHBOARD_PORT", "5050")), debug=False)
