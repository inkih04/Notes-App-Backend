from rest_framework import serializers
from notes.models import Notebook

class NotebookCreateSerializer (serializers.ModelSerializer):
    is_shared = serializers.BooleanField(read_only=True)

    class Meta:
        model = Notebook
        fields = ['id', 'name', 'description', 'color', 'is_shared']
