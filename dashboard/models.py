from django.utils import timezone
from django.db import models

from django.contrib.auth.models import User

from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    badge = models.CharField(max_length=255, blank=True)
    bio = models.CharField( max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True)
    job = models.CharField(max_length=255, null=True)
    image = models.ImageField(upload_to='user_images', blank=True, null=True)


    def __str__(self):
        return str(self.user)

class Events(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255, blank=True)
    image = models.ImageField(upload_to='event_images', blank=True, null=True)
    duration = models.CharField(null=True, blank=True, max_length=255)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Events'

    def __str__(self):
        return str(self.title)


class Info(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    status = models.BooleanField(default=False, help_text="Read")
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title
