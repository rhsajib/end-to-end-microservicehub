from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/chat-service/(?P<chat_id>chat-\w+)/$", consumers.ChatRoomConsumer.as_asgi()),
]