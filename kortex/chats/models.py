from django.db import models
from users.models import User


class Chat(models.Model):
    members = models.ManyToManyField(User, verbose_name="members", related_name="chats")

    def set_interlocutor(self, current_user):
        for user in self.members.all():
            if user.pk is not current_user.pk:
                self.interlocutor = user

    class Meta:
        ordering = ["-pk"]


class Message(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        User, verbose_name="author", on_delete=models.CASCADE, related_name="messages"
    )
    chat = models.ForeignKey(
        Chat, verbose_name="chat", on_delete=models.CASCADE, related_name="messages"
    )
    text = models.TextField(verbose_name="text")

    def serialize(self):
        return {
            "text": self.text,
            "created_at": self.created_at,
            "author": self.author.serialize(),
        }

    class Meta:
        ordering = ["-pk"]
