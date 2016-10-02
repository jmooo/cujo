// All the libs we're going to be using
var gulp = require('gulp'),
    less = require('gulp-less'),
    browserify = require('gulp-browserify'),
    uglify = require('gulp-uglify'),
    watch = require('gulp-watch');

// Our various references
var frontendDir = './frontend',
    jsDir = frontendDir + '/javascript',
    lessDir = frontendDir + '/less',
    staticDir = './cujo/static';

var captureError = function(error){
    console.error(error.toString());
    this.emit('end');
};

gulp.task('build-js', function(){
    return gulp.src(jsDir + '/main.js')
        .pipe(browserify({
            insertGlobals: false,
            debug: false,
            transform: []
        }))
        .on('error', captureError)
        .pipe(gulp.dest(staticDir + '/js/'));
});

gulp.task('build-test', function(){
    return gulp.src(jsDir + '/tests/testSpec.js')
        .pipe(browserify({
            insertGlobals: false,
            debug: false
        }))
        .on('error', captureError)
        .pipe(gulp.dest('./jasmine/spec/'));
});

gulp.task('build-less', ['move-fonts'], function(error){
    return gulp.src(lessDir + '/main.less')
        .pipe(less()).on('error', function(err){
            gutil.log(err);
            this.emit('end');
        })
        .pipe(gulp.dest(staticDir + '/css/'));
});

gulp.task('move-fonts', function(er){
    return gulp.src('./node_modules/bootstrap/fonts/**/*')
        .pipe(gulp.dest(staticDir + '/css/fonts/'));
});

gulp.task('build', ['build-js', 'build-less']);
gulp.task('build-prod', function(error){
    gulp.src(jsDir + '/main.js')
        .pipe(browserify({
            debug: false,
            transform: [reactify]
        }))
        .pipe(uglify())
        .pipe(gulp.dest(staticDir + '/js/'));

    gulp.src(lessDir + '/main.less')
        .pipe(less({compress: true}))
        .pipe(gulp.dest(staticDir + '/css/'));

    gulp.src('./node_modules/bootstrap/fonts/**/*')
        .pipe(gulp.dest(staticDir + '/css/fonts/'));
});

gulp.task('watch', function(){
    gulp.start('build');
    gulp.start('build-test');

    watch(jsDir + "/**/*.{js,jsx}", function() {
        console.log('');
        console.log('-- JS Change Detected --');
        gulp.start('build-js');
        gulp.start('build-test');
    });

    watch(lessDir + "/**/*.{less}", function() {
        console.log('');
        console.log('-- LESS Change Detected --');
        gulp.start('build-less');
    });
});

gulp.task('default', ['build']);
