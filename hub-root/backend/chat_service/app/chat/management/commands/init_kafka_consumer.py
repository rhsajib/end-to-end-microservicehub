# chat/management/commands/init_kafka_consumer.py
from django.core.management.base import BaseCommand
from chat.consumers import Consumer

class Command(BaseCommand):
    help = 'Initialize Kafka consumer'

    def handle(self, *args, **options):
        try:
            print("Initializing Kafka consumer")
            Consumer.init()
            self.stdout.write(self.style.SUCCESS('Kafka consumer initialized successfully'))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Error initializing Kafka: {e}"))
