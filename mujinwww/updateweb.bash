#!/bin/bash
cd ~/www/mujinwww
python manage.py syncdb
django-admin.py compilemessages --locale=ja_JP
ln -s -f `pwd`/mujinwww/static ~/static
