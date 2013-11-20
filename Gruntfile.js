module.exports = function(grunt) {
'use strict';

  // load all grunt tasks
  require('matchdep').filterDev('grunt-*').forEach(grunt.loadNpmTasks);

  grunt.initConfig({

    pkg: grunt.file.readJSON('package.json'),

    jekyll: {
      website: {}
    },
    
    rsync: {
      
      options: {
        recursive: true
      },

      assets: {
        options: {
          src: [
            'img',
            'css',
            'js'
          ],
          dest: '_site'
        }
      },
      
      bower_components: {
        options: {
          src: [
            'bower_components'
          ],
          dest: '_site'
        }
      },
      
      deploy: {
        options: {
          src: ['_site'],
          dest: '/var/www/www/mujin.co.jp',
          host: 'www-data@mujin.co.jp',
          syncDest: true
        }
      }
    },

    less: {

      production: {
        options: {
          yuicompress: true
        },
        files: {
          'css/bootstrap.min.css': 'less/bootstrap.less'
        }
      }
    },

    watch: {

      options: {
        livereload: 12345
      },

      // build the website if anything changes
      website: {
        files: [
          '**/*.yml',
          '**/*.md',
          '**/*.html',

          // exclude a bunch of crap that should not be watched
          '!**/.git/**',
          '!**/node_modules/**',
          '!**/bower_components/**',
          '!**/_site/**'
        ],
        tasks: ['jekyll']
      },
      
      assets: {
        files: [
          'img/**/*',
          'js/**/*',
          'css/**/*'
        ],
        tasks: ['rsync:assets']
      },
      
      less: {
        files: ['less/**/*'],
        tasks: ['less']
      },
      
      bower_components: {
        files: [
          'bower_components/**/*',
        ],
        tasks: ['rsync:bower_components']
      }
    },

    // testing server
    connect: {

      options: {
        hostname: '*',
        port: 1234,
        livereload: 12345,
        base: '_site'
      },

      testserver: {}
    }
  });

  grunt.registerTask('website', function() {

    grunt.task.run([
      'less',
      'jekyll'
    ]);
  });

  grunt.registerTask('gaze', function() {

    grunt.task.run([
      'connect',
      'website',
      'watch'
    ]);
  });

  grunt.registerTask('default', function() {

    grunt.option('force', true);

    grunt.task.run([
      'website'
    ]);
  });

  grunt.registerTask('deploy', function() {

    grunt.task.run([
      'website',
      'rsync:deploy'
    ]);
  });

  // gaze, to be used along with server
  grunt.registerTask('lint', [
    'exec:fixjsstyle'
  ]);
};
