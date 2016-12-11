exports.task = {
  my_target: {
    files: [{
      expand: true,
      cwd: './meninascomp/static/public/',
      src: [ '*.css', '!*.min.css' ], // 1
      dest: './meninascomp/static/public/',
      ext: '.min.css'
    }]
  }
};
