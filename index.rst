MUJIN Home Website Development
------------------------------

Initial Setup
=============

User **mujincontroller**, Password is **testpass**

::

  sudo -u postgres psql --command "CREATE ROLE mujincontroller PASSWORD 'md53c8bec98348b82fb05cc70d4744dfb59' SUPERUSER CREATEDB CREATEROLE INHERIT LOGIN;"
  createdb --host localhost --username mujincontroller --encoding UTF-8 mujinwww

Updating
========

Execute every time mujinwww is updated

::

  python $MUJIN_HOME/../www/mujinwww/manage.py syncdb
  python $MUJIN_HOME/../www/mujinwww/manage.py migrate

Running
=======

::

  python $MUJIN_HOME/../www/mujinwww/manage.py runserver 0.0.0.0:8000

Local website is at `http://http://localhost:8000/`_

IPの見方
sbin ifconfig

Editing
=======

All HTML templates are in **$MUJIN_HOME/../web/mujinwww/mujinwww/templates**. `Tutorial on HTML + Django syntax template language <https://docs.djangoproject.com/en/1.4/topics/templates/>`_

Only write English in the HTML files and only inside these translation blocks:

- `trans <https://docs.djangoproject.com/en/1.4/topics/i18n/translation/#std:templatetag-trans>`_

- `blocktrans <https://docs.djangoproject.com/en/1.4/topics/i18n/translation/#blocktrans-template-tag>`_  

Videos and image filenames should also be written within the translation blocks so that we can substitute them with the language equivalent.

Translating to Japanese
+++++++++++++++++++++++

When English templates are done, execute::

  cd $MUJIN_HOME/../web/mujinwww; django-admin.py makemessages --locale=ja_JP

Open **$MUJIN_HOME/../web/mujinwww/locale/ja_JP/LC_MESSAGES/django.po** and edit the translations. When done execute::

  cd $MUJIN_HOME/../web/mujinwww; django-admin.py compilemessages --locale=ja_JP

Restart the mujinwww server and the new translation should be visible!

Gallery Images
--------------

The front page will have a gallery of images scolling images. Can add or remove images through the **web/mujinwww/mujinwww/static/img/gallery_intro** page.

Production Environment
----------------------

This is for the real site and needs to be run on the MUJIN server. For **Rosen** only.

Setup
=====

Login with the **www-data** user and checkout the code into **/var/www**

  svn co https://svn.mujin.co.jp/web/mujinwww /var/www/mujinwww

When updating can just run::

  /var/www/mujinwww/updateweb.bash


