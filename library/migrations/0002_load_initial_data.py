from django.db import migrations


def load_initial_data(apps, schema_editor):
    from django.core.management import call_command

    call_command('loaddata', 'library/fixtures/authors.json')
    call_command('loaddata', 'library/fixtures/publishers.json')
    call_command('loaddata', 'library/fixtures/categories.json')
    call_command('loaddata', 'library/fixtures/books.json')
    call_command('loaddata', 'library/fixtures/reviews.json')


class Migration(migrations.Migration):

    dependencies = [
        # Ensure this matches the actual initial migration name
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_initial_data),
    ]
