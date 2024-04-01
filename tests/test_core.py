"""Tests standard tap features using the built-in SDK tests library."""

from __future__ import annotations

from singer_sdk.testing import get_tap_test_class

from tap_google_play.tap import TapGooglePlay

SAMPLE_CONFIG = {
    "start_date": "2023-01-01T00:00:00Z",
}


TestTapGooglePlay = get_tap_test_class(TapGooglePlay, config=SAMPLE_CONFIG)
