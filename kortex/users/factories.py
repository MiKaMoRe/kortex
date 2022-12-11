from users.models import User
from factory.django import DjangoModelFactory
from factory import Faker


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    email = Faker("email")
    first_name = Faker("first_name")
    last_name = Faker("last_name")
    password = "simplepass"
