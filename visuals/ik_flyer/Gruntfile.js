module.exports = function(grunt) {
  'use strict';
  //
  // Grunt configuration:
  //
  // https://github.com/cowboy/grunt/blob/master/docs/getting_started.md
  //

  // Dependencies
  // ------------
  
  grunt.loadNpmTasks('grunt-regarde');
  grunt.loadNpmTasks('grunt-contrib-livereload');
  grunt.loadNpmTasks('grunt-exec');
  grunt.loadNpmTasks('grunt-contrib-connect');
  grunt.loadNpmTasks('grunt-contrib-less');
  
  
  // Config
  // ------
  
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    connect: {
      server: {
        options: {
          hostname: '*',
          port: 9001
        }
      }
    },
    less: {
      main: {
        files: {
          'css/main.css': 'css/less/main.less'
        }
      }
    },
    exec: {
      fixjsstyle: {
        command: 'fixjsstyle js/main.js',
        stdout: true
      }
    },
    regarde: {
      app: {
        files: ['css/less/**/*', 'index.html', 'js/**/*'],
        tasks: ['build', 'livereload']
      }
    }
  });


  // Tasks
  // -----

  grunt.registerTask('build', ['exec:fixjsstyle', 'less']);
  
  // handy watch thing for live reloads
  grunt.registerTask('watch', ['connect', 'livereload-start', 'build', 'regarde']);
};
