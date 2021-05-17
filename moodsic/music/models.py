from django.db import models
from django.utils.translation import ugettext_lazy as _


class VideoTags(models.Model):
    title = models.CharField(verbose_name=_('Title'), max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title


class VideoMood(models.Model):
    title = models.CharField(verbose_name=_('Title'), max_length=255, null=True, blank=True)
    
    def __str__(self):
        return self.title


class VideoGenre(models.Model):
    title = models.CharField(verbose_name=_('Title'), max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title


class Music(models.Model):
    video_id = models.CharField(verbose_name=_('Video Id'), max_length=11, null=False, blank=False)
    channel_id = models.CharField(verbose_name=_('Channel Id'), max_length=255, null=False, blank=False)
    title = models.CharField(verbose_name=_('Title'), max_length=511, null=True, blank=True)

    like = models.PositiveIntegerField(verbose_name=_('Like Count'), default=0)
    dislike = models.PositiveIntegerField(verbose_name=_('Dislike Count'), default=0)
    views = models.PositiveIntegerField(verbose_name=_('View Count'), default=0)
    video_length = models.PositiveIntegerField(verbose_name=_('Video Length'))

    description = models.TextField(verbose_name=_('Description'), null=True, blank=True)
    tags = models.ManyToManyField(verbose_name=_('Tags'), to='music.VideoTags', related_name='videos', blank=True)

    custom_rating = models.DecimalField(verbose_name=_('Custom Rating'), null=True, blank=True, max_digits=6,
                                        decimal_places=3)

    mood = models.ManyToManyField(verbose_name=_('Mood'), to='music.VideoMood', related_name='videos', blank=True)
    genre = models.ManyToManyField(verbose_name=_('Genre'), to='music.VideoGenre', related_name='videos', blank=True)

    def __str__(self):
        return self.title
