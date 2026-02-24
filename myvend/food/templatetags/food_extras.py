from django import template
from django.utils.safestring import mark_safe
import markdown as md
import bleach # strips any dangerous html from input before marked safe

register = template.Library()

ALLOWED_TAGS = list(bleach.sanitizer.ALLOWED_TAGS) + [
    'p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'
]

@register.filter(name='markdown')
def markdown(value):
    return mark_safe(md.markdown(value))