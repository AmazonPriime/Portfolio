from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.template.defaultfilters import slugify
from blog.models import Post, View
from blog.forms import PostForm
from datetime import datetime
import json

def index(request):
    context_dict = {}
    posts = Post.objects.all().order_by('-date_created')
    paginator = Paginator(posts, 7)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context_dict['page_obj'] = page_obj
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

@login_required(login_url='index')
def add(request):
    if request.method == 'POST':
        try:
            post_form = PostForm(request.POST)
            if post_form.is_valid:
                post = post_form.save()
            return redirect(reverse('blog_post', args = [post.id]))
        except:
            messages.error(request, "Blog post title is already in use.")
    else:
        post_form = PostForm()

    return render(request, 'blog/addpost.html', {'post_form' : post_form})