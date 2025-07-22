import uuid

from django.db import models
from django.contrib.auth.models import User


class Notebook(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    is_shared = models.BooleanField(default=False)
    users = models.ManyToManyField(User, related_name='notebooks')
    color = models.CharField(max_length=7, default="#FEDC3B")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_notebooks')

    def __str__(self):
        return self.name


class FavNotes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fav_notes')
    note = models.ForeignKey('Note', on_delete=models.CASCADE, related_name='fav_notes')
    class Meta:
        unique_together = ('user', 'note')

    def __str__(self):
        return f"{self.user.username} - {self.note.title}"


class NotebookInvitation(models.Model):
    email = models.EmailField()
    notebook = models.ForeignKey(Notebook, on_delete=models.CASCADE, related_name='invitations')
    token = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    invited_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_invitations')
    accepted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Invite to {self.email} for {self.notebook.name}"


class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    bloc = models.ForeignKey(Notebook, on_delete=models.CASCADE, related_name='notes')
    checked = models.BooleanField(default=False)
    color = models.CharField(max_length=7, default="#FEDC3B")

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} ({self.author.username} - {self.bloc.name})"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"




