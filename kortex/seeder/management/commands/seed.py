from django.core.management.base import BaseCommand
from users.seeds import seed_users, User
from chats.seeds import seed_chats, seed_messages, ChatFactory


class Command(BaseCommand):
    help = "This command init app's seeds"

    def handle(self, *args, **options):
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

