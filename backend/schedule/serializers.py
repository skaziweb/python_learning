from .models import Schedule, Lecture
from helpers.models.custom_serializer import CustomSerializer


class ScheduleSerializer(CustomSerializer):
    class Meta:
        model = Schedule
        fields = ['id', 'day', 'slot', 'active_until', 'sub_category', 'is_deleted']


class LectureSerializer(CustomSerializer):
    class Meta:
        model = Lecture
        fields = '__all__'


