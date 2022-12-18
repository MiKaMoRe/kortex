from django.urls import path
from chats.views import ListChat, DetailChat, SendMessage


urlpatterns = [
    path("", ListChat.as_view(), name="chat_list"),
    path("<int:pk>", DetailChat.as_view(), name="chat_detail"),
    path("<int:pk>/message", SendMessage.as_view(), name="send_message"),
]
