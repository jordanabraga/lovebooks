# Generated by Django 4.2.10 on 2024-02-23 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_book_featured_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
