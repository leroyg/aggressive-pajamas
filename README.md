# Aggressive Pajamas

Host better Brazilian Jiu-Jitsu Competitions

## Installation

Setup a virtualenv and install requirements
(this example uses [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)):

```bash
mkvirtualenv aggressive-pajamas -p python3
pip install -r requirements.txt
```

## Set up database

Create a database named `aggressive-pajamas`.

```
createdb aggressive-pajamas
```

Create database tables:

```
./manage.py migrate
```

## Running server

```bash
./manage.py runserver
```

## Building front-end

To build JavaScript and CSS files, first install npm packages:

```bash
npm install
```

Then to build (and watch for changes locally) just run:

```bash
npm run dev-watch
```

## Running Celery

Celery can be used to run background tasks. To run it you can use:

```bash
celery -A aggressive-pajamas worker -l INFO
```


## Running Tests

To run tests simply run:

```bash
./manage.py test
```

Or to test a specific app/module:

```bash
./manage.py test apps.utils.tests.test_slugs
```


On Linux-based systems you can watch for changes using the following:

```bash
find . -name '*.py' | entr python ./manage.py test
```
