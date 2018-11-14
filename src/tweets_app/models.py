from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save
from django.core.exceptions import ValidationError
from django.urls import reverse_lazy
from django.utils.timesince import timesince
from .validators import validate_content
from datetime import datetime

# Create your models here.
User=get_user_model()
class TweetManager(models.Manager):
    def retweet(self, request_user, tweet):
        if tweet.parent:
            or_parent=tweet.parent
        else:
            or_parent=tweet
        tweet=Tweet.objects.create(user=request_user, parent=or_parent, content=or_parent.content)
        return tweet

class Tweet(models.Model):
    parent=models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    content= models.TextField(max_length=140, validators=[validate_content])
    updated_time= models.DateTimeField(auto_now=True)
    published_time= models.DateTimeField(auto_now_add=True)
    objects=TweetManager()

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse_lazy('tweets_app:tweet_detail', kwargs={'pk':self.pk})

    def time_since(self):
        published_time=self.published_time.strftime("%b %d")
        time_since=timesince(self.published_time)+' ago'
        if 'day' not in time_since and 'month' not in time_since and 'year' not in time_since:
            return time_since
        return published_time
        
    class Meta:
        ordering=['-id']



