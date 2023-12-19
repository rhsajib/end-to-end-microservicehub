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
CORS_ORIGIN_ALLOW_ALL = True

WSGI_APPLICATION = 'core.wsgi.application'
ASGI_APPLICATION = 'core.asgi.application'

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('redis', 6379)],  # Adjust Redis server details as needed
        },
    },
}


# Application definition

INSTALLED_APPS = [
    'daphne',
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
    'file_convert',
    'chat'
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


# ref: https://testdriven.io/blog/storing-django-static-and-media-files-on-amazon-s3/

# Storage configuration
USE_S3 = 1
# USE_S3 = config.USE_S3

if USE_S3:
    # aws settings
    AWS_ACCESS_KEY_ID = config.S3_ACCESS_KEY
    AWS_SECRET_ACCESS_KEY = config.S3_SECRET_ACCESS_KEY
    AWS_STORAGE_BUCKET_NAME = config.S3_BUCKET_NAME
    AWS_DEFAULT_ACL = None
    AWS_S3_REGION_NAME = config.S3_REGION_NAME
    AWS_S3_FILE_OVERWRITE = False
    AWS_QUERYSTRING_AUTH = False
    # AWS_S3_VERIFY = True
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    AWS_S3_OBJECT_PARAMETERS = {
        'CacheControl': 'max-age=86400',
    }

    # In Amazon S3, objects (files) are versioned by default, 
    # and each new version is treated as a separate object. 
    # When we upload a file with the same key (path and filename) as an existing object, 
    # S3 creates a new version of that object instead of overwriting it. 
    # This is part of S3's versioning feature, which helps in preserving and 
    # managing different versions of the same object.
    # if we want to replace a file in database, it will be replaced in database
    # but in s3 bucker a new file will be stored with the same key with different version


    # s3 static settings
    AWS_STATIC_LOCATION = 'static'
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_STATIC_LOCATION}/'
    STATICFILES_STORAGE = 'core.storage_backends.StaticStorage'

    # s3 public media settings
    AWS_PUBLIC_MEDIA_LOCATION = 'media'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_PUBLIC_MEDIA_LOCATION}/'
    DEFAULT_FILE_STORAGE = 'core.storage_backends.PublicMediaStorage'

    # s3 private media settings
    AWS_PRIVATE_MEDIA_LOCATION = 'private'
    # PRIVATE_MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_PRIVATE_MEDIA_LOCATION}/'
    # PRIVATE_FILE_STORAGE = 'core.storage_backends.PrivateMediaStorage'

else:
    STATIC_URL = 'static/'
    STATIC_ROOT = BASE_DIR / 'static'
    MEDIA_URL = 'media/'    
    MEDIA_ROOT = BASE_DIR / 'media'
    DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'




# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field




# Celery Settings
CELERY_BROKER_URL = config.CELERY_BROKER_URL
CELERY_RESULT_BACKEND = config.CELERY_RESULT_BACKEND

# if CELERY_BROKER_URL:
#     print('*********************************************')
#     print('CELERY_BROKER_URL: ', CELERY_BROKER_URL)
#     print('*********************************************')
