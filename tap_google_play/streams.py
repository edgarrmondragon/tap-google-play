"""Stream type classes for tap-google-play."""

from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_google_play.client import GooglePlayStream


class ReviewsStream(GooglePlayStream):
    name = "reviews"
    path = "/reviews"
    primary_keys = ["reviewId"]
    replication_key = None
    records_jsonpath = "$.reviews[*]"

    schema = th.PropertiesList(
        th.Property("reviewId", th.StringType),
        th.Property("authorName", th.StringType),
        th.Property("comments", th.ArrayType(
            th.CustomType({
                "type": ["object", "string", "null"]
            })
        ))
    ).to_dict()

