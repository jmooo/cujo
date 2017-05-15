# Custom Job (cujo) Work Ticket Manager
Ticket system combines management of several concepts, such as work requests, job logs, and service tickets.

## Technologies
* [Python 3.6+](https://www.python.org/)
* [Django](https://www.djangoproject.com/)
* [PostgreSQL](https://www.postgresql.org/): Full-text search with [tsvector](https://www.postgresql.org/docs/current/static/datatype-textsearch.html)? Yes please.
* [Bootstrap 4](https://v4-alpha.getbootstrap.com/): Longest alpha in history
* [Gulp.js](http://gulpjs.com/): Webpack seems like overkill, currently.


## Installation
* `pip install -r requirements.txt` - Install required components
* `npm install` - Install requirements from project.json
* `gulp watch` - Build and auto-reload changes to your scss & js
* `./manage.py makemigrations` - Prepare migrations
* `./manage.py migrate` - Run migrations (needs all db privs for this, not just I.S.U.D)

#### Managing settings and secrets
To choose between dev/stage/prod.py settings append this to your env file, probably at `/<venvs>/cujo/bin/postactivate`:
* `export DJANGO_SETTINGS_MODULE="cujo.settings.dev"`

To keep your usernames/passwords out of git rename [`settings.json.example`](settings.json.example) to `settings.json` in the root project folder.


## Hot tips
* `./manage.py runserver` - Run Django development server
* `django-admin startapp module_name` - Create file layout for a new Django module
* `pip list -o` - List outdated packages
* `npm outdated` - Find your old garbage


## License
MIT (see [LICENSE](LICENSE.md))
