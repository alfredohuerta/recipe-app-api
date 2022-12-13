"""
Test for the Django Admin modifications
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client


class AdminSiteTest(TestCase):
    """Test for django admin"""

    def setUp(self):
        """Create user and client"""
        self.client = Client() # Creates an instance of the Django Client
        self.admin_user = get_user_model().objects.create_superuser(
            email = 'admin@example.com',
            password = 'testpass123',
        )
        self.client.force_login(self.admin_user) # force the authentication for the user
        self.user = get_user_model().objects.create_user(
            email = 'user@example.com',
            password = 'testpass123',
            name = 'Test User',
        )

    def test_user_list(self):
        """Test that users are listed on the page"""
        url = reverse('admin:core_user_changelist') # determines which url are we going to pull from the Django admin
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_page(self):
        """Test the edit user page works"""
        url = reverse('admin:core_user_change', args = [self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Test the create user page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)