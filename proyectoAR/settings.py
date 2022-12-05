"""
Django settings for proyectoAR project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import datetime
import os
from dotenv import load_dotenv
import dj_database_url
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(os.path.join(BASE_DIR, ".env"))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = os.getenv("SECRET_KEY")
# SECRET_KEY = os.getenv("SECRET_KEY")
SECRET_KEY = 'django-insecure-br4-6pry%2h!_wq7w@x$xgm2z9lt-3#7d%c*!vik6!z6a4qsma'
# DATABASE_URL = os.getenv("DATABASE_URL")
DATABASE_URL = 'postgresql://postgres:SE74bEw@containers-51.railway.app:6919/railway'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '0.0.0.0:80',
    '0.0.0.0',
    '0.0.0.0',
    '*',
    '192.168.1.200',
    '127.0.0.1',  # CAMBIO
    'localhost'  # CAMBIO
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework_simplejwt',  # CAMBIO
    'rest_framework',  # CAMBIO
    'drf_yasg',  # CAMBIO
    "corsheaders",  # CAMBIO
    'django_filters',  # CAMBIO
    'personas',
    'usuarios',
    'pacientes',
    'consultas',
    'enfermedades',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "corsheaders.middleware.CorsMiddleware",  # CAMBIO
    'whitenoise.middleware.WhiteNoiseMiddleware'  # CAMBIO
]

ROOT_URLCONF = 'proyectoAR.urls'

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

WSGI_APPLICATION = 'proyectoAR.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases


DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
    # "default": dj_database_url.config(default=DATABASE_URL, conn_max_age=1800),
    # "default": {
    #     "ENGINE": "django.db.backends.postgresql_psycopg2",
    #     'NAME': 'BDPaola',
    #     'USER': 'postgres',
    #     'PASSWORD': 'navau',
    #     'HOST': 'localhost',
    #     'PORT': 5432,
    # }
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        'NAME': 'railway',
        'USER': 'postgres',
        'PASSWORD': 'KKZp8n5WkTx5zBYHXsfF',
        'HOST': 'containers-us-west-32.railway.app',
        'PORT': 6556,
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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

# CAMBIO TOKEN
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"
# CAMBIO SUBIDAS DE ARCHIVOS
MEDIA_URL = '/uploads/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# USERS
AUTH_USER_MODEL = 'usuarios.Usuario'

CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOWED_ORIGINS = [
    "http://192.168.1.200:8000",
]

# CORS_ALLOW_HEADERS = [
#     'accept',
#     'accept-enconding',
#     'authorization',
#     'authorization',
#     'content-type'
#     'dnt'
#     'origin'
#     'user-agent',
#     'x-csrftoken',
#     'x-requested-with'
# ]

# CAMBIO
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(days=360),
}

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_TMP = os.path.join(BASE_DIR, 'static')
STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

os.makedirs(STATIC_TMP, exist_ok=True)
os.makedirs(STATIC_ROOT, exist_ok=True)
os.makedirs(STATIC_DIR, exist_ok=True)


STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
