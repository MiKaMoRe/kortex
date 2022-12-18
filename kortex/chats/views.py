from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import get_object_or_404
from chats.models import Chat, Message
from chats.forms import SendMessageForm
from users.models import User
from kortex.utils import HasPemissionsMixin, JSONResponseMixin


class SendMessage(HasPemissionsMixin, JSONResponseMixin, CreateView):
    model = Message
    form_class = SendMessageForm
    login_url = "sign_in"

    def has_permissions(self, user: User) -> bool:
        return user.is_authenticated

    def render_to_response(self, context, **response_kwargs):
        return self.render_to_json_response(context, **response_kwargs)

    def form_valid(self, form):
        chat_id = self.kwargs["pk"]
        chat = get_object_or_404(Chat, pk=chat_id)

        # Add addintional attributes
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.chat = chat
        self.object.save()

        return self.render_to_response(
            {
                "success": True,
                "message": {
                    "text": self.object.text,
                    "author_slug": self.object.author.slug,
                    "author_first_name": self.object.author.first_name,
                    "author_last_name": self.object.author.last_name,
                },
            },
            status=201,
        )

    def form_invalid(self, form):
        return self.render_to_response({"success": False}, status=422)


class ListChat(HasPemissionsMixin, ListView):
    model = Chat
    context_object_name = "chats"
    paginate_by = 10
    login_url = "sign_in"

    def has_permissions(self, user: User) -> bool:
        return user.is_authenticated

    def get_queryset(self):
        return self.request.user.chats.all().prefetch_related("members")


class DetailChat(HasPemissionsMixin, DetailView):
    model = Chat
    context_object_name = "chat"
    login_url = "sign_in"

    def get(self, request, *args, **kwargs):
        """
        Overridden to set ``self.object`` in ``has_permissions``
        """
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["messages"] = self.object.messages.all()
        context["form"] = SendMessageForm(initial={"post": self.object})
        return context

    def has_permissions(self, user: User) -> bool:
        if user.is_authenticated:
            self.object = self.get_object()
            chat = self.get_context_data().get("chat")
            chat_members_ids = chat.members.values_list("pk", flat=True)
            return user.pk in chat_members_ids
        return False
