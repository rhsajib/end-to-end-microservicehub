import json
import websockets
from core.config import config
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    """
        Django Channels primarily provides a way to handle WebSockets within a Django application, 
        allowing us to integrate WebSocket functionality with your Django views and consumers. 
        However, when connecting to an external or independent WebSocket server, 
        we can use any WebSocket library that is compatible with our application.
    """


    async def connect(self):
        self.room_group_name = self.scope['url_route']['kwargs']['chat_id']
        print(f"WebSocket connected: {self.room_group_name}")

        await self.accept()

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        # Establish a WebSocket connection to the independent server
        self.independent_server_ws = await self.connect_to_independent_server()


    async def disconnect(self, close_code):
        print(f"WebSocket disconnected: {self.room_group_name}, Close Code: {close_code}")

        # Leave room group
        # print('Leave room group')
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

        # Close the WebSocket connection to the independent server
        if hasattr(self, 'independent_server_ws'):
            await self.independent_server_ws.close()

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        print(message)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, 
            {
                # type is a method
                "type": "chat_message",
                "message": message
            }
        )

        # Send the received message to the independent server
        await self.send_to_independent_server(message)


    async def chat_message(self, event):
        message = event["message"]

        # Send message through WebSocket
        await self.send(text_data=json.dumps({"message": message, 'id': 3454}))


    async def send_to_independent_server(self, message):
        try:
            # Construct the payload to be sent to the independent server
            payload = json.dumps({'message': message})

            # Send the payload to the independent server using WebSocket
            await self.independent_server_ws.send(payload)
            # You may receive a response from the server if needed
            response = await self.independent_server_ws.recv()

            # Handle the response if needed
            # For example, check if the notification was successfully received
        except websockets.exceptions.ConnectionClosed as e:
            print(f"Connection to independent server closed: {str(e)}")
        except Exception as e:
            # Handle exceptions (e.g., connection error, server unreachable)
            print(f"Error sending message to independent server: {str(e)}")


    async def connect_to_independent_server(self):
        try:
            ws_endpoint = f'{config.CHAT_SERVICE_BASE_WS}/ws/chat-service/{self.room_group_name}/'

            # Establish a WebSocket connection to the independent server
            return await websockets.connect(ws_endpoint)
        
        except Exception as e:
            print(f"Error connecting to independent server: {str(e)}")


"""
To achieve the desired functionality, you can follow these general steps:

1. **Create User via DRF Viewset:**
   First, create a Django REST Framework (DRF) viewset for user creation. You can use Django's built-in `CreateAPIView` for this purpose.

```python
# views.py
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from .models import User

class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
```

2. **Send Notification via WebSocket:**
   For sending notifications to an independent server via WebSocket, you can use a library like `channels` in Django. Here's a simplified example:

```python
# consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']

        # Handle the received message (e.g., send notification to the independent server)
        # ...

        await self.send(text_data=json.dumps({'message': 'Notification sent'}))
```

3. **Configure Routing for WebSocket:**
   Add a routing configuration for WebSocket consumers using `channels`.

```python
# routing.py
from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/notifications/$', consumers.NotificationConsumer.as_asgi()),
]
```

4. **Include WebSocket Routing in Django Project:**
   Include the WebSocket routing configuration in your Django project's `asgi.py` file.

```python
# asgi.py
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from myapp.routing import websocket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter(websocket_urlpatterns),
})
```

5. **Trigger WebSocket Notification from DRF Viewset:**
   Finally, modify your DRF viewset to trigger the WebSocket notification after successfully creating a user.

```python
# views.py
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .consumers import NotificationConsumer

class UserCreateAPIView(generics.CreateAPIView):
    # ... (same as before)

    def perform_create(self, serializer):
        # Create the user
        instance = serializer.save()

        # Trigger WebSocket notification
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "notifications_group",  # WebSocket group name
            {
                "type": "send_notification",
                "message": "User created: {}".format(instance.username),
            },
        )
```

6. **Handle WebSocket Notification in Consumer:**
   Update the WebSocket consumer to handle the notification and send it to the independent server.

```python
# consumers.py
class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("notifications_group", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("notifications_group", self.channel_name)

    async def receive(self, text_data):
        # Handle any incoming WebSocket messages (if needed)
        pass

    async def send_notification(self, event):
        message = event['message']

        # Handle the received message (e.g., send notification to the independent server)
        # ...

        # Send a response back to the WebSocket client
        await self.send(text_data=json.dumps({'message': 'Notification sent'}))
```

Please note that this is a simplified example, and you might need to adapt it to fit your specific requirements and project structure. Additionally, make sure to install the necessary dependencies, such as `channels`, if you haven't already.

"""




