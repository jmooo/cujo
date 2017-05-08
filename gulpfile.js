var gulp = require('gulp');
var scss = require('gulp-sass');
var uglify = require('gulp-uglify');
var livereload = require('gulp-livereload');
var browserify = require('browserify');
var source = require('vinyl-source-stream');

// Path shortcuts
var assetsPath = './assets',
  jsPath = assetsPath + '/javascript',
  scssPath = assetsPath + '/scss',
  staticPath = './static';


gulp.task('build-scss', function() {
  return gulp.src(scssPath + '/main.scss')
    .pipe(scss())
    .pipe(gulp.dest(staticPath + '/css/'))
    .pipe(livereload());
});

gulp.task('build-js', function() {
  return browserify(jsPath + '/main.js')
    .bundle()
    .pipe(source('main.js'))
    .pipe(gulp.dest(staticPath + '/js/'))
    .pipe(livereload());
});

gulp.task('watch', function() {
  livereload.listen();
  gulp.watch(scssPath + '/**/*.scss', ['build-scss']);
  gulp.watch(jsPath + '/**/*.js', ['build-js']);

  /* Trigger a live reload on any Django template changes */
  gulp.watch('**/templates/*').on('change', livereload.changed);
});

gulp.task('build', ['build-scss', 'build-js']);
gulp.task('default', ['build']);
