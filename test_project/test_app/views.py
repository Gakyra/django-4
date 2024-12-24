from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import CreateView, UpdateView, ModelFormMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post, Comment, User
from .forms import RegistrationForm, LoginForm, PostCreationForm, CommentCreationForm
from .constants import FREE_AND_MORE
from .mixins import SubscriptionLimitationMixin


class IndexView(LoginRequiredMixin, SubscriptionLimitationMixin, ListView):
    template_name = 'index.html'
    model = Post
    context_object_name = 'posts'
    subscription_limitation = FREE_AND_MORE

    def get_queryset(self):
        return Post.objects.all().with_user_info()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'
        return context

# написати сторінку де будуть виводитись списки користувачів із безкоштовною, середньою і про
# на сервері мають бути 3 різні queryset-и


class Users(TemplateView):
    template_name = 'users.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        free = User.objects.filter(subscription__type=FREE)
        advanced = User.objects.filter(subscription__type=ADVANCEd)


class RegistrationView(CreateView):
    template_name = 'authentication/registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('index')


class UserLoginView(LoginView):
    template_name = 'authentication/login.html'
    form_class = LoginForm
    redirect_authenticated_user = True


class AddPostView(LoginRequiredMixin, CreateView):
    template_name = 'posts/add_post.html'
    form_class = PostCreationForm
    success_url = reverse_lazy('add-post')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update(
            {
                'user': self.request.user,
            }
        )
        return kwargs


class PostDetailsView(LoginRequiredMixin, ModelFormMixin, DetailView):
    model = Post
    pk_url_kwarg = 'id'
    template_name = 'posts/post_detail.html'
    context_object_name = 'post'
    form_class = CommentCreationForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context['post_form'] = PostCreationForm(initial={'title': post.title})
        return context


class UpdatePost(LoginRequiredMixin, UpdateView):
    form_class = None
    pk_url_kwarg = 'id'

    def get_success_url(self):
        pass


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentCreationForm
    http_method_names = ['post',]

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update(
            {
                'user': self.request.user,
                'post': Post.objects.get(id=self.kwargs['id']),
            }
        )
        return kwargs

    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'id': self.kwargs['id']})


@login_required
def profile(request):
    return render(request, 'authentication/profile.html', {'user': request.user})




@login_required
def subscription_info(request):
    user = request.user
    return render(request, 'subscription_info.html', {
        'full_name': user.full_name,
        'is_free_subscription': user.is_free_subscription,
        'is_advanced_subscription': user.is_advanced_subscription,
        'is_pro_subscription': user.is_pro_subscription,
    })

@login_required
def user_list(request):
    free_users = User.objects.get_free_users()
    advanced_users = User.objects.get_advanced_users()
    pro_users = User.objects.get_pro_users()
    return render(request, 'user_list.html', {
        'free_users': free_users,
        'advanced_users': advanced_users,
        'pro_users': pro_users,
    })
