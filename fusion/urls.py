from django.urls import path
from .views import FusionHomeView, FusionDetailView

app_name = "fusion"

urlpatterns = [
    path("", FusionHomeView, name="fusion"),
    path("immerse/", FusionDetailView, name="fusion-detail"),
]
