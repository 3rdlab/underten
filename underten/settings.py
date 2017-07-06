
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))

SECRET_KEY = '1v&@t*6t=r+#6b*0d#s#qt2tat)vy@gu#96#yvaccfzkc$sr5q'

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
 
    'article',
    'account',
    'product',

    #for category_tree
    'mptt', #category tree
    'django_mptt_admin',
    'debug_toolbar', # django-debug-toolbar
    'django_summernote',   # WYSIWYG editor
    'crispy_forms', # crispy_form
    'endless_pagination', # endless pagination




)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'underten.urls'

WSGI_APPLICATION = 'underten.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
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

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
STATIC_URL = '/static/'

AUTH_PROFILE_MODULE = 'account.UserProfile'


STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    '/Volumes/BlackGround/dev/python/underten/underten/static',
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)



SUMMERNOTE_CONFIG = {
    'iframe': False,
    'lang': 'ko-KR',
    'inplacewidget_external_css': (                                             
        '//netdna.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap.min.css',      
        '//netdna.bootstrapcdn.com/font-awesome/4.0.3/css/font-awesome.min.css',
    ),                                                                          
    'inplacewidget_external_js': (                                              
        '//code.jquery.com/jquery-1.11.3.min.js',                                
        '//netdna.bootstrapcdn.com/bootstrap/3.1.1/js/bootstrap.min.js',        
    ),
}

CRISPY_TEMPLATE_PACK = 'bootstrap3'


# endless pagination

TEMPLATE_CONTEXT_PROCESSORS += (
    'django.core.context_processors.request',
)

ENDLESS_PAGINATION_PER_PAGE = 10



