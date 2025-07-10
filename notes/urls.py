from django.urls import path, include
from notes.views import *

urlpatterns = [
    path("auth/google/", GoogleAuthView.as_view(), name="google_auth"),
]