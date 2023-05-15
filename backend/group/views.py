from rest_framework.filters import SearchFilter

from .models import Group
from .serializers import GroupSerializer
from helpers.models.custom_model import CustomModelViewSet


class GroupViewSet(CustomModelViewSet):
    def __int__(self):
        self.serializer = GroupSerializer

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    filter_backends = [SearchFilter]
    search_fields = ['hologram', 'medical_book_number']
