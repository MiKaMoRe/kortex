import random
from users.factories import UserFactory


def seed_users():
    users = UserFactory.create_batch(random.randint(9,13))

    print("Users created")

    return users
