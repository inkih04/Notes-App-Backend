from rest_framework.views import APIView
from rest_framework import permissions, generics, status
from rest_framework.exceptions import PermissionDenied, NotFound
from rest_framework.response import Response

from notes.models import Note, Notebook
from notes.serializers import NoteSerializer

class NoteListViewSet(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        bloc_id = self.kwargs['id']

        try:
            notebook = Notebook.objects.get(id=bloc_id)
        except Notebook.DoesNotExist:
            return Note.objects.none()

        if not notebook.users.filter(id=user.id).exists():
            raise PermissionDenied("User does not belong to the notebook")

        return Note.objects.filter(bloc=notebook)

    def list(self, request, *args, **kwargs):
        user = request.user
        bloc_id = self.kwargs['id']

        try:
            notebook = Notebook.objects.get(id=bloc_id)
        except Notebook.DoesNotExist:
            return Response({"detail": "Notebook not found."}, status=404)

        if not notebook.users.filter(id=user.id).exists():
            raise PermissionDenied("User does not belong to the notebook")

        notes = Note.objects.filter(bloc=notebook)
        serializer = self.get_serializer(notes, many=True)

        return Response({
            "name": notebook.name,
            "description": notebook.description,
            "notes": serializer.data
        })

    def perform_create(self, serializer):
        user = self.request.user
        bloc_id = self.kwargs['id']

        try:
            notebook = Notebook.objects.get(id=bloc_id)
        except Notebook.DoesNotExist:
            raise NotFound("Notebook not found")

        if not notebook.users.filter(id=user.id).exists():
            raise PermissionDenied("User does not belong to the notebook")

        serializer.save(author=user, bloc=notebook, checked=False)


class NoteViewSet(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, bloc_id, note_id, user):
        try:
            notebook = Notebook.objects.get(pk=bloc_id)
        except Notebook.DoesNotExist:
            raise NotFound("Notebook not found")

        if not notebook.users.filter(id=user.id).exists():
            raise PermissionDenied("User does not belong to the notebook")

        try:
            note = Note.objects.get(pk=note_id, bloc=notebook)
        except Note.DoesNotExist:
            raise NotFound("Note does not belong to the Notebook")

        return note

    def patch(self, request, bloc_id, pk):
        user = request.user
        note = self.get_object(bloc_id, pk, user)
        serializer = NoteSerializer(note, data=request.data, partial=True, context={'request': request})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, bloc_id, pk):
        user = request.user
        note = self.get_object(bloc_id, pk, user)
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)