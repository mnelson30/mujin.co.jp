# -*- coding: utf-8 -*-
# Copyright (C) 2011-2012 MUJIN Inc

# Django settings for mujinwww project.

import os

try:
    MUJIN_ENV = os.environ['MUJIN_ENV'].lower()
except KeyError:
    MUJIN_ENV = 'dev'

ROOT_PATH = os.path.dirname(__file__)

DEBUG = True
TEMPLATE_DEBUG = DEBUG
IPYTHON_DEBUG = False

ADMINS = (
    ('Controller Admin', 'controllernotification@mujin.co.jp'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mujinwww',
        'USER': 'mujinwww',
        'HOST': 'localhost',
        'PORT': '5432',
        'TIME_ZONE': 'UTC',
    }
}


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'UTC'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
#LANGUAGE_CODE = 'en-us'
SITE_ID = 2

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

LOCALE_PATHS=(
    os.path.join(ROOT_PATH,'..','locale'),
)

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
#~ MEDIA_ROOT = os.path.join(ROOT_PATH, '..', 'locale'),
MEDIA_ROOT = os.path.join(ROOT_PATH, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = 'static/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(ROOT_PATH, 'static'),
    os.path.join(ROOT_PATH, 'static' + MUJIN_ENV),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '2v0f75fqu(y%nkz@h+z1gu((sw&amp;df2nap7#xe(x-tp58u#t=!0'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
	'django.contrib.auth.context_processors.auth',
	'django.contrib.messages.context_processors.messages',
	'django.core.context_processors.static',
	'django.core.context_processors.media',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mujinwww.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'mujinwww.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(ROOT_PATH, 'templates'),
)

INSTALLED_APPS = (
    'mujinwww',

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    #~ 'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.admin',

    'south',
    #'mujin.controller',

    # haystack? # http://haystacksearch.org/
    # Uncomment the next line to enable the admin:
    #'grappelli',
    #'filebrowser',
    'django.contrib.admin',
    # 'django.contrib.admindocs',

    # Uncomment the next line to enable the admin:
    # 'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

# south settings:
# http://south.aeracode.org/docs/settings.html#setting-south-migration-modules

# A dictionary of alternative migration modules for apps. By default, apps look for their migrations in “<appname>.migrations”, but you can override this here, if you have project-specific migrations sets.
# SOUTH_MIGRATION_MODULES = {
#     'controller': 'mujin.controller.migrations',
#     }

SOUTH_LOGGING_ON = False
SOUTH_LOGGING_FILE = os.path.join(os.path.dirname(__file__),'django_south.log')

# A dictionary with database aliases as keys and the database module South will use as values. South defaults to using the internal south.db.<ENGINE> modules.
#SOUTH_DATABASE_ADAPTERS

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_AGE = 86400 # 1 day
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

AUTH_PROFILE_MODULE = "account.UserProfile"

if MUJIN_ENV == 'production':
    from settings_production import *
