from typing import Any
from django.core.management import BaseCommand
from music.models import Music
from nltk import sent_tokenize, word_tokenize, PorterStemmer
from nltk.corpus import stopwords

mood_descriptors = {
    "sad": ["sad", "deplorable", "distressing", "lamentable", "pitiful", "sorry"],
    "gloomy": ['low', 'disconsolate', 'drear', 'dreary', 'grim', 'dark', 'gloomy', 'dingy', 'sulky', 'dispirited',
               'gloomful', 'drab', 'down', 'sorry', 'down_in_the_mouth', 'downhearted', 'glooming', 'downcast',
               'low-spirited', 'depressed', 'blue', 'dismal'],
    "cheerful": ['cheerful', 'pollyannaish', 'upbeat'],
    "happy": ['glad', 'felicitous', 'happy', 'well-chosen'],
}


class Command(BaseCommand):

    @staticmethod
    def get_rating(freq_table):
        score = 0
        main_mood = 'undefined'
        score_obj = {
            'sad': 1, 'gloomy': 2, 'cheerful': 3, 'happy': 4, 'undefined': 0
        }
        for mood in ['sad', 'gloomy', 'cheerful', 'happy']:
            if freq_table.get(mood) > score:
                score = freq_table.get(mood)
                main_mood = mood
        return score_obj.get(main_mood)

    def handle(self, *args: Any, **options: Any) -> None:
        stop_words = set(stopwords.words("english"))
        ps = PorterStemmer()

        for music in Music.objects.all():
            words_count = 0
            freq_table = {'sad': 0, 'gloomy': 0, 'cheerful': 0, 'happy': 0}
            for tag in music.tags.all():
                words = word_tokenize(tag.title)
                for word in words:
                    word = word.lower()
                    word = ps.stem(word)
                    if word in stop_words:
                        continue
                    for mood_descriptor, sub_moods in mood_descriptors.items():
                        if word in sub_moods:
                            words_count += 1
                            freq_table[mood_descriptor] += 1

            for key, value in freq_table.items():
                freq_table[key] = value / words_count if words_count != 0 else 0

            music.custom_rating = self.get_rating(freq_table)
            music.save()
