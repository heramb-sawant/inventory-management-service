from django.test import TestCase
from django.urls import reverse

from .models import Users


# USER MODEL TESTS --------------------------------------------------
class UsersModelTests(TestCase):
    def test_full_name_with_first_and_last_name(self) -> None:
        first_name = "first"
        last_name = "last"

        user = Users(first_name=first_name, last_name=last_name)
        self.assertEqual(user.get_name(), f"{first_name} {last_name}")


# USER VIEW TESTS ---------------------------------------------------
class UserIndexViewTests(TestCase):
    def test_no_users(self) -> None:
        response = self.client.get(reverse("users:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No users are available.")
        self.assertQuerySetEqual(response.context["most_recent"], [])

    def test_one_user(self) -> None:
        user_one = Users.objects.create(first_name="one", last_name="one")

        response = self.client.get(reverse("users:index"))
        self.assertEqual(response.status_code, 200)
        self.assertQuerySetEqual(
            response.context["most_recent"],
            [user_one],
        )
