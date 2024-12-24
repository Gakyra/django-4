from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('registration/', views.RegistrationView.as_view(), name='registration'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('add-post/', views.AddPostView.as_view(), name='add-post'),
    path('post/<int:id>/', views.PostDetailsView.as_view(), name='post-detail'),
    path('post/<int:id>/comment/add/', views.CommentCreateView.as_view(), name='post-comment-add'),
    path('profile/', views.profile, name='profile'),
]
