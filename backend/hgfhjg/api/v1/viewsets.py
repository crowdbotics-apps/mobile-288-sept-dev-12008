from rest_framework import authentication
from hgfhjg.models import Gfkhgkjhgkj
from .serializers import GfkhgkjhgkjSerializer
from rest_framework import viewsets


class GfkhgkjhgkjViewSet(viewsets.ModelViewSet):
    serializer_class = GfkhgkjhgkjSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Gfkhgkjhgkj.objects.all()
