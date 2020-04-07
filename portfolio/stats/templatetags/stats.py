from django import template
from stats.models import Visitor
from projects.models import Project, Language
import json

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

@register.simple_tag
def get_visitors():
    return len(Visitor.objects.all())

@register.simple_tag
def get_projects():
    return len(Project.objects.all())

@register.simple_tag
def get_languages():
    return len(Language.objects.all())

@register.simple_tag
def get_most_used_language():
    projects = Project.objects.all()
    languages = {}
    for project in projects:
        langs = json.loads(project.language_str.replace("'", '"'))
        for language in langs:
            if not language in languages:
                languages[language] = 1
            else:
                languages[language] += 1
    max_value = max(languages.values())
    for language, usage in languages.items():
        if usage == max_value:
            return language
    return None