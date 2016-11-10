from ._devel import *

ALLOWED_HOSTS = ['*']
SECRET_KEY = '2uUqZu93kq9xv^d7@!+9nwk^n2q@_kloa58dvu7#9e4+yru)-G'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sig_dev',
        'USER': 'postgres',
        'PASSWORD': 'phpforever',
        'HOST': 'sig.mdv.net',
        'PORT': '5432',
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = '/tmp/vilcasig/'