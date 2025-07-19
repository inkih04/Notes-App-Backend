from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from notes.models import FavNotes, Note
from notes.serializers import  FavNotesSerializer, NoteSerializer

class FavNotesViewSet(viewsets.ModelViewSet):
    serializer_class = FavNotesSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return FavNotes.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def delete_by_note(self, request, pk=None):
        try:
            fav = FavNotes.objects.get(user=request.user, note_id=pk)
            fav.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except FavNotes.DoesNotExist:
            return Response({"detail": "Favorite not found"}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request, *args, **kwargs):
        queryset = Note.objects.filter(fav_notes__user=request.user)
        serializer = NoteSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

