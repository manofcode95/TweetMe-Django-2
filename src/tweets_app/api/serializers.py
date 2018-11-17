from rest_framework import serializers
from django.urls import reverse_lazy
from accounts_app.api.serializers import UserSerializer
from tweets_app.models import Tweet

class TweetParentSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    time_since=serializers.SerializerMethodField()
    tweet_url=serializers.SerializerMethodField()
    user_url=serializers.SerializerMethodField()
    follow_url=serializers.SerializerMethodField()
    class Meta:
        model=Tweet
        fields=['user', 'id', 'content','time_since', 'tweet_url', 'user_url', 'follow_url',]

    def get_user_url(self, obj):
        return reverse_lazy('profiles_app:user_detail',kwargs={'username':obj.user.username})

    def get_time_since(self, obj):
        return obj.time_since()

    def get_tweet_url(self, obj):
        return obj.get_absolute_url()

    def get_follow_url(self, obj):
        return reverse_lazy('profiles_app:toggle_follow',kwargs={'username':obj.user.username})

class TweetSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    time_since=serializers.SerializerMethodField()
    tweet_url=serializers.SerializerMethodField()
    retweet_url=serializers.SerializerMethodField()
    user_url=serializers.SerializerMethodField()
    follow_url=serializers.SerializerMethodField()
    like_url=serializers.SerializerMethodField()
    is_liked=serializers.SerializerMethodField()
    like_count=serializers.SerializerMethodField()
    parent=TweetParentSerializer(read_only=True)
    class Meta:
        model=Tweet
        fields=['user', 'id', 'content','time_since', 'tweet_url', 'retweet_url', 'user_url', 'follow_url', 'like_url', 'like_count', 'is_liked', 'is_reply', 'parent']

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
    
    def get_like_url(self, obj):
        return reverse_lazy('tweets_api:like_api',kwargs={'pk':obj.pk})
    
    def get_is_liked(self, obj):       
        currentuser=self.context.get('currentuser')
        if currentuser in obj.like.all():
            return True
        return False

    def get_like_count(self, obj):
        return len(obj.like.all())