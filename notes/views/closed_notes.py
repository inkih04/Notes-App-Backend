from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from notes.models import Note, Notebook
from notes.serializers import NoteSerializer

class ClosedNotesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        user_notebooks = Notebook.objects.filter(users=user)
        notes = Note.objects.filter(bloc__in=user_notebooks, checked=True)
        serializer = NoteSerializer(notes, many=True, context={'request': request})
        return Response(serializer.data)