from .models import Position
from helpers.models.custom_serializer import CustomSerializer


class PositionSerializer(CustomSerializer):
    class Meta:
        model = Position
        fields = '__all__'