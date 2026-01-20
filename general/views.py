from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404



class SeoListAPIView(APIView):
    serializer_class = Seoserializer

    def get(self, request):
        seo = Seo.objects.all()
        serializer = self.serializer_class(seo, many=True,context={"request": request})
        return Response(serializer.data)


class SeoRetrieveAPIView(APIView):
    serializer_class = Seoserializer

    def get(self, request, name):
        """Retrieve a single university by id."""
        seo= get_object_or_404(Seo, page=name)
        serializer = self.serializer_class(seo, context={"request": request})
        return Response(serializer.data)

#   blog
class BlogListAPIView(APIView):
    serializer_class = Blogerializer

    def get(self, request):
        blogs = Blog.objects.all()
        serializer = self.serializer_class(blogs, many=True,context={"request": request})
        return Response(serializer.data)


#   blog
class TestimAPIView(APIView):
    serializer_class = Testimserializer

    def get(self, request):
        blogs = Testimonial.objects.all()
        serializer = self.serializer_class(blogs, many=True,context={"request": request})
        return Response(serializer.data)


class VidTestimAPIView(APIView):
    serializer_class = VidTestimserializer

    def get(self, request):
        blogs = VideoTestimonial.objects.all()
        serializer = self.serializer_class(blogs, many=True,context={"request": request})
        return Response(serializer.data)    
    

class BlogRetrieveAPIView(APIView):
    serializer_class = Blogerializer

    def get(self, request, slug):
        """Retrieve a single university by id."""
        blog= get_object_or_404(Blog, slug=slug)
        serializer = self.serializer_class(blog, context={"request": request})
        return Response(serializer.data)

class AboutAPIView(APIView):
    serializer_class = Aboutserializer

    def get(self, request):
        ab = AboutUs.objects.all()
        serializer = self.serializer_class(ab, many=True,context={"request": request})
        return Response(serializer.data)    


#   faq
class FaqListAPIView(APIView):
    serializer_class = Faqserializer

    def get(self, request):
        blogs = FAQ.objects.all()
        serializer = self.serializer_class(blogs, many=True,context={"request": request})
        return Response(serializer.data)

