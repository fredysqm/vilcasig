from ._devel import *

ALLOWED_HOSTS = ['*']
SECRET_KEY = '2uUqZU73kq9xv^d7@!+9Nwk^n2q@_klOa58dvu7#9e4+yru)-G'
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.mysql',
        'NAME': 'vilcasig_dev',
        'USER': 'root',
        'PASSWORD': 'pwd123',
        'HOST': 'localhost',
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = '/tmp/vilcasig/'