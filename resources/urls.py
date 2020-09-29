from django.urls import path
from . import views
from .views import ResourceDetailViewPy, ResourceDetailViewJava, ResourcesHome

app_name = "resources"

urlpatterns = [
    path("", ResourcesHome.as_view(), name="home"),
    path("python/<slug:slug>/",
         ResourceDetailViewPy.as_view(),
         name="detail-python"),
    path("java/<slug:slug>/",
         ResourceDetailViewJava.as_view(),
         name="detail-java"),
]
