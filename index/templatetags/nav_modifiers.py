from django import template
from django.urls import reverse
register = template.Library()


@register.simple_tag
def is_active(current_path, link_path, param=None):
    try:
        if param is None:
            if reverse(link_path) == current_path:
                return 'active'
        else:
            if reverse(link_path, param) == current_path:
                return 'active'
            else:
                return ''
    except:
        return ''