from django.contrib import admin
from .models import (
    Icons,
    Projects,
    Amenities,
    CommonFacilities,
    FloorPlans,
    Specifications,
    LocationAdvantages,
    YoutubeVideos,
    ProjectUpdates,
    ProjectImages,
)
from unfold.admin import ModelAdmin


@admin.register(Icons)
class IconsAdmin(ModelAdmin):
    list_display = ("name", "date_added", "date_updated", "is_deleted")
    search_fields = ("name",)
    list_filter = ("date_added", "is_deleted")


@admin.register(Projects)
class ProjectsAdmin(ModelAdmin):
    list_display = ("name", "location", "status", "project_type", "date_added", "is_deleted")
    search_fields = ("name", "location", "status", "project_type")
    list_filter = ("status", "date_added", "is_deleted")
    prepopulated_fields = {"slug": ("name",)}

@admin.register(ProjectImages)
class ProjectImagesAdmin(ModelAdmin):
    list_display = ("project", "image", "date_added", "is_deleted")
    search_fields = ("project__name",)
    list_filter = ("date_added", "is_deleted")

@admin.register(Amenities)
class AmenitiesAdmin(ModelAdmin):
    list_display = ("project", "name", "date_added", "is_deleted")
    search_fields = ("name", "project__name")
    list_filter = ("date_added", "is_deleted")


@admin.register(CommonFacilities)
class CommonFacilitiesAdmin(ModelAdmin):
    list_display = ("project", "name", "icon", "date_added", "is_deleted")
    search_fields = ("name", "project__name")
    list_filter = ("date_added", "is_deleted")


@admin.register(FloorPlans)
class FloorPlansAdmin(ModelAdmin):
    list_display = ("project", "bhk_type", "plan_type", "date_added", "is_deleted")
    search_fields = ("project__name", "plan_type", "bhk_type")
    list_filter = ("bhk_type", "date_added", "is_deleted")


@admin.register(Specifications)
class SpecificationsAdmin(ModelAdmin):
    list_display = ("project", "title", "icon", "date_added", "is_deleted")
    search_fields = ("title", "project__name")
    list_filter = ("date_added", "is_deleted")


@admin.register(LocationAdvantages)
class LocationAdvantagesAdmin(ModelAdmin):
    list_display = ("project", "category", "icon", "date_added", "is_deleted")
    search_fields = ("category", "project__name")
    list_filter = ("date_added", "is_deleted")


@admin.register(YoutubeVideos)
class YoutubeVideosAdmin(ModelAdmin):
    list_display = ("project", "video_url", "date_added", "is_deleted")
    search_fields = ("project__name", "video_url")
    list_filter = ("date_added", "is_deleted")


@admin.register(ProjectUpdates)
class ProjectUpdatesAdmin(ModelAdmin):
    list_display = ("project", "date", "date_added", "is_deleted")
    search_fields = ("project__name",)
    list_filter = ("date", "date_added", "is_deleted")
