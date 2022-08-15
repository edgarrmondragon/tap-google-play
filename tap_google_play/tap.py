from typing import List

from singer_sdk import Tap, Stream
from singer_sdk import typing as th
from tap_google_play.streams import (ReviewsStream)

STREAM_TYPES = [ReviewsStream]

class TapGooglePlay(Tap):
    """GooglePlay tap class."""
    name = "tap-googleplay"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "app_id",
            th.StringType,
            required=True
        ),
        th.Property(
            "start_date",
            th.DateTimeType,
            required=False
        )
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]

if __name__ == '__main__':
    TapGooglePlay.cli()
