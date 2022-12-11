from chats.models import Chat
from users.factories import UserFactory
from factory.django import DjangoModelFactory
from factory import post_generation


class ChatFactory(DjangoModelFactory):
    class Meta:
        model = Chat

    @post_generation
    def members(self, create, extracted, **kwargs):
        if not create or not extracted:
            for i in range(2):
                self.members.add(UserFactory.create())
            return

        self.members.add(*extracted)