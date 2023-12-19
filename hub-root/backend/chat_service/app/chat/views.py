from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from asgiref.sync import async_to_sync
# from .consumers import ChatRoomConsumer
from rest_framework import viewsets
from .models import Message
from .serializers import MessageSerializer

from core import config
import asyncio




class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def list(self, request, *args, **kwargs):
        chat_id = 'chat-a4sfdkj490'

        # connected = async_to_sync(self.connect_to_websocket)(chat_id)
        # if connected:
        #     print('connected to ws')
        # Run the connection
        # asyncio.run(self.connect_consumer_with_ws(chat_id))

        # async_to_sync(self.connect_consumer_with_ws)(chat_id)
        return super().list(request, *args, **kwargs)
    
    # # Connect the consumer to the WebSocket
    # async def connect_consumer_with_ws(self, chat_id):
    #     # Instantiate ChatRoomConsumer
    #     consumer = ChatRoomConsumer(chat_id=chat_id)
    #     await consumer.connect()
   





    
    async def connect_to_websocket(self, chat_id):
        # try:
        ws_endpoint = f'{config.DJANGO_MAIN_APP_WS_BASE_URL}/ws/file/convert/{chat_id}/'

        # Establish a WebSocket connection to the independent server
        async with websockets.connect(ws_endpoint) as websocket:
            return True
            

        # except Exception as e:
        #     # Handle exceptions (e.g., connection error, server unreachable)
        #     print(f"Error connecting to independent server: {str(e)}")
    



    # def connect_to_websocket(self, chat_id):
    #     channel_layer = get_channel_layer()
    #     consumer = ChatRoomConsumer()
    #     # Set the channel layer for the consumer
    #     consumer.channel_layer = channel_layer

    #     # Manually set the scope to include the chat_id
    #     consumer.scope = {'type': 'websocket.connect'}
    #     consumer.chat_id = chat_id
    #     # Connect to the WebSocket
    #     async_to_sync(consumer.connect)()



        # consumer.scope = {'type': 'websocket.connect', 'channel': channel_name}
        # async_to_sync(consumer.connect)(channel_name)




"""
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from .models import Message
from .serializers import MessagesSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessagesSerializer


    @action(detail=True, methods=['post'])
    async def connect_to_websocket(self, request, *args, **kwargs):
        instance = self.get_object()
        channel_name = f'chat-{instance.id}'
        
        await self.add_channel_to_group(channel_name)
        return Response({'status': 'success'})

    @database_sync_to_async
    def add_channel_to_group(self, channel_name):
        return channel_layer.group_add(channel_name, self.channel_name)

        



        -----------------

    @action(detail=True, methods=['post'])
    def subscribe_to_room(self, request, pk=None):
        # For simplicity, let's assume 'pk' is the room identifier
        room = get_object_or_404(RoomModel, pk=pk)

        # Simulate subscription logic (you can replace this with your actual logic)
        # For example, you might have a subscribers field in your RoomModel
        # and add the current user to it when they subscribe
        room.subscribers.add(request.user)

        return Response({'status': 'success', 'room': room.id})

    



# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'messages', MessageViewSet, basename='messages')

urlpatterns = [
    # Your existing URLs
    path('api/v1/chat/', include(router.urls)),
    # Add the URL for the custom action
    path('api/v1/chat/messages/<int:pk>/subscribe/', MessageViewSet.as_view({'post': 'subscribe_to_room'}), name='subscribe-to-room'),
]



from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    name = models.CharField(max_length=255)
    subscribers = models.ManyToManyField(User, related_name='subscribed_rooms')

    def __str__(self):
        return self.name


"""