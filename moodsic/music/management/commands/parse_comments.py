import requests
from django.core.management import BaseCommand
from typing import Any


def send_request(URL, params):
    r = requests.get(URL + "?", params=params)
    return r.text


class Command(BaseCommand):
    API_KEY = 'AIzaSyDxD2mq5UYvVF-b0vFrqmAradcS3jwhhSs'
    YOUTUBE_COMMENT_URL = "https://www.googleapis.com/youtube/v3/commentThreads"
    PARAMS = {
        'part': 'snippet,replies',
        'maxResults': 1,
        'videoId': 'K1jbDJc4cfQ',
        'textFormat': 'plainText',
        'key': API_KEY
    }

    def handle(self, *args: Any, **options: Any) -> None:
        print(send_request(self.YOUTUBE_COMMENT_URL, self.PARAMS))
