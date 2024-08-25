"""Nox configuration."""

from __future__ import annotations

import nox

python_versions = [
    "3.13",
    "3.12",
    "3.11",
    "3.10",
    "3.9",
    "3.8",
]
nox.options.sessions = ("tests",)


@nox.session(python=python_versions)
def tests(session: nox.Session) -> None:
    """Execute pytest tests."""
    session.run("uv", "run", "--python", f"python{session.python}", "pytest")


@nox.session
def mypy(session: nox.Session) -> None:
    """Check types."""
    deps = ["mypy"]
    args = session.posargs or ("tap_google_play",)
    session.install(".")
    session.install(*deps)
    session.run("mypy", *args)
