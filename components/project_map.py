from wagtail import blocks
from wagtail.blocks import StructBlock, CharBlock, URLBlock, BooleanBlock

class WorldMapBlock(StructBlock):
    """World map block for displaying mission locations."""
    
    title = CharBlock(
        required=False,
        help_text="Optional title for the map section"
    )
    
    show_title = BooleanBlock(
        required=False,
        default=True,
        help_text="Display the title above the map"
    )
    
    # Regional URLs for clickable map areas
    north_america_url = URLBlock(
        required=False,
        help_text="URL to navigate to when North America is clicked"
    )
    
    south_america_url = URLBlock(
        required=False,
        help_text="URL to navigate to when South America is clicked"
    )
    
    europe_url = URLBlock(
        required=False,
        help_text="URL to navigate to when Europe is clicked"
    )
    
    africa_url = URLBlock(
        required=False,
        help_text="URL to navigate to when Africa is clicked"
    )
    
    asia_url = URLBlock(
        required=False,
        help_text="URL to navigate to when Asia is clicked"
    )
    
    oceania_url = URLBlock(
        required=False,
        help_text="URL to navigate to when Oceania is clicked"
    )
    
    # Styling options
    css_class = CharBlock(
        required=False,
        help_text="Additional CSS classes for custom styling"
    )
    
    map_height = CharBlock(
        required=False,
        default="440px",
        help_text="Height of the map (e.g., 440px, 50vh)"
    )
    
    class Meta:
        template = 'components/worldmapblock.html'
        icon = 'globe'
        label = 'World Map'
        help_text = 'Interactive world map with clickable regions'