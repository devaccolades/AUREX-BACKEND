from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import *
from django import forms
from unfold.contrib.forms.widgets import WysiwygWidget
from .forms import *
from django.contrib.auth.models import Group, User
# Register your models here.

# Unregister the Group model
admin.site.unregister(Group)

# Unregister the User model
admin.site.unregister(User)

@admin.register(Seo)
class SeoAdmin(ModelAdmin):

    fieldsets = (
        ("SEO", {
            "classes": ("tab-seo",),
            "fields": ("page", "meta_title", "meta_description"),
        }),
        ("Open Graph", {
            "classes": ("tab-og",),
            "fields": ("og_image", "og_title", "og_description"),
        }),
    )

    tabs = [
        ("SEO", "tab-seo"),
        ("OG Tags", "tab-og"),
    ]


@admin.register(AboutUs)
class AboutusAdmin(ModelAdmin):
    list_display = ("email",)
    fieldsets = (
        ("General", {
            "classes": ("tab-gen",),
            "fields": ("address","map_url","phone1","phone2", "email"),
        }),
        ("Social links", {
            "classes": ("tab-soc",),
            "fields": ("linkedin", "instagram", "x_link","telegram","youtube"),
        }),

    )

    tabs = [
        ("General", "tab-gen"),
        ("Social links", "tab-soc"),
    ]



@admin.register(Testimonial)
class TestimonialAdmin(ModelAdmin):
    list_display = ("name", "job","rating")
    search_fields = ("job", "name",)


@admin.register(VideoTestimonial)
class VideoTestimonialAdmin(ModelAdmin):
    list_display = ("name", "job",)
    search_fields = ("job", "name",)



class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        widgets = {
            'content': WysiwygWidget(),
        }

@admin.register(Blog)
class BlogAdmin(ModelAdmin):
    exclude = ("slug","date_added")
    form = BlogForm

@admin.register(FAQ)
class FaqAdmin(ModelAdmin):
    pass
