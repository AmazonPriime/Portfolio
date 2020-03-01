from django.shortcuts import render

def index(request):
    context_dict = {}
    return render(request, 'blog/blog.html', context_dict)
