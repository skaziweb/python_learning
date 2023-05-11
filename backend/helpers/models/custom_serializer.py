from rest_framework import serializers


class CustomSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    is_deleted = serializers.BooleanField(default=False)
