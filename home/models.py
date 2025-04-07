from wagtail.models import Page
from wagtail.fields import StreamField, RichTextField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.blocks import StructBlock, BooleanBlock, CharBlock, RichTextBlock
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail import blocks
from django.db import models
from missionary_profiles.models import MissionaryProfilePage
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from modelcluster.fields import ParentalKey


class HomePage(Page):
    # Background images for each section
    home_header_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    home_mission_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    home_values_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    home_projects_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    home_envision_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    home_pray_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    home_promo_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    # Visibility toggles for each section
    show_home_header = models.BooleanField(default=True)
    show_home_mission = models.BooleanField(default=True)
    show_home_values = models.BooleanField(default=True)
    show_home_projects = models.BooleanField(default=True)
    show_home_envision = models.BooleanField(default=True)
    show_home_pray = models.BooleanField(default=True)
    show_home_promo = models.BooleanField(default=True)

    content_panels = Page.content_panels + [
        FieldPanel('home_header_image'),
        FieldPanel('show_home_header'),
        FieldPanel('home_mission_image'),
        FieldPanel('show_home_mission'),
        FieldPanel('home_values_image'),
        FieldPanel('show_home_values'),
        FieldPanel('home_projects_image'),
        FieldPanel('show_home_projects'),
        FieldPanel('home_envision_image'),
        FieldPanel('show_home_envision'),
        FieldPanel('home_pray_image'),
        FieldPanel('show_home_pray'),
        FieldPanel('home_promo_image'),
        FieldPanel('show_home_promo'),
    ]


class FullHeightSectionBlock(StructBlock):
    """A single full-height section block."""
    title = CharBlock(required=False, help_text="Optional title for the section")
    content = RichTextBlock(required=False, help_text="Content for the section")
    background_image = ImageChooserBlock(required=False, help_text="Background image for the section")
    visible = BooleanBlock(required=False, default=True, help_text="Show or hide this section")

    class Meta:
        template = "home/full_height_section.html"
        icon = "placeholder"
        label = "Full Height Section"


class CustomPage(Page):
    """A reusable page model for PROJECTS, ABOUT, GET INVOLVED, etc."""
    header_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Full-height header image"
    )
    sections = StreamField(
        [
            ('full_height_section', FullHeightSectionBlock()),
        ],
        blank=True,
        use_json_field=True,
        help_text="Add, remove, and reorder full-height sections"
    )

    content_panels = Page.content_panels + [
        FieldPanel('header_image'),
        FieldPanel('sections'),
    ]


class ProjectsPage(Page):
    """A page to display all missionary profiles."""
    header_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Background image for the intro section"
    )
    intro = RichTextField(blank=True, help_text="Introduction text for the projects page.")

    content_panels = Page.content_panels + [
        FieldPanel('header_image'),
        FieldPanel('intro'),
    ]

    def get_context(self, request):
        # Get the default context
        context = super().get_context(request)
        # Query all MissionaryProfilePage instances
        context['missionary_profiles'] = MissionaryProfilePage.objects.live().order_by('title')
        return context


from wagtail.models import Page
from wagtail.fields import StreamField, RichTextField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.blocks import StructBlock, BooleanBlock, CharBlock, RichTextBlock
from wagtail.admin.panels import FieldPanel
from wagtail import blocks
from django.db import models
from missionary_profiles.models import MissionaryProfilePage
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from modelcluster.fields import ParentalKey


class HomePage(Page):
    # Background images for each section
    home_header_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    home_mission_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    home_values_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    home_projects_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    home_envision_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    home_pray_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    home_promo_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    # Visibility toggles for each section
    show_home_header = models.BooleanField(default=True)
    show_home_mission = models.BooleanField(default=True)
    show_home_values = models.BooleanField(default=True)
    show_home_projects = models.BooleanField(default=True)
    show_home_envision = models.BooleanField(default=True)
    show_home_pray = models.BooleanField(default=True)
    show_home_promo = models.BooleanField(default=True)

    content_panels = Page.content_panels + [
        FieldPanel('home_header_image'),
        FieldPanel('show_home_header'),
        FieldPanel('home_mission_image'),
        FieldPanel('show_home_mission'),
        FieldPanel('home_values_image'),
        FieldPanel('show_home_values'),
        FieldPanel('home_projects_image'),
        FieldPanel('show_home_projects'),
        FieldPanel('home_envision_image'),
        FieldPanel('show_home_envision'),
        FieldPanel('home_pray_image'),
        FieldPanel('show_home_pray'),
        FieldPanel('home_promo_image'),
        FieldPanel('show_home_promo'),
    ]


class FullHeightSectionBlock(StructBlock):
    """A single full-height section block."""
    title = CharBlock(required=False, help_text="Optional title for the section")
    content = RichTextBlock(required=False, help_text="Content for the section")
    background_image = ImageChooserBlock(required=False, help_text="Background image for the section")
    visible = BooleanBlock(required=False, default=True, help_text="Show or hide this section")

    class Meta:
        template = "home/full_height_section.html"
        icon = "placeholder"
        label = "Full Height Section"


class CustomPage(Page):
    """A reusable page model for PROJECTS, ABOUT, GET INVOLVED, etc."""
    header_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Full-height header image"
    )
    sections = StreamField(
        [
            ('full_height_section', FullHeightSectionBlock()),
        ],
        blank=True,
        use_json_field=True,
        help_text="Add, remove, and reorder full-height sections"
    )

    content_panels = Page.content_panels + [
        FieldPanel('header_image'),
        FieldPanel('sections'),
    ]


class ProjectsPage(Page):
    """A page to display all missionary profiles."""
    header_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Background image for the intro section"
    )
    intro = RichTextField(blank=True, help_text="Introduction text for the projects page.")

    content_panels = Page.content_panels + [
        FieldPanel('header_image'),
        FieldPanel('intro'),
    ]

    def get_context(self, request):
        # Get the default context
        context = super().get_context(request)
        # Query all MissionaryProfilePage instances
        context['missionary_profiles'] = MissionaryProfilePage.objects.live().order_by('title')
        return context


class ContactFormField(AbstractFormField):
    """Form fields for the contact page."""
    page = ParentalKey(
        'home.ContactPage',  # Ensure this points to the ContactPage model
        on_delete=models.CASCADE,
        related_name='form_fields'  # This must match the InlinePanel in ContactPage
    )

class ContactPage(AbstractEmailForm):
    """A Wagtail page model for the contact page."""
    header_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Background image for the header section"
    )
    intro = RichTextField(blank=True, help_text="Introduction text for the contact page.")
    thank_you_text = RichTextField(blank=True, help_text="Text displayed after the form is submitted.")

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('header_image'),
        FieldPanel('intro'),
        FieldPanel('thank_you_text'),
        FieldPanel('to_address'),  # Email address to send submissions to
        FieldPanel('from_address'),
        FieldPanel('subject'),
        InlinePanel('form_fields', label="Form Fields"),  # This manages the form fields
    ]