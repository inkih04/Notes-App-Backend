from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from notes.models import Notebook, NotebookInvitation
from django.contrib.auth.models import User

from notes.utils import send_invitation_email


class InviteToNotebookView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, notebook_id):
        email = request.data.get('email')
        try:
            notebook = Notebook.objects.get(id=notebook_id)
        except Notebook.DoesNotExist:
            return Response({"error": "Notebook not found"}, status=status.HTTP_404_NOT_FOUND)

        invitation = NotebookInvitation.objects.create(
            email=email,
            notebook=notebook,
            invited_by=request.user
        )

        send_invitation_email(invitation)

        return Response({"message": "Invitation has been sent"}, status=status.HTTP_200_OK)
