from rest_framework import serializers
from hashtags_app.models import Hashtag
class HashtagSerializer(serializers.ModelSerializer):
    class Meta:
        model=Hashtag
        fields=['regex']