"""GooglePlay tap class."""

from typing import List

from singer_sdk import Tap, Stream
from singer_sdk import typing as th  # JSON schema typing helpers

from tap_google_play.streams import (
    GooglePlayStream,
    ReviewsStream 
)

STREAM_TYPES = [
    ReviewsStream
]


class TapGooglePlay(Tap):
    """GooglePlay tap class."""
    name = "tap-google-play"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "access_token",
            th.StringType
        ),
        th.Property(
            "refresh_token",
            th.StringType
        ),
        th.Property(
            "package_name",
            th.StringType,
            required=True
        ),
        th.Property(
            "start_date",
            th.DateTimeType,
            description="The earliest record date to sync"
        )
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]
