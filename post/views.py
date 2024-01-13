from .models import Post
from comment.models import Comment
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PostSerializer
from rest_framework.permissions import IsAdminUser
from .forms import PostForm
from datetime import datetime


class PostCreateView(APIView):
    permission_classes = (IsAdminUser, )
    
    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            post = Post(title=request.POST["title"], content=request.POST["content"], author=request.POST["author"])
            post.save()
            form.cleaned_data["id"] = post.id
            return Response(form.cleaned_data)
        else: return Response({
            "error": "Failed to make a post"
        })


class PostGetAllView(APIView):    
    def get(self, request):
        queryset = Post.objects.all()
        data = [{
            "id": post.id,
            "title": post.title,
            "author": post.author,
            "date": post.created_on
        } for post in queryset]
        return Response(data)
    

class GetHomePostsView(APIView):    
    def get(self, request):
        queryset = Post.objects.all().order_by('-id')[:3][::-1]
        data = [{
            "id": post.id,
            "title": post.title,
            "content": post.content[0:50] + "...",
            "author": post.author,
            "date": post.created_on
        } for post in queryset]
        return Response(data)
    

class PostGetView(APIView):    
    def get(self, request, id):
        if id is not None:
            try: 
                post = Post.objects.get(pk=id)
                data = PostSerializer(post).data
                comments = Comment.objects.filter(post=post).values()
                data["comments"] = comments
            except Exception: data = {"error": "Invalid ID"}
        else:
            data = {"error": "An error ocuured, please try again!"}
        return Response(data)

