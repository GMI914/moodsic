from django_filters import rest_framework as filters

from music.models import Music


class MusicFilter(filters.FilterSet):
    channel_id = filters.CharFilter(field_name='channel_id', lookup_expr='exact')

    class Meta:
        model = Music
        fields = ['channel_id']
