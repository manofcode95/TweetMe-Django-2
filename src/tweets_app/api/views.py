from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .serializers import TweetSerializer
from tweets_app.models import Tweet
class TweetListAPIView(generics.ListAPIView):
    serializer_class=TweetSerializer
    permission_classes = (IsAdminUser,)

    def get_queryset(self):
        qs=Tweet.objects.all()
        query=self.request.GET.get('q')
        if query:
            qs=qs.filter(Q(user__username__icontains=query)|
                         Q(content__icontains=query))
        return qs

class TweetCreateAPIView(generics.CreateAPIView):
    serializer_class=TweetSerializer
    queryset= Tweet.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TweetRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class=TweetSerializer
    queryset= Tweet.objects.all()


class RetweetAPIView(APIView):
    permission_classes = (IsAdminUser,)
    def get(self, request, pk):
        tweet=Tweet.objects.filter(pk=pk)
        if tweet:
            retweet=Tweet.objects.retweet(self.request.user, tweet.first())
            data=TweetSerializer(retweet).data
            return Response(data)
        return Response(None, status=400)
