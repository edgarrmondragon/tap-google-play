"""Stream type classes for tap-google-play."""

from __future__ import annotations
from os import PathLike

from typing import Iterable

from google_play_scraper import Sort, reviews, app
from pendulum import parse
from singer_sdk import typing as th
import singer_sdk._singerlib as singer
from singer_sdk.tap_base import Tap

from tap_google_play.client import GooglePlayStream


class ReviewsStream(GooglePlayStream):
    """Define custom stream."""

    def __init__(self, *args, **kwargs) -> None:
        self.app_id = kwargs.pop("app_id")
        super().__init__(*args, **kwargs)
        
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
        continuation_token = None
        app_details = app(
            self.app_id,
            lang='en', # defaults to 'en'
            country='us' # defaults to 'us'
        )
        context = {"developerId": app_details["developerId"], "appId": self.app_id}
        start_date = self.get_starting_replication_key_value(context)
        if start_date:
            start_date = parse(start_date)

        self.logger.info("Getting reviews for %s", self.app_id)

        it = 0
        while True:
            result, continuation_token = reviews(
                self.app_id,
                lang="en",
                country="us",
                sort=Sort.NEWEST,
                count=1000,
                continuation_token=continuation_token,
            )

            if not result:
                break
            if it > 0:
                break
            if start_date:
                for record in result:
                    if record.get("at") > start_date.replace(tzinfo=None):
                        yield record
            else:
                yield from result
            it += 1

    def post_process(
        self,
        row: dict,
        context: dict | None = None,  # noqa: ARG002
    ) -> dict | None:
        # row
        row["developerId"] = context["developerId"]
        row["appId"] = context["appId"]
        return super().post_process(row, context)
    
    # def post_process(
    #     self,
    #     row: dict,
    #     context: dict | None = None,  # noqa: ARG002
    # ) -> dict | None:
    #     # row
    #     row["developerId"] = context["developerId"]
    #     row["appId"] = context["appId"]
    #     return super().post_process(row, context)