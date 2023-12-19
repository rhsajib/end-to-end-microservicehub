from django.urls import re_path
from .channels_consumers import ChatConsumer

websocket_urlpatterns = [
    re_path(r"ws/chat/(?P<chat_id>chat-\w+)/$", ChatConsumer.as_asgi()),
]