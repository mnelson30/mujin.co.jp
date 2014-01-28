#[www.mujin.co.jp](http://www.mujin.co.jp)

###Quick start

If you want to do any work on the website please follow these steps

1. Clone the repo and its submodules:

      	git clone https://github.com/mujin/mujin.co.jp.git
      	cd mujin.co.jp

2. Install dependencies to build the website. All you have to do is run:

      	./become-a-website-developer.bash

  This installs all the dependencies you need to work on the website. Here are some of them:
  - `bower` and `grunt` (which need `node` and `npm`)
  - `jekyll` (which needs ruby 1.9.3, `rvm`)

3. You're done. Now you can build the website for the first time and check it out on [http://localhost:1234](http://localhost:1234):

      	grunt gaze

###Vagrant

If you can't (or don't want to) follow the quickstart for whatever reason, you can do all of your work inside a VM if you like. First, install [vagrant](http://www.vagrantup.com/). After that, `cd vagrant`, `vagrant up` and `vagrant ssh`. The `become-a-website-developer.bash` will be run for you automatically when the VM is created and you'll find a ready to use dev environment in `~/mujin.co.jp` once you ssh in.

###Actual website development

The website is implemented with [jekyll](http://jekyllrb.com/), which is a popular and simple static site generator that is very well documented.

To work on the website, just run `grunt gaze` and point your browser to [http://localhost:1234](http://localhost:1234). You can now modify any of the of the files outside of the `_site` directory and it will be automatically rebuilt and your browser will refresh for you. Right now the jekyll build can be slow (It is because of internationalizations -- I'm working on speedups for it) so be patient.

###Deployment

Right now we deploy to `mujin.co.jp` and `www.mujin.co.jp`. This will only work if you have the right SSH keys on both hosts.

        grunt deploy

###Updating translations

The japanese translation index is kept in the `_i18n/ja.yml` file. This index is manually kept, which means that anything you write in english in a translation tag must be manually copied into the YAML file and then translated. If you manually run "jekyll build", it will output all the missing translation keys to give you an idea of what needs to be added. In the future we plan to automatically add missing tags to the YAML file.
