# flake8: noqa
from .base import *

DEBUG = False

ALLOWED_HOSTS = ['localhost']

SECRET_KEY = '7l_pgs2nsv4!w-z2gmi2=ou4*q#emrtaz9*+0ryleqrb7s^odb'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'test_cujo',
        'USER': os.environ.get('CUJO_DATABASE_USER'),
        'PASSWORD': os.environ.get('CUJO_DATABASE_PASSWORD'),
        'HOST': 'localhost',
    },
}
