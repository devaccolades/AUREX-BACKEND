from django.urls import path

from .views import *
from projects import views

urlpatterns = [

    #projects
    path("projects/", views.ProjectsView.as_view(), name="projects"),
    path("projects/<slug:slug>/", views.ProjectsView.as_view(), name="projects-by-slug"),

    path("amenprities/", views.AmenitiesView.as_view(), name="amenities-list"),
    path("amenities/<slug:slug>/", views.AmenitiesView.as_view(), name="amenities-by-slug"),

    path("project-images/", views.ProjectImagesView.as_view(), name="project-images-list"),
    path("project-images/<slug:slug>/", views.ProjectImagesView.as_view(), name="project-images-by-slug"),
    
    path("common-facilities/", views.CommonFacilitiesView.as_view(), name="common-facilities"),
    path("common-facilities/<slug:slug>/", views.CommonFacilitiesView.as_view(), name="common-facilities-by-slug"),

    path("floor-plans/", views.FloorPlansView.as_view(),name="floor-plans"),
    path("floor-plans/<slug:slug>/", views.FloorPlansView.as_view(), name="floor-plans-by-slug"),

    path("specifications/", views.SpecificationsView.as_view(), name="specifications"),
    path("specifications/<slug:slug>/", views.SpecificationsView.as_view(), name="specifications-by-slug"),

    path("location-advantages/", views.LocationAdvantagesView.as_view(), name="location-advantages"),
    path("location-advantages/<slug:slug>/", views.LocationAdvantagesView.as_view(), name="location-advantages-by-slug"),

    path("youtube-videos/", views.YoutubeVideosView.as_view(), name="youtube-videos"),
    path("youtube-videos/<slug:slug>/", views.YoutubeVideosView.as_view(), name="youtube-videos-by-slug"),

    path("project-updates/", views.ProjectUpdatesView.as_view(), name="project-updates"),
    path("project-updates/<slug:slug>/", views.ProjectUpdatesView.as_view(), name="project-updates-by-slug"),
]
