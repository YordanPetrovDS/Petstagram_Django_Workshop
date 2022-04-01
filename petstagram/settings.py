import os
from pathlib import Path
from decouple import config

import cloudinary

from petstagram.utils import is_production, is_test

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = config("DEBUG")
APP_ENVIRONMENT = config("APP_ENVIRONMENT")
SECRET_KEY = config("SECRET_KEY")
# ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS").split()

ALLOWED_HOSTS = [
    config("ALLOWED_HOSTS"),
]

DJANGO_APPS = (
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
)

THIRD_PARTY_APPS = ()

PROJECT_APPS = (
    "petstagram.main",
    "petstagram.accounts",
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + PROJECT_APPS

MIDDLEWARE = [
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "petstagram.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "petstagram.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": config("DB_HOST"),
        "PORT": config("DB_PORT"),
        "NAME": config("DB_NAME"),
        "USER": config("DB_USER"),
        "PASSWORD": config("DB_PASSWORD"),
    }
}

AUTH_PASSWORD_VALIDATORS = []
if is_production():
    AUTH_PASSWORD_VALIDATORS.extend(
        [
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
    )


# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_ROOT = BASE_DIR / "staticfiles"
STATIC_URL = "/static/"

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (BASE_DIR / "static",)
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_ROOT = BASE_DIR / "media/"
MEDIA_URL = "/media/"

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
LOGGING_LEVEL = "DEBUG"

if is_production():
    LOGGING_LEVEL = "INFO"
elif is_test():
    LOGGING_LEVEL = "CRITICAL"

LOGGING = {
    "version": 1,
    "handlers": {
        "console": {
            # DEBUG, WARNING, INFO, ERROR, CRITICAL,
            "level": LOGGING_LEVEL,
            "filters": [],
            "class": "logging.StreamHandler",
        }
    },
    "loggers": {
        "django.db.backends": {
            "level": LOGGING_LEVEL,
            "handlers": ["console"],
        }
    },
}

AUTH_USER_MODEL = "accounts.PetstagramUser"

cloudinary.config(
    cloud_name=config("CLOUDINARY_CLOUD_NAME"),
    api_key=config("CLOUDINARY_API_KEY"),
    api_secret=config("CLOUDINARY_API_SECRET"),
)
