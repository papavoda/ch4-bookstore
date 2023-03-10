from django.contrib.auth import get_user_model
from django.test import TestCase


class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='Testuser',
            email="testuser@example.org",
            password='testpassword123',
        )
        self.assertEqual(user.username, 'Testuser')
        self.assertEqual(user.email, 'testuser@example.org')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)



    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='Superadmin',
            email="superadmin@example.org",
            password='testpassword123',
        )
        self.assertEqual(admin_user.username, 'Superadmin')
        self.assertEqual(admin_user.email, 'superadmin@example.org')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


