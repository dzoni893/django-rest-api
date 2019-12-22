from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):

    def test_create_user_with_email_successful(self):
        """ Test creating a user with email is successful"""
        email = "test@email.com"
        password = "testpass123"
        user = get_user_model().objects.create_user(email=email,
                                                    password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """ Test new user email address normalized"""
        email = "test@EMAIL.COM"
        user = get_user_model().objects.create_user(email, "test123")

        self.assertEqual(user.email, email.lower())

    def test_new_user_email_invalid(self):
        """ Test new user with no email address raises email"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "test123")

    def test_new_superuser(self):
        """ Test new super user creation"""
        email = "superuser@email.com"
        user = get_user_model().objects.create_superuser(email, "test123")

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)



