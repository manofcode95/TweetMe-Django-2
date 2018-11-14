from django.conf.urls import url, include
from .views import TweetListView, TweetDetailView, TweetCreateView, TweetUpdateView, TweetDeleteView
app_name='tweets_app'
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^list/$', RedirectView.as_view(url='/')),
    url(r'^create/$', TweetCreateView.as_view(), name='tweet_create'),
    url(r'^(?P<pk>[\d]+)/$', TweetDetailView.as_view(), name='tweet_detail'),
    url(r'^(?P<pk>[\d]+)/update/$', TweetUpdateView.as_view(), name='tweet_update'),
    url(r'^(?P<pk>[\d]+)/delete/$', TweetDeleteView.as_view(), name='tweet_delete'),
]
