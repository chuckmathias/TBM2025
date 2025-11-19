from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, FieldRowPanel, InlinePanel
from django.db import models
from django.shortcuts import render
from django.http import Http404
from modelcluster.fields import ParentalKey
from wagtail.models import Orderable
from wagtail.images.models import Image

class MissionaryProfilePage(Page):
    # Required fields
    name = models.CharField(max_length=255)
    project = models.CharField(max_length=255)
    region = models.CharField(
        max_length=50,
        choices=[
            ('Africa', 'Africa'),
            ('Asia', 'Asia'),
            ('Europe', 'Europe'),
            ('North America', 'North America'),
            ('South America', 'South America'),
            ('Home Office', 'Home Office'),
        ],
        default='North America'
    )
    information = RichTextField()

    # Optional fields
    special_project = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    place = models.CharField(max_length=100, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)  # Latitude for map
    longitude = models.FloatField(blank=True, null=True)  # Longitude for map
    personal_links = models.TextField(blank=True, null=True)  # Store as JSON or comma-separated
    video_links = models.TextField(blank=True, null=True)  # Store as JSON or comma-separated
    donation_link = models.CharField(max_length=255, blank=True, null=True)
    project_summary = models.TextField(blank=True, null=True)

    # Background images for each section
    profile_header_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    profile_info_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    profile_location_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    # Content panels for the Wagtail admin
    content_panels = Page.content_panels + [
        FieldPanel('name'),
        FieldPanel('project'),
        FieldPanel('special_project'),
        FieldPanel('region'),
        FieldPanel('country'),
        FieldPanel('state'),
        FieldPanel('place'),
        FieldPanel('information'),
        MultiFieldPanel(
            [
                FieldRowPanel([
                    FieldPanel('latitude', classname="col6"),  # Display latitude in one column
                    FieldPanel('longitude', classname="col6"),  # Display longitude in another column
                ]),
            ],
            heading="Location",  # Add a heading for the group
        ),
        FieldPanel('personal_links'),
        FieldPanel('video_links'),
        FieldPanel('donation_link'),
        FieldPanel('project_summary'),
        FieldPanel('profile_header_image'),
        FieldPanel('profile_info_image'),
        FieldPanel('profile_location_image'),
        MultiFieldPanel([
            InlinePanel('gallery_images', label="Photo Gallery"),
        ], heading="Photo Gallery"),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        context['recent_updates'] = self.related_updates.live().order_by('-first_published_at')[:4]
        return context

    def serve(self, request):
        # Check if the request path ends with 'updates/'
        if request.path.endswith('updates/'):
            # Get all related updates for this profile
            updates = self.related_updates.live().order_by('-first_published_at')
            if not updates.exists():
                raise Http404("No updates found for this profile.")
            # Render the updates list template
            return render(request, 'missionary_profiles/missionary_updates_list.html', {
                'page': self,
                'updates': updates,
            })
        # Default behavior for other paths
        return super().serve(request)

class MissionaryUpdatePage(Page):
    # Link to MissionaryProfilePage
    missionary_profile = models.ForeignKey(
        'missionary_profiles.MissionaryProfilePage',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='related_updates'  # This establishes the reverse relationship
    )

    # Header Section
    header_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    show_header = models.BooleanField(default=True)

    # Information Section
    information = RichTextField(blank=True, null=True)
    pdf_document = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    show_information = models.BooleanField(default=True)
    information_background_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    # Pictures Section
    pictures = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    show_pictures = models.BooleanField(default=True)

    # Admin panels
    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('missionary_profile'),
            FieldPanel('header_image'),
            FieldPanel('show_header'),
        ], heading="Header Section"),
        MultiFieldPanel([
            FieldPanel('information'),
            FieldPanel('pdf_document'),
            FieldPanel('show_information'),
            FieldPanel('information_background_image'),
        ], heading="Information Section"),
        MultiFieldPanel([
            FieldPanel('pictures'),
            FieldPanel('show_pictures'),
        ], heading="Pictures Section"),
    ]

class MissionaryNewsletterSignup(models.Model):
    missionary = models.ForeignKey('MissionaryProfilePage', on_delete=models.CASCADE, related_name='newsletter_signups')
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField()
    signup_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.email} for {self.missionary.name}"

class MissionaryProfileGalleryImage(Orderable):
    page = ParentalKey('MissionaryProfilePage', related_name='gallery_images')
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