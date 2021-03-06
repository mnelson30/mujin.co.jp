from __future__ import with_statement
import os
from fabric.api import *

WWW_ROOT = '/var/www/www/mujinwww'
DEV_ROOT = '/var/www/temp/www/mujinwww'

env.user = 'www-data'
env.hosts = ['mujin.co.jp']

env.use_ssh_config = True

env.key_filename = []
for key in os.listdir(os.path.join(os.environ['HOME'], '.ssh')):
    if 'mujin' in key.split('.') and 'pub' not in key.split('.'):
        env.key_filename.append(os.path.join(os.environ['HOME'], '.ssh', key))

def clean():
    with cd(WWW_ROOT):
        run('git reset --hard HEAD')
        run('git clean -fdx')

def pull():
    with cd(WWW_ROOT):
        run('git checkout master')
        run('git pull origin master')

def build_translations():
    with cd(WWW_ROOT):
        run('django-admin.py compilemessages --locale=ja_JP')

def update():
    clean()
    pull()
    build_translations()

def devserver():
    with cd(DEV_ROOT):
        run('git reset --hard HEAD')
        run('git pull origin master')
        run('MUJIN_ENV=dev python manage.py runserver 0.0.0.0:8000')

def update_packages():
    run('sudo apt-get update')
    run('sudo apt-get -y dist-upgrade')
