import random
from chats.models import Chat
from chats.factories import ChatFactory


def seed_chats(users: list):
    chats = []

    for _ in range(random.randint(7, 10)):
        user1 = random.choice(users)
        user2 = random.choice(users)
        chats.append(ChatFactory.create(members=(user1, user2)))

    print("Chats created")

    return chats
