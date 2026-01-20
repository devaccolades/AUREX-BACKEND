from rest_framework import serializers
from .models import *


class IconsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Icons
        fields = "__all__"


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = "__all__"

class ProjectImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImages
        fields = "__all__"


class AmenitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenities
        fields = "__all__"


class CommonFacilitiesSerializer(serializers.ModelSerializer):
    icon = serializers.CharField(source="icon.name", read_only=True)
    class Meta:
        model = CommonFacilities
        fields = (
            "id",
            "name",
            "subtext",
            "icon",
        )


class FloorPlansSerializer(serializers.ModelSerializer):
    class Meta:
        model = FloorPlans
        fields = "__all__"


class SpecificationsSerializer(serializers.ModelSerializer):
    icon = serializers.CharField(source="icon.name", read_only=True)
    class Meta:
        model = Specifications
        fields = (
            "id",
            "title",
            "description",
            "icon",
        )


class LocationAdvantagesSerializer(serializers.ModelSerializer):
    icon = serializers.CharField(source="icon.name", read_only=True)
    class Meta:
        model = LocationAdvantages
        fields = (
            "id",
            "category",
            "icon",
            "advantage_1",
            "distance_1",
            "advantage_2",
            "distance_2",
            "advantage_3",
            "distance_3",
            "advantage_4",
            "distance_4",
            "advantage_5",
            "distance_5",
        )


class YoutubeVideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = YoutubeVideos
        fields = "__all__"


class ProjectUpdatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectUpdates
        fields = "__all__"
