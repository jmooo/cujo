from .base import *

DEBUG = False

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = get_secret("EMAIL_HOST")
EMAIL_HOST_USER = get_secret("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = get_secret("EMAIL_HOST_PASSWORD")
EMAIL_PORT = get_secret("EMAIL_PORT")
EMAIL_USE_TLS = get_secret("EMAIL_USE_TLS")
DEFAULT_FROM_EMAIL = get_secret("DEFAULT_FROM_EMAIL")
