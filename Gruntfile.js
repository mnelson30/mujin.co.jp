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
      }
    },

    watch: {

      options: {
        livereload: 12345
      },

      // build the website if anything changes
      website: {
        files: [
          '_config.yml',
          '_includes/**/*.html',
          '_layouts/**/*.html',
          '*.html'
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
      
      bower_components: {
        files: [
          'bower_components/**/*',

          // exclude a bunch of crap that should not be watched
          '!**/.git/**',
          '!**/node_modules/**',
          '!**/bower_components/**'
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
      'jekyll',
      'connect',
      'watch'
    ]);
  });

  grunt.registerTask('default', function() {

    grunt.option('force', true);

    grunt.task.run([
      'website'
    ]);
  });

  // gaze, to be used along with server
  grunt.registerTask('lint', [
    'exec:fixjsstyle'
  ]);
};
