from django.core.management.base import BaseCommand
from users.seeds import seed_users, User
from chats.seeds import seed_chats, ChatFactory


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

        admins_chat = ChatFactory.create(members=(users[0], admin))

