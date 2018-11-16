from django.conf.urls import url, include
from .views import HashtagListView

app_name='hashtags_app'
urlpatterns = [
    url(r'^(?P<tag>[\w]+)/$', HashtagListView.as_view(), name='hashtag_view')
    
]