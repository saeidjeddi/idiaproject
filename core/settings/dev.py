from .base import *

from datetime import timedelta


DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


INSTALLED_APPS += [
    'rest_framework',
    'rest_framework_simplejwt',
    'accounts.apps.AccountsConfig',

]


MIDDLEWARE += [

    'middlewares.url404.middleware.JsonResponse404Middleware',

]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}


SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
}

AUTH_USER_MODEL = "accounts.User"

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'accounts.authentication.UsernameAuthBackend',
    'accounts.authentication.PhoneAuthBackend',
]


LANGUAGE_CODE = 'fa-ir'
TIME_ZONE = 'Asia/Tehran'
USE_I18N = True
USE_TZ = True
STATIC_URL = 'static/'


WSGI_APPLICATION = 'core.wsgi.application'

