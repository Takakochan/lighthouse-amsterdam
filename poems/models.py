from django.db import models
from django.contrib.auth.models import User


class Poem(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='poems')
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} by {self.author.username}"
