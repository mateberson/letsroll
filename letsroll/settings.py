"""
Django settings for letsroll project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ghu1&oq57a32a%qqn3lx!sv7df(!wt5q%r4x*+p#5o21l=ty4o'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    # django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    
    # allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    
    # crispy-forms
    'crispy_forms',
   
    # anymail
    'anymail',
    
    # local apps
    'core',
    'pages',
    'characterSheets',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'letsroll.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],   # na raiz do projeto, procura a pasta templates para buscar templates
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

WSGI_APPLICATION = 'letsroll.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# django-allauth

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 1
LOGIN_REDIRECT_URL = "/"
ACCOUNT_SESSION_REMEMBER = True


# Email

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"    # Quando um usuario se cadastrar, vou receber um email no console

"""
EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend" 
DEFAULT_FROM_EMAIL = "no-reply@meusite.com"
SERVER_MAIL = DEFAULT_FROM_EMAIL
ANYMAIL = {
    "MAILGUN_API_KEY": "ea5685f58293b1d9f2cfe15729930fe6-71b35d7e-19b2835b",
    "MAILGUN_SENDER_DOMAIN": "sandboxd8c156a8e13b4f788aff02304a860d6b.mailgun.org",
}
"""

ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True                          # por padrão o django pede pra colocar a senha pra se cadastrar 2 vezes
ACCOUNT_USERNAME_REQUIRED = True                                    # Não é necessario username
ACCOUNT_AUTHENTICATION_METHOD = "email"                             # metodo de autenticação = email
ACCOUNT_EMAIL_REQUIRED = True                                       # Por padrão é opcional
ACCOUNT_UNIQUE_EMAIL = True                                         # o Email tem que ser unico


# django-crispy-forms

CRISPY_TEMPLATE_PACK = "bootstrap4"