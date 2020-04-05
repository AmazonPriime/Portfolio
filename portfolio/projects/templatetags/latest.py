from django import template
from projects.models import Project

register = template.Library()

@register.simple_tag
def get_latest_update():
    return Project.objects.all().order_by('-date_updated')[0]

@register.simple_tag
def get_newest_project():
    return Project.objects.all().order_by('-date_created')[0]
