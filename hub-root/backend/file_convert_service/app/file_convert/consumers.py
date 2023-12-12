# chat/consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer

class FileConvertConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['channel_id']
        self.room_group_name = self.room_name
        # self.room_group_name = f'file_convert_{self.room_name}'
        print(f"WebSocket connected: {self.room_name}")

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()


    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        status = text_data_json['status']
        print(status)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {'type': 'update_status', 'status': status}
        )


    async def update_status(self, event):
        status = event['status']

        data = {
            'status': status
        }

        # Send status through WebSocket
        await self.send(text_data=json.dumps(data))