import os
from chat.routing import websocket_urlpatterns as chat_ws_urls
from file_convert.routing import websocket_urlpatterns as fconvert_ws_urls
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')


application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        'websocket': AuthMiddlewareStack(
            URLRouter(
                chat_ws_urls +
                fconvert_ws_urls
            )
        )
    }
)
