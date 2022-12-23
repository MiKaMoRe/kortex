from django.urls import path
from chats.consumers import ChatConsumer

websocket_urlpatterns = [
    path('ws/chats/<int:chat_id>/message', ChatConsumer.as_asgi())
]
