from django.urls import path

from . import views
# from gallery import views
urlpatterns = [
    path("space-gallery/", views.SpaceGalleryView.as_view(), name="space-gallery"),

    path("gallery-videos/", views.GalleryVideosView.as_view(), name="gallery-videos"),

    path("events/", views.EventsView.as_view(), name="events"),

    path("event-gallery/", views.EventGalleryView.as_view(), name="event-gallery"),
    path("event-gallery/<uuid:event_id>/",views.EventGalleryView.as_view(),name="event-gallery-by-event"),
]