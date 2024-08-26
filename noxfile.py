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
nox.needs_version = ">=2024.4.15"
nox.options.default_venv_backend = "uv"
nox.options.sessions = ("tests",)


@nox.session(python=python_versions)
def tests(session: nox.Session) -> None:
    """Execute pytest tests."""
    session.run(
        "uv",
        "run",
        "--verbose",
        "--python",
        f"python{session.python}",
        "pytest",
        *session.posargs,
    )


@nox.session
def mypy(session: nox.Session) -> None:
    """Check types."""
    args = session.posargs or ("tap_google_play",)
    session.run("uv", "run", "mypy", *args)
