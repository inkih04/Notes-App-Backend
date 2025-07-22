from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from notes.views import *

favnotes_list = FavNotesViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

favnotes_detail = FavNotesViewSet.as_view({
    'delete': 'delete_by_note',
})


urlpatterns = [
    path("auth/google/", GoogleAuthView.as_view(), name="google_auth"),
    path("auth/check-token/", CheckTokenView.as_view(), name="check_token"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("notebooks/", NotebookListViewSet.as_view(), name="notebook_list"),
    path("notebooks/<int:pk>/", NotebookViewSet.as_view(), name="notebook_detail"),
    path('notebooks/create/', NotebookCreateView.as_view(), name='notebook-create'),

    path('notebooks/<int:id>/notes/', NoteListViewSet.as_view(), name='note-list'),
    path('notebooks/<int:bloc_id>/notes/<int:pk>/', NoteViewSet.as_view(), name='note-detail'),
    path('fav/notes/', favnotes_list, name='favnotes-list'),
    path('fav/notes/<int:pk>/', favnotes_detail, name='favnotes-detail'),
    path('notes/checked/', ClosedNotesView.as_view(), name='closed_notes'),

    path('notebooks/<int:notebook_id>/invite/', InviteToNotebookView.as_view(), name='invite_to_notebook'),
    path('notebooks/accept-invitation/<uuid:token>/', AcceptInvitationView.as_view(), name='accept_invitation'),

]