from django import forms
from .models import FileItem

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = FileItem
        fields = ['title','description','category','file','meta_title','meta_description']
        