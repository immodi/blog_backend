from .views import *
from django.urls import path

urlpatterns = [
    path('post/<int:id>', PostGetView.as_view(), name="post_get_by_id"),
    path('posts/', PostGetAllView.as_view(), name="post_get_all"),
    path('posts/home', GetHomePostsView.as_view(), name="post_get_home"),
    path('post/create', PostCreateView.as_view(), name="post_create"),
]