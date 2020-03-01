from django.shortcuts import render

def index(request):
    context_dict = {}
    return render(request, 'projects/projects.html', context_dict)
