import os
import django_heroku
from website.settings import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY", "~~~SECRET~~~")

ALLOWED_HOSTS = ['.herokuapp.com']

DEBUG = False

# Activate Django-Heroku.
django_heroku.settings(locals())
