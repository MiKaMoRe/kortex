from django.test import TestCase, RequestFactory, Client
from users.factories import UserFactory
from users.models import User
from chats.views import ListChat
from chats.factories import ChatFactory


class ListChatTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = UserFactory()
        self.chats = reversed(
            ChatFactory.create_batch(10, members=(self.user, UserFactory.create()))
        )

    def test_get_queryset(self):
        response = self._make_request("chat_list", self.user)
        self.assertQuerysetEqual(response.context_data["chats"], self.chats)

    def _make_request(self, url, user: User):
        request = self.factory.get(url)
        request.user = user
        response = ListChat.as_view()(request)
        response.client = Client()
        return response
