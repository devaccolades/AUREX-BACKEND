from django.urls import path


from . import views

urlpatterns = [
    path('careers/', views.CareersViewset.as_view(), name='careers-list'),
    path("careers/<str:slug>/", views.CareerRetrieveAPIView.as_view(), name="careers-detail"),
    path('job-application/', views.JobApplicationPostAPIView.as_view(), name='job-application'),
]