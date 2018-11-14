from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Tweet

# Create your tests here.
User=get_user_model()

class TweetTestCase(TestCase):
    def setUp(self):
        user=User.objects.create_user(username='testuser', password='chau1234')
        Tweet.objects.create(user=user, content='test content')

    def test_create_tweet(self):
        tweet=Tweet.objects.get(content='test content')
        self.assertEqual(tweet.user.username, 'testuser')