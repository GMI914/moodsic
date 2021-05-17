from django_filters import rest_framework as filters

from music.models import Music


class MusicFilter(filters.FilterSet):
    video_id = filters.CharFilter(field_name='video_id', lookup_expr='exact')

    class Meta:
        model = Music
        fields = ['video_id']
