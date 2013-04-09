#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2011-2012 MUJIN Inc
import os

from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

import mujinwww.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mujinwww.views.home', name='home'),
    # url(r'^mujinwww/', include('mujinwww.foo.urls')),

    # the admin
    #url(r'^admin/', include(admin.site.urls)),

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

#from django.contrib.staticfiles.urls import staticfiles_urlpatterns                                                                                                           
#urlpatterns += staticfiles_urlpatterns()  
