from wagtail.images.models import Image
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
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
        # Get all live board member profiles
        context['board_members'] = BoardProfilePage.objects.child_of(self).live().order_by('title')
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
    
    # Contact and links
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    personal_links = models.TextField(blank=True, help_text="Links to personal website, LinkedIn, etc.")
    
    # Images
    profile_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    
    # Term information
    term_start = models.DateField(null=True, blank=True)
    term_end = models.DateField(null=True, blank=True, help_text="Leave blank if currently serving")
    
    content_panels = Page.content_panels + [
        FieldPanel('position'),
        FieldPanel('occupation'),
        FieldPanel('bio'),
        FieldPanel('profile_image'),
        MultiFieldPanel([
            FieldPanel('email'),
            FieldPanel('phone'),
            FieldPanel('personal_links'),
        ], heading="Contact Information"),
        MultiFieldPanel([
            FieldPanel('term_start'),
            FieldPanel('term_end'),
        ], heading="Board Term"),
    ]
    
    class Meta:
        verbose_name = "Board Member Profile"