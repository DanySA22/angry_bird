import os
from .common import *
import dj_database_url

DEBUG = False
SECRET_KEY = os.environ['SECRET_KEY']


ALLOWED_HOSTS = ['angry-bird-on-space-91b54cb540d2.herokuapp.com', 'angrybird.danieldevcloud.com']


DATABASES = {
    'default': dj_database_url.config()
}