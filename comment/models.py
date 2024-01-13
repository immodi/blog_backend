from django.db import models
from post.models import Post

class Comment(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=999)
    content = models.TextField()
    created_on = models.DateField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}"
