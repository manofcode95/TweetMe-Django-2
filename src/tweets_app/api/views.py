from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from django.db.models import Q

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


