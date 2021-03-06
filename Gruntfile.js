module.exports = function(grunt) {

  // Project configuration.
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    uglify: {
      options: {
        banner: '/*! <%= pkg.name %> <%= grunt.template.today("yyyy-mm-dd") %> */\n'
      },
      build: {
        src: './<%= pkg.name %>/static/public/*.js',
        dest: './<%= pkg.name %>/static/public/main.min.js'
      }
    },
    sasslint: {
        options: {
            configFile: '.sass-lint.yml',
        },
        target: ['./<%= pkg.name %>/static/sass/**/*.scss']
    },
    watch: {
      files: './<%= pkg.name %>/static/sass/**/*.scss',
      tasks: [ 'sass', 'cssmin' ]
    },
    sass: require( './custom_modules/sass' ).task,
    cssmin: require( './custom_modules/cssmin' ).task
  });

  // Load the plugin that provides the "uglify" task.
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-sass-lint');
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-contrib-sass');
  grunt.loadNpmTasks('grunt-contrib-cssmin');

  // Default task(s).
  grunt.registerTask('default', ['sasslint', 'uglify', 'watch']);

};
