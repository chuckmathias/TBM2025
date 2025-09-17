# filepath: /home/chuck/Programs/tentmakersbiblemission/menus/templatetags/menu_tags.py
from django import template
from apps.menus.models import Menu

register = template.Library()

@register.inclusion_tag("menus/menu.html", takes_context=True)
def render_menu(context, menu_title):
    """Render a menu by its title."""
    try:
        menu = Menu.objects.get(title=menu_title)
        return {"menu": menu, "request": context["request"]}
    except Menu.DoesNotExist:
        return {"menu": None}