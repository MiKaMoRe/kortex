import random
from users.factories import UserFactory


def seed_users():
    users = UserFactory.create_batch(random.randint(20,30))

    print("Users created")

    return users
