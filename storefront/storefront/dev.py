import os
from .common import *
from dotenv import load_dotenv
load_dotenv()


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True



# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')
ALLOWED_HOSTS = [
    
    'home.shaqserver.com',
    '127.0.0.1',
]
#^ required if DEBUG is turned off


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('RDS_DB_NAME'),
        'USER': os.environ.get('RDS_USERNAME'),
        'PASSWORD': os.environ.get('RDS_PASSWORD'),
        'HOST': os.environ.get('RDS_HOSTNAME'),
        'PORT': os.environ.get('RDS_PORT'),
    }
}



