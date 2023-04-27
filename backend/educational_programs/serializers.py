from rest_framework.serializers import ModelSerializer

from .models import ProgramCategories, ProgramSubCategories


class ProgramCategoriesSerializer(ModelSerializer):
    class Meta:
        model = ProgramCategories
        fields = ['id', 'title', 'code', 'is_deleted']


class ProgramSubCategoriesSerializer(ModelSerializer):
    class Meta:
        model = ProgramSubCategories
        fields = ['id', 'title', 'code', 'category', 'is_deleted']
