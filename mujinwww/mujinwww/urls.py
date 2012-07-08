#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2011-2012 MUJIN Inc
import os

from django.conf.urls import patterns, include, url
from django.conf import settings

#if settings.IPYTHON_DEBUG:
#    from IPython.Shell import IPShellEmbed
    #ipshell = IPShellEmbed(argv='',banner = 'MUJIN Controller Dropping into IPython',exit_msg = 'Leaving Interpreter.')
    #ipshell(local_ns=locals())
    
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.translation import get_language_from_request

def indexview(request,name):
    if len(name) == 0:
        name = 'index.html'

    htmlvars = dict()
    if name == 'index.html':
        # perhaps move this in initialization step for caching?
        gallery_intro_dir = None
        for staticdir in settings.STATICFILES_DIRS:
            if os.path.exists(os.path.join(staticdir,'img','gallery_intro')):
                gallery_intro_dir = os.path.join(staticdir,'img','gallery_intro')
                break
        if gallery_intro_dir is not None:
            LANG = get_language_from_request(request)
            if not os.path.exists(os.path.join(gallery_intro_dir,LANG)):
                LANG = 'en'
            imagefilenames = u''
            imagedirs = [gallery_intro_dir,os.path.join(gallery_intro_dir,LANG)]
            for imagedir in imagedirs:
                urldir = os.path.join(settings.STATIC_URL, os.path.relpath(imagedir,staticdir))
                for imagename in os.listdir(imagedir):
                    ext = os.path.splitext(imagename)[1].lower()
                    if ext == '.png' or ext == '.jpg':
                        imagefilenames += u'<img src="%s" width="640"/>\n'%os.path.join(urldir,imagename)
            htmlvars['intro_gallery_images'] = imagefilenames
    
    return render_to_response(name, RequestContext(request,htmlvars))

urlpatterns = patterns('',
    url(r'^(?P<name>(\w)*)$', indexview),
    # Examples:
    # url(r'^$', 'mujinwww.views.home', name='home'),
    # url(r'^mujinwww/', include('mujinwww.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
