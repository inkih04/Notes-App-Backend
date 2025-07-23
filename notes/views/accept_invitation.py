from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from notes.models import NotebookInvitation, Notebook
from django.contrib.auth.models import User


class AcceptInvitationView(APIView):
    def post(self, request, token):
        try:
            invitation = NotebookInvitation.objects.get(token=token, accepted=False)
        except NotebookInvitation.DoesNotExist:
            return Response({"error": "Invalid or already accepted invitation."}, status=status.HTTP_400_BAD_REQUEST)

        user = request.user if request.user.is_authenticated else None

        if not user:
            return Response({"error": "You must be logged in to accept the invitation."},
                            status=status.HTTP_401_UNAUTHORIZED)

        invitation.notebook.users.add(user)
        invitation.notebook.is_shared = True
        invitation.notebook.save()
        invitation.accepted = True
        invitation.save()

        return Response({"message": "You have been added to the notebook."})
