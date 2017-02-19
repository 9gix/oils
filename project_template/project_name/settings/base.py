"""
Django settings for {{ project_name }} project.

Originally generated by 'django-admin startproject' using Django 1.8.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

SETTINGS_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(SETTINGS_DIR))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '{{ secret_key }}'

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    # Pre-contrib Apps
    'grappelli',

    # Contrib Apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third Party Apps
    'rest_framework',
    'rest_framework_swagger',
    'django_filters',
    'django_countries',
    'django_extensions',
    'django_tables2',
    'haystack',
    'mptt',

    # OILS Apps
    'oils.core',
    'oils.apps.catalog',
    'oils.apps.circulation',
    'oils.apps.dashboard',
    'oils.apps.shelving',
    'oils.apps.library',
    'oils.apps.opac',
    'oils.apps.account',

    # Internal Apps
    '{{ project_name }}',
]

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = '{{ project_name }}.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),            
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = '{{ project_name }}.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '{{ project_name }}',
        'USERNAME': '',
        'PASSWORLD': '',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}

# Authentication User
#AUTH_USER_MODEL = '{{ project_name }}.User'

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
PUBLIC_DIR = os.path.join(BASE_DIR, 'public')

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PUBLIC_DIR, 'static')

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(PUBLIC_DIR, 'media')

# Registration
ACCOUNT_ACTIVATION_DAYS = 7

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
    },
}


# API Resources
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework.filters.DjangoFilterBackend',
    ),
    'PAGE_SIZE': 100,
}


from django.core.urlresolvers import reverse_lazy

OILS = {
    'CATALOG': {},
    'CIRCULATION': {
        'DEFAULT_LOAN_LIMIT': 8,
        'DEFAULT_LOAN_DURATION': 20,
        'DEFAULT_RENEWAL_LIMIT': 3,
    },
    'DASHBOARD': {
        'MENU': [
            {
                'text': 'Membership',
                'description': 'Membership Management, and Patron Management',
                'url': reverse_lazy('dashboard:account:index'),
                'children': [
                    {
                        'text': 'Registration',
                        'url': reverse_lazy('dashboard:account:registration'),
                    },
                ],
            },
            {
                'text': 'Circulation',
                'description': 'Loan, Renewal, Return or Transfer of Books',
                'url': reverse_lazy('dashboard:circulation:loan:index'),
                'children': [
                    {
                        'text': 'Loan Form',
                        'url': reverse_lazy('dashboard:circulation:loan:new'),
                    },
                    {
                        'text': 'Renewal',
                        'url': reverse_lazy('dashboard:circulation:loan:renewal'),
                    }, 
                    {
                        'text': 'Return',
                        'url': reverse_lazy('dashboard:circulation:loan:return'),
                    }, 
                ],
            },
        ],
    },
}
# Catalog Apps
CATALOG = {

}

# Crispy Form
CRISPY_TEMPLATE_PACK = 'bootstrap3'

# Circulation Apps
CIRCULATION = {
    'RENEWAL_POLICY_BACKEND': 'circulation.backends.RenewalFromToday',
}

try:
    from .local_settings import *
except ImportError:
    pass
