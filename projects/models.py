from django.db import models
from django.utils import timezone
import uuid

# Create your models here.
class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_added = models.DateTimeField(db_index=True, default=timezone.now, editable=True)
    date_updated = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False, db_index=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.date_added:
            self.date_added = timezone.now()
        super(BaseModel, self).save(*args, **kwargs)

class Icons(BaseModel):
    name = models.CharField(max_length=200, blank=True, null=True)  

    class Meta:
        verbose_name = "Icons"
        verbose_name_plural = "I.Icons"
        ordering = ('-date_added',)

    def __str__(self):
        return self.name

PROJECT_CHOICES = (
        ("Commercial", "Commercial"),
        ("Residential", "Residential"),
        ("Contracts", "Contracts"),
    )

PROJECT_STATUS_CHOICES = (
    ('completed', 'Completed'),
    ('upcoming', 'Upcoming'),
    ('ready to occupy', 'Ready to Occupy'),
    ('ongoing', 'Ongoing'),
)

class Projects(BaseModel):
    name = models.CharField(max_length=255, blank=True, null=True)  
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    project_type = models.CharField( max_length=100, choices=PROJECT_CHOICES, blank=True, null=True) 
    logo = models.FileField(upload_to='projects/logos', blank=True, null=True)
    logo_alt = models.CharField(max_length=125, null=True, blank=True)
    qr_code = models.ImageField(upload_to='projects/qr', blank=True, null=True)
    location = models.CharField(max_length=500, blank=True, null=True)
    land_mark = models.CharField(max_length=225, null=True, blank=True)
    map_iframe = models.TextField(null=True, blank=True)
    sub_text = models.CharField(max_length=200, blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='projects/images', blank=True, null=True)
    image_alt = models.CharField(max_length=125, null=True, blank=True)
    status = models.CharField(choices=PROJECT_STATUS_CHOICES, max_length=255, blank=True, null=True)
    k_rera = models.CharField(max_length=100, blank=True, null=True)
    property_type = models.CharField(max_length=100, blank=True, null=True)
    total_area = models.CharField(max_length=100, blank=True, null=True )
    total_units = models.CharField(max_length=100, blank=True, null=True)
    sqft_range = models.CharField(max_length=100, blank=True, null=True) 
    brochure = models.FileField(upload_to='projects/brochure',blank=True,null=True)
    highlight_1 = models.CharField(max_length=255, blank=True, null=True)
    highlight_text_1 = models.CharField(max_length=100, blank=True, null=True)
    highlight_2 = models.CharField(max_length=255, blank=True, null=True)
    highlight_text_2 = models.CharField(max_length=100, blank=True, null=True) 
    highlight_3 = models.CharField(max_length=255, blank=True, null=True)
    highlight_text_3 = models.CharField(max_length=100, blank=True, null=True)
    meta_title = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True) 
    
    class Meta:
        verbose_name = "Projects"
        verbose_name_plural = "A.Projects"
        ordering = ('-date_added',)

    def __str__(self):
        return self.name 


    
class Amenities(BaseModel):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='amenities')
    name = models.CharField(max_length=200, blank=True, null=True)  
    subtext = models.CharField(max_length=200, blank=True, null=True)
    image = models.FileField(upload_to='projects/amenities/icons', blank=True, null=True)
    image_alt = models.CharField(max_length=125, null=True, blank=True)

    class Meta:
        verbose_name = "Amenities"
        verbose_name_plural = "B.Amenities"
        ordering = ('-date_added',)

    def __str__(self):
        return f"{self.project.name} - {self.name}"
    
class CommonFacilities(BaseModel):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='common_facilities', blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)  
    subtext = models.CharField(max_length=200, blank=True, null=True)
    icon = models.ForeignKey(Icons, on_delete=models.CASCADE, related_name='common_facilities', blank=True, null=True)

    class Meta:
        verbose_name = "Common Facilities"
        verbose_name_plural = "C.Common Facilities"
        ordering = ('-date_added',)

    def __str__(self):
        return f"{self.project.name} - {self.name}"

