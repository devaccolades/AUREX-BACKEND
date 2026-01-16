from django.contrib import admin

from unfold.admin import ModelAdmin
from .models import *


@admin.register(ContactForm)
class ContactFormAdmin(ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message', 'date_added', 'date_updated', 'is_deleted')
    search_fields = ('name', 'email', 'phone', 'message')
    list_filter = ('date_added', 'is_deleted')

@admin.register(ProjectEnquiryForm)
class ProjectEnquiryFormAdmin(ModelAdmin):
    list_display = ('name', 'email', 'phone', 'project', 'preferred_unit', 'date_added', 'date_updated', 'is_deleted')
    search_fields = ('name', 'email', 'phone', 'project', 'preferred_unit')
    list_filter = ('date_added', 'is_deleted')
