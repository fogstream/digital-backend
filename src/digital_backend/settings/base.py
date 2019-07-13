"""
Базовые параметры приложения

Больше информации об этом файле
https://docs.djangoproject.com/en/2.1/topics/settings/

Для получения полного списка параметров, см.
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import sys

from django.conf.global_settings import *  # @UnusedWildImport


# =============================================================================
# Основные пути приложения

# Корень исход
SOURCES_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../..')
)

# Корень приложения
BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')
)

# Пути для медиа
MEDIA_ROOT = os.path.join(SOURCES_ROOT, 'media')
MEDIA_URL = '/media/'

# Пути для статики
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(SOURCES_ROOT, 'static')

# Пути до статики в пакетах
STATICFILES_DIRS = []

sys.path.insert(0, os.path.join(BASE_DIR))

# =============================================================================

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY', 'sosecret')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '*').split(', ')

# =============================================================================

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'rest_framework',
    'rest_framework.authtoken',
    'drf_yasg'
]

LOCAL_APPS = [
    'digital_backend.apps.suppliers',
    'digital_backend.apps.criteria'
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
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

WSGI_APPLICATION = 'wsgi.application'

# =============================================================================
# Параметры сервера электронной почты

EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = os.getenv('EMAIL_PORT')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS', False)

DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')

# =============================================================================
# Параметры подключения к БД

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('POSTGRES_DB', 'digital_backend'),
        'USER': os.getenv('POSTGRES_USER', 'digital_backend'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'digital_backend'),
        'HOST': os.getenv('POSTGRES_HOST', 'postgres'),
        'PORT': os.getenv('POSTGRES_PORT', '5432'),
    }
}

# =============================================================================

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Asia/Vladivostok'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = (
    os.path.join(SOURCES_ROOT, 'locale'),
)