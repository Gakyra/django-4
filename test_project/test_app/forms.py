from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Post, Comment, User


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    class Meta:
        model = User


class PostAbstractForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content',)

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 100:
            raise ValidationError('Title must be less than 100 characters')
        return title


class PostCreationForm(PostAbstractForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.instance.user = user


class PostUpdateForm(PostAbstractForm):
    pass


class CommentCreationForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        post = kwargs.pop('post')
        super().__init__(*args, **kwargs)
        self.instance.user = user
        self.instance.post = post
