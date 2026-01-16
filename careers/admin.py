from django.contrib import admin
from .models import *
from unfold.admin import ModelAdmin

# Register your models here.
@admin.register(Careers)
class CareersAdmin(ModelAdmin):
    list_display = ('ordering_priority', 'job_title', 'type', 'location', 'date_added', 'date_updated', 'is_deleted')
    search_fields = ('ordering_priority', 'job_title', 'type', 'location')
    list_filter = ('date_added', 'is_deleted')


@admin.register(JobApplicationForm)
class JobApplicationFormAdmin(ModelAdmin):
    list_display = ('name', 'position', 'email', 'date_added', 'date_updated', 'is_deleted')
    search_fields = ('name', 'position', 'email')
    list_filter = ('date_added', 'is_deleted')