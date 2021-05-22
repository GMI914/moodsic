import requests
from django.core.management import BaseCommand
from typing import Any
from collections import defaultdict
import json
from music.models import Music, VideoTags

YOUTUBE_SEARCH_URL = 'https://www.googleapis.com/youtube/v3/search'
YOUTUBE_COMMENT_URL = 'https://www.googleapis.com/youtube/v3/commentThreads'
SAVE_PATH = 'music/parser_output/'

API_KEY = 'AIzaSyDxD2mq5UYvVF-b0vFrqmAradcS3jwhhSs'


def fetchData(URL, params):
    r = requests.get(URL + '?', params=params)
    return r.text


def parseTime(time):
    if 'DT' in time:
        return 0
    time = time.replace('S', '')
    time = time.replace('PT', '')
    seconds = time.split('M')[1]
    if 'H' in time:
        minutes = time.split('M')[0].split('H')[1]
        hours = time.split('M')[0].split('H')[0]
    else:
        minutes = time.split('M')[0]
        hours = 0
    return int(seconds) + int(minutes) * 60 + int(hours) + 3600


class channelVideo:
    def __init__(self, channel_id, maxResults, key):
        self.videos = defaultdict(list)
        self.channel_id = channel_id
        self.params = {
            'part': 'id,snippet,statistics,contentDetails',
            'channelId': channel_id,
            'maxResults': maxResults,
            'key': key
        }

    def parse_videos(self):
        url_response = json.loads(fetchData(YOUTUBE_SEARCH_URL, self.params))
        nextPageToken = url_response.get('nextPageToken')
        self.format_channel_videos(url_response)

        while nextPageToken:
            self.params.update({'pageToken': nextPageToken})
            url_response = json.loads(fetchData(YOUTUBE_SEARCH_URL, self.params))
            nextPageToken = url_response.get('nextPageToken')
            self.format_channel_videos(url_response)

        self.add_data_to_db()

    def format_channel_videos(self, search_response):
        for search_result in search_response.get('items', []):
            if search_result['id']['kind'] == 'youtube#video':
                self.videos['video_id'].append(search_result['id']['videoId'])
                self.videos['title'].append(search_result['snippet']['title'])
                self.videos['like'].append(int(search_result['statistics']['likeCount']))
                self.videos['dislike'].append(int(search_result['statistics']['dislikeCount']))
                self.videos['views'].append(int(search_result['statistics']['viewCount']))
                self.videos['video_length'].append(parseTime(search_result['contentDetails']['duration']))
                self.videos['description'].append(search_result['snippet']['description'])
                self.videos['tags'].append(search_result['snippet']['tags'])

    def add_data_to_db(self):
        for obj in self.videos:
            music, created = Music.objects.update_or_create(video_id=obj.get('video_id'), defaults={
                'channel_id': self.channel_id,
                'title': obj.get('title'),
                'like': obj.get('like'),
                'dislike': obj.get('dislike'),
                'views': obj.get('views'),
                'video_length': obj.get('video_length'),
                'description': obj.get('description'),
            })
            for tag_name in obj.get('tags'):
                tag, tag_created = VideoTags.objects.get_or_create(title=tag_name)
                Music.tags.through.objects.get_or_create(
                    music_id=music.id,
                    tag_id=tag.id
                )


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('channel_id', nargs='+', type=str)

    def handle(self, *args: Any, **options: Any) -> None:
        if not options.get('channel_id'):
            print('No Chanel Id Provided')
            return
        video = channelVideo(options.get('channel_id'), 50, API_KEY)
        video.parse_videos()
