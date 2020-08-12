from django.urls import path
from . import views
from users.views import AccountDetailView, Leaderboard
app_name = 'users'

urlpatterns = [
    path('leaderboard/', Leaderboard.as_view(), name='leaderboard'),
    path('profile/register/', views.signup, name='register'),
    path('profile/edit/', views.profile, name='profile'),
    path('user/<slug:slug>/', AccountDetailView.as_view(), name='profilepage'),

]
