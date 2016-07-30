import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'tests.sqlite'
    }
}

INSTALLED_APPS = (
    'auf.django.references',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.staticfiles',
    'tests.universite',
    'tests.simpletests',
)

ROOT_URLCONF = 'tests.urls'
DEBUG = True
STATIC_URL = '/static/'

TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), 'templates'),)

SECRET_KEY = 'not-secret'

AUF_REFERENCES_MANAGED = True
