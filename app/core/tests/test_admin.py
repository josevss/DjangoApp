from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):
    """docstring forAdminSiteTests."""

    def setUp(self):   # it will run default when the test is run,creating test client
        self.client= Client()
        self.admin_user= get_user_model().objects.create_superuser(
                        email= "admin@gmail.com",
                        password= "password123"
                        )
        self.client.force_login(self.admin_user)
        self.user=get_user_model().objects.create_user(
                        email='test@gmail.com',
                        password='password123',
                        name='test user'
                        )

    def test_users_listed(self):
        url=reverse('admin:core_user_changelist')
        res=self.client.get(url)

        self.assertContains(res, self.user.name)#also checj 200 ok
        self.assertContains(res, self.user.email)


    # def test_user_change_page(self):
    #     url=reverse('admin:core_user_change',args=[se])

    def test_user_page_change(self):
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)


    def test_create_user_page(self):
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
