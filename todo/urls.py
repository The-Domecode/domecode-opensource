from django.urls import path
from .views import TodoCreateView, TodoListView, TodoUpdateView, TodoDeleteView
app_name = 'todo'

urlpatterns = [
    path('', TodoListView.as_view(), name='list'),
    path('<int:pk>/', TodoUpdateView.as_view(), name='update'),
    path('new/', TodoCreateView.as_view(), name='create'),
    path('<int:pk>/delete/', TodoDeleteView.as_view(), name='delete')
]
