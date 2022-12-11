import random
from users.models import User
from users.factories import UserFactory


def seed_users():
    users = UserFactory.create_batch(random.randint(3,5))

    print("Users created")

    return users
