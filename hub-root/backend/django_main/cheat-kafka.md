### Confluent kafka

#### ref

##### microservices
- https://dev.to/paurakhsharma/microservice-in-python-using-fastapi-24cc
- https://blog.devops.dev/building-scalable-microservices-with-django-and-apache-kafka-ab2a13b654ed
  
- https://www.confluent.io/en-gb/blog/event-driven-microservices-with-python-and-kafka/?session_ref=https://docs.confluent.io/&_gl=1*16rmq2t*_ga*Mzc4OTUwMTU2LjE3MDI4MDgyNzc.*_ga_D2D3EGKSGD*MTcwMjgxMTY4MC4yLjEuMTcwMjgxMjAxMi4zNC4wLjA.&_ga=2.217881554.593537590.1702808277-378950156.1702808277
  
- https://github.com/confluentinc/demo-scene/tree/master/python-microservices
  


##### Kafka
- https://www.baeldung.com/ops/kafka-new-topic-docker-compose
- https://python.plainenglish.io/microservices-in-python-kafka-and-django-c4e4fc83b7ef
- https://github.com/confluentinc/confluent-kafka-python/issues/184
  
- https://www.confluent.io/blog/tag/python/

- doc: https://docs.confluent.io/kafka-clients/python/current/overview.html#ak-producer
  
- https://developer.confluent.io/get-started/python/?_ga=2.226162398.593537590.1702808277-378950156.1702808277&_gl=1*fsmwfs*_ga*Mzc4OTUwMTU2LjE3MDI4MDgyNzc.*_ga_D2D3EGKSGD*MTcwMjgwODI3Ni4xLjEuMTcwMjgwODM4MS4zNS4wLjA.#introduction
  
- https://developer.confluent.io/get-started/python/?_ga=2.226162398.593537590.1702808277-378950156.1702808277&_gl=1*fsmwfs*_ga*Mzc4OTUwMTU2LjE3MDI4MDgyNzc.*_ga_D2D3EGKSGD*MTcwMjgwODI3Ni4xLjEuMTcwMjgwODM4MS4zNS4wLjA.#where-next

- https://www.confluent.io/en-gb/blog/event-driven-microservices-with-python-and-kafka/?session_ref=https://docs.confluent.io/&_gl=1*16rmq2t*_ga*Mzc4OTUwMTU2LjE3MDI4MDgyNzc.*_ga_D2D3EGKSGD*MTcwMjgxMTY4MC4yLjEuMTcwMjgxMjAxMi4zNC4wLjA.&_ga=2.217881554.593537590.1702808277-378950156.1702808277

#### docker-compose file


// create topic name
- docker exec -it kafka kafka-topics --create --topic chat_service --partitions 1 --replication-factor 1 --bootstrap-server localhost:9092
- docker exec -it kafka kafka-topics --create --topic chat_service --partitions 1 --replication-factor 1 --bootstrap-server kafka:29092
- docker exec -it kafka kafka-topics --create --zookeeper:2181 --partitions 1 --replication-factor 1 --topic test_topic

Remove Kafka and Zookeeper Data:
rm -rf kafka-data zookeeper-data

  
#### These are inside kafka shell
kafka-topics --bootstrap-server kafka:29092 --list
kafka-topics --bootstrap-server localhost:9092 --list
kafka-topics --bootstrap-server kafka:29092 --delete --topic chat_service




