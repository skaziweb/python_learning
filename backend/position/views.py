from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from .models import Position
from .serializers import PositionSerializer
from helpers.models.custom_model import CustomModelViewSet


class PositionViewSet(CustomModelViewSet):
    def __int__(self):
        self.serializer = PositionSerializer

    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['title']
    search_fields = ['title']

