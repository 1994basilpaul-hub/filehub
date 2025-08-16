from django.db import models
from autoslug import AutoSlugField  # pip install django-autoslug
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=120, unique=True)
    slug = AutoSlugField(populate_from='name', unique=True)

    def str(self): return self.name

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
    meta_description = models.CharField(max_length=160, blank=True)

    class Meta:
        ordering = ['-uploaded_at']

    def str(self): return self.title

    def get_absolute_url(self):
        return reverse('files:detail', kwargs={'slug': self.slug})