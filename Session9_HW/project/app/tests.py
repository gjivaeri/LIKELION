from django.test import TestCase

from django.contrib import auth
from .models import *

class AuthTestCase(TestCase):
    def setUp(self):
        self.u = HW8.objects.create_user('gjivaeri@gmail.com', 'iamtest', 'pass')
        self.u.is_staff = True
        self.u.is_superuser = True
        self.u.is_active = True
        self.u.save()

 def testLogin(self):
        self.client.login(username='gjivaeri@gmail.com', password='pass')