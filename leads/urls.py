from django.urls import path

from . import views

urlpatterns = [
    path('contact/', views.ContactPostAPIView.as_view(), name='contact'),
    path('project-enquiry/', views.ProjectEnquiryPostAPIView.as_view(), name='project-enquiry'),

]