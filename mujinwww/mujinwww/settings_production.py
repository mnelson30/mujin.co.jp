#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2011-2012 MUJIN Inc
import os
ROOT_PATH = os.path.dirname(__file__)

try:
    MUJIN_ENV = os.environ['MUJIN_ENV'].lower()
except KeyError:
    MUJIN_ENV = 'dev'

DEBUG = False
TEMPLATE_DEBUG = False 
IPYTHON_DEBUG = False

EMAIL_HOST='smtp.gmail.com'

if os.path.exists('/var/mujinmanager_gmailpass'):
    EMAIL_HOST_PASSWORD=open('/var/mujinmanager_gmailpass','r').read()
else:
    EMAIL_HOST_PASSWORD=''
EMAIL_HOST_USER='mujinmanager@gmail.com'
EMAIL_PORT=587
EMAIL_SUBJECT_PREFIX='[Home Django] '
EMAIL_USE_TLS=True
SEND_BROKEN_LINK_EMAILS=False
SERVER_EMAIL='mujinmanager@gmail.com'
DEFAULT_FROM_EMAIL = 'mujinmanager@gmail.com'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mujinwww',
        'USER': 'mujinwww',
        'PASSWORD': open('/var/www/.pgpass','r').read().split('\n')[0].split(':')[-1],  # yeahhh
        'HOST': 'mujin.co.jp',
        'PORT': '5432',
        'TIME_ZONE': 'UTC',
    }
}

SESSION_COOKIE_AGE = 3600 # 1 hour
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

MEDIA_ROOT = '/var/www/media/'
MEDIA_URL = '/media/'
STATIC_ROOT = 'static/'
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(ROOT_PATH, 'static'),
    os.path.join(ROOT_PATH, 'static' + MUJIN_ENV),
    #'/var/www/www/mujinwww/mujinwww/static/'
)

