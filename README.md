# End-to-End Microservice Project

Welcome to the End-to-End Microservice project repository. This project showcases a sophisticated microservices architecture, encompassing a Django main app, real-time chat service, file conversion service, and a dynamic React frontend.

## Table of Contents
- [End-to-End Microservice Project](#end-to-end-microservice-project)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Technologies](#technologies)
  - [Microservices](#microservices)
    - [Chat Service](#chat-service)
    - [File Convert Service](#file-convert-service)
  - [Django Main App](#django-main-app)
  - [Setup](#setup)
  - [Usage](#usage)
  - [Docker](#docker)
  - [Contributing](#contributing)
  - [License](#license)

## Overview

The End-to-End Microservice project exemplifies a scalable and modular microservices architecture, integrating real-time chat, file processing, and a dynamic React frontend. Key features include:

- Real-time chat using WebSocket technology.
- File upload and processing with real-time status updates.
- Integration with AWS S3 for media file storage.
- Use of Django Channels for WebSocket communication.
- Integration with third-party APIs for document conversion.
- Asynchronous task processing with Celery and Redis.
- Microservices deployed on independent servers.

## Technologies

- **Backend:** Django, Django Channels, Django Rest Framework, PostgreSQL, Celery, Redis
- **Frontend:** React
- **Cloud:** AWS (S3)
- **Database:** PostgreSQL
- **Message Broker:** Redis
- **Development:** Docker

## Microservices

### Chat Service

The chat service handles real-time chat functionality, leveraging Django Channels for WebSocket communication. Messages are stored in a PostgreSQL database using Django Rest Framework.

**Features:**
1. **Real-time Chat Functionality:**
   - Implements real-time chat functionality using WebSocket technology.

2. **Django Channels Integration:**
   - Utilizes Django Channels to handle WebSocket communication seamlessly.

3. **Database Storage:**
   - Stores chat messages in a PostgreSQL database using Django Rest Framework.

4. **Microservices Architecture:**
   - Functions as an independent microservice, allowing for scalability and separation of concerns.

### File Convert Service

The file convert service manages file uploads, real-time status updates, and document conversion. It uses Django Channels for WebSocket communication, AWS S3 for media file storage, and integrates third-party APIs for document conversion. Asynchronous tasks are managed by Celery with Redis as the message broker.

**Features:**
1. **File Upload and Real-time Status Updates:**
   - Enables users to upload files through the React frontend.
   - Provides real-time status updates on the progress of file uploads.

2. **WebSocket Communication:**
   - Utilizes Django Channels for WebSocket communication to relay real-time status updates to the React frontend.

3. **AWS S3 Integration:**
   - Integrates with AWS S3 for secure and scalable storage of media files.

4. **Asynchronous Document Conversion:**
   - Utilizes Celery and Redis to process document conversion tasks asynchronously.
   - Invokes third-party APIs for document conversion.

5. **Microservices Architecture:**
   - Operates as an independent microservice, facilitating scalability and maintainability.

## Django Main App

The Django main app serves as the main orchestrator for communication between microservices. It manages the overall flow of the application, integrates with Django Rest Framework, employs a WebSocket client to connect with independent chat and file services, and orchestrates third-party API integrations.

**Features:**
1. **Microservices Orchestration:**
   - Serves as the main orchestrator for communication between microservices.
   - Manages the overall flow of the application.

2. **Django Rest Framework (DRF) Integration:**
   - Utilizes DRF to expose APIs and handle communication with the frontend and microservices.

3. **WebSocket Client:**
   - Employs a WebSocket client to connect with independent chat and file services, facilitating real-time updates.

4. **Third-party API Integration:**
   - Integrates with third-party APIs for specific functionalities, such as document conversion.

5. **Scalability and Independence:**
   - Adheres to a microservices architecture, allowing for scalability and independence of each service.

6. **Docker Development Environment:**
   - Facilitates a Docker-based development environment for consistency and ease of development.

## Setup

1. Clone the repository.
2. Set up and activate a virtual environment.
3. Install dependencies using `pip install -r requirements.txt` for the backend and `npm install` for the frontend.
4. Apply migrations using `python manage.py migrate`.
5. Configure environment variables (e.g., AWS credentials, third-party API keys).
6. Run the development servers for the main app and microservices.

## Usage

- Start the Django development server.
- Start the microservices servers.
- Run the React frontend.

Visit the application in your web browser, and explore the real-time chat and file processing features.

## Docker

For development, Docker is utilized to encapsulate dependencies and streamline the development environment. Ensure Docker is installed and run the appropriate Docker commands for development.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).