BHK_CHOICES = (
        ("2BHK", "2 BHK"),
        ("3BHK", "3 BHK"),
        ("4BHK", "4 BHK"),
    )
   
class FloorPlans(BaseModel):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='floor_plans')
    bhk_type = models.CharField( max_length=10, choices=BHK_CHOICES, blank=True, null=True) 
    image = models.FileField(upload_to='projects/floorplans/images', blank=True, null=True)
    image_alt = models.CharField(max_length=125, null=True, blank=True)
    plan_type = models.CharField(max_length=50, help_text="Eg: Type A, Type B, Type D", blank=True, null=True)
    area_label = models.CharField(max_length=100, blank=True, null=True)
    

    class Meta:
        verbose_name = "Floor Plans"
        verbose_name_plural = "D.Floor Plans"
        ordering = ('-date_added',)

    def __str__(self):
        return f"{self.project.name}"
    
class Specifications(BaseModel):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='specifications')
    title = models.CharField(max_length=250, blank=True, null=True)  
    description = models.TextField(blank=True, null=True)
    icon = models.ForeignKey(Icons, on_delete=models.CASCADE,blank=True, null=True)

    class Meta:
        verbose_name = "Specifications"
        verbose_name_plural = "E.Specifications"
        ordering = ('-date_added',)

    def __str__(self):
        return f"{self.project.name} - {self.title}"
    
class LocationAdvantages(BaseModel):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='location_advantages')
    category = models.CharField(max_length=250, blank=True, null=True)  
    icon = models.ForeignKey(Icons, on_delete=models.CASCADE, blank=True, null=True)
    advantage_1 = models.CharField(max_length=250, blank=True, null=True)  
    distance_1 = models.CharField(max_length=250, blank=True, null=True)
    advantage_2 = models.CharField(max_length=250, blank=True, null=True)
    distance_2 = models.CharField(max_length=250, blank=True, null=True)
    advantage_3 = models.CharField(max_length=250, blank=True, null=True)  
    distance_3 = models.CharField(max_length=250, blank=True, null=True)
    advantage_4 = models.CharField(max_length=250, blank=True, null=True)
    distance_4 = models.CharField(max_length=250, blank=True, null=True)
    advantage_5 = models.CharField(max_length=250, blank=True, null=True)
    distance_5 = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        verbose_name = "Location Advantages"
        verbose_name_plural = "F.Location Advantages"
        ordering = ('-date_added',)

    def __str__(self):
        return f"{self.project.name} - {self.category}"
    
class YoutubeVideos(BaseModel):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='youtube_videos')
    video_url = models.CharField(max_length=1500, blank=True, null=True)  

    class Meta:
        verbose_name = "YouTube Videos"
        verbose_name_plural = "G.YouTube Videos"
        ordering = ('-date_added',)

    def __str__(self):
        return f"{self.project.name} - {self.video_url}"
    
class ProjectUpdates(BaseModel):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='project_updates')
    date = models.DateField(blank=True, null=True)
    image = models.FileField(upload_to='projects/updates/images', blank=True, null=True)
    image_alt = models.CharField(max_length=125, null=True, blank=True)

    class Meta:
        verbose_name = "Project Updates"
        verbose_name_plural = "H.Project Updates"
        ordering = ('-date_added',)

    def __str__(self):
        return f"{self.project.name} - {self.date}"   
    
class ProjectImages(BaseModel):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='project_images')
    image = models.FileField(upload_to='projects/gallery/images', blank=True, null=True)
    image_alt = models.CharField(max_length=125, null=True, blank=True)

    class Meta:
        verbose_name = "Project Images"
        verbose_name_plural = "I.Project Images"
        ordering = ('-date_added',)

    def __str__(self):
        return f"{self.project.name} - Image"