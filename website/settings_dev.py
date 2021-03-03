from website.settings import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*qw9#2oqfs5k7(t+3)2j!fy@=nj8b*$o*tful&piwgbx65@h#2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}