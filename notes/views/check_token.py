from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class CheckTokenView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"detail": "Token is valid"}, status=200)
