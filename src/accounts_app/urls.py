from django.conf.urls import url, include
from .views import UserDetailView, ToggleFollowView


app_name='profiles_app'
urlpatterns = [
    url(r'^(?P<username>[\w]+)/$', UserDetailView.as_view(), name='user_detail'),
    url(r'^(?P<username>[\w]+)/follow/$', ToggleFollowView.as_view(), name='toggle_follow'),
]
