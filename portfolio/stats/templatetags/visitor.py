from django import template
from stats.models import Visitor

register = template.Library()

@register.simple_tag
def update_visitors(request):
    if not request.session.session_key:
        request.session.save()
        key = request.session.session_key
    else:
        key = request.session.session_key
    visitor = Visitor.objects.filter(visitor_id = key)
    if not visitor:
        visitor = Visitor(visitor_id = key)
        visitor.save()
    return ""
