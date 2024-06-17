from django.contrib.auth.models import User
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    
class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    content = RichTextUploadingField(blank=True, null=True) 
    # content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    file = models.FileField(upload_to='item_files', blank=True)
    video = models.FileField(upload_to='item_videos', blank=True)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    item = models.ForeignKey(Item, related_name='comments', on_delete=models.CASCADE)
    name =  models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    body = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.item.name, self.name)
    



