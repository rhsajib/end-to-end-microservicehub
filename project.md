### Modified by chat GPT
Project Title: End-to-End Python-Based Event-Driven Scalable Microservices

I have a frontend at port 8080, one main app at port 8000, and two microservices: a file convert service at port 8001 and a chat service at port 8002.

Frontend (Port 8080):
Technologies: React, JavaScript, React Router, Motion, Single Page Application, Client-Side Authentication, WebSocket

1. Main App (Port 8000):
Technologies: Django, Django Rest Framework, PostgreSQL, Django Channels, Celery, Redis, Kafka for producer of events, Kafka-Python, JWT Authentication, Email Verification, AWS S3 Bucket, Requests, Docker, Docker-Compose

Description: My Django main app has three apps - chat for the chat microservice, file_convert for file convert microservice, and users for user management.

Users:
When a client requests to sign up, the Django main app will receive the request and start a Celery task to send a verification email with an account activation link. If the user clicks the activation link, the account will be activated. Then, when the user tries to log in, the system will create a JWT token for authentication. The user can update their profile data and profile photo. The profile photo will be stored in AWS S3 bucket, and the data will be stored in the PostgreSQL database.

File Convert:
When a user clicks the upload button in the frontend to upload a file for conversion (e.g., doc to pdf, excel to pdf), it will create an API request to the Django main app and connect with the main app using WebSocket. The main app will use Django Channel Redis channel layers to connect with the frontend. The main app will forward the request to the file convert service (Port 8001).
File convert service (Port 8001) will update the live status of file conversion. Follow file convert service for the next steps.

Chat:
When a user clicks "new chat" in the frontend, a new chat ID will be created, and the user will be connected with the Django main app through WebSocket. Django will use Django Channels Redis channel layers to communicate with the frontend. Also, a producer will be initialized to produce events using Kafka.

If a chat exists previously, after clicking "continue chat" in the frontend, an API request will be sent to Django main app, and Django main app will forward the request to the chat service. Then, the chat service will give a response with all previous messages, and this response will be sent to the frontend. Frontend will show the previous messages, and they can start a conversation using WebSocket.

When a new message is sent from the frontend using WebSocket to Django main app, the main app will broadcast the messages to other clients connected to the specific chat room and also publish the new message event to a Kafka topic named `chat_service`. My chat service (Port 8002) will consume the events of `chat_service` topic to save it to the database. Follow chat service (Port 8002) for further steps.

Challenges:
As this is my first microservice project, I struggled a little bit to create an API gateway for my chat service and file convert service.

I faced a lot of challenges connecting my chat service to Django main app for real-time communication. At first, I tried to connect Django main app using my chat service Django channels. But later, I understood that Django channel can broadcast messages within the application and cannot broadcast to other separate ported applications.

Then, I used WebSocket to connect my Django main app to the chat service for real-time communication. But I faced another problem. When frontend clients frequently send messages to Django main app, and Django main app tries to send the messages to the chat service using WebSocket before broadcasting messages to clients, some messages get lost by the channel to be broadcasted to clients, which made me tensed. How can I solve the issue? Then I heard about the event-driven architecture, which is really cool and great, also satisfying.

I faced challenges initializing the producer in my Django main app. But I used the app.py file in the chat app inside Django main app for the initialization of the producer. I initialized the producer inside the ready method of the ChatAppConfig class for initializing the producer during starting the Django main app server.

I also faced challenges connecting my producer to the Kafka Docker container in the Docker Compose file using bootstrap servers as port mapping is crucial for connecting the producer with Kafka inside the container. As I was new to Kafka, I also faced challenges to create a Kafka topic using the docker exec command in the Bash shell.

2. File Convert Service (Port 8001):

Technologies:
Django, Django DRF, Redis, Django Channels, AWS S3, PostgreSQL Database, Celery, Integrating Third-Party API, Docker, Docker-Compose

