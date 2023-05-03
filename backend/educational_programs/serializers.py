
from .models import ProgramCategories, ProgramSubCategories
from helpers.models.custom_serializer import CustomSerializer


class ProgramCategoriesSerializer(CustomSerializer):
    class Meta:
        model = ProgramCategories
        fields = ['id', 'title', 'code', 'is_deleted']


class ProgramSubCategoriesSerializer(CustomSerializer):
    class Meta:
        model = ProgramSubCategories
        fields = ['id', 'title', 'code', 'category', 'is_deleted']
