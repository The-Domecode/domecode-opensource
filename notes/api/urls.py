from django.urls import path
from notes.api import views

app_name = "notes"

urlpatterns = [
    path("", views.NotesList.as_view(), name="list"),
    path("<int:pk>/", views.NotesDetail.as_view(), name="detail"),
]
