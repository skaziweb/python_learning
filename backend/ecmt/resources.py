from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from schedule.constants import DAYS_CHOICES
from group.constants import LECTURE_NUMBER_CHOICES


class ResourcesView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = [JWTAuthentication, BasicAuthentication, SessionAuthentication]
    def get(self, request):
        CONSTANTS = {
            "CONSTANTS": {
                "DAYS_CHOICES": DAYS_CHOICES,
                "LECTURE_NUMBER_CHOICES": LECTURE_NUMBER_CHOICES
            }
        }
        return Response(
            CONSTANTS
        )

