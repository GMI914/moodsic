from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.fields import CharField
from django.utils.translation import gettext_lazy as _
from rest_framework.authtoken.serializers import AuthTokenSerializer

from user.models import User


class UserSerializer(serializers.ModelSerializer):
    username = CharField(required=True)
    password = CharField(write_only=True, validators=[validate_password])
    password2 = CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            'id', 'username', 'password', 'password2',
        )

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({
                'password': _("Password fields didn't match."),
                'password2': _("Password fields didn't match"),
            })

        return attrs

    def create(self, validated_data) -> 'User':
        validated_data.pop('password2')
        return User.objects.create_user(**validated_data)
