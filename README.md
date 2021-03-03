SF Global Network Site
======================

This is based on the [Django Starter Tutorial](https://github.com/kws/django-starter).

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

To run locally, try

```shell
pip install -r requirements.txt

./manage.py migrate
./manage.py create-demo-admin
./manage.py create-demo-skills
./manage.py create-demo-users 
./manage.py collectstatic
./manage.py runserver
```