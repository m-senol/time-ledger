from django.test import TestCase

from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from apps.users.models import User
from apps.attendance.models import Attendance
from datetime import date, time
from unittest import skip

# Create your tests here.

class AttendanceTestCase(TestCase):
    def setUp(self):
        self.employee = User.objects.create_user(username='emp1', password='qwerty', is_manager=False)
        self.token = Token.objects.create(user=self.employee)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')
    
    @skip("Should modify after changes")
    def test_check_in_successful(self):
        response = self.client.post('/attendance/check-in/')
        self.assertEqual(response.status_code, 200, "Wrong Status Code")
        attendance = Attendance.objects.get(user=self.employee, date=date.today())
        self.assertIsNotNone(attendance.check_in, "Check-In not saved")

    @skip("Should modify after changes")
    def test_duplicate_check_in(self):
        Attendance.objects.create(user=self.employee, date=date.today(), check_in=time(8, 0))
        response = self.client.post('/attendance/check-in/')
        self.assertEqual(response.status_code, 400, "Wrong Status Code")
        self.assertIn("You have already checked in today.", response.data.get('message'))

    @skip("Should modify after changes")
    def test_check_out_successful(self):
        Attendance.objects.create(user=self.employee, date=date.today(), check_in=time(8, 0))
        response = self.client.post('/attendance/check-out/')
        self.assertEqual(response.status_code, 200, "Wrong Status Code")
        attendance = Attendance.objects.get(user=self.employee, date=date.today())
        self.assertIsNotNone(attendance.check_out, "Check-out not saved")

    @skip("Should modify after changes")
    def test_duplicate_check_out(self):
        Attendance.objects.create(user=self.employee, date=date.today(), check_in=time(8, 0), check_out=time(15, 0))
        response = self.client.post('/attendance/check-out/')
        self.assertEqual(response.status_code, 400, "Wronf Status code")
        self.assertIn("You have already checked out today.", response.data.get('message'))

