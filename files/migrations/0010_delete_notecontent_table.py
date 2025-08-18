from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('files', '0008_alter_notecontent_slug'),
    ]

    operations = [
        migrations.DeleteModel(
            name='NoteContent',
        ),
    ]
