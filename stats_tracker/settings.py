"""
Django settings for stats_tracker project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

import tempfile

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '087rgzin!o5ley)%o$5jp21bh))mli92yai=h^ntcz&o5-i*$u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = DEBUG
TEMPLATE_DIRS = [BASE_DIR + '/common/templates/']
TEMPLATE_LOADERS = (
    'djmako.MakoLoader',
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MAKO_TEMPLATE_DIRS = [BASE_DIR + '/common/templates']
MAKO_MODULE_DIR = BASE_DIR + '/mako_modules/'
MAKO_TEMPLATE_OPTS = dict(
    input_encoding='utf-8',
    cache_impl='djmakocache',
    module_directory=os.path.join(
        tempfile.gettempdir(),
        os.environ.get('LOGNAME', 'someuser'),
        'mysite',
        BASE_DIR.split('/')[-2]
    )
)

ALLOWED_HOSTS = []

# Application definition
MAKO_APPS = (
    'apps.homepage',
    'apps.sports',
    'apps.users',
)
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
) + MAKO_APPS


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'stats_tracker.urls'

WSGI_APPLICATION = 'stats_tracker.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'NAME': 'stats_tracker',
    #     'USER': 'root',
    #     'PASSWORD': '',
    #     'HOST': ''
    # },
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

from django.core.exceptions import ImproperlyConfigured

import os

app_dirs = []
for app in MAKO_APPS:
    i = app.rfind('.')
    if i == -1:
        m, a = app, None
    else:
        m, a = app[:i], app[i + 1:]
    try:
        if a is None:
            mod = __import__(m, {}, {}, [])
        else:
            mod = getattr(__import__(m, {}, {}, [a]), a)
    except ImportError, e:
        raise ImproperlyConfigured('ImportError %s: %s' % (app, e.args[0]))

    app_dirs.append(os.path.dirname(mod.__file__))

app_template_dirs = []
for app_dir in app_dirs:
    template_dir = os.path.join(app_dir, 'templates')
    if os.path.isdir(template_dir):
        app_template_dirs.append(template_dir)

template_dirs = MAKO_TEMPLATE_DIRS
template_dirs += tuple(app_template_dirs)

MEDIA_ROOT = '/var/www/fc/uploaded_media/'
MEDIA_URL = '//media.flyingcolorsdance.com/'
