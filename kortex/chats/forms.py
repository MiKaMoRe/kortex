from chats.models import Message
from django import forms


class SendMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ("text",)
        widgets = {
            "text": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Write a message",
                    "rows": "1",
                }
            ),
        }
