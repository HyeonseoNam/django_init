# Parse database configuration from $DATABASE_URL
import dj_database_url
from os import environ

from .base import *

# TODO : edit and host name
ALLOWED_HOSTS = ['yourproject.example.com']

# TODO : edit databases
DATABASES = {
    'default': dj_database_url.config()
}

STATIC_ROOT = environ['STATIC_ROOT']
