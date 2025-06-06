import os
from pathlib import Path
from decouple import config
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-uqmkdb4p7y7#%b17v293ol-^8rldh07741p&^648_u!p!8e2jl'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")

GOOGLE_RECAPTCHA_SECRET_KEY = config("CAPTCHA")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='127.0.0.1').split(',')
SILENCED_SYSTEM_CHECKS = ['captcha.recaptcha_test_key_error']

# Email settings
EMAIL_BACKEND = config("EMAIL_BACKEND")
EMAIL_HOST = config("EMAIL_HOST")
EMAIL_PORT = config("EMAIL_PORT")
EMAIL_USE_TLS = config("EMAIL_USE_TLS")
EMAIL_HOST_USER = config("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")
CONTACT_EMAIL = config("EMAIL_HOST_USER")


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'parler',
    'django_ckeditor_5',
    'captcha',
    'errors',
    'branding',
    'hotel',
    'home',
    'booking',
    'transportation',
    'meals',
    'grooming',
    'training',
    'water_sports',
    'contact',
    'about',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    } if DEBUG else {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config("DB_NAME"),
        'USER': config("DB_USER"),
        'PASSWORD': config("DB_PASSWORD"),
        'HOST': config("DB_HOST", "localhost"),
        'PORT': config("DB_PORT", "5432"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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


CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': [
            'heading', '|', 'bold', 'italic', 'underline', 'strikethrough', 'highlight', '|',
            'link', 'removeFormat', '|',
            'bulletedList', 'numberedList', '|', 'blockQuote', 'codeBlock', '|',
            'fontColor', 'fontSize', '|', 'insertTable', 'imageUpload', '|', 'fullscreen'
        ],
        'codeBlock': {
            'languages': [
                {'language': 'javascript', 'label': 'JavaScript'},
                {'language': 'python', 'label': 'Python'},
                {'language': 'bash', 'label': 'Bash'},
                {'language': 'nginx', 'label': 'Nginx'},
                {'language': 'html', 'label': 'HTML'},
                {'language': 'css', 'label': 'CSS'}
            ],
        },
    },
}


# Internationalization

PARLER_LANGUAGES = {
    None: (
        {'code': 'en', 'name': 'English'},
        {'code': 'th', 'name': 'Thai'},
        {'code': 'zh', 'name': 'Chinese'},
        {'code': 'km', 'name': 'Khmer'},
        {'code': 'ru', 'name': 'Russian'},
        # Add other languages as needed
    ),
    'default': {
        'fallbacks': ['en'],  # Language fallbacks (optional)
        'hide_untranslated': False,
    }
}

# set languages
LANGUAGES = [
    ('en', 'English'),
    ('th', 'Thai'),
    ('zh', 'Chinese'),
    ('km', 'Khmer'),
    ('ru', 'Russian'),
    # Add other languages as needed
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
USE_L10N = True

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

# Static & Media Files
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
