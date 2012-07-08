#!/bin/bash
cd ~/mujinwww
python manage.py syncdb
django-admin.py compilemessages --locale=ja_JP
svn export mujinwww/static ~/statictemp
rm -rf ~/staticold
mv ~/static ~/staticold
mv ~/statictemp ~/static
