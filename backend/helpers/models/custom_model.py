from rest_framework import status
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication


class CustomModelViewSet(ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = [JWTAuthentication, BasicAuthentication, SessionAuthentication]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.is_deleted:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED, data={
                "error": "If you what to restore the record, send a PUT request with is_deleted=False"
            })
        else:
            instance.is_deleted = True
            instance.save()
            return Response(status=status.HTTP_200_OK, data=self.serializer(instance).data)