"""
Certainly, I'll provide a complete example, including the Django Channels routing configuration and the necessary adjustments to your Django project.

1. **Install required packages:**

```bash
pip install channels channels-redis
```

2. **Update your Django project settings:**

```python
# settings.py
INSTALLED_APPS = [
    # ... other apps
    'channels',
]

# Use channels layer as the default backend for Django's ASGI interface
ASGI_APPLICATION = "your_project.routing.application"
```

3. **Create a `routing.py` file in your app directory:**

```python
# your_app/routing.py
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/notifications/$', consumers.NotificationConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})
```

4. **Update your `consumers.py` with the complete code:**

```python
# consumers.py
import json
import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        await self.send_notification_to_independent_server(message)

    async def send_notification_to_independent_server(self, message):
        try:
            # Replace the following details with your independent server's information
            server_host = "your_server_host"
            server_port = 80
            server_path = "/path/to/notification/endpoint"

            # Construct the WebSocket URI
            uri = f"ws://{server_host}:{server_port}{server_path}"

            # Establish a WebSocket connection to the independent server
            async with self.channel_layer.connection(uri) as websocket:
                # Construct the payload to be sent to the independent server
                payload = json.dumps({'message': message})

                # Send the payload to the independent server using WebSocket
                await websocket.send_json({'type': 'send.notification', 'payload': payload})

                # You may receive a response from the server if needed
                response = await websocket.receive_json()

                # Handle the response if needed
                # For example, check if the notification was successfully received

        except Exception as e:
            # Handle exceptions (e.g., connection error, server unreachable)
            print(f"Error sending notification to independent server: {str(e)}")
```

5. **Update your `views.py` with the DRF viewset:**

```python
# views.py
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from .models import User

class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        self.send_notification(instance.username)

    def send_notification(self, username):
        # This assumes you have a connected WebSocket consumer on the frontend
        # to handle the notification. Adjust this according to your frontend setup.
        async_to_sync(self.channel_layer.group_send)(
            "notifications_group",
            {
                "type": "send_notification",
                "message": f"User created: {username}",
            }
        )
```

Make sure to replace the placeholder values (`your_server_host`, `server_port`, and `server_path`) with the actual details of your independent server.

This example assumes you have set up Django Channels correctly, and you have a connected WebSocket consumer on the frontend to handle the notifications. Adjust the frontend WebSocket handling according to your specific frontend setup.


"""


"""
### WS connection

pip install websockets



# consumers.py
import json
import asyncio
import websockets

from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("notifications_group", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("notifications_group", self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']

        # Handle the received message (e.g., send notification to the independent server)
        await self.send_notification_to_independent_server(message)

    async def send_notification_to_independent_server(self, message):
        try:
            # Replace the following details with your independent server's information
            server_host = "your_server_host"
            server_port = 80
            server_path = "/path/to/notification/endpoint"

            uri = f"ws://{server_host}:{server_port}{server_path}"

            async with websockets.connect(uri) as websocket:
                # Construct the payload to be sent to the independent server
                payload = json.dumps({'message': message})

                # Send the payload to the independent server using WebSocket
                await websocket.send(payload)

                # You may receive a response from the server if needed
                response = await websocket.recv()

                # Handle the response if needed
                # For example, check if the notification was successfully received

        except Exception as e:
            # Handle exceptions (e.g., connection error, server unreachable)
            print(f"Error sending notification to independent server: {str(e)}")


"""



"""
# HTTP connection

# consumers.py
import json
import http.client

from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("notifications_group", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("notifications_group", self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']

        # Handle the received message (e.g., send notification to the independent server)
        self.send_notification_to_independent_server(message)

    async def send_notification_to_independent_server(self, message):
        try:
            # Replace the following details with your independent server's information
            server_host = "your_server_host"
            server_port = 80
            server_path = "/path/to/notification/endpoint"

            connection = http.client.HTTPConnection(server_host, server_port)
            headers = {'Content-type': 'application/json'}

            # Construct the payload to be sent to the independent server
            payload = json.dumps({'message': message})

            # Send the HTTP POST request to the independent server
            connection.request('POST', server_path, payload, headers)

            # Get the response from the independent server
            response = connection.getresponse()

            # Handle the response if needed
            # For example, check if the notification was successfully received

            connection.close()

        except Exception as e:
            # Handle exceptions (e.g., connection error, server unreachable)
            print(f"Error sending notification to independent server: {str(e)}")


"""