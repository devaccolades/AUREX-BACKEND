from django.urls import path


from . import views

urlpatterns = [
    path('careers/', views.CareersViewset.as_view(), name='careers-list'),
    path('job-application/', views.JobApplicationPostAPIView.as_view(), name='job-application'),
]