Description:
When an API request is forwarded from Django main app to the file service, the file service will receive the request using DRF API view, and the file will be saved to the S3 bucket. Then, a Celery task will be triggered to convert the file to the desired format with file content. Meanwhile, the API view will call Django Redis channel layer and update the status of in-progress. This status will be received by Django main app channels and broadcasted the status to the frontend client. The frontend will update the status as in progress.

When the Celery task is triggered, Celery will use the file content and make a third-party API request to convert the file. When the conversion is finished or failed, the status will be sent to the main app using Django Redis channel layer. This status will be received by Django main app channels and broadcasted the status to the frontend client. Frontend will update the status, and the backend will create a link to download the converted file.

Challenges:
I was facing challenges sending the real-time status to Django main app and connecting my file service to Django main app using Django channels or WebSocket. But Django channel layers did it for me. I can call channel layers anytime instead of explicitly connecting my file convert service to Django main app through WebSocket or channels routing. This is amazing.

3. Chat Service (Port 8002):

Technologies: Django, Django DRF, Kafka, Kafka-Python, Django SQLite Default Database, Celery, Redis, Python Threading, Docker, Docker-Compose

Description:
When the chat service server starts, it will initiate the Kafka consumer asynchronously with the chat service application using Python threading. I used DRF ModelViewSet for getting all messages response. When a request comes to get all previous messages, DRF will give a response with all previous messages. Saving new messages is interesting. When Django main app Django channel receives a new message, it will publish the new message event using Kafka with a Kafka topic named `chat_service`. Then the event will be subscribed to in the chat service by the Kafka consumer with the `chat_service` topic name. After decoding the messages, the consumer will trigger a Celery task to save the messages to the database, and this process will be continued repeatedly for every newly created message.

Challenges:
I faced a lot of challenges connecting my chat service to Django main app for real-time communication. At first, I tried to connect my chat service to Django main app using Django channels. But later, I understood that Django channel can broadcast messages within the application and cannot broadcast to other separate ported applications.

Then, I used WebSocket to connect my Django main app to the chat

 service for real-time communication. But I faced another problem. When frontend clients frequently send messages to Django main app, and Django main app tries to send the messages to the chat service using WebSocket before broadcasting messages to clients, some messages get lost by the channel to be broadcasted to clients, which made me tensed. How can I solve the issue? Then I heard about the event-driven architecture, which is really cool and great, also satisfying.

I had two options to choose a message broker for the architecture - RabbitMQ and Kafka. But I studied that Kafka is suitable for a large amount of message delivery. That's why I chose Kafka.

Then I studied about the event-driven architecture using Kafka, but I faced difficulties in learning it. At first, I used Confluent Kafka for initializing producer and consumer. But I faced difficulties starting cp-kafka and cp-zookeeper in the Docker container as I faced an error (default replication factor 3, which is more than broker number 1 error). Then I studied a lot and also adjusted Docker Compose environment variables to solve the issue, but the issue persisted.

Then I shifted to Python-Kafka for initialization inside the application and wurstmeister/kafka and wurstmeister/zookeeper for broker and management, which did not cause any error to start in the Docker container.

Then I faced challenges initializing the producer in my Django main app. But I used the app.py file in the chat app inside Django main app for the initialization of the producer. I initialized the producer inside the ready method of ChatAppConfig class for initializing the producer during starting the Django main app server.

I also faced challenges connecting my producer to Kafka Docker container in Docker Compose file using bootstrap servers, as port mapping is crucial for connecting the producer with Kafka inside the container. As I was new to Kafka, I also faced challenges creating a Kafka topic using the docker exec command in the Bash shell.

When I successfully created a Kafka topic and integrated as well as initialized my producer in Django app and Docker container and published my messages to Kafka topic, a new challenge arose regarding integrating and initializing Kafka consumer in my chat service applications. I was able to integrate the consumer into the chat service application, but I struggled a lot to initialize it during the start of chat service Django application server. As I used synchronous Kafka library, when I initialized the consumer during the start of the server, my server got stuck because starting the consumer is an infinite process. Then I used threading to initialize the consumer during the start of my server, and finally, my application as well as the consumer ran successfully.

