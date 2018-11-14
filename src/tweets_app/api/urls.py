from django.conf.urls import url, include

from .views import TweetListAPIView, TweetCreateAPIView, RetweetAPIView, TweetRetrieveAPIView
app_name='tweets_api'


urlpatterns = [
    url(r'^$', TweetListAPIView.as_view(), name='tweet_api'),
    url(r'^create/$', TweetCreateAPIView.as_view(), name='create_api'),
    url(r'^(?P<pk>[\d]+)/$', TweetRetrieveAPIView.as_view(), name='retrieve_api'),
    url(r'^(?P<pk>[\d]+)/retweet/$', RetweetAPIView.as_view(), name='retweet_api'),
]
