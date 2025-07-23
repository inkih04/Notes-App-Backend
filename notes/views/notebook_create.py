from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated

from notes.serializers import NotebookCreateSerializer


class NotebookCreateView(generics.CreateAPIView):
    serializer_class = NotebookCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        notebook = serializer.save(is_shared=False, author=self.request.user)
        notebook.users.set([self.request.user])
