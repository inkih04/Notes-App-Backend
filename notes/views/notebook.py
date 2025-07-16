from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from notes.models import Notebook
from notes.serializers import NotebookSerializer

class NotebookListViewSet(generics.ListAPIView):
    serializer_class = NotebookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Notebook.objects.filter(users=self.request.user)

class NotebookViewSet(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk, user):
        try:
            return Notebook.objects.get(pk=pk, users=user)
        except Notebook.DoesNotExist:
            return None

    def patch(self, request, pk):
        notebook = self.get_object(pk, request.user)
        if not notebook:
            return Response({"error": "Notebook not found"}, status=404)

        serializer = NotebookSerializer(notebook, data=request.data, partial=True)
        if  serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        notebook = self.get_object(pk, request.user)
        if not notebook:
            return Response({"error": "Notebook not found"}, status=404)
        notebook.delete()
        return Response({"detail": "Notebook deleted"}, status=204)
