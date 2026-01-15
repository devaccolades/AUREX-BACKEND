from django.db import models
from projects.models import *
from django.core.exceptions import ValidationError

# Create your models here.
class SpaceGallery(BaseModel):
    title = models.CharField(max_length=255, blank=True, null=True)
    image = models.FileField(upload_to='projects/gallery', blank=True, null=True)
    image_alt = models.CharField(max_length=125, null=True, blank=True)

    class Meta:
        verbose_name = "Space Gallery"
        verbose_name_plural = "Space Gallery"

    def __str__(self):
        return f"Gallery Image for {self.title}"
    
class GalleryVideos(BaseModel):
    title_video_url = models.CharField(max_length=1500, blank=True, null=True)  
    title_video_thumbnail = models.FileField(upload_to='projects/gallery/gallery/thumbnails', blank=True, null=True)
    title_video_alt = models.CharField(max_length=125, null=True, blank=True)
    main_video_url = models.CharField(max_length=1500, blank=True, null=True)  
    main_video_thumbnail = models.FileField(upload_to='projects/gallery/main/thumbnails', blank=True, null=True)
    main_video_alt = models.CharField(max_length=125, null=True, blank=True)

    class Meta:
        verbose_name = "Gallery Videos"
        verbose_name_plural = "Gallery Videos"

    def clean(self):
        existing_cards = GalleryVideos.objects.exclude(id=self.id).count()
        if existing_cards >= 1:         
            raise ValidationError("Cannot create more than 1 Gallery Videos.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
    
class Events(BaseModel):
    event_name = models.CharField(max_length=255, blank=True, null=True)  

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"

    def __str__(self):
        return f"{self.event_name}"
    
class EventGallery(BaseModel):
    event = models.ForeignKey(Events, on_delete=models.CASCADE, related_name='event_galleries')
    image = models.FileField(upload_to='projects/events/gallery', blank=True, null=True)
    image_alt = models.CharField(max_length=125, null=True, blank=True)

    class Meta:
        verbose_name = "Event Gallery"
        verbose_name_plural = "Event Gallery"

    def __str__(self):
        return f"Gallery Image for {self.event.event_name}"