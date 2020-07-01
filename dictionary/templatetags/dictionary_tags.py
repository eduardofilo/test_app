from urllib.parse import urlencode
from django import template

register = template.Library()


# It allows to replace the value of a GET parameter or add it to the list if it does not exist.
@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)
