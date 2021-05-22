from typing import Any
from django.core.management import BaseCommand

from recombee_api_client.api_client import RecombeeClient
from recombee_api_client.exceptions import APIException
from recombee_api_client.api_requests import *

client = RecombeeClient('moodsic-dev', 'Pb4MhOK6751HmdEGmvISdFJqXjLDWEtVkyb2AIY4Cn1EL3vQWy9V0B236OGEj8iy')

class Command(BaseCommand):

    def handle(self, *args: Any, **options: Any) -> None:
        #client.send(ResetDatabase())
        client.send(AddUserProperty("username", "string"))
        client.send(AddUserProperty("age", "int"))

        client.send(AddItemProperty("mood", "string"))
        client.send(AddItemProperty("length", "double"))
        client.send(AddItemProperty("title", "string"))
        client.send(AddItemProperty("viewCount" , "int"))
        client.send(AddItemProperty("likeDislikeRatio", "double"))
        client.send(AddItemProperty("tags", "set"))

