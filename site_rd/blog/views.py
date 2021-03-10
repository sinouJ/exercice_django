from django.shortcuts import render
from .models import Post
from django.contrib.auth.models import User

def all_posts(request):
    posts = Post.objects.filter(is_published = "True").order_by('published_date')
    users = User.objects.all()
    return render(request, 'blog/all_posts.html', {'posts': posts, 'users': users})

def post_view(request, id):
    post = Post.objects.get(id = id)
    return render(request, 'blog/post_view.html', {'post': post})
