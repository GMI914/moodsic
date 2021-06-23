from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken
from user.views import UserView, CreateUserView, user_logout

urlpatterns = [
    path('getToken/', ObtainAuthToken.as_view(), name='login'),
    path('register/', CreateUserView.as_view(), name='register'),
    path('detail/', UserView.as_view(), name='detail'),
    path('logout/', user_logout, name='logout'),
]
