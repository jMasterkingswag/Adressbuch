"""
Django settings for adressdatenbank project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'odj8+_t4k5ut+7942&6y)rnt_&lyo8@b(5+9-++geop#08(wv-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

THIRD_PARTY_APPS = (
	'registration', # django-registration-redux 1.1
)

# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	'myapp',
) 

INSTALLED_APPS = INSTALLED_APPS + THIRD_PARTY_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'adressdatenbank.urls'

WSGI_APPLICATION = 'adressdatenbank.wsgi.application'


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




# Erzeuge dynamischen Pfad zum Templates-Ordner
TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates')
# Fuege ihn zur Templates Liste hinzu
TEMPLATE_DIRS = (
	TEMPLATE_PATH,
)

STATIC_PATH = os.path.join(BASE_DIR, 'static')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_URL = '/static/'

STATICFILES_DIRS = (
	STATIC_PATH,
)

# Redirect Users who are not logged in there
LOGIN_URL = '/accounts/login/'

REGISTRATION_OPEN = True                	# If True, users can register
ACCOUNT_ACTIVATION_DAYS = 7     		# One-week activation window; you may, of course, use a different value.
REGISTRATION_AUTO_LOGIN = True  		# If True, the user will be automatically logged in.
LOGIN_REDIRECT_URL = '/myapp/'  			# The page you want users to arrive at after they successful log in
LOGIN_URL = '/accounts/login/'  				# The page users are directed to if they are not logged in,
                                                            