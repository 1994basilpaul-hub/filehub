from .models import Category, Note_Category

def navbar_categories(request):
    return {
        'categories': Category.objects.all(),
        'note_categories': Note_Category.objects.all()
    }

