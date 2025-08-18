from django.urls import path
from . import views

app_name = 'files'
urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload_file, name='upload'),
    path('downloads/<slug:slug>/get/', views.download, name='download'),
    path('category/<slug:slug>/', views.category_detail, name='category_detail'),
    path('explain/<slug:slug>/', views.explain, name='explain'),
    # files/urls.py
    path('note_category/<slug:slug>/', views.note_category_detail, name='note_category_detail')

]
