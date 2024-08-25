"""
Django settings for LibraryProject project.

Generated by 'django-admin startproject' using Django 5.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure--%ksg^14std_w3b7m%cdxooxq24yj34gdt2clyi^#=y&1w-z#a"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

# Application definition
AUTH_USER_MODEL = "bookshelf.CustomUser"

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "bookshelf",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "csp.middleware.CSPMiddleware",
]

CSP_DEFAULT_SRC = ["'self'"]
CSP_SCRIPT_SRC = ["'self'"]
CSP_STYLE_SRC = ["'self'"]
CSP_IMG_SRC = ["'self'"]

ROOT_URLCONF = "LibraryProject.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
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


WSGI_APPLICATION = "LibraryProject.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "alx_bookshelf",
        "USER": "lusanda",
        "PASSWORD": "Man8244251",
        "HOST": "localhost",  # Or your database host
        "PORT": "3306",  # Default MySQL port
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Africa/Johannesburg"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Settings to protect against XSS, frame injection and content sniffing attacks

SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = "DENY"
SECURE_CONTENT_TYPE_NOSNIFF = True

# Ensuring that cookies are only sent over HTTPS

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# Security settings to enforce HTTPS and secure cookie transmission

# SECURE_SSL_REDIRECT: Redirects all HTTP requests to HTTPS.
# This setting is critical for production but not needed in local development.
SECURE_SSL_REDIRECT = False if DEBUG else True

# SECURE_HSTS_SECONDS: Instructs browsers to only access the site via HTTPS for the specified time.
# Setting it to 31536000 (1 year) is recommended for production.
SECURE_HSTS_SECONDS = 31536000 if not DEBUG else 0

# SECURE_HSTS_INCLUDE_SUBDOMAINS: Applies the HSTS policy to all subdomains as well.
SECURE_HSTS_INCLUDE_SUBDOMAINS = True if not DEBUG else False

# SECURE_HSTS_PRELOAD: Allows the site to be included in browsers' HSTS preload list.
SECURE_HSTS_PRELOAD = True if not DEBUG else False

# Cookie settings to enforce secure transmission over HTTPS

# SESSION_COOKIE_SECURE: Ensures that session cookies are only sent over HTTPS.
SESSION_COOKIE_SECURE = True

# CSRF_COOKIE_SECURE: Ensures that CSRF cookies are only sent over HTTPS.
CSRF_COOKIE_SECURE = True

# HTTP Headers for additional security

# X_FRAME_OPTIONS: Prevents your site from being framed to protect against clickjacking.
X_FRAME_OPTIONS = "DENY"

# SECURE_CONTENT_TYPE_NOSNIFF: Prevents browsers from MIME-sniffing a response away from the declared content-type.
SECURE_CONTENT_TYPE_NOSNIFF = True

# SECURE_BROWSER_XSS_FILTER: Enables the browser's XSS filtering and helps prevent cross-site scripting attacks.
SECURE_BROWSER_XSS_FILTER = True

# For local development (i.e., without production domains and SSL certificates),
# keep SECURE_SSL_REDIRECT set to False, as enabling it may cause issues without HTTPS.
# In production, you'd enable it by setting SECURE_SSL_REDIRECT = True.
