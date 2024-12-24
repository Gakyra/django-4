from django.db import models


from .abstract import TimeStampedModel
from test_app.managers.post import PostManager


__all__ = ('Post',)


class Post(TimeStampedModel):
    title = models.CharField(max_length=150)
    content = models.TextField()
    user = models.ForeignKey("test_app.User", on_delete=models.CASCADE, related_name="posts")

    objects = PostManager()
