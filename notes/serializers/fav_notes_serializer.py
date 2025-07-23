from rest_framework import serializers
from notes.models import FavNotes

class FavNotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavNotes
        fields = ['id', 'note']
        read_only_fields = ['id']
