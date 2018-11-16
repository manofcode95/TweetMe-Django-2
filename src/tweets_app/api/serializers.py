from rest_framework import serializers
from django.urls import reverse_lazy
from accounts_app.api.serializers import UserSerializer
from tweets_app.models import Tweet
class TweetSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    time_since=serializers.SerializerMethodField()
    tweet_url=serializers.SerializerMethodField()
    retweet_url=serializers.SerializerMethodField()
    user_url=serializers.SerializerMethodField()
    follow_url=serializers.SerializerMethodField()
    class Meta:
        model=Tweet
        fields=['user', 'content','time_since', 'tweet_url', 'retweet_url', 'user_url', 'follow_url', 'parent']

    def get_time_since(self, obj):
        return obj.time_since()

    def get_tweet_url(self, obj):
        return obj.get_absolute_url()

    def get_retweet_url(self, obj):
        return reverse_lazy('tweets_api:retweet_api', kwargs={'pk':obj.pk})

    def get_user_url(self, obj):
        return reverse_lazy('profiles_app:user_detail',kwargs={'username':obj.user.username})
    
    def get_follow_url(self, obj):
        return reverse_lazy('profiles_app:toggle_follow',kwargs={'username':obj.user.username})

