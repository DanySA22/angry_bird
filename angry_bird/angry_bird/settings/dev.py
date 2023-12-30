from .common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SECRET_KEY = 'django-insecure-d9a9-i6a^h#7)0p2((h_!w&^tua$*w1qq)d#&@pm_g2b4g$#+q'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'angry_bird',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'password22W$'
    }
}
