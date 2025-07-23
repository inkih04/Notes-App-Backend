from rest_framework import serializers
from notes.models import Note


class NoteSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.first_name', read_only=True)
    created_at = serializers.DateTimeField(format="%d/%m/%Y", read_only=True)
    is_favourite = serializers.SerializerMethodField()

    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'created_at', 'author', 'checked', 'color', 'is_favourite']
        read_only_fields = ['created_at', 'author', 'is_favourite']

    def get_is_favourite(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            return obj.fav_notes.filter(user=user).exists()

        return False
