from typing import Any
from django.core.management import BaseCommand
from collections import defaultdict
import json
import requests
import pandas as pd


def openURL(URL, params):
    r = requests.get(URL + "?", params=params)
    return r.text


YOUTUBE_SEARCH_URL = "https://www.googleapis.com/youtube/v3/search"
YOUTUBE_COMMENT_URL = "https://www.googleapis.com/youtube/v3/commentThreads"
SAVE_PATH = "music/parser_output/"

API_KEY = 'AIzaSyDxD2mq5UYvVF-b0vFrqmAradcS3jwhhSs'


class VideoComment:
    def __init__(self, maxResults, videoId, key):
        self.comments = defaultdict(list)
        self.replies = defaultdict(list)
        self.params = {
            'part': 'snippet,replies',
            'maxResults': maxResults,
            'videoId': videoId,
            'textFormat': 'plainText',
            'key': key
        }

    def load_comments(self, responseData):
        for item in responseData["items"]:
            comment = item["snippet"]["topLevelComment"]
            # self.comments["id"].append(comment["id"])
            self.comments["comment"].append(comment["snippet"]["textDisplay"])
            # self.comments["author"].append(comment["snippet"]["authorDisplayName"])
            # self.comments["likecount"].append(comment["snippet"]["likeCount"])
            # self.comments["publishedAt"].append(comment["snippet"]["publishedAt"])

            if 'replies' in item.keys():
                for reply in item['replies']['comments']:
                    self.replies["replyComment"].append(reply["snippet"]["textDisplay"])
                    # self.replies["parentId"].append(reply["snippet"]["parentId"])
                    # self.replies["authorDisplayName"].append(reply['snippet']['authorDisplayName'])
                    # self.replies["publishedAt"].append(reply["snippet"]["publishedAt"])
                    # self.replies["likeCount"].append(reply["snippet"]["likeCount"])

    def get_video_comments(self):
        url_response = json.loads(openURL(YOUTUBE_COMMENT_URL, self.params))
        nextPageToken = url_response.get("nextPageToken")
        self.load_comments(url_response)

        while nextPageToken:
            self.params.update({'pageToken': nextPageToken})
            url_response = json.loads(openURL(YOUTUBE_COMMENT_URL, self.params))
            nextPageToken = url_response.get("nextPageToken")
            self.load_comments(url_response)

        self.output_results()

    def output_results(self):
        df = pd.DataFrame().from_dict(self.comments)
        df.to_json(SAVE_PATH + "parent_video_comment.json")

        df = pd.DataFrame().from_dict(self.replies)
        df.to_json(SAVE_PATH + "comment_reply.json")


class Command(BaseCommand):

    def handle(self, *args: Any, **options: Any) -> None:
        video = VideoComment(50, "K1jbDJc4cfQ", API_KEY)
        video.get_video_comments()
