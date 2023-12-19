from celery import shared_task
from .models import Message


@shared_task
def process_kafka_message(key, data):
    """
    Processes a received Kafka message and saves it as a Message model.
    """
    print(f'\nMessage key:{key}')
    print(f"Received message: {data}")

    sender = data.get("sender")
    message_text = data.get("message")

    if sender and message_text:
        Message.objects.create(sender=sender, message=message_text)

@shared_task
def handle_message_error(message, exc_info):
    """
    Handles any errors during message processing.
    """
    print(f"Error processing message: {exc_info}")


