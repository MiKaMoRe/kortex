from chats.models import Chat, Message
from users.factories import UserFactory
from factory.django import DjangoModelFactory
from factory import post_generation, SubFactory, Faker


class ChatFactory(DjangoModelFactory):
    class Meta:
        model = Chat

    @post_generation
    def members(self, create, extracted, **kwargs):
        if not create or not extracted:
            for _ in range(2):
                self.members.add(UserFactory.create())
            return

        self.members.add(*extracted)


class MessageFactory(DjangoModelFactory):
    class Meta:
        model = Message

    text = Faker("paragraph")
    chat = SubFactory(ChatFactory)
    author = SubFactory(UserFactory)
