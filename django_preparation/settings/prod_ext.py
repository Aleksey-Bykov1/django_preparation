from .prod import *


SITE_ID = 1

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'test',
        'USER': 'alex',
        'PASSWORD': '1234',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}
