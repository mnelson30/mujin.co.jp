#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2011-2012 MUJIN Inc
DEBUG = False
TEMPLATE_DEBUG = DEBUG
IPYTHON_DEBUG = False

EMAIL_HOST='gmail.com'
EMAIL_HOST_PASSWORD=open('/var/mujinmanager_gmailpass','r').read()
EMAIL_HOST_USER='mujinmanager@gmail.com'
EMAIL_PORT=587
EMAIL_SUBJECT_PREFIX='[Home Django] '
EMAIL_USE_TLS=False
SEND_BROKEN_LINK_EMAILS=True
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
STATIC_ROOT = '/var/www/www/mujinwww/mujinwww/static/'
STATIC_URL = '/static/'
STATICFILES_DIRS = ('/var/www/www/mujinwww/mujinwww/static/',)
