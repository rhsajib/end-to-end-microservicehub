from django.urls import re_path
from .consumers import FileConvertConsumer

websocket_urlpatterns = [
    re_path(r"ws/file/convert/(?P<channel_id>[\w-]+)/", FileConvertConsumer.as_asgi()),
]

# By default, Django's URL patterns with \w+ might not match hyphens. 
# If our UUIDv4 strings include hyphens, we can modify the pattern to include them. 
# Here's an updated pattern that should match UUIDv4 strings with hyphens:
# previous: r"ws/file/convert/(?P<channel_id>\w+)/"
# now:      r"ws/file/convert/(?P<channel_id>[\w-]+)/"