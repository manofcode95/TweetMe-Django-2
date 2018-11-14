from django.conf.urls import url, include

from .views import TweetListAPIView, TweetCreateAPIView
app_name='tweets_api'


urlpatterns = [
    url(r'^$', TweetListAPIView.as_view(), name='tweet_api'),
    url(r'^create/$', TweetCreateAPIView.as_view(), name='create_api'),
]
