from collections import OrderedDict
import random
from django.db.models import Case, When
from django_filters.rest_framework import DjangoFilterBackend
from typing import List
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
from music.utils.recombee import Recommendation


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

    def reorder(self, result):
        results = self.cut_size(result)
        preserved = Case(*[When(video_id=pk.get('id'), then=pos) for pos, pk in enumerate(results)])
        queryset = Music.objects.filter(video_id__in=[video.get('id') for video in results]).order_by(preserved)
        return queryset

    @staticmethod
    def cut_size(result):
        results = result.get('recomms')
        random.shuffle(results)
        return results[0: int(len(results) / 3)]

    def list(self, request, *args, **kwargs):
        recombee = Recommendation(
            recom_type=request.GET.get('recom_type', 'itu'),
            user_id=request.GET.get('user_id', 0),
            item_id=request.GET.get('item_id', 0),
            scenario=request.GET.get('scenario', 'main'),
            r_filter=request.GET.get('r_filter', 'empty'),
            booster=request.GET.get('booster', 'empty'),
            number_of_items=request.GET.get('number_of_items', 5),
        )
        result = recombee.get_result()
        queryset = self.reorder(result)
        serializer = MusicCustomSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # @action(detail=False, pagination_class=SmallResultsSetPagination)
    # def item_to_user(self, request, *args, **kwargs):
    #     if request.GET.get('video_id'):
    #         client.send(AddRating(1, request.GET.get('video_id'), rating=-1, cascade_create=None))
    #     result = client.send(RecommendItemsToUser(2, 60, scenario='music_main'))
    #     queryset = self.reorder(result)
    #     serializer = MusicCustomSerializer(queryset, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    #
    # @action(detail=False, pagination_class=SmallResultsSetPagination)
    # def item_to_item(self, request, *args, **kwargs):
    #     result = client.send(RecommendItemsToItem(request.GET.get('video_id'), 2, 150, scenario='music_main'))
    #     queryset = self.reorder(result)
    #     serializer = MusicCustomSerializer(queryset, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    #
    # @action(detail=False, pagination_class=SmallResultsSetPagination)
    # def item_to_item_user_selected(self, request, *args, **kwargs):
    #     result_1 = client.send(RecommendItemsToItem(request.GET.get('video_id'), 2, 60, scenario='music_main'))
    #     result_2 = client.send(RecommendItemsToUser(2, 60, scenario='music_main'))
    #     result = {'recomms': result_1.get('recomms', []) + result_2.get('recomms', [])}
    #     queryset = self.reorder(result)
    #     serializer = MusicCustomSerializer(queryset, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

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
