from rest_framework.serializers import ModelSerializer

from teacher.models import Teacher


class TeachersSerializer(ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'