from .user import *
from .post import *
from .comments import *
from .subscription import *




















from django.db.models import Count
from test_app.models import Post, Comment
users_with_few_comments = User.objects.annotate(num_comments=Count('comments')).filter(num_comments__lt=3)
posts = Post.objects.filter(author__in=users_with_few_comments)

for post in posts:
    print(post.title)
