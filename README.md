
## Project Documentation


### Title: End-to-End Python-Based Event-Driven Scalable Microservices

## Table of Contents

- [Project Documentation](#project-documentation)
  - [Title: End-to-End Python-Based Event-Driven Scalable Microservices](#title-end-to-end-python-based-event-driven-scalable-microservices)
- [Table of Contents](#table-of-contents)
- [Introduction](#introduction)
- [Microservices Breakdown](#microservices-breakdown)
  - [Frontend](#frontend)
  - [Main App](#main-app)
  - [Microservices](#microservices)
- [Technology Stack](#technology-stack)
- [Microservices Details](#microservices-details)
  - [1. Main App (Port 8000)](#1-main-app-port-8000)
    - [Users](#users)
    - [File Convert](#file-convert)
    - [Chat](#chat)
  - [2. File Convert Service (Port 8001)](#2-file-convert-service-port-8001)
  - [3. Chat Service (Port 8002)](#3-chat-service-port-8002)
- [Event-Driven Communication](#event-driven-communication)
- [Benefits of Event-Driven Architecture](#benefits-of-event-driven-architecture)
- [Challenges](#challenges)
  - [Overall Challenges](#overall-challenges)
  - [Specific Challenges by Microservice](#specific-challenges-by-microservice)
    - [1. Main App (Port 8000)](#1-main-app-port-8000-1)
    - [2. File Convert Service (Port 8001)](#2-file-convert-service-port-8001-1)
    - [3. Chat Service (Port 8002)](#3-chat-service-port-8002-1)
    - [Additional Difficulties](#additional-difficulties)
- [Conclusion](#conclusion)
- [Further Exploration](#further-exploration)
- [License](#license)

## Introduction

This section provides an overview of a project implementing an event-driven architecture with scalable microservices in Python. It's geared towards software developers interested in understanding the insights of implementing a robust and scalable system using microservices and an event-driven approach.

## Microservices Breakdown

The project comprises three distinct microservices:

### Frontend
- A single-page client-side application built with React, JavaScript, and other web technologies.
  
### Main App
- Powered by Django/Django REST Framework, serving as the central hub for orchestrating service calls, user management, and event production.
  
### Microservices
- **File Convert Service (Port 8001):**
  - Utilizing Django/DRF and third-party APIs, it converts uploaded files to desired formats and updates live status to the main app using Django Channels.
- **Chat Service (Port 8002):**
  - Leverages Django/DRF and Kafka, handling real-time chat communication, message storage, and interaction with the main app.

## Technology Stack

This project leverages a diverse set of technologies to achieve its functionality:

- **Frontend:** React, JavaScript, React Router, Motion, Single Page Application, Client-Side Authentication, WebSocket
- **Main App:** Django, Django Rest Framework, PostgreSQL, Django Channels, Celery, Redis, Kafka-Python, JWT Authentication, Email Verification, AWS S3 Bucket, Requests, Docker, Docker-Compose
- **File Convert Service:** Django, Django DRF, Redis, AWS S3, PostgreSQL Database, Celery, Integrating Third-Party API, Docker, Docker-Compose
- **Chat Service:** Django, Django DRF, Kafka, Kafka-Python, Django SQLite Default Database, Celery, Redis, Python Threading, Docker, Docker-Compose

## Microservices Details

### 1. Main App (Port 8000)

#### Users
- Sign up initiates a Celery task for email verification.
- JWT token creation for authentication.
- User profile updates stored in PostgreSQL and profile photos in AWS S3.

#### File Convert
- Upload triggers an API request to the main app, connecting through WebSocket.
- Live status updates using Django Channel Redis channel layers.

#### Chat
- New chat creation and continuation handled through WebSocket.
- Kafka used for event-driven communication.
- Broadcasting messages and updating the database through Kafka events.

### 2. File Convert Service (Port 8001)

- API requests forwarded from the main app.
- DRF API view for file saving to AWS S3.
- Celery task triggers file conversion using a third-party API.
- Real-time status updates using Django Channel Redis channel layers.

### 3. Chat Service (Port 8002)

- Asynchronous Kafka consumer for handling chat messages.
- DRF ModelViewSet for managing messages.
- Kafka events trigger Celery tasks for message saving to the database.

## Event-Driven Communication

The system relies on an event-driven approach for inter-service communication. Instead of direct API calls, microservices publish and subscribe to events on a Kafka message broker:

- **Main App:**
    - Publishes events for new chat messages, and user actions.
    - Subscribes to events from chat services for status updates and chat messages.
  
- **Chat Service:**
    - Subscribes to new chat message events from the main app.



<!-- * **Main App:**
    * Publishes events for file conversion requests, new chat messages, and user actions.
    * Subscribes to events from file convert and chat services for status updates and chat messages.
* **File Convert Service:**
    * Subscribes to file conversion events from the main app.
    * Publishes events with conversion progress and completion status.
* **Chat Service:**
    * Subscribes to new chat message events from the main app.
    * Publishes received messages to relevant chat rooms. -->



  
## Benefits of Event-Driven Architecture

Using an event-driven architecture offers several advantages:

- **Decoupling:** Microservices are loosely coupled, promoting independent development and deployment.
- **Scalability:** Services can be scaled independently based on workload.
- **Resilience:** Failure in one service doesn't disrupt others due to asynchronous communication.
- **Real-time communication:** Events enable instant reactions and updates across services.

## Challenges 

### Overall Challenges

- **Scaling with Docker Compose:** Creating separate Docker Compose files for each service while sharing Redis across them required implementing a common network, presenting some configuration challenges.
- **Event-Driven Architecture:** Utilizing Kafka for real-time communication was the most significant difficulty, involving:
    - Choosing between RabbitMQ and Kafka. 
    - Learning and implementing the event-driven approach.
    - Overcoming issues with initializing

 Kafka producer and consumer in both main app and chat service.
    - Connecting producers and consumers to the Kafka server in Docker containers.
    - Creating Kafka topics using Docker commands.

### Specific Challenges by Microservice

#### 1. Main App (Port 8000)

- **API Gateway for Chat and File Convert:** Creating an API gateway for these services initially proved challenging.
- **Connecting to Chat Service for Real-time Communication:**
    - Initial attempt using Django Channels failed due to limitations within the same application.
    - Websocket connection resulted in message loss during high-frequency client communication.
    - Implementing event-driven architecture with Kafka solved the communication problems.
- **Initializing Kafka Producer:** Initially struggled with proper initialization, solved by utilizing the Chat app's `app.py` file and initializing within `ChatAppConfig`'s `ready` method.

#### 2. File Convert Service (Port 8001)

- **Real-time Status Updates to Main App:** Initially faced difficulty sending updates using Django Channels or Websocket, but successfully used Redis Channels for efficient communication.

#### 3. Chat Service (Port 8002)

- **Connecting to Main App for Real-time Communication:**
    - Similar challenges as Main App: attempted Django Channels (unsuccessful), faced message loss with Websocket, solved with event-driven architecture using Kafka.
- **Kafka Consumer Initialization:** Initial synchronous approach triggered server hangs, solved by utilizing threading during server startup.

#### Additional Difficulties

- Choosing between Confluent Kafka and Python-Kafka libraries for producer/consumer initialization (settled on Python-Kafka for Docker compatibility).
- Understanding and configuring Kafka in Docker containers, involving port mapping and managing broker/zookeeper connection.

## Conclusion

This project demonstrates a well-designed event-driven microservices architecture using Python and relevant technologies. The approach promotes scalable, flexible, and fault-tolerant systems for modern software development.

## Further Exploration

This documentation provides a high-level overview. For deeper insights, consider exploring:

- Individual microservice architecture and codebases.
- Detailed API documentation for each service.
- Deployment scripts and Docker configurations.

 Feel free to ask any specific questions or request further details on any aspect of the project.

## License

This project is licensed under the [MIT License](LICENSE).


<!-- ## Conclusion

This project serves as a valuable resource for developers aiming to delve into event-driven architecture and microservices. The challenges encountered and solutions devised provide practical insights into creating scalable and robust systems. Understanding the nuances of Docker-Compose configurations and the intricacies of communication between microservices contributes to a well-rounded learning experience. -->


<!-- 
**Overall, your challenges reflect real-world difficulties faced by developers in modern web development. Successfully overcoming these hurdles demonstrates your learning agility, problem-solving skills, and ability to adapt to new technologies like event-driven architecture and Kafka. Highlighting these challenges in your project documentation makes it relatable and showcases your technical competency to potential employers or collaborators.

Overall, you successfully tackled a range of challenges related to microservices, real-time communication, and event-driven architecture. Highlighting these hurdles and your solutions demonstrates your problem-solving skills and technical competency, making your project even more impressive.**
 -->










