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

class NewsEntry(models.Model):
    title = models.CharField(max_length=230)
    language = models.CharField(max_length=230, default=ENGLISH, choices=LANGUAGES)
    pub_date = models.DateTimeField(default=datetime.datetime.now)
    content = models.TextField(help_text='This can have HTML in it')

    def __unicode__(self):
        return self.title + ' ' + self.language

# these are employees
class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)

    language = models.CharField(max_length=230, default=ENGLISH, choices=LANGUAGES)

    def _photo_path(instance, orig_path):
        filename = (unicode(instance) + '_' + orig_path).replace(' ', '_')
        path = os.path.join('employee_photos', filename)
        print path
        return str(path)

    photo = models.ImageField(upload_to=_photo_path)
    bio = models.TextField(help_text='This can have HTML in it')

    def __unicode__(self):
        return self.user.username + ' ' + self.language

#~ enables us to reference the users profile and have it created if it does not exist
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
