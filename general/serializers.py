from rest_framework import serializers
from .models import *

class Seoserializer(serializers.ModelSerializer):
    class Meta:
        model = Seo
        fields = "__all__"

class Blogerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"


class Testimserializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = "__all__"

class VidTestimserializer(serializers.ModelSerializer):
    class Meta:
        model = VideoTestimonial
        fields = "__all__"


class Aboutserializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = "__all__"


class Faqserializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = "__all__"