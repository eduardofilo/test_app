# testapp

This is a small Django application for demostrative purposes.

## Requirements

System requirements:

* Python3
* PostgreSQL
* Using of [virtualenvwrapper](https://apuntes.eduardofilo.es/desarrollo/python.html#instalacion_1) is highly recommended.

The following Python modules are used:

* Django (3.0.7)
* psycopg2 (2.8.5): PostgreSQL connector.
* django-crispy-forms (1.9.1): To manage formsets.
* django-cookie-law (2.0.3): Cookie alert.

## Install/deploy

1. Using [virtualenvwrapper](https://apuntes.eduardofilo.es/desarrollo/python.html#instalacion_1):

    ```
    $ cd ~/git
    $ git clone https://github.com/eduardofilo/test_app
    $ cd ~/git/test_app
    $ mkvirtualenv test_app -p python3
    $ workon test_app
    (test_app) $ setvirtualenvproject $VIRTUAL_ENV .
    (test_app) $ pip install -r requirements.txt
    ```

2. Database setup:

    ```
    $ sudo -u postgres psql
    postgres=# CREATE DATABASE testapp;
    postgres=# CREATE USER testuser WITH ENCRYPTED PASSWORD 'testpwd';
    postgres=# ALTER ROLE testuser SET client_encoding TO 'utf8';
    postgres=# ALTER ROLE testuser SET default_transaction_isolation TO 'read committed';
    postgres=# ALTER ROLE testuser SET timezone TO 'UTC';
    postgres=# GRANT ALL PRIVILEGES ON DATABASE testapp TO testuser;
    postgres=# \q
    ```

3. Apply migrations:

    ```
    $ cd ~/git/test_app
    $ workon .
    (test_app) $ python manage.py migrate
    ```

4. Load mock data (six minutes in my machine):

    ```
    (test_app) $ python manage.py shell < fill_db.py
    ```

5. Run development server:

    ```
    (test_app) $ python manage.py runserver 0.0.0.0:8000
    ```

6. Open [http://localhost:8000](http://localhost:8000) in browser.
