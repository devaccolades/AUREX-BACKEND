from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import EmailMultiAlternatives
from rest_framework.parsers import MultiPartParser, FormParser
from django.template.loader import get_template
from django.conf import settings
from django.core.mail import send_mail

from .models import *
from .serializers import *

# Create your views here.

class ContactPostAPIView(APIView):
    def post(self, request):
        try:
            serializer = ContactFormSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                context = serializer.data
                template = get_template('Contact.html').render(context)
                send_mail(
                    'New Contact Submission on Aurex Builders',
                    None,
                    settings.EMAIL_HOST_USER,
                    ["manjima.accolades@gmail.com"], 
                    fail_silently=False,
                    html_message=template,
                )
                response_data = {
                    "StatusCode": 6001,
                    "detail": "success",
                    "data": serializer.data,
                    "message": "Submitted successfully"
                }
            else:
                response_data = {
                    "StatusCode": 6002,
                    "detail": "validation error",
                    "data": serializer.errors,
                    "message": ""
                }
        except Exception as e:
            response_data = {
                "StatusCode": 6002,
                "detail": "error",
                "data": "",
                "message": f'Something went wrong: {e}'
            }
        return Response(response_data, status=status.HTTP_200_OK)

class ProjectEnquiryPostAPIView(APIView):
    def post(self, request):
        try:
            serializer = ProjectEnquiryFormSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                context = serializer.data
                template = get_template('ProjectEnquiry.html').render(context)
                send_mail(
                    'New Project Enquiry Submission on Aurex Builders',
                    None,
                    settings.EMAIL_HOST_USER,
                    ["manjima.accolades@gmail.com"], 
                    fail_silently=False,
                    html_message=template,
                )
                response_data = {
                    "StatusCode": 6001,
                    "detail": "success",
                    "data": serializer.data,
                    "message": "Submitted successfully"
                }
            else:
                response_data = {
                    "StatusCode": 6002,
                    "detail": "validation error",
                    "data": serializer.errors,
                    "message": ""
                }
        except Exception as e:
            response_data = {
                "StatusCode": 6002,
                "detail": "error",
                "data": "",
                "message": f'Something went wrong: {e}'
            }
        return Response(response_data, status=status.HTTP_200_OK)