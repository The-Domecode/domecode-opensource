from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from todo.api import views
app_name = 'todo'

urlpatterns = [
    path('', views.TodoList.as_view(), name = 'list' ),
    path('<int:pk>/', views.TodoDetail.as_view(), name = 'detail'),
]

