from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Customer
from .serializers import CustomerSerializer
from helpers.models.custom_model import CustomModelViewSet


class CustomersViewSet(CustomModelViewSet):
    def __int__(self):
        self.serializer = CustomerSerializer

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['first_name', 'last_name', 'second_name']
    search_fields = ['first_name', 'last_name', 'phone', 'email']
    ordering_fields = ['first_name', 'last_name', 'phone', 'email', 'created_at']

