from django.urls import path
from chats.views import ListChat


urlpatterns = [
    path("", ListChat.as_view(), name="chat_list")
]
