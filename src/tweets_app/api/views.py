from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .serializers import TweetSerializer
from tweets_app.models import Tweet
class TweetListAPIView(generics.ListAPIView):
    serializer_class=TweetSerializer
    permission_classes = (IsAdminUser,)
    pagination_class= PageNumberPagination 

    def get_queryset(self, **kwargs):
        username=self.kwargs.get('username')
        if username:
            qs=Tweet.objects.get_queryset().filter(user__username=username)
        else:
            qs=Tweet.objects.filter(Q(user__in=self.request.user.profile.get_following()) |
                                    Q(user=self.request.user))
        query=self.request.GET.get('q')
        if query:
            qs=qs.filter(Q(user__username__icontains=query)|
                         Q(content__icontains=query))
        return qs


    def get_serializer_context(self, *args, **kwargs):
        context=super(TweetListAPIView, self).get_serializer_context(*args, **kwargs)
        context['currentuser']=self.request.user
        return context

class TweetCreateAPIView(generics.CreateAPIView):
    serializer_class=TweetSerializer
    queryset= Tweet.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TweetRetrieveAPIView(generics.ListAPIView):
    serializer_class=TweetSerializer
    permission_classes = (IsAdminUser,)
    pagination_class= PageNumberPagination 

    def get_queryset(self, *kwargs):
        obj_pk=self.kwargs.get('pk')
        tweet_obj=Tweet.objects.filter(pk=obj_pk).first()
        if tweet_obj:
            qs=tweet_obj.get_children()
        return qs

class RetweetAPIView(APIView):
    permission_classes = (IsAdminUser,)
    def get(self, request, pk):
        tweet=Tweet.objects.filter(pk=pk).first()
        if tweet:
            the_retweet=Tweet.objects.retweet(self.request.user, tweet)
            data=TweetSerializer(the_retweet).data
            print(the_retweet)
            return Response(data)
        return Response(None, status=400)

class LikeAPIView(APIView):
    permission_classes = (IsAdminUser,)
    def get(self, request, pk):
        tweet=Tweet.objects.filter(pk=pk).first()
        if tweet:
            is_liked=Tweet.objects.do_like(request.user, tweet)
            return Response({'is_liked':is_liked})
        return Response(None, status=400)
    
    