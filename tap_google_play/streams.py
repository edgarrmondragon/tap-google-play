from tracemalloc import start
from typing import Any, Dict, Optional, Union, List, Iterable

from singer_sdk import typing as th 

from tap_google_play.client import GooglePlayStream

import datetime

from google_play_scraper import reviews, Sort

class ReviewsStream(GooglePlayStream):
    """Define custom stream."""
    name = "reviews"
    primary_keys = ["id"]
    replication_key = "at"
    schema = th.PropertiesList(
        th.Property("userName", th.StringType),
        th.Property("userImage",th.StringType),
        th.Property("content",th.StringType),
        th.Property("score",th.IntegerType),
        th.Property("thumbsUpCount",th.IntegerType),
        th.Property("reviewCreatedVersion",th.StringType),
        th.Property("at",th.DateTimeType),
        th.Property("replyContent",th.StringType),
        th.Property("repliedAt",th.DateTimeType),
        th.Property("reviewId",th.StringType),
    ).to_dict()

    def get_records(self, context: Optional[dict]) -> Iterable[dict]:

        app_id = self.config.get("app_id")

        continuation_token = None
        results = []
        result = True

        start_date = self.get_starting_replication_key_value(context)
        if start_date: start_date =  datetime.datetime.strptime(
                                    start_date,'%Y-%m-%dT%H:%M:%S')

        self.logger.info(f"Getting reviews for {app_id}.")
        while result: 

            result,continuation_token = reviews(
                app_id, lang = 'en', country = 'us',
                sort = Sort.NEWEST,
                count = 1000,continuation_token=continuation_token)
                
            if start_date:
                for record in result:
                    if record.get('at') > start_date: 
                        results.append(record)
                    else: result = None
            else: 
                results += result
            
            self.logger.info(f"{results.__len__()} imported records so far.")

        return results 
