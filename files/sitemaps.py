from django.contrib.sitemaps import Sitemap
from .models import FileItem

class FileItemSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.6

    def items(self):
        return FileItem.objects.all()

    def lastmod(self, obj):
        return obj.uploaded_at