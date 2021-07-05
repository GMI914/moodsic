from django.contrib.auth import logout
from django.db import transaction
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import permission_classes, authentication_classes, api_view
from rest_framework.generics import RetrieveAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from user.models import User
from user.serializer import UserSerializer

from recombee_api_client.api_client import RecombeeClient
from recombee_api_client.api_requests import *

client = RecombeeClient('moodsic-dev', 'Pb4MhOK6751HmdEGmvISdFJqXjLDWEtVkyb2AIY4Cn1EL3vQWy9V0B236OGEj8iy')


class CreateUserView(CreateAPIView):
    permission_classes = [~IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request: Request, *args: list, **kwargs: dict) -> 'Response':
        with transaction.atomic():
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            headers = self.get_success_headers(serializer.data)
            client.send(
                SetUserValues(
                    user.id,
                    {
                        "username": user.username,
                    }
                    , cascade_create=True
                )
            )
            return Response(
                data={'token': user.token},
                status=status.HTTP_201_CREATED,
                headers=headers
            )


@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def user_logout(request):
    logout(request)
    return Response()


class UserView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication, ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
