from django import forms
from .models import FileItem,ContactMessage

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = FileItem
        fields = ['title','description','category','file','meta_title','meta_description']

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control form-control-lg rounded-3',
                'placeholder': 'Enter your full name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control form-control-lg rounded-3',
                'placeholder': 'Enter your email address'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control form-control-lg rounded-3',
                'placeholder': 'Subject of your message'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control form-control-lg rounded-3',
                'placeholder': 'Write your message here...',
                'rows': 5,
            }),
        }
        