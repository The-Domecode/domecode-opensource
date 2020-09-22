import os
from decouple import config

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")  # hc

# SECURITY WARNING: don't run with debug turned on in production!
# hc
DEBUG = True
ALLOWED_HOSTS = ["*"]
# Application definition

INSTALLED_APPS = [
    # myapps
    "users.apps.UsersConfig",
    "notes.apps.NotesConfig",
    "todo.apps.TodoConfig",
    "forum.apps.ForumConfig",
    "coder.apps.CoderConfig",
    "quizzes.apps.QuizzesConfig",
    "resources.apps.ResourcesConfig",
    "creator.apps.CreatorConfig",
    "fusion.apps.FusionConfig",
    # crispy
    "crispy_forms",
    # default
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "six",
    # rest
    "rest_framework",
    "rest_framework.authtoken",
    # oauth
    "social_django",
    # ckeditor
    "ckeditor",
    "ckeditor_uploader",
    "storages",
]


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # OAUTH
    "social_django.middleware.SocialAuthExceptionMiddleware",
]

HONEYBADGER = {"API_KEY": "60aaca87"}

ROOT_URLCONF = "domecode.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "social_django.context_processors.backends",  # OAUTH
                "social_django.context_processors.login_redirect",  # OAUTH
            ],
        },
    },
]


WSGI_APPLICATION = "domecode.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        "HOST": config("DB_HOST"),
    }
}

AUTHENTICATION_BACKENDS = (
    "social_core.backends.github.GithubOAuth2",
    "social_core.backends.google.GoogleOAuth2",
    "django.contrib.auth.backends.ModelBackend",
)

SOCIAL_AUTH_GITHUB_KEY = config("SOCIAL_AUTH_GITHUB_KEY")  # hc
SOCIAL_AUTH_GITHUB_SECRET = config("SOCIAL_AUTH_GITHUB_SECRET")  # hc
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = config("SOCIAL_AUTH_GOOGLE_OAUTH2_KEY")  # hc
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = config("SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET")  # hc


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ),
}


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Kolkata"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "notes/static/")
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

CRISPY_TEMPLATE_PACK = "bootstrap4"

LOGIN_URL = "login"

LOGOUT_URL = "logout"
LOGOUT_REDIRECT_URL = "login"

CKEDITOR_UPLOAD_PATH = "uploads/"

CKEDITOR_CONFIGS = {
    "default": {
        "toolbar": "auto",  # You can change this based on your requirements.
        "width": "auto",
        "height": "auto",
        "uiColor": "moona-lisa",
    },
}
"""
# AWS S3

"""


def get_cache():
    import os

    try:
        servers = os.environ["MEMCACHIER_SERVERS"]
        username = os.environ["MEMCACHIER_USERNAME"]
        password = os.environ["MEMCACHIER_PASSWORD"]
        return {
            "default": {
                "BACKEND": "django.core.cache.backends.memcached.PyLibMCCache",
                # TIMEOUT is not the connection timeout! It's the default expiration
                # timeout that should be applied to keys! Setting it to `None`
                # disables expiration.
                "TIMEOUT": None,
                "LOCATION": servers,
                "OPTIONS": {
                    "binary": True,
                    "username": username,
                    "password": password,
                    "behaviors": {
                        # Enable faster IO
                        "no_block": True,
                        "tcp_nodelay": True,
                        # Keep connection alive
                        "tcp_keepalive": True,
                        # Timeout settings
                        "connect_timeout": 2000,  # ms
                        "send_timeout": 750 * 1000,  # us
                        "receive_timeout": 750 * 1000,  # us
                        "_poll_timeout": 2000,  # ms
                        # Better failover
                        "ketama": True,
                        "remove_failed": 1,
                        "retry_timeout": 2,
                        "dead_timeout": 30,
                    },
                },
            }
        }
    except:
        return {"default": {"BACKEND": "django.core.cache.backends.locmem.LocMemCache"}}


CACHES = get_cache()
JUDGE0_RAPID_API_KEY = config("JUDGE0_RAPID_API_KEY")
