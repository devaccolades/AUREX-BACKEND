from django.db import models
from projects.models import *

# Create your models here.
class ContactForm(BaseModel):
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=18, blank=True, null=True)
    message = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Contact Form'
        verbose_name_plural = 'Contact Forms'
        ordering = ('-date_added',)


    def __str__(self):
        return f"Contact Form by {self.name}"
    
class ProjectEnquiryForm(BaseModel):
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=18, blank=True, null=True)
    project = models.CharField(max_length=255, null=True, blank=True)
    preferred_unit = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = 'Project Enquiry Form'
        verbose_name_plural = 'Project Enquiries'
        ordering = ('-date_added',)


    def __str__(self):
        return f"Project Enquiry by {self.name} for {self.project}"