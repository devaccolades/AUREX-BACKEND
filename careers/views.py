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
class CareersViewset(APIView):
    serializer_class = CareerSerializer

    def get(self, request):
        try:
            data = Careers.objects.filter(is_deleted=False)
            serializer = self.serializer_class(data, many=True, context={"request": request})
            return Response(serializer.data)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class JobApplicationPostAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    def post(self, request):
        try:
            print(request.data, "checking the data")
            serializer = JobApplicationSerializer(data=request.data, context={'request': request})
            if serializer.is_valid():
                instance = serializer.save()

                context = {
                    'job_name': instance.position,
                    'name': instance.name,
                    'email': instance.email,
                    'number': instance.number,
                    'location': instance.location,
                    'date_added': instance.date_added,
                }

                html_content = get_template('JobApplication.html').render(context)
                subject = 'Enquiry for abe-education'
                from_email = settings.EMAIL_HOST_USER
                to_email =  ["manjima.accolades@gmail.com"]

                msg = EmailMultiAlternatives(subject, '', from_email, to_email)
                msg.attach_alternative(html_content, "text/html")

                
                if instance.cv_file:
                    cv_path = instance.cv_file.path
                    msg.attach_file(cv_path)


                # Send the email
                msg.send()

                response_data = {
                    "StatusCode": 6001,
                    "detail": "success",
                    "data": serializer.data,
                    "message": "Job Application successfully"
                }
            else:
                response_data = {
                    "StatusCode": 6002,
                    "detail": "validation error",
                    "data": serializer.errors,
                    "message": "Invalid data"
                }

        except Exception as e:
            response_data = {
                "StatusCode": 6002,
                "detail": "error",
                "data": "",
                "message": f'Something went wrong: {e}'
            }

        return Response(response_data, status=status.HTTP_200_OK)