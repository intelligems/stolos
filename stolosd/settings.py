"""
Django settings for stolosd project.

Generated by 'django-admin startproject' using Django 1.9.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import email.utils
import os

import dj_database_url
import django_cache_url


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY',
                       'gb##%!^l!6!^leg&_w#f+)$2mv4b*%(blwa=zao_d7sgd*j3l%')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('PROD') is None

# Security settings
SECURE_HSTS_SECONDS = not DEBUG and 31536000
SECURE_SSL_REDIRECT = not DEBUG
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = []
if not DEBUG and os.getenv('ALLOWED_HOSTS'):
    ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS').split(',')

ADMINS = email.utils.getaddresses(os.getenv('ADMINS', '').split(','))


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_nose',
    'guardian',
    'rest_framework',
    'rest_framework.authtoken',
    'djoser',

    'stolos_watchd',
    'helpers',
    'projects',
    'users',
    'dashboard'
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'stolosd.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'stolosd.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(
        default='sqlite://%(base_dir)s/db.sqlite3' % {
            'base_dir': os.path.abspath(BASE_DIR),
        }),
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Athens'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = '/mnt/static'

# Caches settings

CACHES = {'default': django_cache_url.config('REDIS_URL')}

# Celery settings

BROKER_URL = os.getenv('REDIS_URL')
CELERY_RESULT_BACKEND = BROKER_URL
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

# Ceryx settings

CERYX_API_HOST = os.getenv('STOLOS_WATCHD_CERYX_API_HOST')

# Docker settings

DOCKER_HOST = os.getenv('DOCKER_HOST')
DOCKER_CERT_PATH = os.getenv('DOCKER_CERT_PATH')
DOCKER_IP = os.getenv('DOCKER_IP', 'localhost')

# Nose settings

NOSE_ARGS = [
    '--with-coverage',
    '--cover-package=core,helpers',
]
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

# Django Guardian settings

GUARDIAN_RAISE_403 = True
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'guardian.backends.ObjectPermissionBackend',
)
ANONYMOUS_USER_NAME = None

# Rest framework settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'users.authentication.APITokenAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
        'stolosd.permissions.DjangoObjectPermissions',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework.filters.DjangoObjectPermissionsFilter',
        'rest_framework.filters.DjangoFilterBackend',
    ),
    'EXCEPTION_HANDLER': 'stolosd.error_handling.exception_handler',
}

# Email settings

SERVER_EMAIL = os.getenv('SERVER_EMAIL', 'stolos@stolos.io')
EMAIL_BACKEND = 'django_mailgun.MailgunBackend'
MAILGUN_ACCESS_KEY = os.getenv('MAILGUN_API_KEY')
MAILGUN_SERVER_NAME = os.getenv('MAILGUN_SERVER_NAME')

# Agent settings
AGENT_PORT = os.getenv('AGENT_PORT', 5000)
AGENT_USERNAME = os.getenv('AGENT_USERNAME', 'admin')
AGENT_PASSWORD = os.getenv('AGENT_PASSWORD', 'secretpassword')

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/login/'
