from typing import Any
from django.core.management import BaseCommand

from recombee_api_client.api_client import RecombeeClient
from recombee_api_client.exceptions import APIException
from recombee_api_client.api_requests import *

from music.models import Music

client = RecombeeClient('moodsic-dev', 'Pb4MhOK6751HmdEGmvISdFJqXjLDWEtVkyb2AIY4Cn1EL3vQWy9V0B236OGEj8iy')


class Command(BaseCommand):

    def handle(self, *args: Any, **options: Any) -> None:
        musics = Music.objects.all()
        ratio = 0

        score_obj = {
            1: 'sad', 2: 'gloomy', 3: 'cheerful', 4: 'happy', 0: 'undefined'
        }

        for music in musics:
            if music.dislike == 0:
                ratio = 0
            else:
                ratio = music.like / music.dislike
            client.send(
                SetItemValues(
                    str(music.video_id),
                    {
                        "mood": score_obj.get(music.custom_rating, 'undefined'),
                        "length": music.video_length,
                        "viewCount": music.views,
                        "likeDislikeRatio": ratio,
                        # "title": music.title,
                        # "tags": [tag.title for tag in music.tags.all()]
                    },
                    cascade_create=True
                )
            )
