import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Users


class UsersModelTests(TestCase):
    def test_full_name_with_first_and_last_name(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """

        first_name = "first"
        last_name = "last"

        user = Users(first_name=first_name, last_name=last_name)
        self.assertEqual(user.get_name(), f"{first_name} {last_name}")
