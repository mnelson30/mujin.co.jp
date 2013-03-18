#!/bin/bash
cd ~/www/mujinwww
git reset --hard HEAD # remove any local changes
git pull
python manage.py syncdb
django-admin.py compilemessages --locale=ja_JP
rm ~/static
ln -s -f `pwd`/mujinwww/static ~/static
