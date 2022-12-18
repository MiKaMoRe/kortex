import random
from chats.models import Chat
from chats.factories import ChatFactory, MessageFactory


def seed_chats(users: list):
    chats = []

    for _ in range(random.randint(7, 10)):
        user1 = random.choice(users)
        user2 = random.choice(users)
        chats.append(ChatFactory.create(members=(user1, user2)))

    print("Chats created")

    return chats


def seed_messages(chat: Chat):
    messages = []

    for _ in range(random.randint(10, 20)):
        user = random.choice(chat.members.all())
        messages.append(MessageFactory.create(author=user, chat=chat))

    print("Messages appended to {} chat".format(chat.pk))

    return messages
