from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.functional import cached_property
from django.db import models
from django.utils.translation import gettext_lazy as _
from rest_framework.authtoken.models import Token


class User(AbstractUser):
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    # Creating many to many filed between user and music
    favorite = models.ManyToManyField(verbose_name="Favorite", to="music.Music", related_name='user')

    @cached_property
    def token(self):
        token, created = Token.objects.get_or_create(user=self)
        return token.key

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self) -> str:
        return f'{self.username}'
