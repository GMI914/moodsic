from collections import OrderedDict

from django_filters.rest_framework import DjangoFilterBackend
from typing import List

from recombee_api_client.api_requests import RecommendItemsToItem
from rest_framework import viewsets, mixins, status
from rest_framework.authentication import BaseAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from music.filters import MusicFilter
from music.models import VideoTags, VideoMood, VideoGenre, Music
from music.serializers import VideoTagsSerializer, VideoMoodSerializer, VideoGenreSerializer, MusicSerializer, \
    MusicDetailSerializer, MusicCustomSerializer
from recombee_api_client.api_client import RecombeeClient

client = RecombeeClient('moodsic-dev', 'Pb4MhOK6751HmdEGmvISdFJqXjLDWEtVkyb2AIY4Cn1EL3vQWy9V0B236OGEj8iy')


class SmallResultsSetPagination(PageNumberPagination):
    page_size = 50
    max_page_size = 1000

    def __init__(self):
        self.page = None

    def get_paginated_response(self, kwargs):
        return Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', kwargs)
        ]))


class MusicViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    authentication_classes: List[BaseAuthentication] = []
    pagination_class = SmallResultsSetPagination
    permission_classes = [AllowAny, ]
    queryset = Music.objects.all().prefetch_related('tags', 'mood', 'genre')
    filter_backends = (DjangoFilterBackend,)
    filter_class = MusicFilter
    serializer_classes = {
        'list': MusicSerializer,
        'retrieve': MusicDetailSerializer
    }

    @action(detail=False, pagination_class=SmallResultsSetPagination)
    def custom_list(self, request, *args, **kwargs):
        result = client.send(RecommendItemsToItem('-jaftVDdlqs', 1, 50, ))
        queryset = Music.objects.filter(video_id__in=[video.get('id') for video in result.get('recomms')])
        serializer = MusicCustomSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

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
