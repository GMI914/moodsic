# Generated by Django 3.1.2 on 2021-05-17 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='genre',
            field=models.ManyToManyField(blank=True, related_name='videos', to='music.VideoGenre', verbose_name='Genre'),
        ),
        migrations.AlterField(
            model_name='music',
            name='mood',
            field=models.ManyToManyField(blank=True, related_name='videos', to='music.VideoMood', verbose_name='Mood'),
        ),
        migrations.AlterField(
            model_name='music',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='videos', to='music.VideoTags', verbose_name='Tags'),
        ),
    ]
