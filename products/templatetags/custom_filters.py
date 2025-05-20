from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(name='split')
@stringfilter
def split(value, arg):
    return value.split(arg)


@register.filter(name='strip')
@stringfilter
def strip(value):
    return value.strip()
