from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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

        return self.render_to_json_response(
            {"message": self.object.serialize()},
            status=201,
        )

    def form_invalid(self, form):
        return self.render_to_response({"success": False}, status=422)


class ListChat(HasPemissionsMixin, ListView):
    model = Chat
    context_object_name = "chats"
    paginate_by = 5
    login_url = "sign_in"

    def has_permissions(self, user: User) -> bool:
        return user.is_authenticated

    def get_queryset(self):
        return self.request.user.chats.all().prefetch_related("members")

    def get_context_data(self, **kwargs):
        current_user = self.request.user
        context = super().get_context_data(**kwargs)

        for chat in context["chats"]:
            chat.set_interlocutor(current_user)

        return context


class DetailChat(HasPemissionsMixin, JSONResponseMixin, DetailView):
    model = Chat
    context_object_name = "chat"
    login_url = "sign_in"

    def get(self, request, *args, **kwargs):
        """
        Overridden to set ``self.object`` in ``has_permissions``
        """
        context = self.get_context_data(object=self.object)

        if request.content_type == "application/json":
            return self.render_to_json_response(context, status=200)
        return self.render_to_response(context)

    def get_data(self, context):
        messages = [message.serialize() for message in context["messages"]]
        return {"messages": messages}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        messages = self.object.messages.all().prefetch_related("author")
        paginator = Paginator(messages, 12)
        page_number = self.request.GET.get("page")

        try:
            context["messages"] = paginator.page(page_number)
        except EmptyPage:
            context["messages"] = []
        except PageNotAnInteger:
            context["messages"] = paginator.page(1)

        context["form"] = SendMessageForm(initial={"post": self.object})
        return context

    def has_permissions(self, user: User) -> bool:
        if user.is_authenticated:
            self.object = self.get_object()
            chat = self.get_context_data().get("chat")
            chat_members_ids = chat.members.values_list("pk", flat=True)
            return user.pk in chat_members_ids
        return False
