import json
import websockets
from channels.generic.websocket import AsyncWebsocketConsumer
from core.config import config


class ChatConsumer(AsyncWebsocketConsumer):
    """
        Django Channels primarily provides a way to handle WebSockets within a Django application, 
        allowing us to integrate WebSocket functionality with your Django views and consumers. 
        However, when connecting to an external or independent WebSocket server, 
        we can use any WebSocket library that is compatible with our application.
    
    This consumer handles both internal (port 8000) and external (port 8002) WebSocket connections.
    """

    external_websocket = None  # Track external connection
    async def connect(self):
        self.room_group_name = self.scope['url_route']['kwargs']['chat_id']
        # print(f"WebSocket connected: {self.room_group_name}")

        await self.accept()

        # Join room group on port 8000
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        # Connect to external server on port 8002 (optional)
        await self.connect_to_port_8002()

    async def disconnect(self, close_code):
        # print(f"WebSocket disconnected: {self.room_group_name}, Close Code: {close_code}")

        # Leave room group on port 8000
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

        # Disconnect from external server (if connected)
        await self.connect_to_port_8002(disconnect=True)

    # Receive message from internal WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        print(f"Internal message received: {message}")

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

        # Send the message to external server on port 8002 
        if self.external_websocket:
            try:
                payload = json.dumps({'message': message})
                await self.external_websocket.send(payload)
            except Exception as e:
                print(f"Error sending message to port 8002: {e}")

    async def chat_message(self, event):
        message = event["message"]

        # Send message through internal WebSocket
        await self.send(text_data=json.dumps({"message": message, "id": 3454}))

    async def connect_to_port_8002(self, disconnect=False):
        """
        Connects and disconnects to the external WebSocket server on port 8002.
        """

        if disconnect and self.external_websocket:
            await self.external_websocket.close()
            self.external_websocket = None
            return

        uri = f"{config.CHAT_SERVICE_BASE_WS}/ws/chat-service/{self.room_group_name}/"
        
        self.external_websocket = await websockets.connect(uri)


    
        # async with websockets.connect(uri) as websocket:
        #     self.external_websocket = websocket

            # if not disconnect:
            #     # Initial message upon connection
            #     try:
            #         await websocket.send(json.dumps({"message": f"Connect to room {self.room_group_name}"}))
            #     except Exception as e:
            #         print(f"Error sending initial message to port 8002: {e}")

            # Handle incoming messages from port 8002
            # try:
            #     async for message in websocket:
            #         message_data = json.loads(message)
            #         print(f"Received message from port 8002: {message_data['message']}")
            #         # ... Handle or process the received message here ...

            # # Handle potential disconnection errors
            # except websockets.ConnectionClosedError as e:
            #     print(f"Connection to port 8002 closed: {e}")

            # # Disconnect from the external server if requested
            # finally:
            #     if disconnect or not websocket.open:
            #         await websocket.disconnect()
            #         self.external_websocket = None
        
    # Disconnect from external server during graceful closure
    async def close(self, code):
        await super().close(code)
        await self.connect_to_port_8002(disconnect=True)

