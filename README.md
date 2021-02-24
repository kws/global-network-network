Django Starter Project
======================

This is a project for us to experiment with [Django](https://www.djangoproject.com/)
which is a web framework that makes developing web applications quick and with
minimal amounts of code.

We will roughly follow the plan of the 
[Django Tutorial](https://docs.djangoproject.com/en/3.1/intro/tutorial01/)
without a lot of the inital setup as I have already created the site
application configurations we will be using. 

## Getting Started

Assuming you have by now used git to check out a local copy of this repository 
and used the python environment manager of your choice (we use 
[Anaconda](https://www.anaconda.com/products/individual)) to create a new
environment for this project, you are now ready to install the required libraries to
run this project. The simplest is to install with:

```shell
pip install -r requirements.txt
```

You can have a look at [requirements.txt](./requirements.txt) to see what
this file contains. This is 
[a list of libraries](https://pip.pypa.io/en/stable/reference/pip_install/#requirements-file-format), 
most notably the Django
distribution itself, that we need for this test project. If, as we develop
the site, we need more libraries, we can update the requirements.txt 
and re-run the above command to download the extra libraries. 

## Creating the database and a superuser

Once you have installed the libraries, you can create a new database file 
(the default development configuration uses [SQLite](https://www.sqlite.org/)
which is a file-based relational database system that can run straight from your
hard-disk without requiring additional processes).

Create the database file with:

```shell
python manage.py migrate
```

You can now create a superuser with:

```shell
python manage.py createsuperuser
```

## Running the server

```shell
python manage.py runserver
```