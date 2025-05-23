# Generated by Django 5.1.7 on 2025-04-04 15:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_alter_contactformfield_id'),
        ('wagtailimages', '0027_image_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactpage',
            name='header_image',
            field=models.ForeignKey(blank=True, help_text='Background image for the header section', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
    ]
