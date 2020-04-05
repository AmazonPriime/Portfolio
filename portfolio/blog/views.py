from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from blog.models import Post, Like, View
from blog.forms import PostForm
import json

def index(request):
    context_dict = {}
    posts = Post.objects.all().order_by('-date_created')
    context_dict['posts'] = posts
    return render(request, 'blog/blog.html', context_dict)

def post(request, id):
    context_dict = {}
    try:
        post = Post.objects.get(id = id)
        context_dict['post'] = post
    except:
        return render(request, '404.html')

    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.date_updated = datetime.now()
        post.save()
        return HttpResponse(json.dumps({'title' : post.title, 'content' : post.content}), content_type = "application/json")

    if not request.session.session_key:
        request.session.save()
    key = request.session.session_key

    views = View.objects.filter(post__title = post.title, viewer_id = key)
    if not views:
        views = View(viewer_id = key, post = post)
        views.save()
        post.views += 1
        post.save()

    if request.user.is_superuser:
        context_dict['post_form'] = PostForm(instance = post)

    return render(request, 'blog/post.html', context_dict)
