from django.db import models
from projects.models import *
from ckeditor.fields import RichTextField

# Create your models here.
CAREER_TYPE_CHOICES = (
    ('Full time', 'Full time'),
    ('Part time', 'Part time'),
    ('Hybrid', 'Hybrid'),
    ('Remote', 'Remote'),
    ('Freelancer', 'Freelancer'),
)

class Careers(BaseModel):
    ordering_priority = models.PositiveIntegerField(default=0, blank=True, null=True, help_text="Order of the jobs for display purposes")
    job_title = models.CharField(max_length=300, blank=True, null=True)
    type = models.CharField(choices=CAREER_TYPE_CHOICES, max_length=255, blank=True, null=True)
    job_overview =  models.TextField(blank=True, null=True, help_text="Job description")
    location = models.CharField(max_length=255, blank=True, null=True)
    experience = models.CharField(max_length=255, blank=True, null=True)
    key_responsibilities = models.TextField(blank=True, null=True, help_text="Job responsibilities use comma to separate")
    requirements = models.TextField(blank=True, null=True, help_text="Job requirements use comma to separate")

    class Meta:
        verbose_name = ('Careers')
        verbose_name_plural = ('Careers')
        ordering = ['ordering_priority']

    def __str__(self):
        return self.job_title if self.job_title else str(self.id)
    

class JobApplicationForm(BaseModel):
    name = models.CharField(max_length=255, blank=  True, null=True)
    position = models.CharField(blank=True, null=True, max_length=255)
    email = models.EmailField()
    number = models.PositiveBigIntegerField(blank=True, null=True)
    cv_file = models.FileField(upload_to='cvs/')
    cover_letter = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = ('Job Application')
        verbose_name_plural = ('Job Applications Enquiry')
        ordering = ('-date_added',)

    def __str__(self):
        return f"{self.name} - {self.position}"