from .views import *
from django.urls import path


urlpatterns = [
    path('comment', CommentCreateView.as_view(), name="comment_create_view"),
]