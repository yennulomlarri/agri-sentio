"""
Django settings for agrisentio project.
"""

import os
from pathlib import Path
from decouple import config
import dj_database_url

# ------------------------------------
# BASE DIRECTORY
# ------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent


# ------------------------------------
# SECURITY & ENVIRONMENT VARIABLES
# ------------------------------------
SECRET_KEY = config("SECRET_KEY", default="django-insecure-agri-sentio-backend-2025-mateiyendou-kombat")
DEBUG = config("DEBUG", default=True, cast=bool)
ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="127.0.0.1,localhost").split(",")


# ------------------------------------
# APPLICATION DEFINITION
# ------------------------------------
INSTALLED_APPS = [
    # Django built-in apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party apps
    'rest_framework',
    'rest_framework_simplejwt',
    'drf_spectacular',
    'drf_spectacular_sidecar',
    'corsheaders',

    # Local apps
    'accounts',
    'farms',
    'diagnostics',
    'taxonomy',
    'analytics',
    'core',
]


# ------------------------------------
# TEMPLATES CONFIGURATION
# ------------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# ------------------------------------
# MIDDLEWARE
# ------------------------------------
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ------------------------------------
# URLS / WSGI
# ------------------------------------
ROOT_URLCONF = 'agrisentio.urls'
WSGI_APPLICATION = 'agrisentio.wsgi.application'


# ------------------------------------
# DATABASE CONFIGURATION
# ------------------------------------
DATABASES = {
    'default': dj_database_url.config(
        default=config("DATABASE_URL", default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}")
    )
}


# ------------------------------------
# AUTHENTICATION & PASSWORD VALIDATORS
# ------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

AUTH_USER_MODEL = 'accounts.User'


# ------------------------------------
# INTERNATIONALIZATION
# ------------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# ------------------------------------
# STATIC & MEDIA FILES
# ------------------------------------
STATIC_URL = 'static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# ------------------------------------
# DJANGO REST FRAMEWORK CONFIG
# ------------------------------------
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',  # added
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',  # added
    ),
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}


# ------------------------------------
# CORS CONFIGURATION
# ------------------------------------
CORS_ALLOW_ALL_ORIGINS = True


# ------------------------------------
# DRF-SPECTACULAR (Swagger / OpenAPI) SETTINGS
# ------------------------------------
SPECTACULAR_SETTINGS = {
    'TITLE': 'Agri-Sentio API',
    'DESCRIPTION': 'Backend API for Agri-Sentio Crop Disease Detection Platform',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'SWAGGER_UI_SETTINGS': {
        'deepLinking': True,
        'persistAuthorization': True,
    },
    'COMPONENT_SPLIT_REQUEST': True,
    'SECURITY': [{'BearerAuth': []}],
    'COMPONENTS': {
        'securitySchemes': {
            'BearerAuth': {
                'type': 'http',
                'scheme': 'bearer',
                'bearerFormat': 'JWT',
                'description': 'Enter your JWT token in the format: **Bearer <your_token>**',
            }
        }
    },
}
