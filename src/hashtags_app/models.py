from django.db import models
from django.urls import reverse_lazy
from tweets_app.models import Tweet
from django.utils import timezone
from tweets_app.signals import hashtag_done
from django.db.models.signals import post_save
# Create your models here.
class Hashtag(models.Model):
    regex=models.CharField(max_length=25)
    created_day=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.regex
    
    def get_absolute_url(self):
        return reverse_lazy('hashtags_app:hashtag_view', kwargs={'tag':self.regex})

    def get_tweet(self):
        qs=Tweet.objects.filter(content__icontains='#'+self.regex)
        return qs


def parse_hashtag_receiver(sender, hashtags, **kwargs):
    if len(hashtags)>0:
        for hashtag in hashtags:
            Hashtag.objects.create(regex=hashtag)

hashtag_done.connect(parse_hashtag_receiver)   