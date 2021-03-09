from django.shortcuts import render
from .models import Post

def all_posts(request):
    posts = Post.objects.filter(published_date)
    return render(request, 'blog/all_posts.html')
