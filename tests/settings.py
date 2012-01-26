DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'tests.sqlite'
    }
}

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.staticfiles',
    'auf.django.references',
    'auf.django.references.managedref',
    'tests.universite',
)

ROOT_URLCONF = 'tests.urls'
DEBUG = True
STATIC_URL = '/static/'
