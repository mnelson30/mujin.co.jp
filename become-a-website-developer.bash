#!/bin/bash

sudo apt-get update

# so that add-apt-repository works
sudo apt-get install -y python-setuptools python-software-properties software-properties-common

# install node
sudo add-apt-repository -y ppa:chris-lea/node.js
sudo apt-get update
sudo apt-get install -y nodejs

# install global node deps
sudo npm install -g bower@1.2.8 grunt-cli@0.1.13
sudo rm -r ~/.npm ~/tmp

# install our node and bower deps
if [ -a "/home/vagrant/mujinwww/.vagrant-tmp" ]; then
  cd /home/vagrant/mujinwww/
fi
npm install
bower install

# install linter
sudo easy_install http://closure-linter.googlecode.com/files/closure_linter-latest.tar.gz

# install rvm and ruby 1.9.3
sudo apt-get install -y build-essential curl
curl -L https://get.rvm.io | bash -s stable
if [ -a "/home/vagrant/mujinwww/.vagrant-tmp" ]; then
  source /home/vagrant/.rvm/scripts/rvm
else
  source ~/.rvm/scripts/rvm
fi
rvm install 1.9.3
rvm use 1.9.3

# install jekyll
sudo gem install jekyll -v 1.4.3

# clean up if this was done from vagrant
if [ -a "/home/vagrant/mujinwww/.vagrant-tmp" ]; then
  rm /home/vagrant/mujinwww/.vagrant-tmp
fi

# goodbye!
sudo apt-get install -y toilet
toilet -f future --gay "now go work on the website"

