from django.shortcuts import render
from projects.models import Project

def index(request):
    context_dict = {}
    context_dict['projects'] = Project.objects.all().order_by('-date_updated')
    return render(request, 'projects/projects.html', context_dict)
