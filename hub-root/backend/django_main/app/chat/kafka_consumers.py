import json
from time import time
from kafka import KafkaConsumer
from kafka.errors import KafkaError

class Consumer:
    _consumer = None  # Class variable to hold the consumer instance

    @classmethod
    def init(cls):
        try:    
            cls._consumer = KafkaConsumer(
                bootstrap_servers=['kafka:29092'],
                group_id="my_consumer_group",
                auto_offset_reset='earliest'
            )
            # cls._consumer.subscribe(["chat_service"])
            print('Consumer initialized successfully')
           

        except KafkaError as e:
            print(f"Error initializing consumer: {e}")


    # @classmethod
    # def close(cls):
    #     if cls._consumer:
    #         cls._consumer.close()
    #         cls._consumer = None
    #         print('Consumer closed successfully')

    @classmethod
    def consume_messages(cls):
        if cls._consumer:
            cls._consumer.subscribe(["chat_service"])

            tick = time()                  
            for msg in cls._consumer:
                if time()-tick > 10:
                    print('Time out')
                    break
                try:
                    if msg is None:
                        continue

                    print(f'key: {msg.key}')
                    data = json.loads(msg.value)
                    print(f"Received message: {data}")

                    # Process the consumed message
                
                    # msg = cls._consumer.poll(timeout=1000)  # Timeout in milliseconds
                    
                    # if msg.error():
                    #     if msg.error().code() == KafkaError._PARTITION_EOF:
                    #         # End of partition event, not an error
                    #         print('Reached end of partition')
                    #         continue
                    #     print(f"Error consuming message: {msg.error()}")
                    #     running = False  # Stop the loop on error
                    #     continue
                    # break
                except KafkaError as e:
                    pass
                # finally:
                #     cls.close()
        else:
            print('Consumer not initialized. Call init() first.')

    # @classmethod
    # def consume_messages(cls):
    #     if cls._consumer:
    #         try:
    #             while True:
    #                 msg = cls._consumer.poll(timeout=1.0)  # Timeout in milliseconds
    #                 # msg = cls._consumer.poll(timeout=1000)  # Timeout in milliseconds
    #                 if msg is None:
    #                     continue
    #                 if msg.error():
    #                     if msg.error().code() == KafkaError._PARTITION_EOF:
    #                         # End of partition event, not an error
    #                         continue
    #                     else:
    #                         print(f"Error consuming message: {msg.error()}")
    #                         break

    #                 # Process the consumed message
    #                 value = msg.value().decode('utf-8')
    #                 print(f"Received message: {value}")

    #         except KeyboardInterrupt:
    #             pass
    #         finally:
    #             cls.close()
    #     else:
    #         print('Consumer not initialized. Call init() first.')

# Usage example
# KafkaConsumer.init()
# KafkaConsumer.consume_messages()
# KafkaConsumer.close()



