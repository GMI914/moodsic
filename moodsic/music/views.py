from django_filters.rest_framework import DjangoFilterBackend
from typing import List

from rest_framework import viewsets, mixins
from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated

from music.filters import MusicFilter
from music.models import VideoTags, VideoMood, VideoGenre, Music
from music.serializers import VideoTagsSerializer, VideoMoodSerializer, VideoGenreSerializer, MusicSerializer, \
    MusicDetailSerializer


class MusicViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    authentication_classes: List[BaseAuthentication] = []
    permission_classes = [AllowAny, ]
    queryset = Music.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_class = MusicFilter
    serializer_classes = {
        'list': MusicSerializer,
        'retrieve': MusicDetailSerializer
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(getattr(self, 'action'), MusicSerializer)


class VideoTagsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = VideoTags.objects.all()
    serializer_class = VideoTagsSerializer


class VideoMoodViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = VideoMood.objects.all()
    serializer_class = VideoMoodSerializer


class VideoGenreViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = VideoGenre.objects.all()
    serializer_class = VideoGenreSerializer
