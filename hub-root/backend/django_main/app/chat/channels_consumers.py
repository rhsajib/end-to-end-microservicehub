import json
import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer
from .kafka_producers import Producer
from .kafka_consumers import Consumer


class ChatConsumer(AsyncWebsocketConsumer):
    """
    This consumer handles messages from the frontend,
    broadcast messages to clients and publishes them to a Kafka topic.
    """

    async def connect(self):
        self.room_group_name = self.scope['url_route']['kwargs']['chat_id']
        await self.accept()

        # Join room group (for future use)
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

    async def disconnect(self, close_code):
        # Leave room group (for future use)
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        """
            receive messages from channel layer
        """
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        print(f"Internal message received: {message}")

        # Create event data
        event_data = {
            "chat_id": self.room_group_name,
            "sender": "frontend",  # or extract sender from message
            "message": message,
        }

        # Publish event to Kafka topic using KafkaProducer
        Producer.publish_chat_event(event_data)
        # Consumer.consume_messages()
        
        # Send message to room group on port 8000
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message,
            }
        )

    async def chat_message(self, event):
        message = event["message"]

        # Send message through internal WebSocket
        await self.send(text_data=json.dumps({"message": message, "id": 3454}))

