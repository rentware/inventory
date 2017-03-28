"""
Django settings for rentWare project.

Generated by 'django-admin startproject' using Django 1.9.9.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qszjc%jfu$^5)f)m^)(t4po*z56f(rwx+cx0culn&9q%$ctns+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', '.pythonanywhere.com']


LOGIN_REDIRECT_URL = '/'

#ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'

#ACCOUNT_USERNAME_REQUIRED = True
#ACCOUNT_EMAIL_VERIFICATION = "none"
#SOCIALACCOUNT_QUERY_EMAIL = True
#LOGIN_REDIRECT_URL = "/"

#import smptlib
#s=smtplib.SMTP("smtp.gmail.com", 465)
#s.ehlo()
#s.starttls()
#s.login("email@gmail.com", "password")

#EMAIL_USE_SSL = False

#START_TTLS = True
#EMAIL_HOST = 'smtp.migadu.com'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
#EMAIL_HOST_USER = "piet@nix64bit.com"
EMAIL_HOST_USER = 'peterretief@gmail.com'
EMAIL_USE_TLS = True
EMAIL_HOST_PASSWORD = "peter@password3"

#LATEST SecurityMiddleware
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True

ACCOUNT_SIGNUP_FORM_CLASS = 'rentWareApp.forms.SignupForm'

STRIPE_SECRET_KEY = os.environ.get(
    "STRIPE_SECRET_KEY",
    "sk_test_uVG2ppVI32ZekMsQrJEbIUmR"
)
STRIPE_PUBLIC_KEY = os.environ.get(
    "STRIPE_PUBLIC_KEY",
    "pk_test_yaS9Qi1ZlV3Ag2Wwj4sa6AKj",
    )

INSTALLED_APPS = [
#    'allauth',
#    'allauth.account',
#    'allauth.socialaccount',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rentWareApp',
    #'sales',
    # The Django sites framework is required
    'django.contrib.sites',

#    'allauth.socialaccount.providers.stripe',
#    'allauth.socialaccount.providers.google',
#    "django_forms_bootstrap",
#    'payments',
#    "payments.multipayments",
    'stdimage',
#    'django_bootstrap_breadcrumbs',
#    'django_ajax',
#    'bootstrap3_datetime',
#    'bootstrap3',
#    'bootstrap3_datetime',
    'allauth',
    'allauth.account'
]

SITE_ID = 1

SOCIALACCOUNT_PROVIDERS = \
    {'google':
        {'SCOPE': ['profile', 'email'],
        'AUTH_PARAMS': {'access_type': 'online'}}}

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
#    'breadcrumbs.middleware.BreadcrumbsMiddleware',
]

ROOT_URLCONF = 'rentWare.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
#                'breadcrumbs.middleware.BreadcrumbsMiddleware',
              #  'payments.context_processors.payments_settings',
              #  "payments.multipayments.context_processors.settings",
            ],
        },
    },
]

#addede peter

#PAYMENTS_PLANS = {
#    "monthly": {
#        "stripe_plan_id": "pro-monthly",
#        "name": "Web App Pro ($25/month)",
#        "description": "The monthly subscription plan to WebApp",
#        "price": 25,
#        "interval": "month"
#    },
#    "yearly": {
#        "stripe_plan_id": "pro-yearly",
#        "name": "Web App Pro ($199/year)",
#        "description": "The annual subscription plan to WebApp",
#        "price": 199,
#        "interval": "year"
#    }
#}


AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)


WSGI_APPLICATION = 'rentWare.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbname',
        'USER': 'dbuser',
        'PASSWORD': 'peter@password',
        'HOST': 'localhost',
        'PORT': ''
    }
}
"""


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.'
        'UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
        'MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
        'CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
        'NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

#TIME_ZONE = 'UTC'
TIME_ZONE = 'Africa/Johannesburg'

USE_I18N = True

USE_L10N = True

USE_TZ = True


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
