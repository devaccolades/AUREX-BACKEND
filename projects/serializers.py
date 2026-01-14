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


class AmenitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenities
        fields = "__all__"


class CommonFacilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommonFacilities
        fields = "__all__"


class FloorPlansSerializer(serializers.ModelSerializer):
    class Meta:
        model = FloorPlans
        fields = "__all__"


class SpecificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specifications
        fields = "__all__"


class LocationAdvantagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationAdvantages
        fields = "__all__"


class YoutubeVideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = YoutubeVideos
        fields = "__all__"


class ProjectUpdatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectUpdates
        fields = "__all__"
