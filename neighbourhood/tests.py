from django.test import TestCase
from .models import neighbourhood,healthservices
from django.contrib.auth.models import User
import datetime as dt
# Create your tests here.
class neighbourhoodTestClass(TestCase):
    def setUp(self):
        self.Kasarani = neighbourhood(neighbourhood='Kasarani')

    def test_instance(self):
        self.assertTrue(isinstance(self.Kasarani,neighbourhood))

    def tearDown(self):
        neighbourhood.objects.all().delete()

    def test_create_method(self):
        self.Kasarani.create_neighbourhood()
        hood = neighbourhood.objects.all()
        self.assertTrue(len(hood)>0)

    def test_delete_method(self):
        self.Kasarani.delete_neighbourhood('Kasarani')
        hood = neighbourhood.objects.all()
        self.assertTrue(len(hood)==0)

# class healthservicesTestClass(TestCase):
#     def setUp(self):
#         self.Radiotherapy = healthservices(healthservices='Radiotherapy')

#     def test_instance(self):
#         self.assertTrue(isinstance(self.Radiotherapy,healthservices))

#     def tearDown(self):
#         healthservices.objects.all().delete()

#     def test_save_method(self):
#         self.Radiotherapy.save_healthservices()
#         health = healthservices.objects.all()
#         self.assertTrue(len(health)>0)

#     def test_delete_method(self):
#         self.Radiotherapy.delete_healthservices('Radiotherapy')
#         health = healthservices.objects.all()
#         self.assertTrue(len(health)==0)