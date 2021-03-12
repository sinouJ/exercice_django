from django.urls import path
from . import views 

urlpatterns = [
    path('', views.all_posts, name = 'all_posts'),
    path('post/<int:id>/', views.post_view, name='post_view'),
    path('post/new/', views.post_new, name='post_new')
]