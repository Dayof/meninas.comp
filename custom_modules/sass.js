exports.task = {
  dist: {
    options: {
      style: 'expanded',
      lineNumbers: true, // 1
      sourcemap: 'none'
    },
    files: [{
      expand: true, // 2
      cwd: './meninascomp/static/sass',
      src: [ '**/*.scss' ],
      dest: './meninascomp/static/public',
      ext: '.css'
    }]
  }
};
