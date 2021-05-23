from typing import Any

from django.contrib.auth.models import User
from django.core.management import BaseCommand
from recombee_api_client.api_client import RecombeeClient
from recombee_api_client.api_requests import *

client = RecombeeClient('moodsic-dev', 'Pb4MhOK6751HmdEGmvISdFJqXjLDWEtVkyb2AIY4Cn1EL3vQWy9V0B236OGEj8iy')


class Command(BaseCommand):

    def handle(self, *args: Any, **options: Any) -> None:
        users = User.objects.all()
        for user in users:
            client.send(
                SetUserValues(
                    user.id,
                    {
                        "username": user.email,
                        "age": 22,
                    }
                    , cascade_create=True
                )
            )
