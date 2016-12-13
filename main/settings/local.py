from ._devel import *

ALLOWED_HOSTS = ['*']
SECRET_KEY = '2uUqZu93kq9xv^d7@!+9nwk^n2q@_kloa58dvu7#9e4+yru)-G'
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.mysql',
        'NAME': 'vilcasig_v2',
        'USER': 'root',
        'PASSWORD': 'pwd123',
        'HOST': 'localhost',
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = '/tmp/vilcasig/'