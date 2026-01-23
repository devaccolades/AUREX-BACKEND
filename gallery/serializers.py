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


# class EventGallerySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = EventGallery
#         fields = "__all__"
class EventGallerySerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = EventGallery
        fields = "__all__"

    def get_image(self, obj):
        if obj.image:
            request = self.context.get("request")
            return request.build_absolute_uri(obj.image.url) if request else obj.image.url
        return None