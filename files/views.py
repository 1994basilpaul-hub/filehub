from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db import models
from django.db.models import Q
from .models import FileItem, Category,FileContent
from .forms import FileUploadForm
from django.http import HttpResponseRedirect, FileResponse
import os
from django.conf import settings

def index(request):
    qs = FileItem.objects.all()
    q = request.GET.get('q', '')  # default to empty string
    if q:
        qs = qs.filter(Q(title__icontains=q) | Q(description__icontains=q))

    paginator = Paginator(qs, 12)
    page = request.GET.get('page')
    items = paginator.get_page(page)
    categories = Category.objects.all()  # fetch all categories

    return render(request, 'files/index.html', {
        'items': items,
        'q': q,
        'categories': categories
    })




def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    qs = FileItem.objects.filter(category=category)

    # Pagination
    paginator = Paginator(qs, 12)
    page = request.GET.get('page')
    items = paginator.get_page(page)

    categories = Category.objects.all()  # Add this line

    return render(request, 'files/category_detail.html', {
        'category': category,
        'items': items,
        'categories': categories  # Pass categories to template
    })




def download(request, slug):
    item = get_object_or_404(FileItem, slug=slug)
    path = item.file.path
    # increment download count
    FileItem.objects.filter(pk=item.pk).update(downloads=models.F('downloads') + 1)
    # serve file (development). In production, let Nginx serve and use X-Accel-Redirect or presigned URLs.
    response = FileResponse(open(path, 'rb'), as_attachment=True, filename=os.path.basename(path))
    return response

# simple upload view (restrict with staff_required in production)
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('files:index')
    else:
        form = FileUploadForm()
    return render(request, 'files/upload.html', {'form': form})




def explain(request, slug):
    file_item = get_object_or_404(FileItem, slug=slug)
    contents = file_item.contents.all()

    # take category_no from the first related content
    category_no = contents.first().category_no if contents.exists() else None  

    return render(request, 'files/explain.html', {
        'file_item': file_item,
        'contents': contents,
        'category_no': category_no,
    })

