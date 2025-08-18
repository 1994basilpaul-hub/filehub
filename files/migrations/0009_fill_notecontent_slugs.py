from django.db import migrations
from django.utils.text import slugify

def fill_slugs(apps, schema_editor):
    NoteContent = apps.get_model('files', 'NoteContent')
    for note in NoteContent.objects.filter(slug__isnull=True):
        note.slug = slugify(note.title) or f"note-{note.id}"
        note.save()

class Migration(migrations.Migration):

    dependencies = [
        ('files', '0008_alter_notecontent_slug'),  # previous migration
    ]

    operations = [
        migrations.RunPython(fill_slugs),
    ]
