from django.db import models
from autoslug import AutoSlugField  # pip install django-autoslug
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=120, unique=True)
    slug = AutoSlugField(populate_from='name', unique=True)

    def __str__(self):
        return self.name
    
class Note_Category(models.Model):
    name = models.CharField(max_length=120, unique=True)
    slug = AutoSlugField(populate_from='name', unique=True)

    def __str__(self):
        return self.name


class FileItem(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to='uploads/%Y/%m/')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    slug = AutoSlugField(populate_from='title', unique=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    downloads = models.PositiveIntegerField(default=0)

    # SEO meta
    meta_title = models.CharField(max_length=255, blank=True)
    meta_description = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ['-uploaded_at']

    def __str__(self):
     return self.title


    def get_absolute_url(self):
        return reverse('files:detail', kwargs={'slug': self.slug})
    
# New model for questions/content
class FileContent(models.Model):
    file_item = models.ForeignKey(FileItem, related_name='contents', on_delete=models.CASCADE)
    category_no = models.CharField(max_length=50, blank=True, null=True)  
    content = models.TextField()  # Combined field for English/Malayalam/questions/options/answer/explanation
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Content for {self.file_item.title}"
    
class NoteContent(models.Model):
    title= models.CharField(max_length=255)
    category = models.ForeignKey(Note_Category, on_delete=models.SET_NULL, null=True, blank=True)  
    content = models.TextField()  # Combined field for English/Malayalam/questions/options/answer/explanation
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    