#!/bin/bash

# so that add-apt-repository works
sudo apt-get install -y python-setuptools

# install node
sudo add-apt-repository ppa:chris-lea/node.js
sudo apt-get update
sudo apt-get install -y nodejs

# install global node deps
sudo npm install -g bower grunt-cli
sudo rm -r ~/.npm ~/tmp

# install our node and bower deps 
npm install
bower install

# install linter
sudo easy_install http://closure-linter.googlecode.com/files/closure_linter-latest.tar.gz

# install rvm and ruby 1.9.3
sudo apt-get install -y build-essential curl
curl -L https://get.rvm.io | bash -s stable
source ~/.rvm/scripts/rvm
rvm install 1.9.3
rvm use 1.9.3

# install jekyll
sudo gem install jekyll

# goodbye!
sudo apt-get install -y toilet
toilet -f future --gay "now go work on the website"
