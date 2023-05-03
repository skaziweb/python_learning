from teacher.models import Teacher
from helpers.models.custom_serializer import CustomSerializer


class TeachersSerializer(CustomSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'