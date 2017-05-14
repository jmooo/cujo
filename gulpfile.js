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


gulp.task('styles', function() {
  return gulp.src(scssPath + '/main.scss')
    .pipe(scss())
    .pipe(gulp.dest(staticPath + '/css/'))
    .pipe(livereload());
});

gulp.task('scripts', function() {
  return browserify(jsPath + '/main.js')
    .bundle()
    .pipe(source('main.js'))
    .pipe(gulp.dest(staticPath + '/js/'))
    .pipe(livereload());
});

gulp.task('fonts', function() {
  return gulp.src('./node_modules/font-awesome/fonts/fontawesome-webfont.*')
    .pipe(gulp.dest(staticPath + '/fonts/'));
});

gulp.task('watch', function() {
  gulp.start('build')
  livereload.listen();
  gulp.watch(scssPath + '/**/*.scss', ['styles']);
  gulp.watch(jsPath + '/**/*.js', ['scripts']);

  /* Trigger a live reload on any Django template changes */
  gulp.watch('**/templates/*').on('change', livereload.changed);
});

gulp.task('build', ['styles', 'scripts', 'fonts']);
gulp.task('default', ['build']);
