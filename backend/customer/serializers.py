from rest_framework.serializers import ModelSerializer

from .models import Customer


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

    def create(self, validated_data):
        return Customer.objects.create(**validated_data)
