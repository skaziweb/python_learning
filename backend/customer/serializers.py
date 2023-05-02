from .models import Customer
from helpers.models.custom_serializer import CustomSerializer


class CustomerSerializer(CustomSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

    def create(self, validated_data):
        return Customer.objects.create(**validated_data)
