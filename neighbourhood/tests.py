from django.test import TestCase
from .models import *
from django.contrib.auth.models import User
import datetime as dt
# Create your tests here.

class BusinessClass(TestCase):
    # Set up method
    def setUp(self):
        self.user = User.objects.create_user(username='Emmanuel')
        self.profile = Profile(username = self.user)
        self.profile.save()
        self.business = Business(id=1,logo = 'logos/',description='Entertainment',owner=self.user,name='Pillarframe',email='emmanuel.muchiri@outlook.com',contact='0706915605',address='59160')

#     #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.business,Business))

# #     #Testing Save method
#     def test_save_project(self):
#         self.project.save_project()
#         projects = Project.objects.all()
#         self.assertTrue(len(projects) > 0)

# #     #Testing print all Method
#     def test_print_all(self):
#         self.project.print_all()
#         projects= Project.objects.all()
#         self.assertTrue((len(projects) > -1))
# #     

# class ProfileTestClass(TestCase):
#     # Set up method
#     def setUp(self):
#         self.user = User.objects.create_user(username='Emmanuel')
#         self.profile = Profile(id=1,profpic='/profpics/',bio='test bio',username = self.user,email='emmanuel.muchiri@outlook.com')

#     #Testing instance
#     def test_instance(self):
#         self.assertTrue(isinstance(self.profile,Profile))

#     # Testing save method
#     def test_save_profile(self):
#         self.profile.save_profile()
#         profiles = Profile.objects.all()
#         self.assertTrue(len(profiles) > 0)