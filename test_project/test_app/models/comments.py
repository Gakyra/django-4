from . import User
from .abstract import TimeStampedModel

from django.db import models


__all__ = ('Comment',)


class Comment(TimeStampedModel):
    text = models.TextField()

    user = models.ForeignKey("test_app.User", on_delete=models.CASCADE, related_name="comments")
    post = models.ForeignKey("test_app.Post", on_delete=models.CASCADE, related_name="comments")