```
version: '3.9'

services:
  django-main:
    container_name: django-main
    build:
      context: ./app
      dockerfile: Dockerfile
    ports:
      - 8000:8000
    networks:
      - common_network
    environment:
      - DB_HOST=db
      - CHAT_SERVICE_BASE_URL=http://chat-service:8002
    env_file:
      - ./app/.env
    volumes:
      - ./app/:/usr/src/app/
    depends_on:
      - kafka
      - db
      - redis
    # command: ["./wait-for-kafka.sh", "kafka:9092", "--", "python", "manage.py", "runserver", "0.0.0.0:8000"]
    command: python manage.py runserver 0.0.0.0:8000

  db:
    restart: always
    image: "postgres:15"
    environment:
      - POSTGRES_HOST_AUTH_METHOD=trust
      - POSTGRES_DB=django-main
    env_file:
      - ./app/.env
    volumes:
      - ./postgres_data:/var/lib/postgresql/data/
    ports:
      - 5432:5432
    networks:
      - common_network
  
  redis:
    container_name: redis
    image: "redis"
    ports:
      - 6379:6379
    networks:
      - common_network

  kafka:
    image: confluentinc/cp-kafka:latest
    hostname: kafka
    container_name: kafka
    networks:
      - common_network
    restart: always
    environment:
 
      KAFKA_BROKER_ID: 1
      # KAFKA_REPLICATION_FACTOR: 1
      KAFKA_ADVERTISED_HOST_NAME: kafka
      KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181

      KAFKA_LISTENERS: PLAINTEXT://0.0.0.0:29092,PLAINTEXT_HOST://0.0.0.0:9092
      KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://kafka:29092,PLAINTEXT_HOST://localhost:9092
      # KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://:29092,PLAINTEXT_HOST://:9092
      KAFKA_LISTENER_SECURITY_PROTOCOL_MAP: PLAINTEXT:PLAINTEXT,PLAINTEXT_HOST:PLAINTEXT
      KAFKA_INTER_BROKER_LISTENER_NAME: PLAINTEXT
      # KAFKA_LISTENERS: INSIDE://0.0.0.0:9093,OUTSIDE://0.0.0.0:9092
      # KAFKA_ADVERTISED_LISTENERS: INSIDE://kafka:9093,OUTSIDE://localhost:9092
      # KAFKA_LISTENER_SECURITY_PROTOCOL_MAP: INSIDE:PLAINTEXT,OUTSIDE:PLAINTEXT
      # KAFKA_INTER_BROKER_LISTENER_NAME: INSIDE
      # KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181

      KAFKA_CONFLUENT_TOPIC_REPLICATION_FACTOR: 1
      KAFKA_CONSUMER_OFFSETS_REPLICATION_FACTOR: 1
      KAFKA_AUTO_CREATE_TOPICS_ENABLE: "false"
      # KAFKA_GROUP_INITIAL_REBALANCE_DELAY_MS: 0
      # KAFKA_CONFLUENT_LICENSE_TOPIC_REPLICATION_FACTOR: 1
      # KAFKA_CONFLUENT_BALANCER_TOPIC_REPLICATION_FACTOR: 1
      # KAFKA_TRANSACTION_STATE_LOG_MIN_ISR: 1
      # KAFKA_TRANSACTION_STATE_LOG_REPLICATION_FACTOR: 1

      # avoid the following error inside kafka container by setting the next 4 env vars
      # kafka connect exception, Replication factor: 3 larger than available brokers: 1
      # ref: https://stackoverflow.com/questions/62525026/kafka-connect-exception-replication-factor-3-larger-than-available-brokers-1
      # CONNECT_CONFIG_TOPIC_REPLICATION_FACTOR: 1
      # CONNECT_CONFIG_STORAGE_REPLICATION_FACTOR: 1
      CONNECT_OFFSETS_TOPIC_REPLICATION_FACTOR: 1
      # CONNECT_OFFSET_STORAGE_REPLICATION_FACTOR: 1
      # CONNECT_STATUS_STORAGE_REPLICATION_FACTOR: 1
      # CONNECT_CONFLUENT_TOPIC_REPLICATION_FACTOR: 1

      # if we set same port of KAFKA_ADVERTISED_LISTENERS
      # java.lang.IllegalArgumentException: requirement failed: Each listener must have a different port, listeners: PLAINTEXT://0.0.0.0:9092,PLAINTEXT_HOST://0.0.0.0:9092
      
      # it will create kafka topic automatically 
      # otherwise we will need to create topic manually by using the following command
      # docker exec -it kafka kafka-topics --create --topic your_topic_name --partitions 1 --replication-factor 1 --bootstrap-server kafka:29092
      # KAFKA_AUTO_CREATE_TOPICS_ENABLE: "false"

      # If you are creating topics explicitly using kafka-topics.sh, you can exclude internal topics by using the --exclude-internal option:
      # kafka-topics --create --topic your_topic --partitions 1 --replication-factor 1 --bootstrap-server kafka:29092 --exclude-internal
      # The --exclude-internal flag ensures that internal topics are not created manually.

      #  Kafka to be accessible at PLAINTEXT://kafka:29092 within the Docker network 
      # and PLAINTEXT_HOST://kafka:9092 from the host machine. 
      # Therefore, the bootstrap server for your Django service (producer) should be kafka:29092.


     
      # In a typical Kafka deployment, Zookeeper is used for coordination among the Kafka brokers and maintaining metadata. 
      # The --bootstrap-server option specifies the Kafka broker that should be contacted to create the topic.

      # To clarify:

      # Zookeeper:

      # Used for coordination among Kafka brokers.
      # Manages distributed brokers and maintains metadata.
      # Used less in newer Kafka versions, as more metadata management has moved to Kafka itself.

      # Bootstrap Server:

      # Specifies the initial broker that a Kafka client (e.g., kafka-topics command) connects to.
      # Provides the connection information for the client to discover other brokers and communicate with the Kafka cluster.

      # To summarize, 
      # both Zookeeper and the Kafka broker are essential components of a Kafka cluster, 
      # and they serve different purposes. Zookeeper helps manage the Kafka cluster, 
      # while the Kafka broker handles the actual communication and data storage. 
      # The --bootstrap-server option is used to specify the broker to which a Kafka client connects.
     
      
      

    ports:
      - 9092:9092
    # volumes:
    #   - ./bitnami/kafka:/bitnami/kafka
    depends_on:
      - zookeeper
    
  
  zookeeper:
    image: confluentinc/cp-zookeeper:latest
    container_name: zookeeper
    environment:
      ZOOKEEPER_CLIENT_PORT: 2181
      ZOOKEEPER_TICK_TIME: 2000
      ALLOW_ANONYMOUS_LOGIN: yes
    ports:
      - 2181:2181
    # volumes:
    #   - ./bitnami/zookeeper:/bitnami/zookeeper
    networks:
      - common_network

volumes:
  postgres_data:

networks:
  common_network:
    external: true

```