from django.test import TestCase

from accounts import factories


class AccountsTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = factories.UserFactory()

    def test_return_email_when_str_is_called(self):
        self.assertEqual(self.user.email, self.user.__str__())
