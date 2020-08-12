from notes.models import Notes
from notes.api.serializers import NotesSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView



class NotesList(generics.ListCreateAPIView):
	permission_classes = [IsAdminUser]
	queryset = Notes.objects.all()
	serializer_class = NotesSerializer


class NotesDetail(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = [IsAdminUser]
	queryset = Notes.objects.all()
	serializer_class = NotesSerializer


"""
from rest_framework import mixins
class notesList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
	queryset = notes.objects.all()
	serializer_class = notesSerializer

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)
class notesDetail(mixins.RetrieveModelMixin,	mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
	queryset = notes.objects.all()
	serializer_class = notesSerializer

	def get(self, request, *args, **kwargs):
		return self.retrieve(request, *args, **kwargs)

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)
"""
