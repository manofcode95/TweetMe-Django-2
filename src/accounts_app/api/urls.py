from django.conf.urls import url, include
from tweets_app.api.views import TweetListAPIView

app_name='accounts_api'


urlpatterns = [
    url(r'^(?P<username>[\w]+)/$', TweetListAPIView.as_view(), name='user_api'),   
]
