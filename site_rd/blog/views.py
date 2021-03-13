# Django imports
from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login

# Post imports
from .models import Post
from .forms import PostForm

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
    post = get_object_or_404(Post, id = id)
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
        form = PostForm(instance = post)
        return render(request, 'blog/post_new.html', {'form': form, 'page_title': page_title})

def publish_post(request, id):
    post = get_object_or_404(Post, id = id)

    post.is_published = True
    post.published_date = timezone.now()
    post.save()

    return redirect('all_posts')

def archive_post(request, id):
    post = get_object_or_404(Post, id = id)

    post.is_published = False
    post.save()

    return redirect('all_posts')

def user_signup(request):
    page_title = 'Inscription'

    if(request.method == 'POST'):
        form = UserCreationForm(request.POST)

        if(form.is_valid()):
            form.save()
    else:
        form = UserCreationForm()

    return render(request, 'blog/user_signup.html', {'form': form})

def user_logout(request):
    logout(request)

    return redirect('all_posts')

def user_login(request):

    if(request.method == 'POST'):
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('all_posts')
        
        else:
            return 'TODO error log message'

    else: 
        form = AuthenticationForm()

    return render(request, 'blog/user_login.html', {'form': form})