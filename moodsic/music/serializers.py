from rest_framework import serializers

from music.models import VideoTags, VideoMood, VideoGenre, Music


class VideoTagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoTags
        fields = ('id', 'title')


class VideoMoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoMood
        fields = ('id', 'title')


class VideoGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoGenre
        fields = ('id', 'title')


class MusicSerializer(serializers.ModelSerializer):
    tags = VideoTagsSerializer(read_only=True, many=True)

    class Meta:
        model = Music
        fields = ('id', 'title', 'video_id', 'channel_id', 'tags')


class MusicDetailSerializer(serializers.ModelSerializer):
    tags = VideoTagsSerializer(read_only=True, many=True)
    mood = VideoMoodSerializer(read_only=True, many=True)
    genre = VideoGenreSerializer(read_only=True, many=True)

    class Meta:
        model = Music
        fields = (
            'id', 'video_id', 'channel_id', 'title', 'like', 'dislike', 'views', 'video_length', 'description', 'tags',
            'custom_rating', 'mood', 'genre')


class MusicCustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ('title', 'video_id', 'views', 'image_url')
