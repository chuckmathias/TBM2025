from wagtail.images.models import Image
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, FieldRowPanel
from django.db import models


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


class BoardProfilePage(Page):
    """Individual board member profile"""
    
    parent_page_types = ['board_profiles.BoardMembersIndexPage']
    subpage_types = []
    
    # Board member specific fields
    position = models.CharField(max_length=100, blank=True, help_text="e.g., Chairman, Secretary, Treasurer")
    occupation = models.CharField(max_length=200, blank=True)
    bio = RichTextField(blank=True)
    
    # Images
    profile_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    
    # New fields for member type
    is_board_member = models.BooleanField(default=True, verbose_name="Is Board Member")
    
    content_panels = Page.content_panels + [
        FieldPanel('position'),
        FieldPanel('occupation'),
        FieldPanel('bio'),
        FieldPanel('profile_image'),
        FieldPanel('is_board_member'),
    ]
    
    class Meta:
        verbose_name = "Board Member Profile"