from django.db import models
from users.models import User


class Chat(models.Model):
    members = models.ManyToManyField(User, verbose_name="members", related_name="chats")


class Message(models.Model):
    author = models.ForeignKey(
        User, verbose_name="author", on_delete=models.CASCADE, related_name="messages"
    )
    chat = models.ForeignKey(
        Chat, verbose_name="chat", on_delete=models.CASCADE, related_name="messages"
    )
    text = models.TextField(verbose_name="text")
