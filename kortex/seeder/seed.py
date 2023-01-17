from users.seeds import seed_users
from users.models import User
from chats.seeds import seed_chats, seed_messages, ChatFactory


def seed():
    users = seed_users()
    chats = seed_chats(users)
    admin = User.objects.create_superuser(
        first_name="John",
        last_name="Johnson",
        email="admin@gmail.com",
        password="simplepass",
    )
    admin.save()

    for user in users:
        chats.append(ChatFactory.create(members=(user, admin)))

    for chat in chats:
        seed_messages(chat)
