from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from chats.models import Chat


class ListChat(LoginRequiredMixin, ListView):
    model = Chat
    context_object_name = "chats"
    paginate_by = 10
    login_url = "sign_in"

    def get_queryset(self):
        return self.request.user.chats.all()
