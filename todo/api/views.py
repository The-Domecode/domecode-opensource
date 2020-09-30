from todo.models import Todo
from todo.api.serializers import TodoSerializer
from rest_framework import generics


class TodoList(generics.ListCreateAPIView):
	queryset = Todo.objects.all()
	serializer_class = TodoSerializer


class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Todo.objects.all()
	serializer_class = TodoSerializer
