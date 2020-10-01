from notes.models import Notes
from notes.api.serializers import NotesSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser


class NotesList(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer


class NotesDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer
