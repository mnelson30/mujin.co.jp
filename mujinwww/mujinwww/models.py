# -*- coding: utf-8 -*-
# Copyright (C) 2013 MUJIN Inc
import os
import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from django.contrib.auth.models import User

ENGLISH = 'en'
JAPANESE = 'ja'
LANGUAGES = (
    (ENGLISH, _('English')),
    (JAPANESE, _('Japanese'))
)

class TranslatedNewsEntry(models.Model):
    language = models.CharField(max_length=230, default=ENGLISH, choices=LANGUAGES)
    title = models.CharField(max_length=230)
    content = models.TextField(help_text='HTML supported')

    def __unicode__(self):
        return self.title + ' (%s)'%self.language

class NewsEntry(models.Model):
    pub_date = models.DateTimeField(default=datetime.datetime.now)
    en = models.ForeignKey(TranslatedNewsEntry, unique=True, related_name=ENGLISH)
    ja = models.ForeignKey(TranslatedNewsEntry, unique=True, related_name=JAPANESE)

    def __unicode__(self):
        if hasattr(self.en, 'title'):
            return '%s (%s)'%(self.en.title, self.pub_date)
        else:
            return self.pub_date

class TranslatedUserProfile(models.Model):
    language = models.CharField(max_length=230, default=ENGLISH, choices=LANGUAGES)
    bio = models.TextField(help_text='HTML supported')

# these are employees
class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    en = models.ForeignKey(TranslatedUserProfile, unique=True, related_name=ENGLISH)
    ja = models.ForeignKey(TranslatedUserProfile, unique=True, related_name=JAPANESE)

    def _photo_path(instance, orig_path):
        filename = (unicode(instance) + '_' + orig_path).replace(' ', '_')
        path = os.path.join('employee_photos', filename)
        print path
        return str(path)

    photo = models.ImageField(upload_to=_photo_path)

    def __unicode__(self):
        return self.user.username

#~ enables us to reference the users profile and have it created if it does not exist
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
