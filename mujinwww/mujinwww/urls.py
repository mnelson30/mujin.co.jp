# -*- coding: utf-8 -*-
# Copyright (C) 2012-2013 MUJIN Inc
import os

from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

from . import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mujinwww.views.home', name='home'),
    # url(r'^mujinwww/', include('mujinwww.foo.urls')),

    # for sending inquiry emails
    url(r'^sendinquiry', 'mujinwww.views.sendinquiry'),

    url(r'^/|^index', 'mujinwww.views.index'),
    url(r'^news', 'mujinwww.views.news'),
    
    # to serve the media directory statically when using the dev server
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

    # why is this here?
    url(r'^google958ac3d7145e5350.html$', 'django.views.generic.simple.redirect_to', {'url': '/static/google958ac3d7145e5350.html'}),
    
    # the catchall, serves everything
    url(r'^(?P<name>(\w)*)$', 'mujinwww.views.catchallhtml'),
)

try:
    MUJIN_ENV = os.environ['MUJIN_ENV'].lower()
    if MUJIN_ENV == 'dev':
        urlpatterns += patterns('', url(r'^admin/', include(admin.site.urls)),)
except KeyError:
    pass


#from django.contrib.staticfiles.urls import staticfiles_urlpatterns                                                                                                           
#urlpatterns += staticfiles_urlpatterns()  
