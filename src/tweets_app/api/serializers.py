from rest_framework import serializers
from accounts_app.api.serializers import UserSerializer
from tweets_app.models import Tweet
class TweetSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    time_since=serializers.SerializerMethodField()
    tweet_url=serializers.SerializerMethodField()
    class Meta:
        model=Tweet
        fields=['user', 'content','time_since', 'tweet_url']

    def get_time_since(self, obj):
        return obj.time_since()

    def get_tweet_url(self, obj):
        return obj.get_absolute_url()

