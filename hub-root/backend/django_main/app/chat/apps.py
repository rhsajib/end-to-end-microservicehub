from django.apps import AppConfig


class ChatConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chat'

    def ready(self):
        # This method is called when Django starts.
        # You can initiate your Kafka producer here.
        # Importing here to avoid circular imports
        from .kafka_producers import Producer
        from .kafka_consumers import Consumer
        # Initialize the Kafka producer asynchronously
        # KafkaProducer.init()
        try:
            # bootstrap_servers = "kafka:29092"  # Replace with your actual IP
            # bootstrap_servers = "kafka"  # Replace with your actual IP
            print("initializing Kafka producer")
            Producer.init()
            print("initializing Kafka consumer")
            Consumer.init()
            # KafkaProducer.init(bootstrap_servers)
        except Exception as e:
            print(f"Error initializing Kafka: {e}")
