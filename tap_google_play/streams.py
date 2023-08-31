"""Stream type classes for tap-google-play."""

from __future__ import annotations

from typing import Iterable

from google_play_scraper import Sort, reviews
from pendulum import parse
from singer_sdk import typing as th

from tap_google_play.client import GooglePlayStream


class ReviewsStream(GooglePlayStream):
    """Define custom stream."""

    name = "reviews"
    primary_keys = ["reviewId"]  # noqa: RUF012
    replication_key = "at"
    schema = th.PropertiesList(
        th.Property("userName", th.StringType),
        th.Property("userImage", th.StringType),
        th.Property("content", th.StringType),
        th.Property("score", th.IntegerType),
        th.Property("thumbsUpCount", th.IntegerType),
        th.Property("reviewCreatedVersion", th.StringType),
        th.Property("at", th.DateTimeType),
        th.Property("replyContent", th.StringType),
        th.Property("repliedAt", th.DateTimeType),
        th.Property("reviewId", th.StringType),
        th.Property("appVersion", th.StringType),
    ).to_dict()

    def get_records(self, context: dict | None) -> Iterable[dict]:
        """Return a generator of row-type dictionary objects."""
        app_id = self.config.get("app_id")

        continuation_token = None

        start_date = self.get_starting_replication_key_value(context)
        if start_date:
            start_date = parse(start_date)

        self.logger.info("Getting reviews for %s", app_id)

        while True:
            result, continuation_token = reviews(
                app_id,
                lang="en",
                country="us",
                sort=Sort.NEWEST,
                count=1000,
                continuation_token=continuation_token,
            )

            if not result:
                break

            if start_date:
                for record in result:
                    if record.get("at") > start_date.replace(tzinfo=None):
                        yield record
            else:
                yield from result
