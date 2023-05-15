from teacher.models import Teacher, Workload
from helpers.models.custom_serializer import CustomSerializer

class TeachersSerializer(CustomSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class WorkloadSerializer(CustomSerializer):
    class Meta:
        model = Workload
        fields = '__all__'