from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from . import devsettings
from django.conf.urls.static import static
from decouple import config

admin.autodiscover()

urlpatterns = [
    path(config("ADMIN_URL"), admin.site.urls),
    path("oauth/", include("social_django.urls", namespace="social")),
    path(
        "profile/login/",
        auth_views.LoginView.as_view(template_name="users/login.html"),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("", include("users.urls")),
    path("", include("notes.urls")),
    path("", include("forum.urls")),
    path("todo/", include("todo.urls")),
    path("tracks/", include("resources.urls")),
    path("practice/", include("coder.urls")),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path("quiz/", include("quizzes.urls")),
    path("products/", include("creator.urls")),
    path("fusion/", include("fusion.urls")),
    # REST FRAMEWORK URLS
    path("api/todo/", include("todo.api.urls", "todo_api")),
    path("api/notes/", include("notes.api.urls", "notes_api")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)

elif devsettings.DEBUG:
    urlpatterns += static(devsettings.MEDIA_URL,
                          document_root=devsettings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=devsettings.STATIC_ROOT)
