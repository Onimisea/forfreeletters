from .common import *

DEBUG = os.getenv('DEBUG')

SECRET_KEY = os.getenv('SECRET_KEY')

ALLOWED_HOSTS = ['dev.forfreeletters.com', 'forfreeletters.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DATABASE_NAME'),
        'USER': os.getenv('DATABASE_USER'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD'),
        'HOST': os.getenv('DATABASE_HOST'),
        'PORT': os.getenv('DATABASE_PORT'),
    }
}

CSRF_TRUSTED_ORIGINS = ['dev.forfreeletters.com', 'forfreeletters.com']

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}