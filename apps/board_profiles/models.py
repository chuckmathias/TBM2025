from wagtail.images.models import Image
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, FieldRowPanel, InlinePanel
from django.db import models
from django.shortcuts import render
from django.http import Http404
from wagtail.images.models import Image
from modelcluster.fields import ParentalKey
from wagtail.models import Orderable


class BoardMembersIndexPage(Page):
    """Landing page for board members"""

    parent_page_types = ['home.CustomPage']
    subpage_types = ['board_profiles.BoardProfilePage']
    max_count = 1  # Only allow one board members page
    
    intro = RichTextField(blank=True)
    
    # New field for header image
    header_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Header image for the board members page"
    )
    
    content_panels = Page.content_panels + [
        FieldPanel('header_image'),
        FieldPanel('intro'),
    ]
    
    def get_context(self, request):
        context = super().get_context(request)
        all_profiles = BoardProfilePage.objects.child_of(self).live().order_by('title')
        context['board_members'] = all_profiles.filter(is_board_member=True)
        context['board_consultants'] = all_profiles.filter(is_board_member=False)
        return context
    
    class Meta:
        verbose_name = "Board Members Index Page"


class BoardProfileGalleryImage(Orderable):
    page = ParentalKey('BoardProfilePage', related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.CASCADE,
        related_name='+'
    )
    caption = models.CharField(max_length=250, blank=True)

    panels = [
        FieldPanel('image'),
        FieldPanel('caption'),
    ]


class BoardProfilePage(Page):
    """Individual board member profile"""
    
    parent_page_types = ['board_profiles.BoardMembersIndexPage']
    subpage_types = []
    
    # Board member specific fields
    position = models.CharField(max_length=100, blank=True, help_text="e.g., Chairman, Secretary, Treasurer")
    occupation = models.CharField(max_length=200, blank=True)
    bio = RichTextField(blank=True)
    
    # Pictures Section
    pictures = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    show_pictures = models.BooleanField(default=True)

    
    # Member or Consultant Checkbox
    is_board_member = models.BooleanField(default=True, verbose_name="Is Board Member")

    # Profile Image
    profile_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Main profile image"
    )

    # Admin panels
    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('profile_image'),
            FieldPanel('is_board_member'),
            FieldPanel('position'),
            FieldPanel('occupation'),
            FieldPanel('bio'),
        ], heading="Profile Information"),
        MultiFieldPanel([
            FieldPanel('pictures'),
            FieldPanel('show_pictures'),
        ], heading="Pictures Section (Single Image)"),
        MultiFieldPanel([
            InlinePanel('gallery_images', label="Gallery Images", min_num=0, max_num=20),
        ], heading="Gallery Section (Multiple Images)"),
    ]
    
    class Meta:
        verbose_name = "Board Member Profile"