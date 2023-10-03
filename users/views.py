from rest_framework import viewsets

from users.models import User
from users.serializers import UserListSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserListSerializer
    queryset = User.objects.all()
