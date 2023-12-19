from django.urls import re_path

from . import channels_consumers

websocket_urlpatterns = [
    re_path(r"ws/chat-service/(?P<chat_id>chat-\w+)/$", channels_consumers.ChatRoomConsumer.as_asgi()),
]