from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from teacher.models import Teacher, Workload
from teacher.serializers import TeachersSerializer, WorkloadSerializer


# Create your views here.
class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeachersSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['name']
    search_fields = ['name']
    ordering_fields = ['name']

class WorkloadViewSet(ModelViewSet):
    queryset = Workload.objects.all()
    serializer_class = WorkloadSerializer
    filter_backends = [SearchFilter]
    search_fields = ['teacher', 'lecture']