from rest_framework import serializers
from .models import *   



class SpaceGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = SpaceGallery
        fields = "__all__"


class GalleryVideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryVideos
        fields = "__all__"


class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = "__all__"


class EventGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = EventGallery
        fields = "__all__"