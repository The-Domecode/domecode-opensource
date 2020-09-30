from django.urls import path
from todo.api import views

app_name = "todo"

urlpatterns = [
    path("", views.TodoList.as_view(), name="list"),
    path("<int:pk>/", views.TodoDetail.as_view(), name="detail"),
]