Overall Challenges:
I faced challenges regarding Docker-Compose running. As I wanted to scale the application, I used a separate Docker-Compose file for each. But Redis was used in Django main app, chat service, and file convert application. Creating a common network for the system and implementing it for all Docker-Compose files was a little challenging.

For me, the most challenging part of my project was using event-driven architecture. Configuring Kafka broker, initializing producer & consumer in Django main app and chat service accordingly, and connecting them with Kafka server was the most challenging part for me in this project.

### Raw text
project title: end to end python based event driven scalabe microservices

i have frontend at port 8080, 
one main app at port 8000, 
two microservices which are file convert service at port 8001 and chat service at port 8002.

frontend (port 8080): 
technologies: react, javascript, react router, motion, single page application, client side authentication, websocket

1. main app (port 8000): 
technologies: django, django rest framework, postgresql, django channels, celery, redis, kafka for producer of events, kafka-python, JWT authentication, email verification, aws s3 bucket, requests, docker, docker-compose

description: my django main app has 3 apps - chat for chat microservice, file_convert for file convert microservice, users for user management.

users:
when client request for sign up, django main app will get the request and start a celery task to send a verification email with an account activation link. if the user click the activation link, the account will be activated. then when the user will try to log in , system will create a JWT token for authentication. user can update his profile data and profile photo. profile photo will be stored AWS S3 bucket and data will be stored in postgresql database.

file_convert:
when user will click upload button in frontend to upload a file for conversion (doc to pdf, excel to pdf etc), it will create an api request to django main app and connected with the main app with websocket. main app will use django channel redis channel layes to connect with frontend. main app will forward the request to file convert service (port 8001).
file convert service (port 8001) will update the live status of file convertion. follow file convert service for next steps.

chat:
when user will click new chat in frontend,  a new chat id will be created and user will be connected with django main app through websocket. django will use django channels redis channel layers to communicate with frontend. also a producer will be initialized to produce events using kafka.

if a chat exists previously, after clicking the continue chat in frontend, an api request will be sent to django main app and django main app will forward request to chat service. then chat service will give response will all previous messages and this response will be sent to frontend. frontend will show the previous messages. the they can start conversation using websocket.

when a new message is sent from frontend using websocket to django main app, main app will broadcast the messages to other clients connected to the specific chat room and also publish the new message event to a  kafka topic named `chat_service`. and my chat service (port 8002) will consume the events of `chat_service`topic to save it to database. follow chat service (port 8002) for further steps.

Challenges:
As this is my first microservice project, i struggled a little bit to create api gateway for my chat service and file convert service. 

i faced a lot of challenges for connecting my chat service to django main app for real time communication. at first i tried to connect  django main app using to my chat service django channels. but later i understood that , django channel can broadcast messages within the application and can not broadcast to other separate ported application. 

then, i used websocket to connect my django main app to chat service to real time communicate. but i faced another problem. when frontend clients frequently send messages to django main app and django main app tries to send the messages to chat service using websocket before broadcasting messages to clients, some messages get lost by channel to be broadcasted to clients. which made me tensed, how can i solve the issue. then i heard about the event driven architecture which is really cool and great also satisfying. 

i faced challenges initialising the producer in my django main app. but i used  app.py file in chat app inside django main app for initialization of producer. i initialized the producer inside ready method of ChatAppConfig class for initializing the producer during starting the django main app server.

i also faced challenges to connect my producer to kafka docker container in docker compose file using bootstrap servers as port mapping is crucial for connecting the producer with kafka inside the container. as i was new in kafka, i also faced challenges to create kafka topic using docker exec command in bash shell.



2. file convert service (port 8001):

technologies: 
django, django DRF, redis, django channels, aws S3, postgresql database, celery, integrating third party api, docker, docker-compose

description: 
when a api request will be forwarded from django main app to file service, file service will receive the request using DRF api view and file will be saved to s3 bucket. then a celery task will be triggered to convert the file to desire format with file content. mean while api view will call django redis channel layer and update the status of in progress. this status will be received by django main app channels and broadcasted the status to the frontend client. frontend will update the status as in progress. 

