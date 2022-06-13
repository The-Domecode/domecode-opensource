from rest_framework import serializers
from notes.models import Notes


class NotesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notes
        fields = ["user", "title", "content", "category", "created"]
