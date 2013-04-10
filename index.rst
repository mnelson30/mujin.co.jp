MUJIN Home Website Development
------------------------------

Initial Setup
=============

User **mujinwww**, Password is **testpass**

::

  sudo -u postgres psql --command "CREATE ROLE mujinwww PASSWORD 'md5f2884d0c1dc57fa66c837bea9a244ba2' SUPERUSER CREATEDB CREATEROLE INHERIT LOGIN;"
  sudo createdb --host localhost --username mujinwww --encoding UTF-8 mujinwww
  python manage.py syncdb
  python manage.py schemamigration mujinwww --initial
  python manage.py migrate

Updating
========

Execute every time mujinwww is updated

::

  python $MUJIN_HOME/../www/mujinwww/manage.py syncdb
  python manage.py schemamigration mujinwww
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

  cd $MUJIN_HOME/../www/mujinwww; django-admin.py makemessages --locale=ja_JP

Open **$MUJIN_HOME/../web/mujinwww/locale/ja_JP/LC_MESSAGES/django.po** and edit the translations. When done execute::

  cd $MUJIN_HOME/../www/mujinwww; django-admin.py compilemessages --locale=ja_JP

Restart the mujinwww server and the new translation should be visible!


Production Environment
----------------------

This is for sending things to the real site.

Setup
=====

In order to push to mujin.co.jp, it needs your ssh public key. Your public key is probably in ~/.ssh/id_rsa.mujin.<yourname>.pub. You need to send this file to someone and have them add it to the authorized keys on mujin.co.jp.

::

  cat ~/.ssh/id_rsa.mujin.<yourname>.pub

Verify that the key was added by trying to ssh into mujin.co.jp. You'll know everything is working correctly when you try to ssh and immediately see a prompt for www-data@mujinserver0 without having to enter a password.

::

  ssh www-data@mujin.co.jp

Next, you need to install fabric, the tool that we use for pushing updates to mujin.co.jp

::

  sudo pip install fabric


Updating
========

To push updates to the website, just run "fab update" in the same directory as manage.py



Overall Workflow
----------------

This is the workflow to follow when doing work on the website

1. Before starting work, make sure you pull in the latest changes from master

::

  git pull origin master

2. Next, make the changes you want and test them locally on the django dev server

3. Once you're done making edits or whatever, make sure to add and commit everything you worked on. The "git status" is useful for looking at what was changed. Note that if you added a new file, it will be in the list for untracked files until you explicitly add it. Also be sure to write a DETAILED, CONCISE COMMIT MESSAGE. This lets others know what you did without having to look through your entire commit. Finally you need to push your changes to master if you want them to appear on the main website.

::

  git add <the files you worked on>
  git commit -m "<detailed, concise commit message>"
  git push origin master

4. Finally, to deploy your changes to the live website, simply run the update task with fabric from the same directory as manage.py

::

  fab update

5. Check that the changes you made actually worked with a web browser. Mistakes are easy to make and you can't be too careful with these things.