when the celery task is triggered, celery will use the file content and make a third party api request to convert the file. when the conversion is finished or failed, the status will be sent to main app using django redis channel layer. this status will be received by django main app channels and broadcasted the status to the frontend client. frontend will update the status. backend will create a link to to download the converted file.

challenges: 
I was facing challenges to send the real time status to django main app and connect my file service to django main app using django channels or websocket. but django channel layers did it for me. i can call channel layres any time instead of explicitely connecting my file convert service to django main app through websocket or channels routing. this is amazing.


3. chat service (port 8002):

technologies: django, Django DRF, kafka, kafka-python, django sqlite default database, celery, redis, python threading, docker, docker-compose

description:
when the chat service server will start, it will initiate the kafka consumer asynchronously with chat service application using python threading.
i used DRF ModelViewset for get all messages response. when a request come to get all previous messages, DRF will give response will all previous messages. saving new messages is interesting. when django main app django channel will receive a new message it will publish the new message event using kafka with a  kafka topic named `chat_service`. then the event will be subscribed in chat service by kafka consumer with the `chat_service` topic name. then after decoding the messages, consumer will trigger celery task to save the messages to database. and this process will be continued repeatedly for every newly creaed messages.

challenges:
i faced a lot of challenges for connecting my chat service to django main app for real time communication. at first i tried to connect my chat service to django main app using django channels. but lated i understood that , django channel can broadcast messages within the application and can not broadcast to other separate ported application. 

then, i use websocket to connect my djngo main app to chat service to real time communicate. but i faced another problem. when frontend clients frequently send messages to django main app and django main app tries to send the messages to chat service using websocket before broadcasting messages to clients, some messages get lost by channel to be broadcasted to clients. which made me tensed, how can i solve the issue. then i heard about the event driven architecture which is really cool and great also satisfying. 

i had two options to choose message broker for the architecture- Rabbitmq and kafka. but i studied that kafka is suitable for large amount of messages delivery. thats why i choose kafka.

then i studied about the event driven architecture using kafka. but i faced difficulties to learn it. at first i used confluent kafka for initializing producer and consumer. but i faced difficulties to start cp-kafka and cp-zookeeper in docker container as i faced an error ( default replication factor 3 which is more then broker number 1 error). then i studied a lot and also adjusted docker comopse environment variables to solve the issue but the issue persisted. 

then i shifted to python-kafka for initialization inside the application and  wurstmeister/kafka and wurstmeister/zookeeper for broker and management which did not cause any error to start in docker container.

then i faced challenges initialising the producer in my django main app. but i used  app.py file in chat app inside django main app for initialization of producer. i initialized the producer inside ready method of ChatAppConfig class for initializing the producer during starting the django main app server.

i also faced challenges to connect my producer to kafka docker container in docker compose file using bootstrap servers as port mapping is crucial for connecting the producer with kafka inside the container. as i was new in kafka, i also faced challenges to create kafka topic using docker exec command in bash shell.

when i successfully created kfka topic  and intigrated as well as initialized my producer in django app and docker container and published my messages to kafka topic, a new challenge arose regarding integrating and initialising kafka consumer in my chat service applications. i was able to integrate the consumer in chat service application but i struggled a lot to initializing it during the start of chat service django application server. as i used synchronous kafka library, when i initialized the consumer during staring of server, my server got stuck because starting the consumer is an infinite process. then i used threading to initialize the consumer during start of my server and finally my application as well as consumer run successfully.



Overall challenges:
I faced challenges regarding docker-compose running. As i wanted to scale the application, i used separate docker-compose file for each. but redis was used in django main app, chat service, and file convert application. creating a common network for the system and implementing it for all docker-compose file was a little challenging.

for me, the most challenging part of my project was to used event driven architecture. Configuring kafka broker, initializing producer & consumer in django main app and chat service accordingly and connecting them with kafka server was the most challenging part for me in this project.















