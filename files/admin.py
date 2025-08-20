from django.contrib import admin
from .models import FileItem, Category,FileContent, Note_Category, NoteContent, ContactMessage

@admin.register(FileItem)
class FileItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'uploaded_at', 'downloads')
    search_fields = ('title', 'description')

admin.site.register(Category)
admin.site.register(FileContent)
admin.site.register(Note_Category)
admin.site.register(NoteContent)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "created_at")
    search_fields = ("name", "email", "subject")

