from django.contrib import admin
from .models import *
from unfold.admin import ModelAdmin

# Register your models here.

@admin.register(SpaceGallery)
class SpaceGalleryAdmin(ModelAdmin):
    list_display = ("title", "date_added", "date_updated", "is_deleted")
    search_fields = ("title",)
    


@admin.register(GalleryVideos)
class GalleryVideosAdmin(ModelAdmin):
    list_display = (
        "id",
        "title_video_url",
        "main_video_url",
        "date_added", "date_updated", "is_deleted"
    )
    search_fields = ("title_video_url", "main_video_url")


@admin.register(Events)
class EventsAdmin(ModelAdmin):
    list_display = ("event_name", "date_added", "date_updated", "is_deleted")
    search_fields = ("event_name",)


@admin.register(EventGallery)
class EventGalleryAdmin(ModelAdmin):
    list_display = ("event", "date_added", "date_updated", "is_deleted")
    search_fields = ("event__event_name",)
    list_filter = ("event",)