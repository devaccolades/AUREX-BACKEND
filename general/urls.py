from django.urls import path

from .views import *

urlpatterns = [
    path('seo/', SeoListAPIView.as_view(), name='seo-list'),
    path("seo/<str:name>/", SeoRetrieveAPIView.as_view(), name="seo-detail"),
    path('blogs/', BlogListAPIView.as_view(), name='blog-list'),
    path('testimonials/', TestimAPIView.as_view(), name='testim-list'),
    path('v-testimonials/', VidTestimAPIView.as_view(), name='vid-testim-list'),
    path('aboutus/', AboutAPIView.as_view(), name='aboutus'),
    path("blogs/<str:slug>/", BlogRetrieveAPIView.as_view(), name="blog-detail"),
]
