"""Extracts data from Google Play reviews."""

from __future__ import annotations

from singer_sdk import Stream, Tap
from singer_sdk import typing as th

from tap_google_play import streams


class TapGooglePlay(Tap):
    """Singer tap for extracting data from the Google Play reviews."""

    name = "tap-google-play"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "app_id",
            th.StringType,
            description="The app ID to extract reviews from.",
        ),
        th.Property(
            "app_id_list",
            th.ArrayType(th.StringType),
            description="A list of app IDs to extract reviews from.",
        ),
        th.Property(
            "start_date",
            th.DateTimeType,
            required=False,
            description="The date to start extracting reviews from",
        ),
    ).to_dict()

    def discover_streams(self) -> list[Stream]:
        """Return a list of discovered streams."""
        return [
            streams.ReviewsStream(tap=self),
        ]


if __name__ == "__main__":
    TapGooglePlay.cli()
