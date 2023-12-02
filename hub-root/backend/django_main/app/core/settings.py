from pathlib import Path
from core.config import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/


SECRET_KEY = config.SECRET_KEY
DEBUG = config.DEBUG
ALLOWED_HOSTS = config.ALLOWED_HOSTS
ROOT_URLCONF = 'core.urls'
WSGI_APPLICATION = 'core.wsgi.application'
CORS_ORIGIN_ALLOW_ALL = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # packagesa
    'corsheaders',
    'rest_framework',
    'drf_yasg',

    # apps
    'users',

]


MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


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



# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': config.DATABASE_ENGINE,
        'NAME': config.POSTGRES_DB,
        'USER': config.POSTGRES_USER,
        'PASSWORD': config.POSTGRES_PASSWORD,
        'HOST': config.DB_HOST,            # It should be set to the service name defined in your docker-compose.yml
        'PORT': config.DB_PORT,       
    }
}





# if DATABASES['default']['HOST']:
#     print('*********************************************')
#     print('HOST: ', DATABASES['default']['HOST'])
#     print('*********************************************')


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators
# https://www.youtube.com/watch?v=-mEICwwmtjw&ab_channel=VeryAcademy

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        'OPTIONS':{
            'user_attributes':(
                'username', 'email', 'first_name', 'last_name'
            ),
            'max_similarity': 0.5
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS':{
            'min_length': 6,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


AUTH_USER_MODEL = 'users.User'

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Media settings
MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = 'media/'


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



# Celery Settings
CELERY_BROKER_URL = config.CELERY_BROKER_URL
CELERY_RESULT_BACKEND = config.CELERY_RESULT_BACKEND

# if CELERY_BROKER_URL:
#     print('*********************************************')
#     print('CELERY_BROKER_URL: ', CELERY_BROKER_URL)
#     print('*********************************************')