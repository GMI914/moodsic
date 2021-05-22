from typing import Any
from django.core.management import BaseCommand
from django.core.management import call_command

CHANNEL_IDS = [
    '',
]


class Command(BaseCommand):

    @staticmethod
    def parse_all():
        print(f'>>> parsing channels', flush=True)
        for channel in CHANNEL_IDS:
            call_command('parse_channel', channel)
            print(f'>>> parsing {channel}')

    def handle(self, *args: Any, **options: Any) -> None:
        self.parse_all()
