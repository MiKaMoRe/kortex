from django.contrib.auth.models import AnonymousUser
from django.core.exceptions import PermissionDenied
from django.test import TestCase, RequestFactory, Client
from users.factories import UserFactory
from users.models import User
from chats.views import ListChat, DetailChat
from chats.factories import ChatFactory, MessageFactory


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

    def test_get_with_user(self):
        response = self._make_request("chat_list", self.user)
        self.assertEqual(response.status_code, 200)

    def test_get_with_no_user(self):
        response = self._make_request("chat_list", AnonymousUser())
        self.assertEqual(response.status_code, 302)

    def _make_request(self, url, user: User):
        request = self.factory.get(url)
        request.user = user
        response = ListChat.as_view()(request)
        response.client = Client()
        return response


class DetailChatTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.author = UserFactory()
        self.chat = ChatFactory.create(members=(self.author, UserFactory()))
        self.messages = reversed(
            MessageFactory.create_batch(20, chat=self.chat, author=self.author)
        )

    def test_get_with_author(self):
        response = self._make_request("chat_detail", self.author)
        self.assertEqual(response.status_code, 200)

    def test_get_with_other_user(self):
        with self.assertRaises(PermissionDenied):
            self._make_request("chat_detail", UserFactory())

    def test_get_with_no_user(self):
        response = self._make_request("chat_detail", AnonymousUser())
        self.assertEqual(response.status_code, 302)

    def _make_request(self, url, user: User):
        request = self.factory.get(url)
        request.user = user
        response = DetailChat.as_view()(request, pk=self.chat.pk)
        response.client = Client()
        return response
