from django.shortcuts import render
from django.views import View

from .models import Hashtag
from tweets_app.models import Tweet
from tweets_app.api.serializers import TweetSerializer



class HashtagView(View):
    queryset=None
    def get(self, request, tag, *args, **kwargs):
        hashtag , created = Hashtag.objects.get_or_create(regex=tag)
        return render(request, 'hashtags_app/hashtag.html', {'object':hashtag})