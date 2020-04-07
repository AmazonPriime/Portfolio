from django.shortcuts import render
from projects.models import Project
import json

def index(request):
    context_dict = {}
    projects = Project.objects.all()
    languages = {}
    for project in projects:
        langs = json.loads(project.language_str.replace("'", '"'))
        for language in langs:
            if not language in languages:
                languages[language] = langs[language]
            else:
                languages[language] += langs[language]
    context_dict['languages'] = languages
    return render(request, 'index.html', context_dict)