from django.shortcuts import render

def all_posts(request):
    return render(request, 'blog/all_posts.html')
