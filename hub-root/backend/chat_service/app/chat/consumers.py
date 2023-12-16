import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Messages
from channels.layers import get_channel_layer


class ChatRoomConsumer(AsyncWebsocketConsumer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.channel_layer = get_channel_layer()
        self.chat_id = None
      
    async def connect(self):
        # Extract room name from URL parameters
        self.room_group = self.scope["url_route"]["kwargs"]["chat_id"]
        self.chat_id = f'chat_service-{self.room_group}'

        await self.accept()

        await self.channel_layer.group_add(
            self.chat_id, 
            self.channel_name
        )

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.chat_id, 
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message_text = text_data_json["message"]

        event_data = {
            "type": "new_message", 
            "message": message_text
        }

        # Send message to room group and save to database
        await self.channel_layer.group_send(
            self.chat_id,
            event_data
        )
        await self.create_message(message_text)

    async def new_message(self, event):
        message_text = event["message"]

        # Send message through internal WebSocket
        await self.send(text_data=json.dumps({"message": message_text, "id": 3454}))

    @database_sync_to_async
    def create_message(self, message_text):
        return Messages.objects.create(message=message_text)


    