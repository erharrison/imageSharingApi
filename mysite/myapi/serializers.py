from rest_framework import serializers
from .models import ImagePost


class ImagePostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ImagePost
        fields = ('id', 'image', 'caption', 'author', 'upload_date', 'likes', 'dislikes')
