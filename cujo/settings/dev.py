from .base import *

DEBUG = True

# Enable use of 'if debug' in templates (google analytics, etc)
INTERNAL_IPS = (
    '0.0.0.0',
    '127.0.0.1',
)

ALLOWED_HOSTS = ['localhost']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
