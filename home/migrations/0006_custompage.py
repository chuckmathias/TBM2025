# Generated by Django 5.1.7 on 2025-04-03 16:12

import django.db.models.deletion
import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_rename_banner_image_homepage_home_header_image_and_more'),
        ('wagtailcore', '0094_alter_page_locale'),
        ('wagtailimages', '0027_image_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('sections', wagtail.fields.StreamField([('full_height_section', 4)], blank=True, block_lookup={0: ('wagtail.blocks.CharBlock', (), {'help_text': 'Optional title for the section', 'required': False}), 1: ('wagtail.blocks.RichTextBlock', (), {'help_text': 'Content for the section', 'required': False}), 2: ('wagtail.images.blocks.ImageChooserBlock', (), {'help_text': 'Background image for the section', 'required': False}), 3: ('wagtail.blocks.BooleanBlock', (), {'default': True, 'help_text': 'Show or hide this section', 'required': False}), 4: ('wagtail.blocks.StructBlock', [[('title', 0), ('content', 1), ('background_image', 2), ('visible', 3)]], {})}, help_text='Add, remove, and reorder full-height sections')),
                ('header_image', models.ForeignKey(blank=True, help_text='Full-height header image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
