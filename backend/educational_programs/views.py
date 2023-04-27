from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from .models import ProgramCategories, ProgramSubCategories
from .serializers import ProgramCategoriesSerializer, ProgramSubCategoriesSerializer


# Create your views here.
class ProgramCategoriesViewSet(ModelViewSet):
    queryset = ProgramCategories.objects.all()
    serializer_class = ProgramCategoriesSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['code', 'title']
    search_fields = ['code', 'title']
    ordering_fields = ['code']

class ProgramSubCategoriesViewSet(ModelViewSet):
    queryset = ProgramSubCategories.objects.all()
    serializer_class = ProgramSubCategoriesSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['code', 'title']
    search_fields = ['code', 'title']
    ordering_fields = ['code']