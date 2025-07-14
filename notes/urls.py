from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from notes.views import *


urlpatterns = [
    path("auth/google/", GoogleAuthView.as_view(), name="google_auth"),
    path("auth/check-token/", CheckTokenView.as_view(), name="check_token"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("notebooks/", NotebookListViewSet.as_view(), name="notebook_list"),
    path("notebooks/<int:pk>/", NotebookViewSet.as_view(), name="notebook_detail"),
    path('notebooks/create/', NotebookCreateView.as_view(), name='notebook-create'),

]