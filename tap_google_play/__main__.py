"""Entrypoint for tap-google-play."""

from __future__ import annotations

from tap_google_play.tap import TapGooglePlay

TapGooglePlay.cli()
