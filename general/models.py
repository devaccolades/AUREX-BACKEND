from django.db import models
from django.core.files.base import File
from PIL import Image
from io import BytesIO
import os
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from datetime import datetime


class Seo(models.Model):
    page = models.CharField(max_length=255)
    meta_title = models.CharField(max_length=255)
    meta_description = models.TextField()
    og_image = models.ImageField(upload_to="seo/og/", blank=True, null=True)
    og_title = models.CharField(max_length=255, blank=True, null=True)
    og_description = models.TextField(blank=True, null=True)
    def save(self, *args, **kwargs):

        # Save original first to get file path
        super().save(*args, **kwargs)

        if self.og_image:
            original_path = self.og_image.path
            img = Image.open(self.og_image)

            if img.mode != "RGB":
                img = img.convert("RGB")

            # Optional: Resize if very large (uncomment if needed)
            # max_size = (1920, 1920)
            # img.thumbnail(max_size, Image.ANTIALIAS)

            # Save WebP version in memory
            webp_io = BytesIO()
            img.save(webp_io, format='WebP', quality=70, method=6, optimize=True)

            # Generate .webp filename
            original_filename = os.path.basename(self.og_image.name)
            base, _ = os.path.splitext(original_filename)
            new_filename = f"{base}.webp"

            # Replace the image with optimized WebP version
            self.og_image.save(new_filename, File(webp_io), save=False)

            # Remove original file if not WebP
            if os.path.exists(original_path) and not original_path.endswith('.webp'):
                os.remove(original_path)

            # Save the instance again with updated image
            super().save(update_fields=['og_image'])

    class Meta:
        verbose_name_plural = "SEO data"

    def __str__(self):
        return self.page
    
from django.core.validators import MinValueValidator, MaxValueValidator

#  about us
class Testimonial(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="testimonials/", blank=True, null=True)
    description = models.TextField()
    job = models.CharField(max_length=255,blank=True, null=True)
    rating = models.FloatField(
        blank=True,
        null=True,
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],
        help_text="Enter a rating between 0 and 5"
    )
    def __str__(self):
        return self.name

class VideoTestimonial(models.Model):
    """For video testimonials (vertical/portrait videos)"""
    name = models.CharField(max_length=255)
    video = models.FileField(
        upload_to="testimonials/videos/",
        help_text="Upload a vertical (portrait) video testimonial — e.g., 9:16 aspect ratio."
    )
    job = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Video Testimonial - {self.name}"


class AboutUs(models.Model):
    address = models.TextField()
    phone1 = models.CharField(max_length=20)
    phone2 = models.CharField(max_length=20)
    email = models.EmailField()
    copyright_year = models.CharField(max_length=25)

    linkedin = models.URLField(max_length=255, blank=True, null=True)
    instagram = models.URLField(max_length=255, blank=True, null=True)
    telegram = models.URLField(max_length=255, blank=True, null=True)
    youtube = models.URLField(max_length=255, blank=True, null=True)
    x_link = models.URLField("X (Twitter) Link", max_length=255, blank=True, null=True)
    map_url = models.URLField(max_length=500, blank=True, null=True)

    class Meta:
        verbose_name_plural = "About Us"

    def __str__(self):
        return "About Us"


class FAQ(models.Model):
    page_name = models.CharField(max_length=255, blank=True, null=True)  # e.g. "Admissions"
    question = models.CharField(max_length=500)
    answer = models.TextField()
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"

    def __str__(self):
        return self.question



class Blog(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="blogs/covers/", blank=True, null=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)  # blank=True to allow setting it in save()
    content = RichTextField()
    date_added = models.DateField(auto_now_add=True)
    meta_title = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Optional SEO title (defaults to blog title)"
    )
    meta_description = models.TextField(
        blank=True,
        null=True,
        help_text="Optional SEO description"
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            date_part = self.date_added.strftime("%Y-%m-%d") if self.date_added else datetime.now().strftime("%Y-%m-%d")
            base_slug = slugify(f"{self.title}-{date_part}")[:50]
            slug = base_slug
            counter = 1
            while Blog.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                # Add suffix with counter, making sure total length <= 50
                suffix = f"-{counter}"
                slug = base_slug[:50 - len(suffix)] + suffix
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
