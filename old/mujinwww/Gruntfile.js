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
  grunt.loadNpmTasks('grunt-contrib-less');

  // Config
  // ------
  
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    exec: {
      fixjsstyle: {
        command: 'fixjsstyle mujinwww/static/js/mujinwww.js',
        stdout: true
      }
    },
    less: {
      everything: {
        files: {
          "mujinwww/static/css/main.css": "mujinwww/static/css/less/main.less",
          "mujinwww/static/css/flyer.css": "mujinwww/static/css/less/flyer.less"
        }
      }
    },
    regarde: {
      mujinwww: {
        files: ['mujinwww/**/*', '!mujinwww/static/css/*'],
        tasks: ['build', 'livereload']
      }
    }
  });


  // Tasks
  // -----

  grunt.registerTask('build', ['exec:fixjsstyle', 'less']);
  
  // handy watch thing for live reloads
  grunt.registerTask('watch', ['build', 'livereload-start', 'regarde']);
};
