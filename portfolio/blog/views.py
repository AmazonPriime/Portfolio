from django.shortcuts import render
from blog.models import Post, Like, View

def index(request):
    context_dict = {}
    posts = Post.objects.all().order_by('-date_created')
    for post in posts:
        post.likes = sum([1 for i in Like.objects.all().filter(post__title = post.title)])
        post.views = sum([1 for i in View.objects.all().filter(post__title = post.title)])
    context_dict['posts'] = posts
    return render(request, 'blog/blog.html', context_dict)
