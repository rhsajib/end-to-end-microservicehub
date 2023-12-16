import json
import websockets
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.layers import get_channel_layer
# from channels_redis.core import WebsocketClient
from channels_redis.websocket.client import WebsocketClient

from core.config import config


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

        # Join room group on port 8000
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        # Connect to port 8002 (optional)
        await self.connect_to_port_8002()


    async def disconnect(self, close_code):
        print(f"WebSocket disconnected: {self.room_group_name}, Close Code: {close_code}")

        # Leave room group on port 8000
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

        # Disconnect from port 8002 (optional)
        await self.connect_to_port_8002(disconnect=True)


    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        print(message)

        # Add message type to event dictionary
        event_data = {
            "type": "chat_message",
            "message": message,
        }

        # Send message to room group on port 8000
        await self.channel_layer.group_send(
            self.room_group_name,
            event_data
        )

        # Send the message to port 8002 as well
        await self.send_to_port_8002(message)
        

    async def chat_message(self, event):
        message = event["message"]

        # Send message through WebSocket
        await self.send(text_data=json.dumps({"message": message, 'id': 3454}))

    async def send_to_port_8002(self, message):
        # Use the WebsocketClient instance from connect_to_port_8002
        # to send the message to the desired endpoint on port 8002
        try:
            await self.client.send(text_data=json.dumps({"message": message}))
        except Exception as e:
            print(f"Error sending message to port 8002: {e}")

    # Receive messages from port 8002
    # async def port_8002_message(self, event):
    #     message = event["message"]
    #     print(f"Received message from port 8002: {message}")
    #     # Handle or process message received from port 8002 here
    #     # ...

    async def connect_to_port_8002(self, disconnect=False):
        channel_layer = get_channel_layer()
        ws_endpoint = f'{config.CHAT_SERVICE_BASE_WS}/ws/chat-service/{self.room_group_name}/'
        self.client = WebsocketClient(channel_layer, ws_endpoint)

        try:
            await self.client.connect()
            if not disconnect:
                await self.client.send(text_data=json.dumps({"message": f"Connect to room {self.room_group_name}"}))
            # Handle connection response or error from port 8002
            # ...
        finally:
            if disconnect:
                await self.client.disconnect()
