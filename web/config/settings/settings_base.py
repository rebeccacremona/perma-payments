"""
Django settings for project.

Generated by 'django-admin startproject' using Django 1.11.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # extras
    'nested_inline',
    'polymorphic',
    'simple_history',

    # ours
    'perma_payments',

    # admin last, to allow easier overrides
    'django.contrib.admin',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # extras
    'simple_history.middleware.HistoryRequestMiddleware',
]

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'example',
        'HOST': 'pp-db',
        'PORT': 5432,
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
        'NAME': 'perma_payments.security.AlphaNumericValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

# Email
DEFAULT_FROM_EMAIL = 'info@perma.cc'
DEFAULT_CONTACT_EMAIL = DEFAULT_FROM_EMAIL
# in production, DEFAULT_REPLYTO_EMAIL and DEFAULT_FROM must be different
DEFAULT_REPLYTO_EMAIL = DEFAULT_FROM_EMAIL
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# Admin
ADMIN_ENABLED = False
READONLY_ADMIN = True
# in non-dev environments, set ADMIN_URL in private settings.py

PERMA_TIMESTAMP_MAX_AGE_SECONDS = 120

# Direct all Perma.cc communications to perma dev by default
PERMA_URL = 'https://perma-dev.org'
PERMA_SUBSCRIPTION_CANCELED_REDIRECT_URL = 'https://perma-dev.org/settings/subscription/'
INDIVIDUAL_DETAIL_PATH = '/manage/users/'
REGISTRAR_DETAIL_PATH = '/manage/registrars/'
REGISTRAR_USERS_PATH = '/manage/registrar-users?registrar='

# Direct all CyberSource communications to their test server by default
CS_MODE = 'test'

# Exception handling for bulk updating subscription statuses;
# override if desired for easier testing (e.g., in dev)
RAISE_IF_SUBSCRIPTION_NOT_FOUND = True
RAISE_IF_MULTIPLE_SUBSCRIPTIONS_FOUND = True

# If an annual subscription is scheduled to be renewed on the day we
# update subscription statuses, we can't know the subscription's status
# with certainty: has their card been charged yet today or not?
#
# What's the upper limit of free days we want to grant the registrar
# in this situation?
# Perma.cc staff must update subscription statuses again...
# if 0: tomorrow
# if 7: within the next week
# if 31: next month (that is, exactly as usual, as though this never happened)
GRACE_PERIOD = 31

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
            'formatter': 'standard',
        },
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}
