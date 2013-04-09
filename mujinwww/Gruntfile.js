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
    regarde: {
      app: {
        files: 'mujinwww/' + '**/*',
        tasks: ['exec:fixjsstyle', 'livereload']
      }
    }
  });


  // Tasks
  // -----

  // handy watch thing for live reloads
  grunt.registerTask('watch', ['livereload-start', 'regarde']);
};
