# Fitapp

## Local setup

Copy `.envs/.env.example` into `.env` and adjust the configuration variables.

### Pre-requirements
If you do not have Python 3.7 in your system install it from repository
or compile it by yourself.

### Installation

#### Virtualenv

```bash
$ mkvirtualenv fitapp --python=/usr/local/bin/python3
$ pip install -r requirements-dev.txt
$ pre-commit install
```

#### Database setup

```bash
$ ./manage.py migrate
```

#### Initial data

Load default system data. Default dashboard user is admin/demo12345

```bash
$ ./manage.py load_initial_data
```

### Usage

#### Run web server

Start the development server at given port.

``` bash
$ ./manage.py runserver 0.0.0.0:8000
```

### Development

#### Run tests

```bash
pytest
```

#### Reformat code

```bash
black .
```

#### Check code formatting

```bash
flake8
```

#### Reset the environment

> Be careful as this command completely wipes out your data in database! 

```bash
./manage.py reset_db -c && ./manage.py migrate && ./manage.py load_initial_data && ./manage.py runserver 0.0.0.0:80000
```