from django.contrib import admin

from music.models import VideoTags, VideoMood, VideoGenre, Music


class VideoTagsInline(admin.StackedInline):
    model = Music.tags.through
    extra = 1
    def has_change_permission(self, request, obj=None):
        return False     
    def has_add_permission(self, request, obj=None):        
         return False      
    def has_delete_permission(self, request, obj=None):        
         return False

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
    list_display = ["title", "video_id"]
    list_filter = ["video_id", "id"]
    # inlines = [VideoTagsInline,]
    readonly_fields = ["tags", "mood", "genre"]


admin.site.register([VideoMood, VideoGenre])
