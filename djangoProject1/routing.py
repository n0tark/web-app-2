from django.urls import re_path

from .consumers import OnlineStatusConsumer, PhoneConsumer

websocket_urlpatterns = [
    re_path(r'ws/online/$', OnlineStatusConsumer.as_asgi()),
    re_path(r'ws/phones/$', PhoneConsumer.as_asgi()),
]
