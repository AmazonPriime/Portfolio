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
                languages[language] = 1
            else:
                languages[language] += 1
    context_dict['languages'] = sorted(languages.items(), key = lambda x: x[1], reverse = True)[:7]
    return render(request, 'index.html', context_dict)
