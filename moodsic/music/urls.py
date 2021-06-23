from django.urls import path, include
from rest_framework import routers

from music.views import MusicViewSet, VideoTagsViewSet, VideoMoodViewSet, VideoGenreViewSet

app_name = 'music'
router = routers.SimpleRouter()
router.register(r'music', MusicViewSet, basename='music')
router.register(r'tags', VideoTagsViewSet, basename='tags')
# router.register(r'mood', VideoMoodViewSet, basename='mood')
# router.register(r'genre', VideoGenreViewSet, basename='genre')
urlpatterns = [
    path('', include(router.urls)),
]
