from .common import *

DEBUG = True

SECRET_KEY = 'django-insecure-x!n@xxzgu&6m2r1r&2*i=5@kg4m+z9$1cl(x@xv#p%2&er4p8@'

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}