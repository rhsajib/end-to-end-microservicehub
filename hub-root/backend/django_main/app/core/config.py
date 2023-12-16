import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

# Load environment variables from the .env file in the current directory
load_dotenv()


class CommonConfig(BaseSettings):
    SECRET_KEY: str = os.environ.get('SECRET_KEY')
    DEBUG: str = os.environ.get('DEBUG')
    # ALLOWED_HOSTS: list = os.environ.get('ALLOWED_HOSTS', '').split(',')  # must be list or tuple  # ['host1', 'host2', 'host3']
    ALLOWED_HOSTS: list = ['*']


class AwsS3Config(BaseSettings):
    USE_S3: bool = os.environ.get('USE_S3') == 1
    S3_ACCESS_KEY: str =os.environ.get('S3_ACCESS_KEY')
    S3_SECRET_ACCESS_KEY: str = os.environ.get('S3_SECRET_ACCESS_KEY')
    S3_BUCKET_NAME: str = os.environ.get('S3_BUCKET_NAME')
    S3_REGION_NAME: str = os.environ.get('S3_REGION_NAME')


class DbConfig(BaseSettings):
    DATABASE_ENGINE: str = os.environ.get('DATABASE_ENGINE')
    POSTGRES_DB: str = os.environ.get('POSTGRES_DB')
    POSTGRES_USER: str = os.environ.get('POSTGRES_USER')
    POSTGRES_PASSWORD: str = os.environ.get('POSTGRES_PASSWORD')
    # For docker, DB_HOST should be set to the service name defined in your docker-compose.yml
    DB_HOST: str =  os.environ.get('DB_HOST')
    DB_PORT: str = os.environ.get('PORT')


class CeleryConfig(BaseSettings):
    CELERY_BROKER_URL: str = os.environ.get('CELERY_BROKER', 'redis://redis:6379/0')
    CELERY_RESULT_BACKEND: str  = os.environ.get('CELERY_BACKEND', 'redis://redis:6379/0')

class FileConvertServiceConfig(BaseSettings):
    FILE_CONVERT_SERVICE_BASE_URL: str = os.environ.get('FILE_CONVERT_SERVICE_BASE_URL')

class ChatServiceConfig(BaseSettings):
    CHAT_SERVICE_BASE_URL: str = os.environ.get('CHAT_SERVICE_BASE_URL')
    CHAT_SERVICE_BASE_WS: str = os.environ.get('CHAT_SERVICE_BASE_WS')

# class EmailSettings(BaseSettings):
#     SENDER_EMAIL: str = os.environ.get('SENDER_EMAIL')
#     EMAIL_PASSWORD: str= os.environ.get('EMAIL_PASSWORD')

class CoreConfig(
    CommonConfig, 
    AwsS3Config,
    DbConfig, 
    CeleryConfig,
    FileConvertServiceConfig,
    ChatServiceConfig,
):
    model_config = SettingsConfigDict(case_sensitive=True)



config = CoreConfig()

