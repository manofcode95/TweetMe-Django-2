from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import UserProfile

# Create your tests here.
User=get_user_model()

class TweetTestCase(TestCase):
    def setUp(self):
        user=User.objects.create_user(username='test_userprofile', password='chau1234')

    def test_userprofile_created(self):
        user_profile=UserProfile.objects.filter(user__username='test_userprofile')
        self.assertTrue(user_profile.exists())