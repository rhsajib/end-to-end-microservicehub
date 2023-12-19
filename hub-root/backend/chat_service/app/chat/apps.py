# chat/apps.py
from django.apps import AppConfig
from threading import Thread

class ChatConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chat'

    def ready(self):
        # from django.core import management

        # try:
        #     print("Initializing Kafka consumer asynchronously")
        #     Thread(target=management.call_command, args=('init_kafka_consumer',)).start()
        # except Exception as e:
        #     print(f"Error initializing Kafka: {e}")

        from .consumers import Consumer
        
        try:
            print("Initializing Kafka consumer asynchronously")
            Thread(target=Consumer.init).start()
        except Exception as e:
            print(f"Error initializing Kafka: {e}")

