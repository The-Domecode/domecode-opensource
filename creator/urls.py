from django.urls import path
from .views import (
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
)

app_name = "creator"

urlpatterns = [
    path("", ProductListView.as_view(), name="list"),
    path("new/", ProductCreateView.as_view(), name="create"),
    path("<slug:slug>/", ProductDetailView.as_view(), name="detail"),
    path("<slug:slug>/update/", ProductUpdateView.as_view(), name="update"),
    path("<slug:slug>/delete/", ProductDeleteView.as_view(), name="delete"),
]
