import factory

from accounts import models


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Faker("email")
    email = factory.SelfAttribute(".username")

    class Meta:
        model = models.User
