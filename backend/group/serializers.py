from .models import Group
from helpers.models.custom_serializer import CustomSerializer


class GroupSerializer(CustomSerializer):
    class Meta:
        model = Group
        fields = '__all__'