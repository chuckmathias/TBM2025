from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, PageChooserPanel, InlinePanel
from wagtail.snippets.models import register_snippet
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel


@register_snippet
class Menu(ClusterableModel):
    title = models.CharField(max_length=255)

    panels = [
        FieldPanel("title"),
        InlinePanel("items", label="Menu Items"),  # Inline panel to manage menu items
    ]

    def __str__(self):
        return self.title


class MenuItem(models.Model):
    menu = ParentalKey(Menu, related_name="items", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    link_page = models.ForeignKey(
        Page, null=True, blank=True, on_delete=models.CASCADE, related_name="+"
    )
    link_url = models.URLField(blank=True, null=True)
    open_in_new_tab = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)  # Field for ordering menu items

    panels = [
        FieldPanel("title"),
        PageChooserPanel("link_page"),
        FieldPanel("link_url"),
        FieldPanel("open_in_new_tab"),
        FieldPanel("order"),
    ]

    class Meta:
        ordering = ["order"]  # Default ordering by the `order` field

    def __str__(self):
        return self.title