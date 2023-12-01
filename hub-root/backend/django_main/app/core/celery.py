import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery(
    'core',
    broker_connection_retry_on_startup=True,
) 

app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks(['task_manager'])
# app.autodiscover_tasks()

@app.task
def add_number():
    return


