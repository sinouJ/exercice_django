from django.urls import path
from . import views 

urlpatterns = [
    path('', views.all_posts, name = 'all_posts'),
    path('post/<int:id>/', views.post_view, name='post_view'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:id>/edit/', views.post_edit, name="post_edit"),
    path('post/<int:id>/publish_post/', views.publish_post, name="publish_post"),
    path('post/<int:id>/archive_post/', views.archive_post, name="archive_post"),
]