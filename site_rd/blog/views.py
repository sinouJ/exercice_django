from django.shortcuts import render
from .models import Post
from django.contrib.auth.models import User
from .forms import PostForm
from django.shortcuts import redirect, get_object_or_404

def all_posts(request):
    page_title = 'Derniers posts | Home'
    posts = Post.objects.filter(is_published = "True").order_by('published_date')
    unpublished_posts = Post.objects.filter(is_published = "False").order_by('created_date')
    users = User.objects.all()
    return render(
        request, 
        'blog/all_posts.html', 
        {
            'posts': posts, 
            'users': users, 
            'unpublished_posts': unpublished_posts, 
            'page_title': page_title
        }
    )

def post_view(request, id):
    post = Post.objects.get(id = id)
    page_title = post.title + ' | Post'
    return render(request, 'blog/post_view.html', {'post': post, 'page_title': page_title})

def post_new(request):
    page_title = 'Créer un post'

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
        return render(request, 'blog/post_new.html', {'form': form, 'page_title': page_title})

def post_edit(request, id):
    page_title = 'Éditer un post'

    post = get_object_or_404(Post, id = id)

    if request.method == 'POST':
        form = PostForm(request.POST, instance = post)

        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user
            post.is_published = False
            post.save()
            return redirect('post_view', id=post.id)

    else:
        form = PostForm()
        return render(request, 'blog/post_new.html', {'form': form, 'page_title': page_title})