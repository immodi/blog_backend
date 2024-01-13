from django.db import models
from django.urls import reverse


class Post(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_on = models.DateField(auto_now_add=True)
    author = models.CharField(max_length=255)

    def get_absolute_url(self):
        return reverse('post', args=[self.id])

    def __str__(self):
        return f"{self.id}"
    
    class Meta:
        ordering = ['created_on']

        def __unicode__(self):
            return self.title