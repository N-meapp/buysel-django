"""
Django settings for bysel project.

Generated by 'django-admin startproject' using Django 5.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-1-s_7q@r=a$qwuct#=m42d@%5j(d&$c+24=e&w#@nx5t&i2oh9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = []

ALLOWED_HOSTS = ['0.0.0.0', '127.0.0.1', 'localhost', 'anjanarealestates.com']

# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
    'developer',
    'agents',
    "cloudinary",
    "cloudinary_storage",  

    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    
]


# CSRF settings should be enabled by default:
CSRF_COOKIE_SECURE = False  # Set to True if using HTTPS


ROOT_URLCONF = 'bysel.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [('templates')],
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

WSGI_APPLICATION = 'bysel.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

SECRET_KEY = 'django-insecure-^d$ql1#@@d668f3n!j_s7(ikc-qr*$94jk##p#!aphw$d&2tq%'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

# import os

# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/5.1/howto/static-files/
# STATIC_URL = 'static/'
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media') 
# # Default primary key field type

import os
# Base directory




# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field
LOGIN_URL = '/login/'  

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# settings.py

# settings.py

SESSION_ENGINE = 'django.contrib.sessions.backends.db'  # Make sure this is set to use the database
SESSION_COOKIE_NAME = 'sessionid'  # The cookie name for sessions
SESSION_EXPIRE_AT_BROWSER_CLOSE = True  # Optional: Automatically clear session when the browser is closed
SESSION_COOKIE_AGE = 60 * 30  # 30 minutes session timeout (in seconds)



from dotenv import load_dotenv

load_dotenv()  # Load environment variables

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.getenv('CLOUDINARY_CLOUD_NAME'),
    'API_KEY': os.getenv('CLOUDINARY_API_KEY'),
    'API_SECRET': os.getenv('CLOUDINARY_API_SECRET'),
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

import cloudinary
import cloudinary.uploader
import cloudinary.api

# Cloudinary Configuration
cloudinary.config( 
  cloud_name = "dnklcdsjq", 
  api_key = "619665329545319", 
  api_secret = "MKWJwARG2buK0YwGjAsYbi4SCkQ", 
)







BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/
STATIC_URL = '/static/'

# Directory where collectstatic will gather files
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Directories where Django will look for additional static files
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Media files (uploads)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')