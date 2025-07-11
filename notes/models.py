from django.db import models
from django.contrib.auth.models import User


class NoteBook(models.Model):
    name = models.CharField(max_length=255)
    users = models.ManyToManyField(User, related_name='notebooks')

    def __str__(self):
        return self.name

class Attachment(models.Model):
    file_name = models.CharField(max_length=255)
    url = models.URLField()
    def __str__(self):
        return self.file_name


class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    bloc = models.ForeignKey(NoteBook, on_delete=models.CASCADE, related_name='notes')
    checked = models.BooleanField(default=False)
    important = models.BooleanField(default=False)
    attachments = models.ManyToManyField(Attachment, blank=True, related_name='notes')
    color = models.CharField(max_length=7, default="#FEDC3B")  # Color in hex format

    class Meta:
        unique_together = ('bloc', 'title')
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} ({self.author.username} - {self.bloc.name})"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, null=True)
   # profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True) #TODO: Hay que guardarlo en algun sitio

    def __str__(self):
        return f"{self.user.username}'s Profile"




