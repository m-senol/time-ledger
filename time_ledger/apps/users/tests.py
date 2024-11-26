from django.test import TestCase

from apps.users.models import User
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from unittest import skip


# Create your tests here.

class UserAuthenticationTest(TestCase):
    def setUp(self):
        self.employee = User.objects.create_user(username='emp1', password='qwerty', is_manager=False)
        self.manager  = User.objects.create_user(username='man1', password='qwerty', is_manager=True)
        self.client = APIClient()

    def test_employee_login_successful(self):
        response = self.client.post('/users/employee-login/', {'username': 'emp1', 'password': 'qwerty'})
        self.assertEqual(response.status_code, 302)

    @skip("Should modify after changes")
    def test_employee_login_failed(self):
        response = self.client.post('/users/employee-login/', {'username': 'emp1', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Invalid username or password', status_code=200, html=True)


    def test_manager_login_successful(self):
        response = self.client.post('/users/manager-login/', {'username': 'man1', 'password': 'qwerty'})
        self.assertEqual(response.status_code, 302)

    @skip("Should modify after changes")
    def test_manager_login_failed(self):
        response = self.client.post('/users/manager-login/', {'username': 'man1', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Invalid username or password', status_code=200, html=True)

    @skip("Should modify after changes")
    def test_logout_employee(self):
        self.client.login(username='emp1', password='qwerty')
        response = self.client.get('/users/logout/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, 'home')
    
    @skip("Should modify after changes")
    def test_logout_manager(self):
        self.client.login(username='man1', password='qwerty')
        response = self.client.get('/users/logout/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')

class LeaveDaysTestCase(TestCase):
    def setUp(self):
        self.employee = User.objects.create_user(username='emp1', password='qwerty', is_manager=False, available_leave_days=15)
        self.client = APIClient()

    @skip("Should modify after changes")
    def test_leave_days_retrieval(self):
        pass
