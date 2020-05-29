[![Scope](https://app.scope.dev/api/badge/9141d86b-7846-450a-859b-30be15cafff1/default)](https://app.scope.dev/external/v1/inspect/f0a213f0-b550-4bb0-a651-c1d5b9eff041/9141d86b-7846-450a-859b-30be15cafff1/default)

# Python Demo App

Demo project for Python server application

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for developing and testing purposes.

### Prerequisites

1. You’ll need to have Python 3.6+.

### Installing

1. Clone repository

```bash
$ git clone git@github.com:scope-demo-app/python-demo-app.git
```

2. Access the repository folder

```bash
$ cd python-demo-app
```

3. Install dependencies

Take a look at [virtualenv](https://virtualenv.pypa.io/en/latest/) and [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/).

```bash
$ pip install -r requirements.txt
```

4. Setup database

The database is PostgreSQL. You need to setup the following environment variables:

```
DB_PASS=<database_password>
DB_USER=<database_user>
DB_NAME=<database_name>
DB_HOST=<database_host>
DB_PORT=<database_port>
```

5. Run migrations

```bash
$ ./manage.py migrate
```

## Run locally

To run the application locally:

```bash
$ scope-run ./manage.py runserver
```

## Run tests

### Django tests

To run Django tests:

```bash
$ ./manage.py test
```

### unittest tests

To run unittest tests:

```bash
$ python -m unittest api/tests_unittest.py
```

### pytest tests

To run pytest tests:

```bash
$ pytest api/tests_pytest.py
```

## Report results to Scope

If you want to report your test results to Scope you need to run your tests with the `SCOPE_DSN` env variable. An option would be:

```bash
$ SCOPE_DSN=<your_namespace_dsn> ./manage.py test
```

### How to obtain SCOPE_DSN

Go to [Scope](https://app.scope.dev/) for more information about how to get your SCOPE_DSN.

## Reviewing the tests

After the tests run, you'll get a URL in the console with a direct link to the test results:

```bash
** Scope Test Report **
Access the detailed test report for this build at:
   https://app.scope.dev/external/v1/results/...
```

Alternatively, the `Scope for Mac` and `Scope for Windows` applications will also show recent runs. Clicking on these will take you directly to the test reports.

When reviewing the tests in Scope, filter by `demotest` in the search bar to find the most interesting tests. Other tests, particularly those tagged as `dummy` may not contain useful information.
