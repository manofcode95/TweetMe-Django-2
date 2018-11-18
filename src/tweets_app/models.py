from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save
from django.core.exceptions import ValidationError
from django.urls import reverse_lazy
from django.utils.timesince import timesince
from django.db.models.signals import post_save
from .validators import validate_content
from datetime import datetime
from .signals import hashtag_done
import re
# Create your models here.
User=get_user_model()
class TweetManager(models.Manager):
    def retweet(self, request_user, tweet):
        if tweet.parent:
            og_parent=tweet.parent
        else:
            og_parent=tweet
        
        was_retweeted=Tweet.objects.filter(user=request_user).filter(parent=og_parent).exists()
        if not was_retweeted:
            retweet=Tweet.objects.create(user=request_user, parent=og_parent, content=og_parent.content)
            return retweet
        return None

    def do_like(self, request_user, tweet):
        if request_user in tweet.like.all():
            tweet.like.remove(request_user)
            is_liked=False
        else:
            tweet.like.add(request_user)
            is_liked=True
        return is_liked

class Tweet(models.Model):
    parent=models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    content= models.TextField(max_length=140, validators=[validate_content])
    like=models.ManyToManyField(User, blank=True, related_name="did_like")
    updated_time= models.DateTimeField(auto_now=True)
    published_time= models.DateTimeField(auto_now_add=True)
    is_reply=models.BooleanField(default=False)
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
    
    def get_parent(self):
        the_parent=self
        if self.parent:
            the_parent=self.parent
        return the_parent

    def get_children(self):
        the_parent=self.get_parent()
        qs=Tweet.objects.filter(parent=the_parent)
        parent_qs=Tweet.objects.filter(pk=the_parent.pk)
        return (qs|parent_qs).distinct().order_by('id')
        
    class Meta:
        ordering=['-id']




def post_save_tweet_receiver(sender, instance, created, *args, **kwargs):
    # do something after creating hashtags
    hashtag_regex='#([\w]+)'
    hashtags=re.findall(hashtag_regex, instance.content)
  
    hashtag_done.send(sender=instance.__class__, hashtags=hashtags)


post_save.connect(post_save_tweet_receiver, sender=Tweet)