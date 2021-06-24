from django.contrib.auth.password_validation import MinimumLengthValidator
from django.contrib.auth.validators import UnicodeUsernameValidator
from rest_framework import serializers
from rest_framework.fields import CharField
from django.utils.translation import gettext_lazy as _
from rest_framework.authtoken.serializers import AuthTokenSerializer

from music.serializers import MusicCustomSerializer
from user.models import User


class UserSerializer(serializers.ModelSerializer):
    username = CharField(required=True, validators=[UnicodeUsernameValidator])
    password = CharField(write_only=True, validators=[MinimumLengthValidator])
    password2 = CharField(write_only=True)
    favorite = MusicCustomSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = User
        fields = (
            'id', 'username', 'password', 'password2', 'favorite',
        )

    def validate(self, attrs):
        if len(list(User.objects.filter(username=attrs['username']))) != 0:
            raise serializers.ValidationError({
                'username': _("This Username Is Already Taken"),
            })
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({
                'password': _("Password fields didn't match."),
                'password2': _("Password fields didn't match"),
            })
        return attrs

    def create(self, validated_data) -> 'User':
        validated_data.pop('password2')
        return User.objects.create_user(**validated_data)
