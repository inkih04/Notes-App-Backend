from rest_framework import serializers
from notes.models import Notebook

class NotebookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notebook
        fields = ['id', 'name', 'description', 'is_shared', 'color']