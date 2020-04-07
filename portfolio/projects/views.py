from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from projects.models import Project, View

def index(request):
    context_dict = {}
    projects = Project.objects.all().order_by('-date_updated')
    paginator = Paginator(projects, 7)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context_dict['page_obj'] = page_obj
    return render(request, 'projects/projects.html', context_dict)

def views(request, name):
    try:
        project = Project.objects.get(name = name)
    except:
        return render(request, '404.html')

    if not request.session.session_key:
        request.session.save()
    key = request.session.session_key

    views = View.objects.filter(project__name = project.name, viewer_id = key)
    if not views:
        views = View(viewer_id = key, project = project)
        views.save()
        project.views += 1
        project.save()

    return HttpResponseRedirect(project.url)