from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Home page
    path('', views.home, name='home'),

    # Authentication URLs
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),  # profile URL

     # Blog Post URLs for CRUD
    path('posts/', views.PostListView.as_view(), name='posts'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),              # singular 'post'
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),  # 'update' instead of 'edit'
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    # Comment URLs
    path('posts/<int:pk>/comments/new/', views.add_comment, name='comment-create'),
    path('comments/<int:pk>/edit/', views.CommentUpdateView.as_view(), name='comment-update'),
    path('comments/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment-delete'),
]
