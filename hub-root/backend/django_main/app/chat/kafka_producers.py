#  doc: https://docs.confluent.io/kafka-clients/python/current/overview.html#ak-producer
# https://developer.confluent.io/get-started/python/?_ga=2.226162398.593537590.1702808277-378950156.1702808277&_gl=1*fsmwfs*_ga*Mzc4OTUwMTU2LjE3MDI4MDgyNzc.*_ga_D2D3EGKSGD*MTcwMjgwODI3Ni4xLjEuMTcwMjgwODM4MS4zNS4wLjA.#introduction
# https://developer.confluent.io/get-started/python/?_ga=2.226162398.593537590.1702808277-378950156.1702808277&_gl=1*fsmwfs*_ga*Mzc4OTUwMTU2LjE3MDI4MDgyNzc.*_ga_D2D3EGKSGD*MTcwMjgwODI3Ni4xLjEuMTcwMjgwODM4MS4zNS4wLjA.#where-next
# https://www.confluent.io/en-gb/blog/event-driven-microservices-with-python-and-kafka/?session_ref=https://docs.confluent.io/&_gl=1*16rmq2t*_ga*Mzc4OTUwMTU2LjE3MDI4MDgyNzc.*_ga_D2D3EGKSGD*MTcwMjgxMTY4MC4yLjEuMTcwMjgxMjAxMi4zNC4wLjA.&_ga=2.217881554.593537590.1702808277-378950156.1702808277
# https://github.com/confluentinc/demo-scene/tree/master/python-microservices
# https://blog.devops.dev/building-scalable-microservices-with-django-and-apache-kafka-ab2a13b654ed


import json
from kafka import KafkaProducer
from kafka.errors import KafkaError


CHAT_SERVICE_TOPIC = "chat_service"

class Producer:
    _producer = None  # Class variable to hold the producer instance

    @classmethod
    def init(cls):
        try:
            cls._producer = KafkaProducer(bootstrap_servers=["kafka:29092"])
            print('Producer initialized successfully')

        except KafkaError as e:
            print(f"Error initializing producer: {e}")

    # @classmethod
    # def close(cls):
    #     # Close the producer and commit any pending transactions
    #     # cls._producer.flush()
    #     # await cls._producer.commit_transactions()
    #     # cls._producer = None
    #     if cls._producer:
    #         cls._producer.flush()
    #         cls._producer = None
    #         print('Producer closed successfully')

    @classmethod
    def publish_chat_event(cls, event_data):
        if cls._producer:
            try:
                cls._producer.send(
                    CHAT_SERVICE_TOPIC, 
                    key=b'new_message', 
                    value=json.dumps(event_data).encode("utf-8"))
                
                print('Message published successfully')

            except KafkaError as e:
                print(f"Error publishing message: {e}")
        else:
            print('Producer not initialized. Call init() first.')


# Usage example (not relevant with AppConfig approach)

# event_data = json.dumps({"sender": "John", "message": "Hello everyone!"})
# await KafkaProducer.publish_chat_event(event_data)
