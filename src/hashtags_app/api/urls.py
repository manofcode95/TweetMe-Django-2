from django.conf.urls import url, include

from .views import HashtagAPIView
app_name='hashtags_api'


urlpatterns = [
    url(r'^(?P<tag>[\w]+)/$', HashtagAPIView.as_view(), name='tag_api'),

]
