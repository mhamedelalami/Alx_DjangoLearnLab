from django.urls import path
from .views import UserProfileView, UserRegistrationView, CustomAuthToken, FollowUserView, UnfollowUserView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow-user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow-user'),
]
