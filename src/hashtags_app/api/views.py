from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.pagination import PageNumberPagination
from hashtags_app.models import Hashtag
from tweets_app.models import Tweet
from django.db.models import Q
from django.contrib.auth import get_user_model
from tweets_app.api.serializers import TweetSerializer

User=get_user_model()
class HashtagAPIView(generics.ListCreateAPIView):
    serializer_class=TweetSerializer
    permission_classes = (IsAdminUser,)
    pagination_class= PageNumberPagination 

    def get_queryset(self, **kwargs):
        tag=self.kwargs.get('tag')
        hashtag=None
        if tag:
            hashtag , created = Hashtag.objects.get_or_create(regex=tag)
            

        qs=hashtag.get_tweet()
        return qs


