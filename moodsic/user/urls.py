from django.urls import path, include
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import routers
from user.views import UserView


router = routers.SimpleRouter()
router.register(r'user', UserView, basename='user')


urlpatterns = [
    path('', include(router.urls)),
    path('getToken/', ObtainAuthToken.as_view()),
]