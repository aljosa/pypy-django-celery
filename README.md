Django/Celery on PyPy
=

Example Django project w/ Celery (just import) running on PyPy 2.0.2 and results in "RuntimeError: not holding the import lock" but works (renders a web page w/ text "home") on CPython 2.7.x or PyPy 1.9.

**PyPy version (Ubuntu 13.04; from PyPy PPA):**

    Python 2.7.3 (2.0.2+dfsg-1~ppa1, May 22 2013, 11:26:59)
    [PyPy 2.0.2 with GCC 4.6.3] on linux2

**Steps to reproduce error:**

1) git clone this repo:

    $ git clone git://github.com/aljosa/pypy-django-celery.git
    $ cd pypy-django-celery

2) create and activate virtualenv w/ pypy 2.0.2:

    $ virtualenv -p pypy env
    $ . env/bin/activate

3) use pip to install requirements from requirements.txt (django + celery):

    $ pip install -r requirements.txt

4) source profile file, it sets DJANGO_SETTINGS_MODULE and PYTHONPATH:

    $ . profile

5) run django-admin.py runserver:

    $ django-admin.py runserver

6) open http://localhost:8000 in browser:

    $ xdg-open http://localhost:8000
