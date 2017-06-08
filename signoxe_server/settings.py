# -*- coding: utf-8 -*-
"""
Django settings for signoxe_server project.

Generated by 'django-admin startproject' using Django 1.9.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
import raven
from everett.manager import (ConfigDictEnv, ConfigEnvFileEnv, ConfigIniEnv, ConfigManager,
                             ConfigOSEnv, ListOf, )

config = ConfigManager([
    ConfigOSEnv(),
    ConfigIniEnv(['config.ini',
                  '/etc/signoxe/server.ini']),
    ConfigDictEnv({
        'SECRET_KEY': 'vo7v#s9o7$t%x=fpbt7j5#%=-bl^y6e4&n2hpklg&rzx%z2mp$',
        'DEBUG': 'false',
    })
])

# Core config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ADMINS = (
    ('Kshitij Sobti', 'xitij2000@gmail.com'),
)

DEBUG = config('DEBUG', parser=bool)

SECRET_KEY = config('SECRET_KEY')

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='', parser=ListOf(str))

# Cors config

CORS_ORIGIN_ALLOW_ALL = config('ORIGIN_ALLOW_ALL', namespace='cors', default=str(DEBUG),
                               parser=bool)

CORS_ORIGIN_WHITELIST = config('ORIGIN_WHITELIST', namespace='cors',
                               default='', parser=ListOf(str))

# Database config

DATABASES = {
    'default': {
        'ENGINE': config('ENGINE', namespace='database', default='django.db.backends.sqlite3'),
        'NAME': config('NAME', namespace='database', default='db.sqlite3'),
        'USER': config('USER', namespace='database', default=''),
        'PASSWORD': config('PASSWORD', namespace='database', default=''),
        'HOST': config('HOST', namespace='database', default=''),
        'PORT': config('PORT', namespace='database', default=''),
    }
}

# Apps config

INSTALLED_APPS = [
    # Django core apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',

    'django.contrib.staticfiles',

    # Signoxe server apps
    'devicemanager',
    'mediamanager',
    'feedmanager',
    'client_manager',
    'schedule_manager',
    'notification_manager',

    # Django REST Framework
    'rest_framework',
    'rest_framework.authtoken',
    'djoser',

    # Sets CORS headers to permit / deny API requests from other apps
    'corsheaders',

    # Sentry app to report errors to Sentry
    'raven.contrib.django.raven_compat',

    # Django-storages to save files to s3
    'storages',

    # Django hosts to allow splitting app across sub-domains
    'django_hosts',

    # Django channels to support background tasks and async web apps like
    # websockets
    'channels',

    # Support for tagging items
    'taggit',
]

# DRF config
DRF_RENDERER_CLASSES = ('rest_framework.renderers.JSONRenderer',)

if DEBUG:
    DRF_RENDERER_CLASSES += ('rest_framework.renderers.BrowsableAPIRenderer',)

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_RENDERER_CLASSES': DRF_RENDERER_CLASSES,
}

MIDDLEWARE_CLASSES = (
    'django_hosts.middleware.HostsRequestMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_hosts.middleware.HostsResponseMiddleware',
)

ROOT_URLCONF = 'signoxe_server.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['signoxe_server/templates'],
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

WSGI_APPLICATION = 'signoxe_server.wsgi.application'

if not DEBUG:
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Sentry config

SENTRY_KEY = config('KEY', namespace='sentry', default='')
SENTRY_SECRET = config('SECRET', namespace='sentry', default='')
SENTRY_PROJECT = config('PROJECT', namespace='sentry', default='')

if (not DEBUG
        and SENTRY_KEY != ''
        and SENTRY_PROJECT != ''
        and SENTRY_SECRET != ''):
    DSN = 'https://{key}:{secret}@app.getsentry.com/{project}'.format(
            key=SENTRY_KEY,
            secret=SENTRY_SECRET,
            project=SENTRY_PROJECT,
    )
    RAVEN_CONFIG = {
        'dsn': DSN,
        'release': raven.fetch_git_sha(BASE_DIR),
        'ignore_exceptions': ('Http404', 'django.exceptions.http.Http404',),
        'environment': 'development' if DEBUG else 'production',
    }

# AWS Config

AWS_HEADERS = {
    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
    'Cache-Control': 'max-age=94608000',
}

USE_S3_STORAGE = config('USE_S3_STORAGE', namespace='AWS', default='false', parser=bool)

if USE_S3_STORAGE:
    AWS_STORAGE_BUCKET_NAME = config('STORAGE_BUCKET_NAME', namespace='aws')
    AWS_ACCESS_KEY_ID = config('ACCESS_KEY_ID', namespace='aws')
    AWS_SECRET_ACCESS_KEY = config('SECRET_ACCESS_KEY', namespace='aws')
    AWS_S3_HOST = config('S3_HOST', namespace='aws')
    AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

    DEFAULT_FILE_STORAGE = 'utils.files.DedupedS3MediaStorage'

    MEDIA_URL = 'https://%s/' % AWS_S3_CUSTOM_DOMAIN
else:
    DEFAULT_FILE_STORAGE = 'utils.files.DedupedMediaStorage'
    MEDIA_URL = config('MEDIA_URL', default='')

# Signoxe app config

SIGNOXE_THUMBNAIL_WIDTH = 320
SIGNOXE_THUMBNAIL_HEIGHT = 180

# Django hosts config

ROOT_HOSTCONF = 'signoxe_server.hosts'
DEFAULT_HOST = 'wildcard'
PARENT_HOST = config('PARENT_HOST', namespace='host', default='')
HOST_PORT = config('PORT', namespace='host', default='')
HOST_SCHEME = config('SCHEME', namespace='host', default='http' if DEBUG else 'https')

# Paths config
SERVER_ROOT = config('SERVER_ROOT', default='/srv/www/signoxe_server/')
STATIC_URL = config('STATIC_URL', default='/static/')
STATIC_ROOT = config('STATIC_ROOT', default=os.path.join(SERVER_ROOT, 'staticfiles'))
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
MEDIA_ROOT = config('MEDIA_ROOT', default=os.path.join(SERVER_ROOT, 'media'))

# Djoser config

DJOSER = {
    'DOMAIN': config('FRONTEND_DOMAIN', default='localhost:3000'),
    'SITE_NAME': 'Signoxe DNB',
    'PASSWORD_RESET_CONFIRM_URL': 'forgot-password/confirm/{uid}/{token}',
    'SERIALIZERS': {
        'user': 'client_manager.serializers.UserClientSerializer'
    }
}

# Email config

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
SERVER_EMAIL = config('SERVER_EMAIL', namespace='email', default='dev.signoxe@eml.cc')
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL', namespace='email', default='dev.signoxe@eml.cc')
NOTIFICATION_FROM_EMAIL = config('NOTIFICATION_FROM_EMAIL', namespace='email',
                                 default='dev.signoxe@eml.cc')
EMAIL_HOST = config('HOST', namespace='email', default='email-smtp.us-east-1.amazonaws.com')
EMAIL_HOST_USER = config('HOST_USER', namespace='email', default='')
EMAIL_HOST_PASSWORD = config('HOST_PASSWORD', namespace='email', default='')
EMAIL_USE_TLS = True

# Cookie config
SESSION_COOKIE_DOMAIN = config('COOKIE_DOMAIN', namespace='session', default='')
SESSION_COOKIE_SECURE = config('COOKIE_SECURE', namespace='session', parser=bool, default='false')
SESSION_COOKIE_NAME = config('COOKIE_NAME', namespace='session', default='sessionid')

# Django Channels Config

REDIS_HOST = config('HOST', namespace='redis', default='localhost')
REDIS_PORT = config('PORT', namespace='redis', default='6379', parser=int)

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'asgi_redis.RedisChannelLayer',
        'CONFIG': {
            'hosts': [(REDIS_HOST, REDIS_PORT)],
        },
        'ROUTING': 'signoxe_server.routing.channel_routing'
    }
}

TAGGIT_CASE_INSENSITIVE = True

# Cache config

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': f'redis://{REDIS_HOST}:{REDIS_PORT}/1',
        'TIMEOUT': 30 if DEBUG else 60 * 5,
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}