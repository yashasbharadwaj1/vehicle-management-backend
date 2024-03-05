from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


class IndexView(views.APIView):
    permission_classes = ((AllowAny),)

    def get(self, request):
        return Response(
            {
                "msg": "Vehicle management system api",
            },
            status=status.HTTP_200_OK,
        )
