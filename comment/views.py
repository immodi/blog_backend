from rest_framework.views import APIView
from comment.models import Comment
from post.models import Post
from .forms import CommentForm
from rest_framework.response import Response

class CommentCreateView(APIView):    
    def post(self, request):
        form = CommentForm(request.POST)
        try:
            if form.is_valid():
                post = Post.objects.get(pk=form.cleaned_data.get("post_id", None))
                if post is not None:
                    comment = Comment(name=form.cleaned_data.get("name"), content=form.cleaned_data.get("content"), post=post)
                    comment.save()
                    return Response(form.cleaned_data)
                else: raise Exception("no such post :O")
            else: raise Exception("failed to make a comment")
        except Exception as e: return Response({"error": str(e)})
