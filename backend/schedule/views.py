from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Schedule, Lecture
from .serializers import ScheduleSerializer, LectureSerializer
from helpers.models.custom_model import CustomModelViewSet


class SchedulesViewSet(CustomModelViewSet):
    def __int__(self):
        self.serializer = ScheduleSerializer

    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['sub_category', 'day']
    search_fields = ['sub_category', 'day']
    ordering_fields = ['sub_category', 'day', 'active_until']


class LectureViewSet(CustomModelViewSet):
    def __int__(self):
        self.serializer = LectureSerializer

    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['lecture_date']
    search_fields = ['lecture_date']
    ordering_fields = ['lecture_date']