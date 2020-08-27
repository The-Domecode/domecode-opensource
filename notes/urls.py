# todo - update the urls.py with private and public mode urls
from django.urls import path
from .import views
from .views import NotesCreateView, NotesListView, NotesUpdateView, NotesDeleteView, NotesDetailView
app_name = 'notes'

urlpatterns = [
    path('', views.home, name='home'),
    path('notes/', NotesListView.as_view(), name='list'),
    path('notes/new/', NotesCreateView.as_view(), name='create'),
    path('notes/<slug:slug>/delete/', NotesDeleteView.as_view(), name='delete'),
    path('notes/<slug:slug>/', NotesDetailView.as_view(), name='detail'),
    path('notes/<slug:slug>/update/', NotesUpdateView.as_view(), name='update'),
    path('about/', views.about, name='about'),
    path('music/', views.music, name='music'),
    path('sponsor/', views.sponsor, name='sponsor'),
    path('privacypolicy/', views.privacy, name='privacy'),
    path('termsofservice/', views.tos, name='tos')

]
