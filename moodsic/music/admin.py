from django.contrib import admin

from music.models import VideoTags, VideoMood, VideoGenre, Music


class VideoTagsInline(admin.StackedInline):
    model = Music.tags.through
    extra = 1


class VideoMoodInline(admin.StackedInline):
    model = Music.mood.through
    extra = 1


class VideoGenreInline(admin.StackedInline):
    model = Music.genre.through
    extra = 1


@admin.register(VideoTags)
class VideoTagsAdmin(admin.ModelAdmin):
    list_filter = ('title',)


@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    pass
    # inlines = [VideoTagsInline, VideoMoodInline, VideoGenreInline]


admin.site.register([VideoMood, VideoGenre])
