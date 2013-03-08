#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2011-2012 MUJIN Inc
import os

from django.conf.urls import patterns, include, url
from django.conf import settings

from django.shortcuts import render_to_response
from django.template import RequestContext, TemplateDoesNotExist
from django.utils.translation import get_language_from_request

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

import mujinwww.views

def indexview(request, name):
    if len(name) == 0:
        name = 'index'

    htmlvars = dict()

    # TODO: maybe get rid of this and make a model?
    if name == 'index':
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
    try:
        return render_to_response(name, RequestContext(request, htmlvars))
    except TemplateDoesNotExist:
        return render_to_response(name + '.html', RequestContext(request, htmlvars))

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mujinwww.views.home', name='home'),
    # url(r'^mujinwww/', include('mujinwww.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^contact_us', 'mujinwww.views.contact_us'),

    url(r'^(?P<name>(\w)*)$', indexview),
    url(r'^google958ac3d7145e5350.html$', 'django.views.generic.simple.redirect_to', {'url': '/static/google958ac3d7145e5350.html'}),
)
