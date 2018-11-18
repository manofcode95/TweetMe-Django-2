from django.conf.urls import url, include
from .views import HashtagView

app_name='hashtags_app'
urlpatterns = [
    url(r'^(?P<tag>[\w]+)/$', HashtagView.as_view(), name='hashtag_view')
    
]