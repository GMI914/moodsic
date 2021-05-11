import requests
from django.core.management import BaseCommand
from typing import Any

from collections import defaultdict
import json
import pandas as pd

YOUTUBE_SEARCH_URL = "https://www.googleapis.com/youtube/v3/search"
YOUTUBE_COMMENT_URL = "https://www.googleapis.com/youtube/v3/commentThreads"
SAVE_PATH = "music/parser_output/"

API_KEY = 'AIzaSyDxD2mq5UYvVF-b0vFrqmAradcS3jwhhSs'


def openURL(URL, params):
    r = requests.get(URL + "?", params=params)
    return r.text


class channelVideo:
    def __init__(self, channelid, maxResults, key):
        self.videos = defaultdict(list)
        self.params = {
            'part': 'id,snippet',
            'channelId': channelid,
            'maxResults': maxResults,
            'key': key
        }

    def load_channel_videos(self, search_response):
        for search_result in search_response.get("items", []):
            if search_result["id"]["kind"] == "youtube#video":
                self.videos["title"].append(search_result["snippet"]["title"])
                self.videos["description"].append(search_result["snippet"]["description"])
                self.videos["publishedAt"].append(search_result["snippet"]["publishedAt"])
                self.videos["videoId"].append(search_result["id"]["videoId"])
                # self.videos["liveBroadcastContent"].append(search_result["snippet"]["liveBroadcastContent"])

    def get_channel_videos(self):
        url_response = json.loads(openURL(YOUTUBE_SEARCH_URL, self.params))
        nextPageToken = url_response.get("nextPageToken")
        self.load_channel_videos(url_response)

        while nextPageToken:
            self.params.update({'pageToken': nextPageToken})
            url_response = json.loads(openURL(YOUTUBE_SEARCH_URL, self.params))
            nextPageToken = url_response.get("nextPageToken")
            self.load_channel_videos(url_response)

        self.create_df()

    def create_df(self):
        df = pd.DataFrame().from_dict(self.videos)
        df.to_json(SAVE_PATH + "search_channel_id.json")


class Command(BaseCommand):

    def handle(self, *args: Any, **options: Any) -> None:
        video = channelVideo('UCsUeNbrb8t2Td1faP1VbK2g', 50, API_KEY)
        video.get_channel_videos()
