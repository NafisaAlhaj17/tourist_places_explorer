import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY: set via env on Render, fallback for local development
SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key-here')

DEBUG = os.getenv('DEBUG', 'True') == 'True'

# ALLOWED_HOSTS configuration
ALLOWED_HOSTS = ['localhost', '127.0.0.1']
# For production on Render - add your domain
if os.getenv('ALLOWED_HOSTS'):
    allowed = os.getenv('ALLOWED_HOSTS').split(',')
    ALLOWED_HOSTS.extend([host.strip() for host in allowed])

# Applications
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'places',
    'users',
    'contact',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # serve static
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'tourist_places_explorer.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'tourist_places_explorer.wsgi.application'
ASGI_APPLICATION = 'tourist_places_explorer.asgi.application'

# Database - SQLite for easy Render deployment
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Render deployment: use PostgreSQL if DATABASE_URL is set
try:
    import dj_database_url
    if 'DATABASE_URL' in os.environ:
        DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)
except ImportError:
    pass  # dj_database_url not installed, use default SQLite

# Password validation (default)
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True

# Static and Media
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'   # for collectstatic on Render
STATICFILES_DIRS = [BASE_DIR / 'static']

# WhiteNoise static files
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Login URLs
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# Email (development) - console backend. Configure for production via envs.
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
