from rest_framework import serializers
from .models import *


class ContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactForm
        fields = '__all__'

class ProjectEnquiryFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectEnquiryForm
        fields = '__all__'