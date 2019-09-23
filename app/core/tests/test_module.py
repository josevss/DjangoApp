from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """docstring for ModelTests."""

    def test_create_user_with_email_successful(self):
        """test creating a new user with email successfull"""
        email = "test@gmail.com"
        password = "testpass123"

        user = get_user_model().objects.create_user(
                email=email,
                password=password
                )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalization(self):
        """ test email """
        email = "hello@GMAIL.com"
        user = get_user_model().objects.create_user(
                email,
                'test123'
                )
        self.assertEqual(user.email, email)

    def test_create_new_superuser(self):
        user = get_user_model().objects.create_superuser(
            'test@londonappdev.com',
            'test123'
            )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')
