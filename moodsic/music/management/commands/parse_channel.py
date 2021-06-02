import requests
from django.core.management import BaseCommand
from typing import Any
import json
from music.models import Music, VideoTags

YOUTUBE_VIDEO_URL = 'https://www.googleapis.com/youtube/v3/videos'
YOUTUBE_SEARCH_URL = 'https://www.googleapis.com/youtube/v3/search'
SAVE_PATH = 'music/parser_output/'

API_KEY = 'AIzaSyDxD2mq5UYvVF-b0vFrqmAradcS3jwhhSs'


def fetchData(URL, params):
    r = requests.get(URL + '?', params=params)
    return r.text


def parseTime(time):
    if not time:
        return 0
    if 'D' in time:
        return 0
    if 'H' in time:
        return 0
    time = time.replace('S', '')
    time = time.replace('PT', '')
    if 'M' in time:
        seconds = time.split('M')[1]
        if 'H' in time:
            minutes = time.split('M')[0].split('H')[1]
            hours = time.split('M')[0].split('H')[0]
        else:
            minutes = time.split('M')[0]
            hours = 0
    else:
        seconds = time
        minutes = 0
        hours = 0

    if seconds == '':
        seconds = 0
    if minutes == '':
        minutes = 0
    if hours == '':
        hours = 0

    return int(seconds) + int(minutes) * 60 + int(hours) * 3600


class channelVideo:
    def __init__(self, channel_id, maxResults, key):
        self.videos = []
        self.video_ids = []
        self.maxResults = maxResults
        self.key = key
        self.channel_id = channel_id

    def parse_videos(self):
        for video_id in self.video_ids:
            # if Music.objects.filter(video_id=video_id).get():
            #     continue
            print(f'parsing video - {video_id}')
            params = {
                'part': 'id,snippet,statistics,contentDetails',
                'id': video_id,
                'maxResults': self.maxResults,
                'key': self.key
            }

            url_response = json.loads(fetchData(YOUTUBE_VIDEO_URL, params))
            nextPageToken = url_response.get('nextPageToken')
            self.format_channel_videos(url_response)

            while nextPageToken:
                params.update({'pageToken': nextPageToken})
                url_response = json.loads(fetchData(YOUTUBE_VIDEO_URL, params))
                nextPageToken = url_response.get('nextPageToken')
                self.format_channel_videos(url_response)

        self.add_data_to_db()

    def get_video_list(self, search_response):
        for search_result in search_response.get('items', []):
            if search_result['id']['kind'] == 'youtube#video':
                self.video_ids.append(search_result['id']['videoId'])

    def format_channel_videos(self, search_response):
        for search_result in search_response.get('items', []):
            if search_result['kind'] == 'youtube#video':
                video = {
                    'video_id': search_result['id'],
                    'title': search_result['snippet'].get('title', None),
                    'image_url': search_result['snippet'].get('thumbnails', {}).get('medium', {}).get('url', None),
                    'like': int(search_result['statistics'].get('likeCount', 0)),
                    'dislike': int(search_result['statistics'].get('dislikeCount', 0)),
                    'views': int(search_result['statistics'].get('viewCount', 0)),
                    'video_length': parseTime(search_result['contentDetails'].get('duration')),
                    'description': search_result['snippet'].get('description', ''),
                    'tags': search_result['snippet'].get('tags', [])
                }
                self.videos.append(video)

    def add_data_to_db(self):
        for obj in self.videos:
            music, created = Music.objects.update_or_create(video_id=obj.get('video_id'), defaults={
                'channel_id': self.channel_id,
                'title': obj.get('title'),
                'image_url': obj.get('image_url'),
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
                    videotags_id=tag.id
                )


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('channel_id', type=str)

    def handle(self, *args: Any, **options: Any) -> None:
        channel_id = options.get('channel_id')
        if not channel_id:
            print('No Chanel Id Provided')
            return

        params = {
            'part': 'id,snippet',
            'channelId': channel_id,
            'maxResults': 50,
            'key': API_KEY
        }
        video = channelVideo(channel_id, 50, API_KEY)

        url_response = json.loads(fetchData(YOUTUBE_SEARCH_URL, params))
        nextPageToken = url_response.get('nextPageToken')
        video.get_video_list(url_response)

        while nextPageToken:
            params.update({'pageToken': nextPageToken})
            url_response = json.loads(fetchData(YOUTUBE_SEARCH_URL, params))
            nextPageToken = url_response.get('nextPageToken')
            video.get_video_list(url_response)

        video.parse_videos()
