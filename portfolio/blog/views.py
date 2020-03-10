from django.shortcuts import render
from blog.models import Post, Like, View

def index(request):
    context_dict = {}
    posts = Post.objects.all().order_by('-date_created')
    context_dict['posts'] = posts
    return render(request, 'blog/blog.html', context_dict)

def post(request, slug):
    context_dict = {}
    try:
        post = Post.objects.get(title_slug = slug)
        context_dict['post'] = post
    except:
        return render(request, '404.html')

    if not request.session.session_key:
        request.session.save()
    key = request.session.session_key

    views = View.objects.filter(post__title = post.title, viewer_id = key)
    if not views:
        views = View(viewer_id = key, post = post)
        views.save()
        post.views += 1
        post.save()

    return render(request, 'blog/post.html', context_dict)
