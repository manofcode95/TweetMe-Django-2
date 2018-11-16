from django.db import models
from django.urls import reverse_lazy
from tweets_app.models import Tweet
# Create your models here.
class Hashtag(models.Model):
    regex=models.CharField(max_length=25)

    def __str__(self):
        return self.regex
    
    def get_absolute_url(self):
        return reverse_lazy('hashtags_app:hashtag_view', kwargs={'tag':self.regex})

    def get_tweet(self):
        qs=Tweet.objects.filter(content__icontains='#'+self.regex)
        return qs