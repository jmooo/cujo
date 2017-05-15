from .base import *

DEBUG = True

SECRET_KEY = get_secret("SECRET_KEY")

# Enable use of 'if debug' in templates (google analytics, etc)
INTERNAL_IPS = (
    '0.0.0.0',
    '127.0.0.1',
)

ALLOWED_HOSTS = ['localhost']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': get_secret("DATABASE_NAME"),
        'USER': get_secret("DATABASE_USER"),
        'PASSWORD': get_secret("DATABASE_PASSWORD"),
        'HOST': get_secret("DATABASE_HOST"),
    },
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
