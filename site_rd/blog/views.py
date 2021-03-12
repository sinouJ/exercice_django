from django.shortcuts import render
from .models import Post
from django.contrib.auth.models import User
from .forms import PostForm
from django.shortcuts import redirect

def all_posts(request):
    posts = Post.objects.filter(is_published = "True").order_by('published_date')
    users = User.objects.all()
    return render(request, 'blog/all_posts.html', {'posts': posts, 'users': users})

def post_view(request, id):
    post = Post.objects.get(id = id)
    return render(request, 'blog/post_view.html', {'post': post})

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user
            post.is_published = False
            post.save()
            return redirect('post_view', id=post.id)

    else:
        form = PostForm()
        return render(request, 'blog/post_new.html', {'form': form})