from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import RegisterView 
from tweets_app.views import TweetListView
urlpatterns = [
    url(r'^$', TweetListView.as_view(), name='tweet_list'),
    url(r'^admin/', admin.site.urls),
    # tweets_app
    url(r'^tweet/', include('tweets_app.urls')),
    url(r'^api/tweet/', include('tweets_app.api.urls')),
    # hashtags_app
    url(r'^tag/', include('hashtags_app.urls')),
    url(r'^api/tag/', include('hashtags_app.api.urls')),
    # accounts
    url(r'^profile/', include('accounts_app.urls')),
    url(r'^api/profile/', include('accounts_app.api.urls')),
    url(r'^accounts/login/$', auth_views.login, name='login'),
    url(r'^accounts/logout/$', auth_views.logout, name='logout'),
    url(r'^accounts/register/$', RegisterView.as_view(), name='register'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)