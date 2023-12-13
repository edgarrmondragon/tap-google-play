"""Stream type classes for tap-google-play."""

from __future__ import annotations

from typing import Iterable

from google_play_scraper import Sort, app, reviews
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
        th.Property("appId", th.StringType),
        th.Property("developerId", th.StringType),
    ).to_dict()

    def get_records(self, context: dict | None) -> Iterable[dict]:
        """Return a generator of row-type dictionary objects."""
        start_date = self.get_starting_timestamp(context)
        if start_date:
            start_date = start_date.replace(tzinfo=None)

        for app_id in self.config.get("app_id_list", [self.config.get("app_id")]):
            self.logger.info("Getting reviews for %s", app_id)
            app_details = app(app_id, lang="en", country="us")
            continuation_token = None
            while True:
                result, continuation_token = reviews(
                    app_id,
                    lang="en",
                    country="us",
                    sort=Sort.NEWEST.value,
                    count=1000,
                    continuation_token=continuation_token,
                )

                if not result:
                    break

                for record in result:
                    replication_value = record.get("at")
                    if (
                        start_date
                        and replication_value
                        and replication_value < start_date
                    ):
                        break
                    record["developerId"] = app_details["developerId"]
                    record["appId"] = app_id
                    yield record
