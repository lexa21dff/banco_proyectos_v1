from rest_framework import viewsets
from rest_framework import permissions
from proyectos.serializers.user import *


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserModelSerializer