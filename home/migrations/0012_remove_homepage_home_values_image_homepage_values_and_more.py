# Generated by Django 5.1.8 on 2025-04-07 15:34

import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_contactpage_header_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='home_values_image',
        ),
        migrations.AddField(
            model_name='homepage',
            name='values',
            field=wagtail.fields.StreamField([('value', 4)], blank=True, block_lookup={0: ('wagtail.blocks.CharBlock', (), {'help_text': 'Title of the value', 'required': True}), 1: ('wagtail.blocks.RichTextBlock', (), {'help_text': 'Description of the value', 'required': False}), 2: ('wagtail.blocks.URLBlock', (), {'help_text': 'Optional link for the value', 'required': False}), 3: ('wagtail.images.blocks.ImageChooserBlock', (), {'help_text': 'Optional background image for the value', 'required': False}), 4: ('wagtail.blocks.StructBlock', [[('title', 0), ('description', 1), ('link', 2), ('background_image', 3)]], {})}, help_text='Add, delete, or rearrange values for the Values section'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='show_home_values',
            field=models.BooleanField(default=True, help_text='Show or hide the Values section'),
        ),
    ]
