import pickle
from typing import Any
from django.core.management import BaseCommand
import pandas as pd
import sqlite3 as sq
import numpy as np
from collections import Counter
from music.models import Music


class Command(BaseCommand):

    def handle(self, *args: Any, **options: Any) -> None:
        con = sq.connect("db.sqlite3")
        df_rg = pd.read_sql_query(
            '''
            select m.id,m.video_id,m.channel_id,t.title from music_music m 
            join music_music_tags j on m.id=j.music_id 
            join music_videotags t on t.id=j.videotags_id 
            where j.videotags_id in (select t.id from music_videotags t 
                                    join music_music_tags j on t.id=j.videotags_id 
                                    group by t.id having count(j.music_id)>100)
            ''',
            con)

        df = df_rg.copy()
        df = pd.get_dummies(df, columns=['title'])
        df = df.groupby(["id", "video_id", "channel_id"], as_index=False).agg(np.sum)
        df_t = df.iloc[:, 3:]

        with open('km.pickle', 'rb') as f:
            km = pickle.load(f)

        km.fit(df_t)

        p = km.predict(df_t)
        Counter(p)

        df_t.insert(0, "cluster", p)
        df_t.insert(1, "video_id", df.video_id)
        df_t.insert(2, "id", df.id)
        df_t.insert(2, "channel_id", df.channel_id)

        # music = Music.objects.filter(video_id="").get()
        # if music.custom_rating == 0:
        #     music.custom_rating = 0
        #     music.save()
