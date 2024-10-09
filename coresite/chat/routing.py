from django.forms.models import construct_instance
from django.urls import path
from . import  consumers

websocket_urlpatterns = [
    path('ws/sc/', consumers.MySyncConsumer.as_asgi()),
    path('ws/ac/', consumers.MyASyncConsumer.as_asgi()),
    path('ws/sc/echo/', consumers.EchoConsumer.as_asgi()),
]