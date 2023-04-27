from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from teacher.models import Teacher
from teacher.serializers import TeachersSerializer


# Create your views here.
class TeachersViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeachersSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['name']
    search_fields = ['name']
    ordering_fields = ['name']
