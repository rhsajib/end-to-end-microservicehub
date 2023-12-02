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
    


class DbConfig(BaseSettings):
    DATABASE_ENGINE: str = os.environ.get('DATABASE_ENGINE')
    POSTGRES_DB: str = os.environ.get('POSTGRES_DB')
    POSTGRES_USER: str = os.environ.get('POSTGRES_USER')
    POSTGRES_PASSWORD: str = os.environ.get('POSTGRES_PASSWORD')
    # For docker, DB_HOST should be set to the service name defined in your docker-compose.yml
    DB_HOST: str =  os.environ.get('DB_HOST')
    DB_PORT: str = os.environ.get('PORT')

class CeleryConfig(BaseSettings):
    CELERY_BROKER_URL: str = os.environ.get('CELERY_BROKER')
    CELERY_RESULT_BACKEND: str = os.environ.get('CELERY_BACKEND')

    

# class EmailSettings(BaseSettings):
#     SENDER_EMAIL: str = os.environ.get('SENDER_EMAIL')
#     EMAIL_PASSWORD: str= os.environ.get('EMAIL_PASSWORD')

class CoreConfig(
    DbConfig, 
    CommonConfig, 
    CeleryConfig       
):
    model_config = SettingsConfigDict(case_sensitive=True)



config = CoreConfig()

