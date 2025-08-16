from django.contrib import admin
from .models import FileItem, Category

@admin.register(FileItem)
class FileItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'uploaded_at', 'downloads')
    search_fields = ('title', 'description')

admin.site.register(Category)
