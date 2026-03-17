
import os
from .base import *

DEBUG = True
ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'full_search_demo',
        'USER': 'postgres',
        'PASSWORD': os.getenv("DB_PASSWORD", "postgres"),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}