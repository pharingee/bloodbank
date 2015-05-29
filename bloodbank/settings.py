"""
Django settings for bloodbank project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import dj_database_url

BASE_DIR = lambda *x: os.path.join(
    os.path.dirname(os.path.dirname(__file__)), *x)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_5gy+1bm1@ghp3kii7d)5$wc_*s%3+%2ot_6rzezy-op%jbut-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    # 3rd party app
    'suit',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'bloodbank.urls'

WSGI_APPLICATION = 'bloodbank.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config()
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

'''
=================================================================
Blood Bank Settings
==================================================================
'''

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/dashboard/'

APPEND_SLASH = True

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
)

AUTH_USER_MODEL = 'users.User'

THIRD_PARTY_APPS = (
    'storages',
    'imagekit',
    'corsheaders',
)

LOCAL_APPS = (
    'apps.users',
    'apps.common',
    'apps.donations',
    'apps.transfusions',
)

INSTALLED_APPS += THIRD_PARTY_APPS + LOCAL_APPS

# Static files (CSS, JavaScript, Images)
STATIC_ROOT = 'staticfiles'
MEDIA_ROOT = 'media'

# Root folders
AVATAR_ROOT = os.path.join(MEDIA_ROOT, 'avatar')

TEMPLATE_DIRS = [BASE_DIR('templates')]
STATICFILES_DIRS = [BASE_DIR('static')]

# AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
# AWS_S3_SECURE_URLS = os.environ.get('AWS_S3_SECURE_URLS') == 'True'
# AWS_QUERYSTRING_AUTH = os.environ.get('AWS_QUERYSTRING_AUTH') == 'True'
# AWS_S3_ACCESS_KEY_ID = os.environ.get('AWS_S3_ACCESS_KEY_ID')
# AWS_S3_SECRET_ACCESS_KEY = os.environ.get('AWS_S3_SECRET_ACCESS_KEY')
# AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
S3_URL = ''

CORS_ORIGIN_ALLOW_ALL = True
CORS_URLS_REGEX = r'^/api/.*$'
CORS_ALLOW_CREDENTIALS = True

SUIT_CONFIG = {
    # header
    'ADMIN_NAME': 'Blood Bank',
    'MENU_EXCLUDE': ('auth',),
}
