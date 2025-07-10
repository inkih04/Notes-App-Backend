
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from google.oauth2 import id_token
from google.auth.transport import requests as google_requests
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
import requests
from django.conf import settings

from notes.models import UserProfile
from notes.serializers import UserProfileSerializer


User = get_user_model()

class GoogleAuthView(APIView):

    def post(self, request):
        code =  request.data.get('code')
        if not code:
            return Response({"error": "Code is required"}, status=status.HTTP_400_BAD_REQUEST)

        token_endpoint = 'https://oauth2.googleapis.com/token'
        data = {
            'code': code,
            'client_id': settings.GOOGLE_CLIENT_ID,
            'client_secret': settings.GOOGLE_CLIENT_SECRET,
            "redirect_uri": "postmessage",
            'grant_type': 'authorization_code'
        }

        token_response = requests.post(token_endpoint, data=data)

        if token_response.status_code != 200:
            return Response({"error": "Failed to retrieve access token"}, status=status.HTTP_400_BAD_REQUEST)

        tokens = token_response.json()
        id_token_str = tokens['id_token']

        try:
            idinfo = id_token.verify_oauth2_token(id_token_str, google_requests.Request(), settings.GOOGLE_CLIENT_ID)
        except ValueError:
            return Response({"error": "Invalid ID token"}, status=status.HTTP_400_BAD_REQUEST)

        email = idinfo.get('email')
        username = idinfo.get('given_name')

        user, created = User.objects.get_or_create(
            email=email,
            defaults= {
                "username": username,
                "first_name": idinfo.get('given_name', '')
            }#TODO: "profile_picture": idinfo.get('picture', '')
        )

        user_profile, created = UserProfile.objects.get_or_create(
            user=user,
            defaults= {
                "bio": "",
                "user": user,
            }
        )

        if not created:
            pass #TODO: Update profile picture

        refresh = RefreshToken.for_user(user)

        userProfileSerializer = UserProfileSerializer(user_profile)

        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "profile": userProfileSerializer.data
        })#falta el serializer


