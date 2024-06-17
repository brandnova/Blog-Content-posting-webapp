from django.utils import timezone
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


from django.contrib.auth.models import User

# from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class Todo(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField(max_length=255)
    tag = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.user.username}: {self.content[:20]}..."  
    
class Review(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255, null = True)
    comment = models.TextField(max_length=500, null = True)
    image = models.ImageField(upload_to='review_images', blank=True, null=True)

    
    def __str__(self):
        return self.name
    
class Team(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    image = models.ImageField(upload_to='team_images', blank=True, null=True)
    port_link = models.CharField(max_length=500, blank=True)


    def __str__(self):
        return self.name
    
class Messages(models.Model):
    user = models.ForeignKey(User, related_name='message', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField(max_length=500)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Messages'

    def __str__(self):
        return str(self.user)
    
class ContactInfo(models.Model):
    name = models.CharField(null=True, max_length=255)
    icon = models.TextField(null=True, max_length=255)
    content = models.CharField(null=True, max_length=255)

    def __str__(self):
        return self.name
    
class AboutInfo(models.Model):
    name = models.CharField(null=True, max_length=255)
    icon = models.TextField(null=True, max_length=255)
    content = models.CharField(null=True, max_length=255)

    def __str__(self):
        return f"{self.name[:10]}"
    

class ServiceInfo(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    list = models.ManyToManyField('ServiceList', blank=True)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='service_images', blank=True, null=True)

    def __str__(self):
        return self.name
    
class ServiceList(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class UserVisit(models.Model):
    user = models.TextField(default=None)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user

    def user_count(self):
        return UserVisit.objects.count()

    # other methods or fields if needed


class Terms(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextUploadingField(blank=True, null=True) 
    image = models.ImageField(upload_to='item_images', blank=True, null=True)

    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Terms'

    def __str__(self):
        return self.title
    
class Privacy(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextUploadingField(blank=True, null=True) 
    image = models.ImageField(upload_to='item_images', blank=True, null=True)

    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Privacy'

    def __str__(self):
        return self.title