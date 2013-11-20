#[mujin.co.jp](http://mujin.co.jp)
----

##Welcome

First, if you want to do any work on the website please run the become-a-website-developer.bash in this directory.
This installs all the dependencies to work on the website. Here are the big ones:
- bower and grunt (which needs node and npm)
- jekyll (which needs ruby 1.9.3, rvm)

##Actual website development

Just run "grunt gaze" and point your browser to [http://localhost:1234](http://localhost:1234)
You can now modify any part of the website and it will be automatically rebuilt and your browser will refresh.
Right now the jekyll build is really slow (It is because of internationalizations -- I'm working on speedups for it).

##Updating translations

The japanese translation index is kept in the _i18n/ja.yml file. This index is manually kept, which means that anything you put in a translation tag must be manually copied into the YAML file and then translated. If you manually run "jekyll build", it will output all the missing translation keys to give you an idea of what needs to be added.
